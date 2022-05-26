<template>
  <div @click.self="hideHamburgerModal">
    <div class="hambuger-modal font-gray">
      <ul class="hamburger-modal__title">
        <li @click="hideHamburgerModal">
          <router-link :to="{ name: 'home' }" class="nav__content">
            홈
          </router-link>
        </li>
        <li @click="hideHamburgerModal">
          <router-link
            :to="{
              name: 'articles',
              params: { newPayload: newPayload },
            }"
          >
            게시판
          </router-link>
        </li>
        <li @click="hideHamburgerModal">
          <router-link :to="{ name: 'trailer' }"> 쇼츠 </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "TheHamburgerModal",
  data() {
    return {
      newPayload: {
        type: "all",
        query: null,
        title: null,
        content: null,
        nickname: null,
      },
    };
  },
  props: {
    datas: {
      props: String,
    },
  },
  methods: {
    hideHamburgerModal() {
      this.$emit("hide-hamburger-modal");
    },
  },
};
</script>

<style scoped>
.hambuger-modal {
  background-color: #202225;
  width: 100vw;
  height: 300px;
  position: fixed;
  top: 85px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.hamburger-modal__title {
  width: 100%;
}

.hamburger-modal__title > li > a {
  text-align: center;
  text-decoration: none;
  color: inherit;
  display: block;
  padding: 1em;
  font-size: 1.2em;
  font-weight: bold;
  transition: 0.4s;
  width: 100%;
}

.hamburger-modal__title > li:hover {
  font-size: 1.7em;
  color: white;
}
</style>
