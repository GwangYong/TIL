
오늘은 평소와 다름없이 공부한걸 TIL 하려고 github에 push를 하려고 하였는데 에러가 뜨면서 push가 안 되는 일이 생겼습니다. 아래와 같은 오류가 났다.

```bash
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead. 
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information. fatal: unable to access 'https://github.com/yagi4168/TIL.git/': The requested URL returned error: 403
```

인터넷으로 찾아보니 2021년 8월 13일부로 Github에서 push, clone, pull의 Git 작업 인증 시에 비밀번호 대신 토큰을 사용하도록 변경되었다고 나와서 알아보았다.

<br>

# Personal access token 생성하기
우선, 자신의 github에 들어가서 사진과 같이 오른쪽 위를 클릭하여 Sign out 위에 있는 Settings으로 들어간다.

<img src = "https://blog.kakaocdn.net/dn/bJfkQV/btrb7zY2vO2/9eilW7ZJBb6kmO3TWikRcK/img.png" width = "50%" height="50%">

그 후에 왼쪽의 사이드 바에서 Developer settings를 클릭하여 들어간다.

<img src = "https://blog.kakaocdn.net/dn/NQcFa/btrcjab8fUk/VMCUQUyrez99mgYVgpZjs0/img.png" width = "50%" height="50%">

그리고 또다시 왼쪽의 사이드 바에서 Personal access tokens를 클릭하여 들어가서, 오른쪽 위의 Generate
new token을 클릭한다.

<img src = "https://blog.kakaocdn.net/dn/BirMb/btrb9QeIKx3/5nBKCQgUsdIUCiLCorz65K/img.png" width = "50%" height="50%">

<img src = "https://blog.kakaocdn.net/dn/b95kTV/btrb9P1bDtB/L9aTQvPuCwRqVy0DFmdjF1/img.png" width = "50%" height="50%">

<br>

Generate new token을 클릭하셨으면 이제 토큰을 생성하는 단계이다. 아래와 같은 화면이 보인다.

- Note: 어떠한 용도의 토큰인지 알 수 있도록 이름을 지어준다.
- Select scopes: 해당 토큰에 부여할 권한을 선택한다. (자신의 용도에 맞게 설정)
(레파지토리 관리만이 목적이라면 repo만 클릭해주면된다. (그러면 그 하위의 항목도 체크됨)

<img src = "https://blog.kakaocdn.net/dn/bgiJWI/btrb7bD83ru/uNOUfH2DezQwNTw3kpXttK/img.png" width = "50%" height="50%">

<br>

여기까지 했다면, 맨 아래의 초록색 버튼인 Generate token을 클릭하셔서 토큰을 생성해준다.

<img src = "https://blog.kakaocdn.net/dn/t9izv/btrb66P02Q3/Zxmu0mmXCwMW6nmTNaCW5k/img.png" width = "50%" height="50%">

자 여기까지 하셨다면 아래와 같은 토큰이 생성된다. 이제 이 토큰을 사용해 줄 건데, **다음에 다시 토큰 값을 확인할 수 없으니 이 토큰을 안전한 곳에 저장한다.** 

<br>

여기까지 했으면, 이제 git push, clone, pull 등을 하실 때 PW를 입력하라고 나오면 비밀번호 대신에 방금 생성해준 토큰 값을 입력하면 된다. 하지만 mac os 환경에서 여기까지 하고 git push 명령어를 하였는데,

```shell
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access to ken instead. ... The requested URL returned error: 403
```

이처럼 403 에러가 계속 뜬다면 아래를 보고 따라하자.

<br>

# The requested URL returned error: 403 에러
이 경우는 키체인에 저장되어있는 비밀번호 때문에 나는 것이라고 한다. 매우 간단하게 해결해 보자.

우선 cmd + space bar를 눌러서 Spotlight에서 키체인 접근을 찾아서 실행해주자
<img src = "https://blog.kakaocdn.net/dn/p2e4Q/btrcb78mXqn/WGheOfLR4FNetWU42qArR1/img.png" width = "50%" height="50%">

<br>

그러면 아래와 같이 나올 텐데, 키체인에 "로그인"이라고 되어있는 github.com을 클릭하여 들어가자

<img src = "https://blog.kakaocdn.net/dn/ob0Cz/btrb7yFUUBB/M7bQop6yURlEDvo7SJK621/img.png" width = "50%" height="50%">

자 그러면 아래와 같은 화면이 나올거다.

<img src = "https://blog.kakaocdn.net/dn/T82Kk/btrb83ejNO7/yIHYs8mig0sF8iboDzIX1K/img.png" width = "50%" height="50%">

이제 암호 보기 오른쪽의 네모 박스를 체크하여 그 안에 있는 github의 비밀번호를 아까 고이 모셔둔 토큰으로
대체해주시면 이제 push를 했을 때 문제없이 될것이다.