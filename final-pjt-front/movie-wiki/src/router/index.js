import Vue from "vue";
import VueRouter from "vue-router";
// import ArticleCreateView from '@/views/ArticleCreateView.vue'
// import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleListView from "@/views/ArticleListView.vue";
// import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import HomeView from "@/views/HomeView.vue";
// import MovieDetailView from '@/views/MovieDetailView.vue'
// import MovieReviewView from '@/views/MovieReviewView.vue'
// import SearchMovieView from '@/views/SearchMovieView.vue'
import TrailerView from "@/views/TrailerView.vue";
// import UserInfoArticleView  from '@/views/UserInfoArticleView.vue'
// import UserCommentView from '@/views/UserCommentView.vue'
// import UserInfoFavorite from '@/views/UserInfoFavorite.vue'
// import UserReviewView from '@/views/UserReviewView.vue'

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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
