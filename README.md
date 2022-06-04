# SSAFY 1학기 관통 프로젝트: 영화 커뮤니티만들기

####  ヽ(✿ﾟ▽ﾟ)ノ 최우수 프로젝트 수상 ヽ(✿ﾟ▽ﾟ)ノ

---

 **`2022/05/13` ~ `2022/05/26`**

대전 2반 8조 박재경, 황상윤

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
| 영화에 대한 정보가 궁금하다.   | 1. 영화 검색 , <br />2. 영화 상세 정보 조회  <br />3. 영화 정보 공유 게시판 | 1. 영화 기사 클리퍼                                          |
| 어떤 영화를 봐야할지 모르겠다. | 1. 영화 추천                                                 |                                                              |
| 그냥 심심하다.                 | 1. 유튜브 쇼츠와 비슷한 킬링타임용 기능<br />2,  커뮤니티    | 1. 영화기반의 SNS, <br />2. 와챠파티와 같이 넷플릭스를 함께 보고싶은 유저들을 중계해주는 사이트 |

결국, 특별한 기능은 없지만 유저의 편의를 고려한 웹사이트를 만드는 것을 목적으로 기획을 하기 시작했습니다. 

<br>

### 2)  진행 과정

- 기획: `2022/05/13`  ~ `2022/05/16`

- 백엔드: `2022/05/17`  ~ `2022/05/19`

- 프론트엔드: `2022/05/20` ~ `2022/05/26`

![MovieWiki진행과정](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EC%A7%84%ED%96%89%EA%B3%BC%EC%A0%95.png)

#### 기획 단계 

