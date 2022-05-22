import Vue from "vue";
import VueRouter from "vue-router";
// import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import ArticleListView from "@/views/ArticleListView.vue";
// import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import HomeView from "@/views/HomeView.vue";
import MovieDetailView from '@/views/MovieDetailView.vue'
// import MovieReviewView from '@/views/MovieReviewView.vue'
// import SearchMovieView from '@/views/SearchMovieView.vue'
import TrailerView from "@/views/TrailerView.vue";
import NotFound404View from "@/views/NotFound404View.vue"
import UserInfoView from "@/views/UserInfoView.vue";

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
    component: MovieDetailView
  },
  {
    path: "/404",
    name: "NotFound",
    component: NotFound404View
  },
  {
    path: "*",
    redirect: "/404"
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
