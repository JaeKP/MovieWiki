import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { library } from "@fortawesome/fontawesome-svg-core";

{
  /* font-awsome 아이콘 코드
<font-awesome-icon icon="fa-solid fa-magnifying-glass" />
<font-awesome-icon icon="fa-solid fa-heart" />
<font-awesome-icon icon="fa-solid fa-thumbs-up" /> 
<font-awesome-icon icon="fa-solid fa-x" />*/
}

import {
  faMagnifyingGlass,
  faHeart,
  faThumbsUp,
  faX,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faMagnifyingGlass, faHeart, faThumbsUp, faX);

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
