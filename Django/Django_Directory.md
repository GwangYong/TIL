# Django_Directory

```
Django_m
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

<br>

`manage.py` 는 [스크립트]()인데, 사이트 관리를 도와주는 역할을 한다.<br>
이 스크립트로 다른 설치 작업 없이, 컴퓨터에서 웹 서버를 시작할 수 있다.

`mysite` 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장된다. <br>이 디렉토리 내의 이름을 이용하여,(mysite.urls 와 같은 방식으로) 프로젝트의 어디서나 Python 패키지들을 import 할 수 있다.

`settings.py` 는 웹사이트 설정이 있는 파일이다. 현재 Django 프로젝트의 환경 및 구성을 저장한다.

`urls.py` 현재 Django 프로젝트의 URL 선언을 저장한다. Django 로 작성된 사이트의 '목차'라고 할 수 있다.

`wsgi.py` 는 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점이다.

`__init__.py` 는 Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일이다.

### Django의 동작 원리(구조)

- Django의 구조(MTV Pattern)
    - Model(데이터 관리)
    - Template(사용자가 보는 화면)
    - View(중간 관리자)
    
- Django의 동작 원리
    - 사용자가 1번 강의를 보겠다고 요청을 보냄(URL 주소 입력)
    - View(중간 관리자)는 받은 요청을 확인하고, Model(데이터 관리)에 1번 강의를 찾아달라고 지시를 내림.
    - Model(데이터 관리)은 Database에서 1번 강의를 찾아서 View(중간 관리자)에게 전달
    - View(중간 관리자)는 1번 강의를 Template에 전달하여, HTML 파일과 조합하여 화면을 사용자에게 전달.
    
![Django MTV Pattern](https://i.imgur.com/7wc39KX.png)

    