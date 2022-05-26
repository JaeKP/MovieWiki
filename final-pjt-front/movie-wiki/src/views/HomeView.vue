<template>
  <div>
    <progress-bar class="progress-bar"></progress-bar>
    <magic-home class="magic-home"></magic-home>
    <!-- 계절별 추천 -->
    <!-- 최신 인기 -->
    <card-list
      class="test-margin"
      URL="http://localhost:8000/api/v1/movie/list"
      Tag="최신 인기 영화"
    ></card-list>
    <div>
      <card-list
        class="card-list"
        URL="http://localhost:8000/api/v1/movie/recommendation/season/"
        :Tag="`${season} 이런 영화 어때요?`"
      ></card-list>
    </div>
    <!-- 요즘 제일 핫 -->
    <card-list
      URL="http://localhost:8000/api/v1/movie/recommendation/interest/"
      Tag="요즘 제일 핫한 영화"
    ></card-list>
    <!-- 유저와 또래의 유저가 좋아요한 수 -->
    <card-list
      v-if="isLoggedIn"
      :URL="`http://localhost:8000/api/v1/movie/recommendation/age/?age=${userProfile.age}`"
      :Tag="`${userProfile.nickname}님과 또래의 유저들이 좋아하는 영화`"
    ></card-list>

    <!-- 년도 인기 영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=year&query=${sampleYear}`"
      :Tag="`${sampleYear}0년대 인기 영화`"
    ></card-list>
    <!-- 날씨별 -->
    <card-list
      v-if="isLoggedIn"
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=weather&query=${userProfile.region}`"
      :Tag="Weather_condition_codes[weather]"
    ></card-list>
    <!-- 장르 추천 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=genre&query=${sampleGenre2.genre}`"
      :Tag="`${sampleGenre2.name} 장르의 영화`"
    ></card-list>
    <!-- 최고 평점 -->
    <card-list
      URL="http://127.0.0.1:8000/api/v1/movie/filter?type=score"
      Tag="최고의 평점"
    ></card-list>
    <!-- 배우가 나온 영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=actor&query=${sampleActor1.actorId}`"
      :Tag="`${sampleActor1.actor} 출연한 영화`"
    ></card-list>
    <!-- 장르 추천 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=genre&query=${sampleGenre1.genre}`"
      :Tag="`${sampleGenre1.name} 장르의 영화`"
    ></card-list>

    <!-- 나라별 인기영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=country&query=${sampleCountry.countryId}`"
      :Tag="`${sampleCountry.country}에서 인기있는 영화`"
    ></card-list>
    <!-- 감독이 제작한 영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=director&query=${sampleDirector1.directorId}`"
      :Tag="`${sampleDirector1.director} 감독이 제작한 영화`"
    ></card-list>

    <!-- 배우가 나온 영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=actor&query=${sampleActor2.actorId}`"
      :Tag="`${sampleActor2.actor} 출연한 영화`"
    ></card-list>
    <!-- 감독이 제작한 영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=director&query=${sampleDirector2.directorId}`"
      :Tag="`${sampleDirector2.director} 감독이 제작한 영화`"
    ></card-list>
    <!-- 배우가 나온 영화 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=actor&query=${sampleActor3.actorId}`"
      :Tag="`${sampleActor3.actor} 출연한 영화`"
    ></card-list>

    <!-- 장르 추천 -->
    <card-list
      :URL="`http://127.0.0.1:8000/api/v1/movie/filter?type=genre&query=${sampleGenre3.genre}`"
      :Tag="`${sampleGenre3.name} 장르의 영화`"
    ></card-list>
  </div>
</template>

<script>
import CardList from "@/components/CardList.vue";
import _ from "lodash";

import { mapGetters } from "vuex";
import ProgressBar from "@/components/ProgressBar.vue";
import MagicHome from "@/components/MagicHome.vue";

