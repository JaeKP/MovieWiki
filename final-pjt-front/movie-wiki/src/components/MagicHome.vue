<template>
  <div>
    <img src="@/assets/doctor.png" class="human" alt="닝겐" />
    <img src="@/assets/1.png" id="glass1" class="glass1" alt="유리" />
    <img src="@/assets/2.png" id="glass2" class="glass2" alt="유리" />
    <img src="@/assets/3.png" id="glass3" class="glass3" alt="유리" />
    <img src="@/assets/4.png" id="glass4" class="glass4" alt="유리" />
    <img src="@/assets/5.png" id="glass5" class="glass5" alt="유리" />
    <img src="@/assets/6.png" id="glass6" class="glass6" alt="유리" />
    <img src="@/assets/7.png" id="glass7" class="glass7" alt="유리" />
    <img src="@/assets/8.png" id="glass8" class="glass8" alt="유리" />
    <img src="@/assets/9.png" id="glass9" class="glass9" alt="유리" />
    <img src="@/assets/10.png" id="glass10" class="glass10" alt="유리" />
    <img src="@/assets/11.png" id="glass11" class="glass11" alt="유리" />
    <img src="@/assets/12.png" id="glass12" class="glass12" alt="유리" />
    <img src="@/assets/13.png" id="glass13" class="glass13" alt="유리" />
    <img src="@/assets/14.png" id="glass14" class="glass14" alt="유리" />
    <img src="@/assets/bg.png" class="bg" alt="벽" />
  </div>
</template>

<script>
export default {
  name: "MagicHome",
  data() {
    return {
      x: 0,
      y: 0,
    };
  },
  methods: {
    mouseMove(e) {
      this.x = e.clientX - window.innerWidth / 2;
      this.y = e.clientY - window.innerHeight / 2;
    },

    magicHome() {
      let mx = 0;
      let my = 0;
      let speed = 0.1;
      let human = document.getElementsByClassName("human")[0];
      let bg = document.getElementsByClassName("bg")[0];
      let glass1 = document.getElementsByClassName("glass1")[0];
      let glass2 = document.getElementsByClassName("glass2")[0];
      let glass3 = document.getElementsByClassName("glass3")[0];
      let glass4 = document.getElementsByClassName("glass4")[0];
      let glass5 = document.getElementsByClassName("glass5")[0];
      let glass6 = document.getElementsByClassName("glass6")[0];
      let glass7 = document.getElementsByClassName("glass7")[0];
      let glass8 = document.getElementsByClassName("glass8")[0];
      let glass9 = document.getElementsByClassName("glass9")[0];
      let glass10 = document.getElementsByClassName("glass10")[0];
      let glass11 = document.getElementsByClassName("glass11")[0];
      let glass12 = document.getElementsByClassName("glass12")[0];
      let glass13 = document.getElementsByClassName("glass13")[0];
      let glass14 = document.getElementsByClassName("glass14")[0];

      mx += (this.x - mx) * speed;
      my += (this.y - my) * speed;

      human.style.transform =
        "translate(" + -mx / 15 + "px," + -my / 15 + "px)";

      bg.style.transform = "translate(" + -(mx / 50) + "px," + 0 + "px)";

      glass1.style.transform =
        "translate3d(" +
        -(mx / 50) +
        "px," +
        -(my / 50) +
        "px,0) rotate3d(0,1,0," +
        mx * 2 +
        "deg)";
      glass2.style.transform =
        "translate3d(" +
        mx / 200 +
        "px," +
        my / 7 +
        "px,0) rotate3d(-1,1,0.3," +
        -mx / 20 +
        "deg)";
      glass3.style.transform =
        "translate3d(" +
        mx / 4 +
        "px," +
        -my / 2 +
        "px,0) rotate3d(0.2,1,0," +
        -mx / 20 +
        "deg)";
      glass4.style.transform =
        "translate3d(" +
        -mx / 2 +
        "px," +
        -my / 2 +
        "px,0) rotate3d(-1,0.5,0," +
        mx / 20 +
        "deg)";
      glass5.style.transform =
        "translate3d(" +
        -mx / 7 +
        "px," +
        my / 1 +
        "px,0) rotate3d(1,1,0," +
        -mx / 4 +
        "deg)";
      glass6.style.transform = "rotate3d(-1,-1,0," + mx / 20 + "deg)";
      glass7.style.transform = "rotate3d(0,1,0," + mx * 2 + "deg)";
      glass8.style.transform = "rotate3d(-0.5,1,0," + mx / 20 + "deg)";
      glass9.style.transform = "rotate3d(-0.1,0.5,0," + mx / 40 + "deg)";
      glass10.style.transform = "rotate3d(0.3,0.2,0," + mx / 20 + "deg)";
      glass11.style.transform =
        "translate3d(" +
        -mx / 20 +
        "px," +
        my / 20 +
        "px,0) rotate3d(1,1,0.1," +
        mx / 50 +
        "deg)";
      glass12.style.transform =
        "translate3d(" +
        -(mx / 20) +
        "px," +
        -(my / 20) +
        "px,0) rotate3d(0,1,0," +
        -mx * 1.5 +
        "deg)";
      glass13.style.transform = "rotate3d(1,-0.3,0," + mx / 200 + "deg)";
      glass14.style.transform = "rotate3d(-1,0.7,0," + mx / 200 + "deg)";
    },
  },
  mounted() {
    window.addEventListener("mousemove", this.mouseMove);
    this.progressbarHandler = setInterval(this.magicHome, 10);
  },
  beforeDestroy() {
    window.removeEventListener("mousemove", this.mouseMove);
    if (this.progressbarHandler != null) {
      clearInterval(this.progressbarHandler);
      this.progressbarHandler = null;
    }
  },
};
</script>

<style>
body {
  position: relative;
}

.human {
  position: absolute;
  width: 100vw;
  z-index: 1;
}
.bg {
  width: 120%;
  z-index: 0;
}
.glass1 {
  position: absolute;
  z-index: 2;
  top: 0;
  width: 100vw;
  transform-style: preserve-3d;
  perspective: 300px;
}
.glass2 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass3 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass4 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass5 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass6 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass7 {
  position: absolute;
  z-index: 2;
  top: 0;
  width: 100vw;
}
.glass8 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass9 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass10 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass11 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass12 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass13 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
.glass14 {
  position: absolute;
  z-index: 1;
  top: 0;
  width: 100vw;
}
</style>