- **기능 명세서 ( 05월 13일 )**
  - [링크](https://docs.google.com/spreadsheets/d/13-9IrDFRCBZyD7dkMfqYZtNMpP68iiz1fK5H-jnfsAM/edit?usp=sharing)
  - 구글 스프레드 시트를 활용하여 채택된 아이디어들을 기반으로 웹사이트에 필요한 기능을 구체적으로 나열했습니다.
- **와이어 프레임(05월 14일)**
  - [링크](https://www.figma.com/file/CqrSKHWMJg6BryWXfnyvXL/%EB%91%98%EC%BD%94%EC%BD%94-team-library?node-id=0%3A1)
  - 피그마를 활용하여 앞서 나온 기능들을 어떻게 표현할지 구체적으로 설계했습니다. 
- **ERD 설계 (05월 16일)**
  - [링크](https://evanescent-tuba-146.notion.site/Project-65922167b74447a49f2d13dcb46b7352)
  - 앞서 정한 기능을 구현하기 위해 필요한 데이터를 구조화 했습니다. 또한, TMDB API를 활용하여 영화 데이터를 저장하기 위한 코드를 준비했습니다. 
  - 이미 기능을 구현하기 위한 필요한 데이터가 정해져있었기 때문에, 비교적 쉽게 설계할 수 있었습니다. 효율은.,,몰루,,🙄
- **컴포넌트 설계 (05월 16일)**
  - [링크](https://evanescent-tuba-146.notion.site/Project-65922167b74447a49f2d13dcb46b7352)
  - 원활한 협업을 위해 미리 컴포넌트를 설계했습니다.
  - 물론 이대로 진행되지는 않았습니다..😅

<br>

#### 백엔드~ 프론트엔드:  기능 단위로 업무를 나눠 진행

![MovieWikiAssign](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWikiAssign.png)

<br>

#### 협업 진행 과정

기능단위로 업무를 진행하기 때문에, 의사소통이 가장 중요하다고 생각했습니다. 

- Notion을 활용하여 매일 아침 9시에 스크럼 회의를 진행한 내역을 기록하였습니다. 또한, 일일 회고 및 칸반보드를 활용하여 전반적인 일정 관리를 했습니다.
- 깃허브의 이슈, 풀 리퀘를 통해 실시간으로 서로의 진행 현황을 공유했습니다.
- 디스코드를 통해 문제 상황이 발생했을경우 빠른 해결을 할 수 있었습니다. 

<br>

## 2. 프로젝트 소개

### 1) 영화 추천 및 검색 기능

#### 메인 홈: 추천

<br>

#### 검색바: 검색

<br>

#### 쇼츠: 랜텀 트레일러

<br>

### 2) 영화 상세 정보 조회

#### 영화 상세 페이지: 영화 상세 정보 조회 및 좋아요와 공유하기

![MovieWiki영화상세페이지](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EC%98%81%ED%99%94%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80.gif)

- **영화에 대한 상세한 정보를 제공한다.** 
  - 포스터, 영화 장르, 개봉일, 줄거리, 평점
  - 감독 및 배우(배역과 배우 이름)
  - 유튜브 트레일러

<br>

- **찜하기와 공유하기** 
  - `찜하기`: 영화를 찜해서 유저 프로필 페이지에서 확인할 수 있다. 
  - `공유하기`: 카카오톡을 통해 친구에게 해당 페이지를 공유할 수 있다. 

<br>

- **비슷한 영화**
  - 포스터에 마우스를 올리면, 줄거리와 타이틀이 표시된다. 
  - 포스터를 클릭하면 해당 영화의 상세 페이지로 이동한다. 

<br>

- **영화 한줄 평**

  - 유저가 작성한 영화에 대한 한줄평을 확인할 수 있다.

  - 만약 한줄평이 한개도 작성되지 않았을 경우, 한줄평 작성을 유도하는 문구가 있다. 

   ``` 
    아직 등록된 리뷰가 없습니다 😢
    리뷰를 남겨주세요!
   ```

<br>

#### 영화 상세페이지: 한줄평 

![MovieWiki영화한줄평](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EC%98%81%ED%99%94%ED%95%9C%EC%A4%84%ED%8F%89.gif)

- 한줄평 CRUD과 좋아요
  - 영화 한줄평을 Create, Read, Update, Delete 할 수 있다. 
  - delete할 경우, 정말 삭제할 것인지 확인하는 알럿이 뜬다. 
  - 한줄평에 대해 좋아요를 누를 수 있다. 

<br>

- 한줄평 정렬
  - 최신순, 인기순(좋아요 순)으로 한줄평을 정렬할 수 있다.
  - 최신순으로 정렬할 경우, 한줄평 작성 날짜를 표시한다.
  - 인기순으로 정렬할 경우, 좋아요 수를 표시한다.

<br>

- 스포일러 한줄 평
  - 스포일러 기능을 통해, 원치 않는 스포일러를 방지 한다. 
  - 스포일러를 체크하고 한줄평을 작성할 경우, 해당 한줄 평을 클릭해야 내용을 확인할 수 있다. 

<br>

- 욕설 제재 문구와 필터링 기능

  - 한줄평을 작성하는 란에 광고 및 욕설을 제재하는 문구가 적혀 있다. 

    ```
    광고 및 욕설, 비속어나 타인을 비방하는 문구를 사용하면 비공개 될 수 있습니다.
    ```

  - 욕설로 설정한 단어를 한줄평에 작성할 경우 아래와 같은 알럿이 뜨고 해당 한줄평은 등록되지 않는다. 
    <img src="https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220604010235245.png" width="300">


<br>

#### 영화 상세페이지: 비로그인 유저

![MovieWiki영화상세페이지비로그인유저](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EC%98%81%ED%99%94%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%9C%A0%EC%A0%80.gif)

- 비로그인 유저는 영화 찜하기와 한줄평 기능에 접근할 수 없다.
  - `영화 찜하기`: 우측 상단에 로그인 유저만 접근할 수 있다는 알럿이 뜬다. 
  - `한줄평 조회`: 한줄평은 블러처리가 되어 있고, 로그인을 유도하는 배너가 뜬다.

<br>

### 3) 커뮤니티 

#### 커뮤니티 게시판 : 게시판 필터와 검색

<br>

#### 커뮤니티 게시판 : 게시글 작성과 수정

<br>

#### 커뮤니티 게시글 : 댓글과 좋아요 

<br>

#### 커뮤니티 게시판: 비로그인

![MovieWiki게시판비로그인](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EA%B2%8C%EC%8B%9C%ED%8C%90%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8.gif)

- 비로그인 유저의 경우, 게시판 기능에 접근할 수 없다.
  - `게시글 작성`, `게시글 조회` 자체가 불가능 하며 우측 상단에 로그인 유저만 접근이 가능하다는 알럿이 뜬다. 

<br>

### 4) 유저 프로필

#### 회원가입 및 로그인

![MovieWiki회원가입](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.gif)

- 회원가입
  - 아이디, 이메일, 닉네임, 비밀번호, 지역, 나이에 대한 정보를 요청한다.
  - 회원가입을 하면, 자동으로 로그인이 된다. 
  - 회원가입시, 기본 프로필 이미지를 제공한다. 
  - 하단에 위치한 `다른 아이디로 로그인 하기`를 클릭하면, 회원 가입 모달은 꺼지고 로그인 모달이 켜진다.  

<br>

- 로그인과 로그아웃
  - 로그인 모달의 하단에 위치한 `회원 가입`을 클릭하면, 로그인 모달은 꺼지고 회원가입 모달이 켜진다. 
  - 로그인을 하면 네비바에 있는 회원가입, 로그인 버튼이 유저 프로필 이미지로 대체된다.
  - 네비바에 있는 유저 프로필 이미지를 클릭하면 로그아웃을 하거나 유저 프로필 페이지로 이동할 수 있는 모달이 뜬다. 

<br>

#### 회원가입 및 로그인: 오류창 

![MovieWiki회원가입오류](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EC%98%A4%EB%A5%98.gif)

- 회원 가입 혹은 로그인 중 오류가 발생하면 유저에게 알럿을 통해 알려준다.
  - `회원가입`: 이미 사용 중인 아이디와 이메일을 사용하여 회원 가입 시도
  - `회원가입`: 쉬운 비밀번호를 사용
  - `회원가입`: 비밀번호와 비밀번호 확인을 다르게 기입
  - `로그인`: 아이디 혹은 비밀번호를 틀린 경우
  - etc...

<br>

#### 유저 프로필 페이지: 내 정보 수정, 탈퇴 

![MovieWiki회원정보수정](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%88%98%EC%A0%95.gif)

- 활동 내역 확인
  - `내가 찜한 영화`, `내 게시글`, `내 댓글`, `내 평가`를 한 눈에 확인 할 수 있다.
  - 만약 나의 프로필 페이지가 아니라면, `내 평가`는 확인할 수 없다. (한줄평은 익명으로 진행되기 때문에 본인만 확인할 수 있다. )

<br>

- 회원 정보 수정
  - 닉네임, 프로필 이미지, 거주 지역, 나이를 수정할 수 있다. 

<br>

- 회원 탈퇴
  - 회원 정보 수정 모달의 하단에 위치한 회원 탈퇴를 누르면 회원 탈퇴를 확인하는 알럿창이 뜬다.
  - 회원 탈퇴가 되면, 자연스럽게 메인 홈으로 이동된다. 

<br>

#### 유저 프로필 페이지: 활동내역 확인 

![MovieWiki프로필페이지](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%ED%94%84%EB%A1%9C%ED%95%84%ED%8E%98%EC%9D%B4%EC%A7%80.gif)

- 내가 찜한 영화
  - 영화 상세 페이지에서 찜하기를 누른 영화 포스터를 확인 할 수 있다. 
  - 포스터에 마우스를 올리면, 줄거리와 타이틀이 표시된다. 
  - 포스터를 클릭하면 해당 영화의 상세 페이지로 이동한다. 

<br>

- 내 게시글과 내 댓글
  - 내가 작성한 게시글과 댓글을 확인할 수 있다. 
  - 게시글 제목을 클릭하면 해당 게시글의 상세 페이지로 이동한다.

<br>

- 내 리뷰
  - 내가 어떤 영화(포스터 이미지)에 어떻게 한줄평을 작성 했는지, 한 번에 확인 할 수 있다. 
  - 다른 사람을 프로필일 경우, 확인할 수 없다. (한줄평의 익명성을 보장하기 위함이다.)
  - 영화 포스터를 클릭할 시, 해당 영화의 상세 페이지로 이동할 수 있다. 

<br>

### 5) 모바일

![MovieWiki반응형](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/MovieWiki%EB%B0%98%EC%9D%91%ED%98%95.png)

<br>

## 3. 프로젝트 회고 

### 1)  박재경

> 배운 점

API를 통한 서버와 클라이언트가 통신하는 방법과 이를 통해 클라이언트의 기능을 구현하는 방법을 배웠다.



> 소감

나는 감자다. 나의 가장 큰 적은 어제의 내 코드이다. 🙃

하지만 내가 만든 서비스를 사용하는 것을 상상하면서 만드는 과정은 꽤나 재미있었다! 더하고 싶다!

<br>

### 2) 황상윤

이 정도로 무언가에 집중해서 오랬동한 진행한 일은 처음이였던거 같다. 자는 시간도 아껴가면서 진행했지만 그와는 반대로 시간이 순식간에 지나서 벌써 마감날이 되었다. (별로 한것도 없는거 같은데;;)  처음부터 욕심을 한가득 가지고 시작한 만큼 많이 힘들었지만 그만큼 힘든 만큼 결과물이 잘나와서 기분이 좋다. 물론 완벽하다고는 말은 못하지만 완벽한 하나의 홈페이지를 만드는 것도 누군가와 이정도로 하루조일 붙어서 협업해본 것도 처음이라는 것을 생각하면 만족스러운 것 같다. 하지만 역시 실력 부족으로 구현하지 못했던 기능들을 생각 하면 정말로 아쉽다. 그로 인해 공부의 필요성을 더욱 느끼게 되는 계기가 되었다. 거기에다 프로젝트를 하면서 겪었던 어려움들의 대부분이 기초가 부족해서 겪었다는 것 생각해보면 공부를 더 해야 할 것 같다. 몸은 힘들었지만 하면서 새로 배우고 느낀 감정을 생각해보면 개발을 공부하기 잘했다는 생각이 든다. 마지막으로 같이 힘써준 코코씨 감사합니다!!!