export default {
  components: { CardList, ProgressBar, MagicHome },
  name: "HomeView",
  data() {
    return {
      actor1: [
        { actor: "키아누 리브스가", actorId: "6384" },
        { actor: "윌 스미스가", actorId: "2888" },
        { actor: "짐 캐리가", actorId: "206" },
        { actor: "제니퍼 애니스톤이", actorId: "4491" },
        { actor: "케이트 윈슬렛이", actorId: "204" },
        { actor: "앤서니 홉킨스가", actorId: "4173" },
      ],
      actor2: [
        { actor: "드류 베리모어가", actorId: "69597" },
        { actor: "앤 해서웨이가", actorId: "1813" },
        { actor: "메릴 스트립이", actorId: "5064" },
        { actor: "매즈 미켈슨이", actorId: "1019" },
        { actor: "톰 홀랜드가", actorId: "1136406" },
        { actor: "브래드 피트가", actorId: "287" },
      ],
      actor3: [
        { actor: "대니얼 래드클리프가", actorId: "10980" },
        { actor: "톰 크루즈가", actorId: "500" },
        { actor: "조니 뎁이", actorId: "85" },
        { actor: "니콜 키드먼이", actorId: "2227" },
        { actor: "베네딕트 컴버배치가", actorId: "71580" },
      ],
      director1: [
        { director: "알프레드 히치콕", directorId: "2636" },
        { director: "팀 버튼", directorId: "510" },
        { director: "미야자키 하야오", directorId: "608" },
        { director: "스티븐 스필버그", directorId: "488" },
        { director: "마틴 스콜세지", directorId: "1032" },
        { director: "마이클 베이", directorId: "865" },
      ],
      director2: [
        { director: "클린트 이스트우드", directorId: "190" },
        { director: "우디 앨런", directorId: "1243" },
        { director: "리들리 스콧", directorId: "578" },
        { director: "론 하워드", directorId: "6159" },
        { director: "데이비드 핀처", directorId: "7467" },
        { director: "샘 레이미", directorId: "7623" },
      ],
      year: ["199", "200", "201"],
      country: [
        { country: "중국", countryId: "156" },
        { country: "일본", countryId: "392" },
        { country: "영국", countryId: "826" },
        { country: "한국", countryId: "410" },
        { country: "미국", countryId: "840" },
        { country: "프랑스", countryId: "250" },
      ],
      API_KEY: "5d654e5750cf87fe1521ba1afb50a11a",
      area_data: {
        서울: [37.56667, 126.97806],
        인천: [37.469221, 126.573234],
        광주: [35.15972, 126.85306],
        대구: [35.798838, 128.583052],
        울산: [35.519301, 129.239078],
        대전: [36.321655, 127.378953],
        부산: [35.198362, 129.053922],
        경기: [37.567167, 127.190292],
        강원: [37.555837, 128.209315],
        충남: [36.557229, 126.779757],
        충북: [36.628503, 127.929344],
        경북: [36.248647, 128.664734],
        경남: [35.259787, 128.664734],
        전북: [35.716705, 127.144185],
        전남: [34.8194, 126.893113],
        제주: [33.364805, 126.542671],
      },
      weather: "",
      Weather_condition_codes: {
        Thunderstorm: "천둥치는 날 으스스한 호러영화 어때요?",
        Rain: "비가 오는 날 으스스한 호러영화 어때요?",
        Drizzle: "이슬비 내리는 날 감성있는 드라마 어때요?",
        Clouds: "안개 끼는 날 감성있는 드라마어때요?",
        Clear: "햇살 좋은날 기분좋은 음악영화 어때요?",
        Snow: "눈내리는 추운날 따뜻한 가족영화 어때요?",
      },
      season: "",
      genres1: [
        { genre: "35", name: "코미디" },
        { genre: "36", name: "역사" },
        { genre: "37", name: "서부" },
        { genre: "53", name: "스릴러" },
        { genre: "80", name: "범죄" },
        { genre: "99", name: "다큐멘터리" },
        { genre: "878", name: "SF" },
      ],
      genres2: [
        { genre: "12", name: "모험" },
        { genre: "14", name: "판타지" },
        { genre: "16", name: "애니메이션" },
        { genre: "18", name: "드라마" },
        { genre: "27", name: "공포" },
        { genre: "28", name: "액션" },
      ],
      genres3: [
        { genre: "9648", name: "미스터리" },
        { genre: "10402", name: "음악" },
        { genre: "10749", name: "로맨스" },
        { genre: "10751", name: "가족" },
        { genre: "10752", name: "전쟁" },
      ],
    };
  },
  methods: {},
  computed: {
    ...mapGetters(["userProfile", "isLoggedIn"]),
    sampleActor1() {
      return _.sample(this.actor1);
    },
    sampleActor2() {
      return _.sample(this.actor2);
    },
    sampleActor3() {
      return _.sample(this.actor3);
    },
    sampleDirector1() {
      return _.sample(this.director1);
    },
    sampleDirector2() {
      return _.sample(this.director2);
    },
    sampleYear() {
      return _.sample(this.year);
    },
    sampleCountry() {
      return _.sample(this.country);
    },
    sampleGenre1() {
      return _.sample(this.genres1);
    },
    sampleGenre2() {
      return _.sample(this.genres2);
    },
    sampleGenre3() {
      return _.sample(this.genres3);
    },
  },
  async created() {
    if (this.userProfile.region) {
      const response = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${
          this.area_data[this.userProfile.region][0]
        }&lon=${this.area_data[this.userProfile.region][1]}&appid=${
          this.API_KEY
        }&units=metric`
      );
      const weather = await response.json();
      this.weather = weather.weather[0].main;
    }

    const nowdate = new Date();
    const month = nowdate.getMonth();
    if (month === 3 || month === 4 || month === 5) {
      this.season = "따사로운 봄날";
    } else if (month === 6 || month === 7 || month === 8) {
      this.season = "무더운 여름";
    } else if (month === 9 || month === 10 || month === 12) {
      this.season = "시원한 가을";
    } else {
      this.season = "추운 겨울";
    }
  },
};
</script>

<style>
.progress-bar {
  margin-top: 80px;
}

.test-margin {
  /* position: absolute; */
  margin-top: -140px;
  z-index: 10;
}
.card-list {
  z-index: 5;
}
.bg2 {
  position: absolute;
}
</style>
