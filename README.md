# :information_desk_person: SSAFYED_IN
SSAFY 교육생들을 위한 커뮤니티 서비스



## :one: Overview

>SSAFY 교육생만의, SSAFY 교육생들을 위한 커뮤니티 서비스!
>
>"선후배간의 소통과 취업정보까지 한 번에!"



- SSAFYED_IN 서비스는 SSAFY 교육생간의 소통이 어려운 점을 해소하기 위해 오픈된 공간을 제공하여 서로 교류할 수 있는 환경을 제공해주는 서비스 입니다.
- 프로젝트 기간: 20.01.13 - 20.02.28





## :two: Tech Stack

![image](https://user-images.githubusercontent.com/52685247/82723595-ea0a5180-9d0a-11ea-851a-e2157ae8f4c0.png)

:round_pushpin: **Frontend** : `Vue.js`

:round_pushpin: **Backend** : `Django`

:round_pushpin: **Database** : `MySQL`

:round_pushpin: **Development Environment** : Python 3.7.4, Django 2.2.7, Node.js higer than 10.16.x, Vue CLI higher than 4.2.x

:round_pushpin: **Using Editor** : Visual Studio Code





## :three: Quick Start

### :pushpin: Local에서 실행

:heavy_check_mark: <b>Backend Installation & Run</b>

```
cd ssafy-backend
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata total.json
python manage.py runserver
```

:heavy_check_mark: <b>Frontend Installation & Run</b>

```
cd ssafy-frontend
npm instlal
npm run serve
```





### :pushpin: 배포 환경에서 실행

- http://i02b102.p.ssafy.io/ 주소를 접속해서 볼 수 있습니다.







## :four: Homepage Configuration

#### (1) 메인 페이지

- 포트폴리오, 채용 공고, 공모전 게시글, SSAFYED 人 랭크 등의 최근 게시물을 간략하게 표시하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82724105-aca7c300-9d0e-11ea-98b1-2a93f3b7ef00.png)

![image](https://user-images.githubusercontent.com/52685247/82724233-977f6400-9d0f-11ea-981d-8f4099803258.png)



#### (2) 회원 권한 변경(인증 단계)

- SSAFY 교육생은 학생증을 통해, 기업 채용담당자는 사원증을 통해 인증과정을 거치게 됩니다.
- 인증을 통해 게시글 등록 권한을 가지게 됩니다.

![image](https://user-images.githubusercontent.com/52685247/82724148-fabcc680-9d0e-11ea-928d-e0ea095c35b9.png)





#### (3) 포트폴리오 목록 페이지

- SSAFY SSAFY 사용자들이 등록한 포트폴리오 중 '공개' 설정된 포트폴리오들을 보여줍니다.
- 사용자들이 작성한 포트폴리오를 서로 공유할 수 있도록 하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82724246-b120ab80-9d0f-11ea-84fb-da816eb13a92.png)





#### (4) 공모전 게시판

- 공모전 홍보, 공모전 팀원을 모집하는 글을 올려 참가자들을 모집하는 페이지
- 공모전 이미지, 필요 기술 스택과 같은 필수 요건은 바로 확인할 수 있도록 목록에서도 표시되도록 하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82724840-d7484a80-9d13-11ea-9c72-e77a5e5fcf88.png)





#### (5) 채용 게시판

- 채용담당자가 원하는 인재를 채용할 수 있도록 요구하는 기술 스택, 근무 조건 등을 포함한 게시글을 작성하는 페이지

![image](https://user-images.githubusercontent.com/52685247/82724883-0a8ad980-9d14-11ea-9857-12d8e47c09ef.png)





#### (6) 메세지 보내기 기능

- 사용자간에 메일 전송외에 메세지를 통해 직접 연락할 수 있는 기능
- 보내고자 하는 사용자의 개인 페이지로 접근하여 메세지를 보낼 수 있도록 하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82724934-7a995f80-9d14-11ea-9e3a-2168ff69bdb6.png)



#### (7) 포트폴리오 등록 페이지

- 자신의 포트폴리오를 소개하기 위한 서비스 개요, 이미지, 기술 스택 등 포트폴리오를 소개하는 데에 필요한 모든 내용을 기입할 수 있도록 하였습니다.

- filepond를 통해 drag&drop으로 이미지를 업로드할 수 있도록 하였습니다.
- Public / Private 기능을 통해 개인적으로 포트폴리오를 저장할 수 있도록  하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82727270-72492080-9d24-11ea-8b01-80b548dd93d6.png)

![image](https://user-images.githubusercontent.com/52685247/82729495-fc988100-9d32-11ea-90b4-1cf6b69d913b.png)





#### (8) 공모전 등록

- 공모전에 함께 참여할 팀원을 모집하는 글을 작성할 수 있는 기능
- 공모전 이미지, 활동 기간, 필요 기술 스택 등의 공모전 지원 시 확인해야 할  내용을 작성할 수 있도록 하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82729727-d4118680-9d34-11ea-957e-15ca4d79a8ed.png)

![image](https://user-images.githubusercontent.com/52685247/82729751-163ac800-9d35-11ea-9bfb-0c368c83e0c0.png)



#### (9) 공모전 지원

- 공모전 목록 페이지에서 공모전을 선택하여 지원하는 기능
- 공모전 지원 시 공모전을 작성한 사용자에게 메일을 통해 알림을 보내 두 사용자가 메일과 메세지를 통해 연락할 수 있도록 하였습니다.

![image](https://user-images.githubusercontent.com/52685247/82729796-4bdfb100-9d35-11ea-9429-d7832a447924.png)

![image](https://user-images.githubusercontent.com/52685247/82729807-6a45ac80-9d35-11ea-9dc8-363fddfa4a1f.png)





#### (10) 전송된 메세지 확인

- 사용자끼리 주고받은 메세지를 한번에 볼 수 있고, 바로 답장할 수 있는 페이지 구현

![image](https://user-images.githubusercontent.com/52685247/82729522-2d78b600-9d33-11ea-8dbb-2c895f713ab8.png)