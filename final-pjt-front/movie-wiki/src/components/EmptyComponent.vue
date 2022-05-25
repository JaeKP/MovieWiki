<template>
  <div class="bg-navbar-black empty-componenet">
    <p class="font-basic">{{ data }} 없습니다😢</p>
  </div>
</template>

<script>
export default {
  name: "EmptyComponent",
  props: {
    data: {
      type: String,
    },
  },
};
</script>

<style scoped>
.empty-componenet {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0.4em;
  padding: 1.5em;
  font-size: 1.2em;
  border-radius: 0.4em;
  height: 200px;
  width: 80%;
}
</style>
