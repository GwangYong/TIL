### Django_templates  
```markdown
      <form action= = " " method = "POST">{% csrf_token %}
      
      </from>
```
- action은 서버로 데이터를 전달할 때 어떠한 url로 전달할 것인지를 나타낸다.<br>
      즉, 내가 action에 적어주는 경로로 데이터가 전달된다. `ex) ./createTodo/`
      
- mdthod에 POST 방식을 사용할 경우, {% csrf_token %}을 적어 주어야 한다.
      
- 함수에서 일정한 처리 후, 메인 페이지로 돌아가려면, 다시 메인 페이지의 url로 돌아가게 해야 하므로, HttpResponseRedirect 함수를 사용한다.
<br> HttpResponseRedirect 함수를 이용할 때는 우리가 원하는 url에 더 쉽게 매핑해주기 위해 reverse 함수를 이용한다.
    
    
### Django_Request and Response

- HttpResponse
    - ```markdown
      HttpResponse(data, content_type)
      ```
    - response를 반환하는 가장 기본적인 함수
    - 주로 html을 반환함.
    - ```markdown
      # string 전달하기
      HttpResponse("Here's the text of the web page.")
    
      # html 태그 전달하기
      response = HttpResponse()
      >>> response.write("<p>Here's the text of web page.</p>")
      ```
      
- HttpRedirect
    - ```markdown
      HttpResponseRedirect(url)
      ```
    - 별다른 response를 하지는 않고, 지정된 url페이지로 redirect를 함.
    - 첫번째 인자로 url을 반드시 지정해야 하며, 경로는 절대경로 혹은 상대경로를 이용할 수 있음.
    
- Render
    - ```markdown
      render(request(필수), template_name(필수),
            context=None, content_type=None,
            status=None, using=None)
      ```
    - `render`은 `httpResponse` 객체를 반환하는 함수로 template을 context와 엮어 `httpResponse`로 쉽게 반환해주는 함수이다.
    - template_name에는 불러오고 싶은 템플릿명을 적는다.
    - context에는 View에서 사용하던 변수(dictionary 자료형)를 html 템플릿에서 전달하는 역할을 한다.
    - key 값이 템플릿에서 사용할 변수 이름, value 값이 파이썬 변수가 된다.
    - ```markdown
      # views.py
      
      from django.shortcuts import render
      
      def my_view(request):
          name = "sgo"
          return render(request, 'app/index.html', {
              'name': name,
          }
      ```
     
     
### Serializer

Serializer는 Django Rest Framework에서 처음 나온 새로운 요소이다.<br>
사전적인 의미로는 직렬화를 해주는 무언가 정도로 생각하면 되는데, 간단하게 파이썬 데이터를 JSON 타입의 데이터로 변환해준다 정도로 생각하면 된다.

정확한 의미의 직렬화는 Django 프로젝트에서 내가 만든 모델로부터 뽑은 queryset, 즉 모델 인스턴스를 JSON 타입으로 바꾸는 것이다.<br>
그냥 Django 모델을 JSON으로 변환하기 위한 모양 틀 정도로 이해하면 좋을 것 이다.


### migrations & migrate

모델을 다 작성해줬으면, migrations와 migrate를 해줘야 한다.<br>
migrations는 테이블을 두어 마이그레이션 적용 여부를 추적하고, migrate를 할 때 문제가 있는지 미리 확인해준다. <br>
migrate는 데이터베이스 테이블에 적용시켜 주는데, migrate 과정은 model 작성, 수정 시에만 사용된다. 


### 가상환경은 왜 쓰이는건가?

프로젝트 별로 사용하는 패키지가 다른데, 사용하지 않는 패키지나 버전이 다른 패키지들을 독립적으로 관리하기 위해 가상환경을 사용한다. <br>
가상환경을 사용하면 가상환경 끼리는 패키지가 독립적으로 관리되서 필요한 것만 설치하여 사용할 수 있다.


### ViewSets & Router

REST 프레임워크는 `ViewSets`라는 추상 클래스를 제공한다. 이를 통해 개발자는 API의 상호작용이나 상태별 모델링에 집중할 수 있고, URL 구조는 기본 관례에 따라 자동으로 설정된다. <br>

`ViewSet`클래스는 `View`클래스와 거의 비슷하지만, `get`과 `put`메서드는 지원하지 않고, `read`와 `update`메서드를 지원한다. <br>

`ViewSet`클래스는 핸들러 메서드가 실제 뷰로 구체와할 때 이를 연결해주기만 하고, 이때 보통은 `Router`클래스를 사용하여 복잡한 URL설정을 처리한다.

`View`클래스 대신 `ViewSet`클래스를 사용하면, URL을 설정할 필요가 없다. <br>
`Router`클래스를 사용하면 뷰 코드와 뷰, URL이 관례적으로 자동 연결된다. 단지 뷰를 라우터에 적절히 등록해주기만 하면 된다. 그러면 REST 프레임워크가 알아서 다 해준다. 