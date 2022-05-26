<template>
  <div class="progress">
    <span class="bar" id="bar"></span>
  </div>
</template>

<script>
export default {
  name: "ProgressBar",
  methods: {
    updateProgressbar() {
      let el = document.getElementById("bar");
      let scrollTop = document.documentElement.scrollTop;
      let per =
        (scrollTop / (document.body.scrollHeight - window.outerHeight)) * 100;
      el.style.width = per + "%";
    },
  },
  created() {
    this.progressbarHandler = setInterval(this.updateProgressbar, 30);
    console.log(window.outerHeight);
  },
  destroyed() {
    if (this.progressbarHandler != null) {
      clearInterval(this.progressbarHandler);
      this.progressbarHandler = null;
    }
  },
};
</script>

<style>
.progress {
  position: fixed;
  width: 100%;
  height: 5px;
  top: 0;
  left: 0;
  background-color: black;
  z-index: 10;
}
.bar {
  position: absolute;
  width: 0%;
  height: 5px;
  top: 0;
  left: 0;
  background-color: #ed4245;
  z-index: 10;
}
</style>
