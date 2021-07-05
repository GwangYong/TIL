# MVC Pattern 이란?

> MVC 패턴은 Model + View + Controller를 합친 용어이다.

![MVC Pattern](https://media.vlpt.us/images/sso0022/post/965b0cae-8f16-4d1f-994a-8603c1ab48fe/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.26.24.png)

<br>

## MVC 패턴 구조
- Model : 어플리케이션에 사용되는 데이터와 그 데이터를 처리하는 부분
- View : 사용자에게 보여지는 UI 부분
- Controller : 사용자의 입력(Action)을 받고 처리하는 부분

<br>

## MVC 패턴 동작
1. 사용자의 Action은 Controller에 들어오게 된다.
2. Controller는 들어온 Action을 확인한 후, Model 데이터를 업데이트한다.
3. Controller는 Model을 나타내줄 View를 선택한다.
4. View는 Model을 이용하여 사용자의 화면에 나타내준다.

<br>

## MVC 패턴의 장/단점
- 장점
    - 다른 패턴에 비해 코드량이 적다.
    - 많은 개발자들에게 친숙한 패턴이기 때문에 개발자들이 쉽게 유지보수할 수 있다.

- 단점
    - 코드 재사용성이 떨어지고, 유닛 테스트를 진행하기 어렵다.
    - 대부분의 코드가 Controller에 밀집되어 크기가 비대해지고 구조가 복잡해진다.
    - 코드가 복잡해지기 때문에, 프로젝트의 규모가 커질수록 유지보수가 힘들어진다.

<br><br>

# MVVM Pattern 이란?
> MVVM 패턴은 Model + View + View Model을 합친 용어이다.

![MVVM Pattern](https://t1.daumcdn.net/thumb/R720x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/aUYX/image/ykBFfLMPB4Gd0fa0G93N3f39uwM.png)

<br>

## MVVM 패턴 구조
- Model : 어플리케이션에 사용되는 데이터와 그 데이터를 처리하는 부분
- View : 사용자에게 보여지는 UI부분
- View Model : View를 표현하기 위해 만든 View를 위한 Model. View를 나타내주기 위한 Model이자 View를 나타내기 위한 데이터를 처리하는 부분

<br>

## MVVM 패턴 동작
1. 사용자의 Action은 View를 통해 들어오게 된다.
2. View에 Action이 들어오면, Command 패턴으로 View Model에 Action을 전달한다.
3. View Model은 Model에게 데이터를 요청한다.
4. Model은 View Model에게 요청받은 데이터를 응답해준다.
5. View Model은 응답 받은 데이터를 가공해서 저장한다.
6. View는 View Model과 Data Binding하여 화면에 나타내준다.

<br>

## MVVM 패턴의 장/단점
- 장점
    - MVC 패턴보다 유지보수에 좋다.
    - 새로운 개발자라도 빠르게 적응이 가능한 난이도와 복잡성
    - View와 Model 사이의 의존성이 없기 때문에, 독립적이여서 모듈화 하여 개발할 수 있다.

- 단점
    - 단순한 프로젝트를 개발할 때는 MVC 패턴에 비해 시간이 더 오래걸린다.
    - View Model의 설계가 쉽지 않다.

<br><br>

# Command Pattern 이란?
커맨드 패턴(Command Pattern)은 이벤트가 발생했을 때 실행될 기능이 다양하면서 변경이 필요한 경우에 이벤트를 발생시키는 클래스를 변경하지 않고 재사용할 때 유용하게 사용된다.<br>
실행될 기능을 "캡슐화"함으로써 주어진 여러 기능을 실행할 수 있는 재사용성이 높은 클래스를 설계하는 패턴이다.

<br>

# Data Binding 이란?
데이터 바인딩의 개념은 쉽게 말해서 Model과 UI 요소 간의 싱크를 맞춰주는 것 이라고 생각하면 된다.<br>
이 패턴을 통하여 View와 로직이 분리되어 있어도 한 쪽이 바뀌면 다른 한 쪽도 업데이트가 이루어지면서 데이터의 일관성을 유지하는것이 가능해진다.


<br>

<!-- > 참고
- https://beomy.tistory.com/43
- https://velog.io/@sso0022/iOS-MVC-%EC%99%80-MVVM -->