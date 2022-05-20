const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLE = 'article/'
const MOVIE = 'movie/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },

  article: {
    articles: () => HOST + ARTICLE,
    article: articlePk => HOST + ARTICLE + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLE + `${articlePk}/` + 'likes/',
    comments: articlePk =>  HOST + ARTICLE + `${articlePk}/` + 'comment/',
    comment: (articlePk, commentPk) => HOST + ARTICLE + `${articlePk}/` + 'comment/' + `${commentPk}/` 
  },
  
  movie: {
    movies: () => HOST + MOVIE,
    movie: moviePk =>  HOST + MOVIE + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIE + `${moviePk}/` + 'like/',
    moveiReview: (moviePk, filterPk) => HOST + MOVIE +`${moviePk}/` + 'review/' + `${filterPk}/`,
    movieReviewDetail: (moviePk, filterPk, reviewPk) => HOST + MOVIE + `${moviePk}/` + 'review/' + `${filterPk}/` + 'detail/' + `${reviewPk}/`,
    search: q => HOST + MOVIE + 'search/' + `${q}/`,
    genre: genrePk => HOST + MOVIE + 'genre/' + `${genrePk}/`,
    country: countryPk => HOST + MOVIE + 'country/' + `${countryPk}/`,
    director: directorPk => HOST + MOVIE + 'director/' + `${directorPk}/`,
    actor: actorPk => HOST + MOVIE + 'actor/' + `${actorPk}/`,
    year: yearPk => HOST + MOVIE + 'year/' + `${yearPk}/`,
    weather: weatherPk => HOST + MOVIE + 'weather/' + `${weatherPk}/`,
    weatherData: HOST + MOVIE + 'data/',
    weatherBaseData: HOST + MOVIE + 'basedata/',
    trailer: HOST + MOVIE + 'trailer/',
    recommendation: type => HOST + MOVIE + 'recommendation/' + `${type}/`,  
  }
}
