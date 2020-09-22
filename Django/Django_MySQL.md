# Django와 MySQL 연결하기

> mysql과 mysqlclient는 다른거같음. mysqlclient라는 라이브러리를 통하여 MySQL과 DB를 연동시킬 수 있다.

먼저, pymysql을 설치해준다.

```markdown
pip install pymysql
```

추가로 settings.py의 맨 위에 작성해준다.
```markdown
import pymysql

pymysql.install_as_MySQLdb()
```

settings.py의 DATABASES 부분을 수정해준다. <br>
원래는 sqlite를 사용하므로, 그 부분을 수정해서 MySQL DB와 연결해준다.

![MySQL](https://mblogthumb-phinf.pstatic.net/MjAxODAxMTVfMTYz/MDAxNTE1OTUwNzIxNTQy.H2D-swxMO-KFHiqMIpyiU1L-3TJE51N-ZhlNxZwAYFcg.JHW5e0Db5-AlPFRGrwl3sJo7Trrc5JC76Ajn5pHhsFAg.PNG.uko02111/image_7402045451515950688023.png?type=w800)



"mysql -uroot -p" 명령어를 이용하여 비밀번호를 입력하고 로그인 할 수 있다. <br>
정삭적으로 로그인이 되면 쉘이 "mysql>"로 변경된 걸 확인할 수 있다.

"mysql>"쉘에서 로그아웃 명령어는 "exit" 또는 "quit"이며,
MySQL 서버 종료 명령어는 "mysql.server stop"이다.

### MySQL 삭제 방법