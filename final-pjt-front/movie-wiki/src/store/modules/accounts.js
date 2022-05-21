import router from "@/router";
import drf from "@/api/drf";
import axios from "axios";
import Swal from "sweetalert2";

export default {
  state: {
    // 내 정보!!
    token: localStorage.getItem("token") || "",
    currentUser: {},
    userProfile: JSON.parse(localStorage.getItem("userProfile")) || {},

    // 프로필 페이지 관련
    userInfoName: localStorage.getItem("userInfoName") || "",
    userInfoDetail: JSON.parse(localStorage.getItem("userInfoDetail")) || {},
  },
  getters: {
    // 로그인
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    userProfile: (state) => state.userProfile,
    // 유저의 토큰
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),

    // 프로필 페이지 유저 이름
    userInfoName: (state) => state.userInfoName,
    userInfoDetail: (state) => state.userInfoDetail,
  },
  mutations: {
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, userProfile) => (state.userProfile = userProfile),
    SET_USER_INFO_NAME: (state, userInfoName) =>
      (state.userInfoName = userInfoName),
    SET_USER_INFO_DETAIL: (state, userInfoDetail) =>
      (state.userInfoDetail = userInfoDetail),
  },
  actions: {
    // 토큰 저장하기
    saveToken({ commit }, token) {
      commit("SET_TOKEN", token);
      localStorage.setItem("token", token);
    },

    // 토큰 제거하기
    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("token", "");
    },
    removeprofile({ commit }) {
      commit("SET_PROFILE", "");
      localStorage.setItem("profile", {});
    },
    setUserInfoDetail({ commit }, userInfoDetail) {
      commit("SET_USER_INFO_DETAIL", userInfoDetail);
      localStorage.setItem("userInfoDetail", JSON.stringify(userInfoDetail));
    },
    // userInfoName 저장, 관련 내용 저장
    setUserInfoName({ commit, dispatch }, userInfoName) {
      commit("SET_USER_INFO_NAME", userInfoName);
      localStorage.setItem("userInfoName", userInfoName);
      axios({
        url: drf.accounts.profile(userInfoName),
        method: "get",
      }).then((response) => {
        dispatch("setUserInfoDetail", response.data);
      });
    },
    // 프로필 저장하기
    fetchProfile({ getters, commit }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: "get",
        header: getters.authHeader,
      }).then((response) => {
        const profileDict = {
          username: response.data.username,
          nickname: response.data.nickname,
          age: response.data.age,
          region: response.data.region,
          image: response.data.profile_image,
        };
        const JsonProfileDict = JSON.stringify(profileDict);
        console.log(profileDict);
        commit("SET_PROFILE", profileDict);
        localStorage.setItem("userProfile", JsonProfileDict);
      });
    },

    // 토큰과 맞는 username과 프로필 가져오기
    fetchCurrentUser({ dispatch, getters, commit, state }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: "get",
          headers: getters.authHeader,
        })
          .then((response) => {
            commit("SET_CURRENT_USER", response.data);
            dispatch("fetchProfile", state.currentUser);
          })
          .catch((error) => {
            if (error.response.status === 401) {
              dispatch("removeToken");
              dispatch("removeProfile");
              router.push({ name: "login" });
            }
          });
      }
    },

    // 회원가입
    signUp({ dispatch }, credential) {
      axios({
        url: drf.accounts.signup(),
        method: "post",
        data: credential,
      })
        .then((response) => {
          const token = response.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
        })
        .catch((error) => {
          // 오류 내용을 뽑는다.
          const err = JSON.parse(error.request.response);
          const errMessage = Object.values(err)[0][0];
          // 오류 알럿!
          Swal.fire({
            text: errMessage,
            icon: "error",
            width: "25%",
            showConfirmButton: false,
            timer: 2000,
            timerProgressBar: true,
            position: "center",
          });
        });
    },

    // 로그인
    logIn({ dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((response) => {
          const token = response.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
        })
        .catch(() => {
          // 오류 알럿!
          Swal.fire({
            text: "아이디 또는 비밀번호를 잘못 입력했습니다.",
            icon: "error",
            width: "25%",
            showConfirmButton: false,
            timer: 2000,
            timerProgressBar: true,
            position: "center",
          });
        });
    },

    // 로그아웃
    logOut({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: "post",
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch("removeToken");
          dispatch("removeprofile");
          router.push({ name: "home" });
        })
        .error((error) => {
          console.error(error);
        });
    },
  },
};
