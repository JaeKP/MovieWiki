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
    userInfoName: "",
    userInfoDetail: {},
  },
  getters: {
    // 로그인
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    userProfile: (state) => state.userProfile,
    // 유저의 토큰
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
    authToken: (state) => `Token ${state.token}`,

    // 프로필 페이지 유저 이름
    userInfoName: (state) => state.userInfoName,
    userInfoDetail: (state) => state.userInfoDetail,

    // 내 프로필인지 확인한다.
    isSelf: (state) => {
      return state.userInfoName === state.userProfile.username ? true : false;
    },
  },
  mutations: {
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, userProfile) => (state.userProfile = userProfile),
    SET_PROFILE_IMAGE: (state, userProfileImage) =>
      (state.userProfile.image = userProfileImage),
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
    },
    // userInfoName 저장, 관련 내용 저장
    setUserInfoName({ commit, dispatch }, userInfoName) {
      commit("SET_USER_INFO_NAME", userInfoName);
      axios({
        url: drf.accounts.profile(userInfoName),
        method: "get",
      })
        .then((response) => {
          console.log(response.data);
          dispatch("setUserInfoDetail", response.data);
        })
        .catch((error) => {
          console.log(error.response.data);
          if (error.response.status === 404) {
            router.push({ name: "NotFound" });
          }
        });
    },
    // 프로필 이미지만 저장
    setUserProfileImage({ commit }, userProfileImage) {
      commit("SET_PROFILE_IMAGE", userProfileImage);
    },

    // 프로필 저장하기
    fetchProfile({ getters, commit }, username) {
      axios({
        url: drf.accounts.profile(username),
        method: "get",
        headers: getters.authHeader,
      }).then((response) => {
        const profileDict = {
          id: response.data.id,
          username: response.data.username,
          nickname: response.data.nickname,
          age: response.data.age,
          region: response.data.region,
          image: response.data.profile_image || "@/assets/MovieWIki.png",
          searchKeywords: [],
        };
        const JsonProfileDict = JSON.stringify(profileDict);
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
            dispatch("fetchProfile", state.currentUser.username);
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
            heightAuto: false,
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
            heightAuto: false,
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
          router.push({ name: "home" }).catch(() => {});
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // 프로필 수정
    changeProfile(
      { getters, dispatch },
      { username, nickname, age, region, profile_image }
    ) {
      const formdata = new FormData();
      formdata.append("nickname", nickname);
      formdata.append("age", age);
      formdata.append("region", region);
      if (typeof profile_image !== "object" || profile_image === null) {
        axios({
          url: drf.accounts.onlyProfile(username),
          method: "put",
          data: { nickname, age, region },
          headers: getters.authHeader,
        }).then(() => {
          dispatch("fetchProfile", username);
          dispatch("setUserInfoName", username);
        });
      } else {
        for (let i = 0; i < profile_image.length; i++) {
          formdata.append("profile_image", profile_image[i]);
        }
        axios({
          url: drf.accounts.profile(username),
          method: "put",
          data: formdata,
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: getters.authToken,
          },
        }).then(() => {
          dispatch("fetchProfile", username);
          dispatch("setUserInfoName", username);
        });
      }
    },
    // 정보 수정 중 업로드한 이미지
    temporaryImageUpload({ getters, dispatch }, { username, profile_image }) {
      console.log("된다!");
      const formdata = new FormData();
      for (let i = 0; i < profile_image.length; i++) {
        formdata.append("profile_image", profile_image[i]);
      }
      axios({
        url: drf.accounts.temporaryImageUpload(username),
        method: "post",
        data: formdata,
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: getters.authToken,
        },
      }).then((response) =>
        dispatch("setUserProfileImage", response.data.profile_image)
      );
    },

    // 회원 탈퇴
    deleteUserData({ getters, dispatch }, username) {
      axios({
        url: drf.accounts.profile(username),
        method: "delete",
        headers: getters.authHeader,
      }).then(() => {
        dispatch("removeToken");
        dispatch("removeprofile");
        router.push({ name: "home" });
      });
    },
  },
};
