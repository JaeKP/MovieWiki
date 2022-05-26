# SSAFY 1학기 관통 프로젝트: 영화 커뮤니티만들기

 **`2022/05/13` ~ `2022/05/26`**

**대전 2반 8조 박재경, 황상윤**

[팀 노션페이지](https://evanescent-tuba-146.notion.site/d71f0e701e314d7abfcf72ede38fe8b6)  /  [깃허브 메인 Repository](https://github.com/JaeKP/MovieWiki)

<br>

## 1. 기획 스케치

### 1) 기획 의도

왜 사람들이 영화사이트를 사용할까? 에서부터 구현해야 할 기능들에 대해 아이디어를 공유했습니다. 

사이트를 사용하는 니즈는 크게 3가지가 있다고 생각을 했고, 이를 충족시키기 위한 기능을 픽스하게 되었습니다. (구현 가능성을 중심으로 정하게 되었습니다.)

| 왜?                            | 채택된 기능                                                  | 채택되지 않은 아이디어                                       |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 영화에 대한 정보가 궁금하다.   | 1. 영화 검색 , <br />2. 영화 상세 정보 조회 , <br />3. 영화 정보 공유 게시판 | 1. 영화 기사 클리퍼                                          |
| 어떤 영화를 봐야할지 모르겠다. | 1. 영화 추천                                                 |                                                              |
| 그냥 심심하다.                 | 1. 유튜브 쇼츠와 비슷한 킬링타임용 기능<br />2,  커뮤니티    | 1. 영화기반의 SNS, <br />2. 와챠파티와 같이 넷플릭스를 함께 보고싶은 유저들을 중계해주는 사이트 |

결국, 특별한 기능은 없지만 유저의 편의를 고려한 웹사이트를 만드는 것을 목적으로 기획을 하기 시작했습니다. 

<br>

### 2)  기획 과정 

#### (1) 기능 명세서 ( 05월 13일 )

[기능 명세서](https://docs.google.com/spreadsheets/d/13-9IrDFRCBZyD7dkMfqYZtNMpP68iiz1fK5H-jnfsAM/edit?usp=sharing)

전반적으로, 앞서 나온 아이디어들을 기반으로 웹사이트에서 사용될 기능들을 구체적으로 나열했습니다.

#### ![MovieWiki기능명세서](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EA%B8%B0%EB%8A%A5%EB%AA%85%EC%84%B8%EC%84%9C.png)

<br>

#### (2) 와이어 프레임(05월 14일)

[와이어 프레임](https://www.figma.com/file/CqrSKHWMJg6BryWXfnyvXL/%EB%91%98%EC%BD%94%EC%BD%94-team-library?node-id=0%3A1)

피그마를 활용하여 앞서 나온 기능들을 어떻게 표현할지 구체적으로 설계했습니다. 

![MovieWiki와이어프레임](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%84.png)

<br>

#### (3) ERD 설계 (05월 16일)

앞서 정한 기능을 구현하기 위해 필요한 데이터를 구조화 했습니다. 또한, TMDB API를 활용하여 영화 데이터를 저장하기 위한 코드를 준비했습니다. 

![둘코코.drawio](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/%EB%91%98%EC%BD%94%EC%BD%94.drawio.png)

이미 기능을 구현하기 위한 필요한 데이터가 정해져있었기 때문에, 비교적 쉽게 설계할 수 있었습니다.
효율은.,,몰루,,🙄

<br>

#### (4) 컴포넌트 설계 (05월 16일)

추후 효율적으로 협업을 하기 위해, 컴포넌트 구조를 미리 정했습니다. (물론 설계대로 진행되지 않았다...😅...매우 많이 수정되었다...)

```
├── 
├── src
│   ├── api
│   ├── assets
│   ├── components
│   │   ├── NavBar.vue
│   │   ├── CardList.vue
│   │   ├── CardListItem.vue
│   │   ├── InputForm.vue
│   │   ├── TheButton.vue
│   │   ├── ScrollProgress.vue
│   │   ├── ThePagenation.vue
│   │   ├── ProfileAvatar.vue
│   │   ├── SearchMovieModal.vue
│   │   ├── TheLoginModal.vue
│   │   ├── TheProfileModal.vue
│   │   ├── TheSignUpModal.vue
│   │   ├── UserInfo.vue
│   │   ├── UserInfoContent.vue
│   │   ├── UserChangeModal.vue
│   │   ├── UserStateModal.vue
│   │   ├── CardCarousel.vue
│   │   ├── ReviewForm.vue
│   │   ├── ReviewList.vue
│   │   ├── ReviewListItem.vue
│   │   ├── DetailBody.vue
│   │   ├── ThumnailTrailerList.vue
│   │   ├── ThumnailTrailerListItem.vue
│   │   ├── ReviewModal.vue
│   │   ├── ArticleList.vue
│   │   ├── ArticleListItem.vue
│   │   ├── ArticleDetail.vue
│   │   ├── ArticleDetailModal.vue
│   │   ├── ArticleCommentForm.vue
│   │   ├── ArticleCommentList.vue
│   │   ├── ArticleCommentListItem.vue
│   │   ├── ArticleCreateForm.vue
│   │   ├── ProfileAvatarForm.vue
│   │   ├── RecentSearchList.vue
│   │   └── RecentSearchListItem.vue
├── router
│   └── index.js
├── store
│   └── modules
│   │   └── accounts.
│   └── index.js
├── views
│   ├── HomeView.vue
│   ├── MovieDetailView.vue
│   ├── MovieReviewView.vue
│   ├── TrailerView.vue
│   ├── ArticleListView.vue
│   ├── ArticleDetailView.vue
│   ├── ArticleCreateView.vue
│   ├── ArticleUpdateView.vue
│   ├── UserInfoView.vue
│   └── SearchMovieView.vue
├── main.js
├── .env.local
...생략
└── READEME.md

```

<br>

## 2. 진행 과정

- 기획: `2022/05/13`  ~ `2022/05/16`

- 백엔드: `2022/05/17`  ~ `2022/05/19`

- 프론트엔드: `2022/05/20` ~ `2022/05/26`

![MovieWiki진행과정](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EC%A7%84%ED%96%89%EA%B3%BC%EC%A0%95.png)

### 1) 기능 단위로 업무를 나눠 진행

![MovieWikiAssign](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWikiAssign.png)

<br>

### 2) 협업 진행 과정

![MovieWikiCollabo](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWikiCollabo.png)

<br>

## 3. 프로젝트 소개

### 1) 메인 홈 



### 2) 유저 프로필 (ACCOUNT 관련) 



### 3) 영화 상세페이지



### 4) 게시판 (커뮤니티)



### 5) 트레일러 





<br>

## 4. 프로젝트 회고 