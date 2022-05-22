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
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

{
  /* font-awsome 아이콘 코드
<font-awesome-icon icon="fa-solid fa-magnifying-glass" />
<font-awesome-icon icon="fa-solid fa-heart" />
<font-awesome-icon icon="fa-solid fa-thumbs-up" /> 
<font-awesome-icon icon="fa-solid fa-x" />*/
}

library.add(faMagnifyingGlass, faHeart, faThumbsUp, faX, faCirclePlus);

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.use(VueSweetalert2);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
