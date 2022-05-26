import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { library } from "@fortawesome/fontawesome-svg-core";
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";
import {
  faMagnifyingGlass,
  faHeart,
  faThumbsUp,
  faX,
  faCirclePlus,
  faEllipsisVertical,
  faMessage,
  faStar,
  faAnglesRight,
  faAnglesLeft,
  faShare,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import AOS from "aos";
import "aos/dist/aos.css";

{
  /* font-awsome 아이콘 코드
<font-awesome-icon icon="fa-solid fa-magnifying-glass" />
<font-awesome-icon icon="fa-solid fa-heart" />
<font-awesome-icon icon="fa-solid fa-thumbs-up" /> 
<font-awesome-icon icon="fa-solid fa-x" />*/
}

library.add(
  faMagnifyingGlass,
  faHeart,
  faThumbsUp,
  faX,
  faCirclePlus,
  faEllipsisVertical,
  faMessage,
  faStar,
  faAnglesRight,
  faAnglesLeft,
  faShare
);

// 폰트어썸
Vue.component("font-awesome-icon", FontAwesomeIcon);

//  오류 메시지, 무한 스크롤 관련 라이브러리
Vue.use(VueSweetalert2, AOS);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
  mounted() {
    AOS.init();
  },
}).$mount("#app");
