# HTTP

```markdown
### HTTP 통신
Client의 요청(Request)이 있을 때만 서버가 응답(Response)하여 해당 정보를 전송하고, 곧바로 연결을 종료하는 방식. <br>
쉽게 풀어서 얘기하면, "나는 이렇게 줄 테니 너는 이렇게 받고 난 너가 준것을 그렇게 받을게" 라고 보면 된다.
```

HTTP 통신은 기본적으로 `요청(Request)`과 `응답(Response)`으로 이루어져 있다.<br>

클라이언트가 서버에 요청을 보내면, 그에 맞는 응답 결과를 돌려주고, 클라이언트는 사용자에게 서버로부터 응답받은 결과를 보여주는 것 이다.

![HTTP](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile21.uf.tistory.com%2Fimage%2F992C024B5A9AA3E2123E44)

HTTP 통신은 기본적으로 연결이 되어 있지 않다.<br>

즉, 클라이언트가 서버에 요청을 보내고 응답을 받으면 그것으로 통신이 종료되는 **단방향 통신**이다. 서버는 클라이언트가 웹 사이트에 접속해 있는지 알 수 없다.

![종료](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F994FFC435A9AAAF93275B3)

위의 사진과 같이 클라이언트가 서버에 요청을 보내고, 서버로부터 필요한 파일을 모두 받고나면 접속이 종료(Connection Close)된다.<br>

연결(Connection)이 계속되어 있지 않다는 것이 HTTP 통신의 특징이다.<br>

요청을 보내고 받을 떄, 그 정보들을 패킷(Packet)이라는 작은 조각에 실어서 보내게 되는데, 패킷은 크게 `헤더(Header)`와 `바디(Body)`로 구성되어 있으며 `Header`에는 보내는 사람의 주소, 받는 사람의 주소, 패킷의 생명기간(TTL, Time To Live) 등이 담겨있고, `Body`에는 우리가 전하고자 하는 실제 내용이 들어있다.

HTTP 프로토콜은 일반적으로 TCP/IP 통신 위에서 동작하며, 기본 포트는 80번이다.

<br>

### HTTP 주요 메소드 4가지

|  `메소드`  |     `역할`     |
|:----------:|:-------------:|
| GET |  GET을 통해 해당 리소스를 조회한다. 리소스를 조회하고 해당 도큐먼트에 대한 자세한 정보를 가져온다.  |
| POST |   POST를 통해 해당 URI를 요청하면 리소스를 생성함.    |
| PUT | PUT을 통해 해당 리소스를 수정한다. |
| DELETE | DELETE를 통해 리소스를 삭제한다. |


- **GET** : GET은 보통 리소스를 조회할 때 사용된다. 메시지 바디를 통해서 데이터를 전달할 수 있지만, 지원하지 않는 곳이 많기 때문에 권장하지 않는다.
- **POST** : POST는 데이터 요청을 처리하고, 메시지 바디를 통해 서버로 데이터를 전달한다. 주로 신규 리소스를 등록하거나 프로세스 처리에 사용된다.
- **PUT** : PUT은 리소스가 있으면 대체하고 리소스가 없으면 생성한다. 쉽게 말해서 덮어쓴다고 보면 된다.
- **PATCH** : PATCH는 주요 메소드는 아니지만, PUT과 비슷하다. 마찬가지로 리소스를 수정할 때 사용하지만, PUT과 다르게 리소스의 `일부분만 변경`할 수 있다.
- **DELETE** : DELETE는 리소스를 제거할떄 사용된다


<br>

### HTTP 상태 코드

**`2xx - 성공`**

>200번대의 상태 코드는 대부분 성공을 의미한다.

    - 200 : GET 요청에 대한 성공
    - 204 : No Content 성공했으나, 응답 본문에 데이터가 없음
    - 205 : Reset Content 성공했으나, 클라이언트의 화면을 새로고침 하도록 권고
    - 206 : Partial Content 성공했으나, 일부 범위의 데이터만 반환
    
<br>

**`3xx - 리다이렉션`**

>300번대의 상태 코드는 대부분 클라이언트가 이전 주소로 데이터를 요청하여, 서버에서 새로운 URL로 리다이렉트를 유도하는 경우이다.
    
    - 301 : Moved Permanently 요청한 자원이 새 URL에 존재함
    - 303 : See Other 요청한 자원이 임시 주소에 존재함
    - 304 : Not Modified 요청한 자원이 변경되지 않았으므로, 클라이언트에서 캐싱된 자원을 사용하도록 권고. <br>
    
<br>
    
**`4xx - 클라이언트 에러`**

>400번대의 상태 코드는 대부분 클라이언트가 잘못된 경우이다.<br>
유효하지 않은 자원을 요청했거나 요청이나 권한이 잘못된 경우 발생한다. 가장 익숙한 상태 코드는 404 코드이다. 요청한 자원이 서버에 없다는 의미이다.

    - 400 : Bad Request 잘못된 요청
    - 401 : Unauthorized 권한 없이 요청. Authorization 헤더가 잘못된 경우
    - 403 : Forbidden 서버에서 해당 자원에 대해 접근 금지
    - 405 : Method Not Allowed 허용되지 않은 요청 메서드
    - 409 : Conflict 최신 자원이 아닌데 업데이트 하는 경우
    
<br>
    
**`5xx - 서버 에러`**

> 500번대의 상태 코드는 서버 쪽에서 오류가 난 경우이다.

    - 501 : Not Implemented 요청한 동작에 대한 서버가 수행할 수 없는 경우
    - 503 : Service Unavailable 서버가 과부화 또는 유지 보수로 내려간 경우
        
<br>
    
### URL (Uniform Resource Locator)

- URL이란?
    - 인터넷 상의 자원의 위치
    - 특정 웹 서버의 특정 파일에 접근하기 위한 경로 혹은 주소
- URL의 표현
    - 접근 프로토콜:// IP주소 또는 도메인 이름 (:포트번호) / 자원의 경로 / 자원의 이름
![URL](https://joshua1988.github.io/images/posts/web/http/url-structure.png)
    
- URI (Uniform Resource Identifier)
    - 요청하는 자원의 식별자 (규약)
    - 자원을 고유하게 식별하고 위치를 지정할 수 있다.
    - URI의 하위 개념으로 URL이 포함됨. 즉, URI > URL
    
<br>

# HTTPS

![HTTPS](https://miro.medium.com/max/1400/0*wokY_yLExsbG-vkl.jpg)

- HTTPS는 웹사이트를 SSL/TLS 인증서로 보안하는 경우 URL 창에 표시된다.
- HTTPS는 HTTP의 보안이 강화된 버전이다.
- HTTPS는 SSL 프로토콜을 통해 세션 데이터를 암호화 한다.
