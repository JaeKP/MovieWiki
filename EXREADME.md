# SSAFY 1학기 관통 프로젝트: 영화 커뮤니티만들기

 **`2022/05/13` ~ `2022/05/26`**

**대전 2반 8조 박재경, 황상윤**

[팀 노션페이지](https://evanescent-tuba-146.notion.site/d71f0e701e314d7abfcf72ede38fe8b6)  /  [깃허브 메인 Repository](https://github.com/JaeKP/MovieWiki)

<br>

**<프로젝트 오버뷰>**

![Honeycam 2022-05-27 05-18-27](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2005-18-27.gif)



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

![Honeycam 2022-05-27 05-28-26](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2005-28-26.gif)

<br>

#### 1.메인페이지 인터렉티브 이미지

- window의 마우스 무브값을 받아 커서의 위치값에 따라 각각의 이미지의 위치를 이동시켜줘 인터렉티브한 효과를 줍니다.

![Honeycam 2022-05-27 05-18-27](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2005-18-27.gif)

<br>

#### 2. 영화 프리뷰와 Carousel 기능

- 화살표와 마우스 스크롤으로 좌우로 이동할 수 있는 Carousel입니다.
- 영화 포스터에 마우스를 올려놓을 시 영화의 타이틀과 오버뷰를 보여 줍니다.

- 영화 포스터를 클릭하면 영화의 상세 페이지로 이동합니다.

![Honeycam 2022-05-27 06-03-15](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-03-15.gif)

<br>

#### 3. 영화 추천 기능들

- 최신 인기영화 추천

  ![image-20220527054829753](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054829753.png)



- 계절 기반 추천 

  ![image-20220527053128670](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527053128670.png)

   

- 30일 이내의 유저들의 한줄평과 좋아요순으로 추천

  ![image-20220527053814830](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527053814830.png)



- 로그인한 유저와 나이대가 비슷한 사람들이 좋아하는 영화 추천

  ![image-20220527054149427](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054149427.png)

  

- 10년 단위 년도별 인기영화 추천

  ![image-20220527054101500](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054101500.png)

  

- 사용자가 사는 지역의 날씨를 기반으로 한 추천

  ![image-20220527054236945](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054236945.png)



- 장르별 인기영화 추천

  ![image-20220527054312255](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054312255.png)



- 평점이 높은 영화 추천

  ![image-20220527054458732](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054458732.png)



- 특정 배우가 출연한 영화들을 추천

  ![image-20220527054540930](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054540930.png)



- 특정 나라에서 인기있는 영화 추천

  ![image-20220527054621402](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054621402.png)



- 특정 감독이 제작한 영화들을 추천

  ![image-20220527054716171](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527054716171.png)

<br>

### 2) 네비 바

#### (1) 회원 가입 모달 

| <img src="https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-01-05.gif?raw=true" > | <img src="https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2005-57-28.gif?raw=true" > |
| :----------------------------------------------------------: | ------------------------------------------------------------ |

<figure>
<img src="https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220527060319863.png" width="40%" >
<img src="https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2005-57-28.gif?raw=true" width="40%" >
</figure>


<br>

#### (2) 로그인 모달

![image-20220527060341848](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220527060341848.png)

<br>

![로그인 오류](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-01-05.gif?raw=true)

<br>

#### (3) 프로필 모달

![image-20220527060427400](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220527060427400.png)

<br>

#### (4) 스크롤 프로그래스 바

- 우측 스크롤 바를 없애는 대신 네비 바 하단에 스크롤의 정보를 표시해 줍니다.

![Honeycam 2022-05-27 05-23-24](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2005-23-24.gif)

<br>

#### (5)검색 모달

- 돋보기 모양을 누르면 검색을 할 수 있는 모달이 등장합니다.
- 검색은 실시간 자동완성으로 영화의 제목을 5개씩 보여 줍니다.
- 찾은 검색 결과에서 키워드에 해당되는 부분은 흰색으로 하이라이팅해서 보여 줍니다.

![Honeycam 2022-05-27 05-50-25](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2005-50-25.gif)

- 검색 결과를 클릭 할 경우 해당 영화의 상세 페이지로 이동합니다.

![Honeycam 2022-05-27 06-04-12](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-04-12.gif)



<br>

### 4) 유저 프로필 (ACCOUNT 관련) 

#### (1) 정보페이지

![image-20220527060524231](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220527060524231.png)

<br>

![유저프로필](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-06-07.gif?raw=true)



<br>

#### (2) 회원 정보 수정 모달

![image-20220527060651746](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220527060651746.png)

<br>

![회원 정보 수정](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-07-36.gif?raw=true)

### 4) 영화 상세페이지

#### (1) 영화 상세 페이지 들어가기

![Honeycam 2022-05-27 06-11-20](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-11-20.gif?raw=true)

<br>

#### (2) 영화 좋아요, 공유하기 

![Honeycam 2022-05-27 06-15-45](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-15-45.gif?raw=true)



<br>

#### (3) 영화 한줄평 작성  , 욕설 필터링 기능

![Honeycam 2022-05-27 06-17-50](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2006-17-50.gif?raw=true)

<br>

#### (4) 영화 한줄평 조희, 스포일러 기능 

![Honeycam 2022-05-27 08-39-00](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2008-39-00.gif?raw=true)

<br>

#### (5) 영화 한줄평 필터와 좋아요 

![Honeycam 2022-05-27 08-40-07](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2008-40-07.gif?raw=true)

<br>

#### (6) 영화 한줄평 수정, 삭제 

![Honeycam 2022-05-27 08-45-44](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2008-45-44.gif?raw=true)

<br>

![Honeycam 2022-05-27 08-46-58](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2008-46-58.gif?raw=true)

<br>

### 5) 게시판 (커뮤니티)

#### (1) 게시글 리스트

![image-20220527060621640](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527060621640.png)

<br>

#### (2) 게시판 필터 기능

- 전체를 보여주는 전체 게시판과 인기글을 보여주는 인기 게시판, 3가지 타입의 게시글을 분류 해주는 자유, 영화, 배우 게시판으로 나누어져있다.
- 게시판을 선택하면 선택한 게시판이 활성화 되면서 버튼의 색이 변한다.

![Honeycam 2022-05-27 06-11-05](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-11-05.gif)

- 각 글에 앞에 있는 게시글의 타입을 클릭해도 해당 게시판으로 이동된다.

![Honeycam 2022-05-27 06-11-57](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-11-57.gif)

- 검색을 한 이후에 게시판을 옮겨도 검색 정보가 초기화 되지 않는다.

![Honeycam 2022-05-27 06-12-47](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-12-47.gif)

<br>

#### (3) 게시판 검색 기능

![image-20220527061413637](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527061413637.png)

- 제목, 내용, 제목 + 내용, 작성자로 4가지로 분류해서 검색할 수 있다.

![image-20220527061424732](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527061424732.png)

- 엔터나 검색 버튼을 통해 검색이 가능하다.
- 게시판의 타입이 선택된 상태에서 검색할 경우 전체게시판으로 초기화 시킨다.

![Honeycam 2022-05-27 06-15-45](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-15-45.gif)

<br>

#### (4) 게시글 작성

![image-20220527061759843](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527061759843.png)

- toast ui를 사용하여 게시글을 작성하기 위한 다양한 툴을 제공해 준다.
- 사진도 추가 할 수 있다.

![Honeycam 2022-05-27 06-20-26](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/Honeycam%202022-05-27%2006-20-26.gif)

<br>

#### (5) 게시글 상세 페이지

- 상단에서 게시글의 정보와 작성자 정보가 나온다.
- 작성자 프로필 이미지를 클릭하면 상세정보로 이동한다.
- 우측에서 댓글과 좋아요 수를 확인할 수 있다.

![image-20220527062141551](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527062141551.png)

- 옵션 버튼을 누르면 게시글 수정 및 삭제가 가능하다.

![image-20220527062743463](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527062743463.png)

- 게시글 하단에서 좋아요를 할 수 있다.

![image-20220527062845869](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527062845869.png)

- 댓글을 작성 할 수 있다.

![image-20220527062911670](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527062911670.png)

- 댓글에서도 유저의 정보를 간단하게 얻을 수 있고 유저 상세페이지로 이동도 가능하다.
- 댓글에도 좋아요를 누를 수 있다.

![image-20220527063045081](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527063045081.png)

- 옵션 버튼을 클릭하면 댓글 수정과 삭제가 가능하다.

![image-20220527063311607](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527063311607.png)

![image-20220527063323626](https://raw.githubusercontent.com/shrewslampe/image_sever/master/img/image-20220527063323626.png)

<br>

### 6) 쇼츠 기능

![Honeycam 2022-05-27 08-40-57](https://github.com/JaeKP/image_repo/blob/main/img/Honeycam%202022-05-27%2008-40-57.gif?raw=true)

<br>

#### (7) 알럿

<br>

#### (8) 반응형 웹페이지

<br>

## 4. 프로젝트 회고 

#### 박재경

난 감자다, 

#### 황상윤

이 정도로 무언가에 집중해서 오랬동한 진행한 일은 처음이였던거 같다. 자는 시간도 아껴가면서 진행했지만 그와는 반대로 시간이 순식간에 지나서 벌써 마감날이 되었다. (별로 한것도 없는거 같은데;;)  처음부터 욕심을 한가득 가지고 시작한 만큼 많이 힘들었지만 그만큼 힘든 만큼 결과물이 잘나와서 기분이 좋다. 물론 완벽하다고는 말은 못하지만 완벽한 하나의 홈페이지를 만드는 것도 누군가와 이정도로 하루조일 붙어서 협업해본 것도 처음이라는 것을 생각하면 만족스러운 것 같다. 하지만 역시 실력 부족으로 구현하지 못했던 기능들을 생각 하면 정말로 아쉽다. 그로 인해 공부의 필요성을 더욱 느끼게 되는 계기가 되었다. 거기에다 프로젝트를 하면서 겪었던 어려움들의 대부분이 기초가 부족해서 겪었다는 것 생각해보면 공부를 더 해야 할 것 같다. 몸은 힘들었지만 하면서 새로 배우고 느낀 감정을 생각해보면 개발을 공부하기 잘했다는 생각이 든다. 마지막으로 같이 힘써준 코코씨 감사합니다!!!
