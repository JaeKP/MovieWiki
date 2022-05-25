<template>
  <div class="not-found">
    <h1 class="font-basic">404 Not Found</h1>
    <h2 class="font-basic">우리 팀원 고양이 귀엽죠</h2>
    <h3 class="font-basic">🌱 둘기씨가 발견할 때까지 존버한다,, 🌱</h3>
  </div>
</template>

<script>
export default {
  name: "NotFound404View",
};
</script>

<style>
.not-found {
  margin: 10em;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1em;
  background-image: url("@/assets/404Not.png");
  height: calc(100vh - 80px);
}
</style>
