<template>
  <div>
    <nav class="bg-navbar-black">
      <ul class="font-icon-gray nav-title">
        <li>
          <router-link :to="{ name: 'home' }" class="nav-content">
            홈
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'trailer' }"> 트레일러 </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'articles' }"> 게시판 </router-link>
        </li>
      </ul>
      <ul class="flex-ul nav-button">
        <font-awesome-icon
          icon="fa-solid fa-magnifying-glass"
          class="font-real-white"
        />
        <div>
          <button class="bg-icon-blue font-real-white">회원가입</button>
          <button class="bg-real-white font-nav-black">로그인</button>
        </div>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style>
nav {
  height: 80px;
  display: flex;
}

ul {
  display: flex;
}

a {
  text-align: center;
  text-decoration: none;
  color: inherit;
  display: block;
  padding: 1em;
  font-size: 1.2rem;
  font-weight: bold;
}

.nav-title {
  width: 80%;
  display: flex;
}

.nav-title link {
  width: 33.333333%;
}
</style>
