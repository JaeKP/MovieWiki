import Vue from "vue";
import VueRouter from "vue-router";
import ArticleCreateView from "@/views/ArticleCreateView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import ArticleListView from "@/views/ArticleListView.vue";
import ArticleUpdateView from "@/views/ArticleUpdateView.vue";
import HomeView from "@/views/HomeView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
// import MovieReviewView from '@/views/MovieReviewView.vue'
// import SearchMovieView from '@/views/SearchMovieView.vue'
import TrailerView from "@/views/TrailerView.vue";
import NotFound404View from "@/views/NotFound404View.vue";
import UserInfoView from "@/views/UserInfoView.vue";
import store from "@/store/index";
import Swal from "sweetalert2";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/trailer",
    name: "trailer",
    component: TrailerView,
  },
  {
    path: "/articles",
    name: "articles",
    component: ArticleListView,
  },
  {
    path: "/articles/:articlePk",
    name: "article",
    component: ArticleDetailView,
    meta: { isLoggedIn: true },
    beforeEnter: function (to, from, next) {
      const isLogin = store.getters["isLoggedIn"];
      if (
        to.matched.some(function (routeInfo) {
          return routeInfo.meta.isLoggedIn;
        })
      ) {
        // console.log(isLogin);
        if (isLogin) {
          // console.log("routing success : '" + to.path + "'");
          next(); // 페이지 전환
        } else {
          Swal.fire({
            title: "로그인한 유저만 접근이 가능합니다.",
            icon: "info",
            width: "400px",
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 2000,
            timerProgressBar: true,
            heightAuto: false,
          });
        }
      } else {
        next();
      }
    },
  },
  {
    path: "/articles/new",
    name: "ArticleCreate",
    component: ArticleCreateView,
    meta: { isLoggedIn: true },
    beforeEnter: function (to, from, next) {
      const isLogin = store.getters["isLoggedIn"];
      if (
        to.matched.some(function (routeInfo) {
          return routeInfo.meta.isLoggedIn;
        })
      ) {
        console.log(isLogin);
        if (isLogin) {
          console.log("routing success : '" + to.path + "'");
          next(); // 페이지 전환
        } else {
          // 이동할 페이지에 인증 정보가 필요하면 경고 창을 띄우고 페이지 전환은 하지 않음
          Swal.fire({
            title: "로그인한 유저만 접근이 가능합니다.",
            icon: "info",
            width: "400px",
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 2000,
            timerProgressBar: true,
            heightAuto: false,
          });
        }
      } else {
        next();
      }
    },
  },
  {
    path: "/articles/:articlePk/edit",
    name: "articleUpdate",
    component: ArticleUpdateView,
  },

  {
    path: "/profile/:username",
    name: "profile",
    component: UserInfoView,
    props: true,
  },
  {
    path: "/movies/:movieId",
    name: "movieDetail",
    component: MovieDetailView,
  },
  {
    path: "/404",
    name: "NotFound",
    component: NotFound404View,
  },
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  // 라우터 이동 시 스크롤 위로
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});

// const guardRoutes = [
//   { path: "/articles/:articlePk", component: ArticleDetailView },
// ];
// guardRoutes.beforeEach(function (to, from, next) {
//   console.log("안되지롱");
// });

export default router;
