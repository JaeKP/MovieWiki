<template>
  <div class="review-modal" @click.self="hideReviewModal">
    <div class="review-modal__container"></div>
  </div>
</template>

<script>
export default {
  name: "TheReviewModal",
  methods: {
    hideReviewModal() {
      this.$emit("hide-review-modal", false);
    },
  },
};
</script>

<style>
.review-modal {
  width: 100%;
  justify-content: center;
  align-items: center;
}

.review-modal__container {
  background-color: #36393f;
  border-radius: 0.3em;
  width: 50%;
  height: 500px;
}
</style>
