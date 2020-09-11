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
    