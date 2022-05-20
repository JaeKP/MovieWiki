const HOST = "http://localhost:8000/api/v1/";

const ACCOUNTS = "accounts/";
const ARTICLE = "article/";
const MOVIE = "movie/";

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + "login/",
    logout: () => HOST + ACCOUNTS + "logout/",
    signup: () => HOST + ACCOUNTS + "signup/",
    currentUserInfo: () => HOST + ACCOUNTS + "user/",
    profile: (username) => HOST + ACCOUNTS + "profile/" + username,
  },

  article: {
    //  게시판 전체 조회 및 글 작성
    articles: () => HOST + ARTICLE,
    // 게시판 상세 페이지 조회 및 수정, 삭제
    article: (articlePk) => HOST + ARTICLE + `${articlePk}/`,
    // 게시판 상세 페이지 글 좋아요
    likeArticle: (articlePk) => HOST + ARTICLE + `${articlePk}/` + "like/",
    // 게시판 상세글 댓글 생성
    comments: (articlePk) => HOST + ARTICLE + `${articlePk}/` + "comment/",
    // 게시판 상세글 댓글 수정 및 삭제
    comment: (articlePk, commentPk) =>
      HOST + ARTICLE + `${articlePk}/` + "comment/" + `${commentPk}/`,
    // 게시판 댓글 좋아요
    commentLike: (articlePk, commentPk) =>
      HOST + ARTICLE + `${articlePk}/` + "comment/" + `${commentPk}/` + "like/",
    // 게시글 검색
    // params : query(찾을 데이터 명)
    //          title, content, nickname 취사 선택
    //          값이 있는지 없는지만 구분
    articleSearch: () => HOST + ARTICLE + "search",
  },

  movie: {
    // Movie Base URL
    movies: () => HOST + MOVIE,
    // 영홧 상세 정보
    movieDetail: (moviePk) => HOST + MOVIE + `${moviePk}/`,
    // 영화 좋아요
    likeMovie: (moviePk) => HOST + MOVIE + `${moviePk}/` + "like/",
    // 영화 리뷰 조회 작성
    // params: movie_id, type
    moveiReview: () => HOST + MOVIE + "review",
    // 영화 리뷰 수정, 삭제, 좋아요
    // params: movie_id, type, review_id
    movieReviewDetail: () => HOST + MOVIE + "reviewDetail",
    // 영화 검색
    // params : query(찾을 데이터 명)
    //          type(genre, country, director, actor, year,weather)
    movieSearch: () => HOST + MOVIE + "search",
    // 필터 기능
    // params : query(찾을 데이터 명)
    //          type(actor, director, title)
    filter: () => HOST + MOVIE + "filter",
    // 영화 트레일러
    trailer: HOST + MOVIE + "trailer/",
    // latest: 최근에 개봉한 영화 , interest: 최근 관심 , season: 계절 추천
    recommendation: (type) => HOST + MOVIE + "recommendation/" + `${type}/`,
  },
};
