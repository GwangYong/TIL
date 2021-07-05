# MVC Pattern 이란?

> MVC 패턴은 Model + View + Controller를 합친 용어이다.

![MVC Pattern](https://media.vlpt.us/images/sso0022/post/965b0cae-8f16-4d1f-994a-8603c1ab48fe/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.26.24.png)

<br>

## MVC 패턴 구조
- Model : 어플리케이션에 사용되는 데이터와 그 데이터를 처리하는 부분
- View : 사용자에게 보여지는 UI 부분
- Controller : 사용자의 입력(Action)을 받고 처리하는 부분

## MVC 패턴 동작
1. 사용자의 Action은 Controller에 들어오게 된다.
2. Controller는 들어온 Action을 확인한 후, Model 데이터를 업데이트한다.
3. Controller는 Model을 나타내줄 View를 선택한다.
4. View는 Model을 이용하여 사용자의 화면에 나타내준다.

## MVC 패턴의 장/단점
MVC 모델은 View와 Model 사이의 의존성이 높아, 유지보수가 어렵다

<br><br>

# MVVM Pattern 이란?
> MVVM 패턴은 Model + View + View Model을 합친 용어이다.

![MVVM Pattern](https://t1.daumcdn.net/thumb/R720x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/aUYX/image/ykBFfLMPB4Gd0fa0G93N3f39uwM.png)

<br>

MVVM 패턴은 Model / View / ViewModel로 이루어져 있는 패턴이다.
Model = 데이터 캡슐화
View = 시각적 요소, 컨트롤 표시..(UI 반영하는 코드 & 생명주기 관리 코드 등)
ViewModel = Model 데이터를 View에 맞게 가공 및 처리 (View에 반영될 데이터 비즈니스 로직 담당)

## MVVM 패턴 구조
- Model : 어플리케이션에 사용되는 데이터와 그 데이터를 처리하는 부분
- View : 사용자에게 보여지는 UI부분
- View Model : View를 표현하기 위해 만든 View를 위한 Model. View를 나타내주기 위한 Model이자 View를 나타내기 위한 데이터를 처리하는 부분

## MVVM 패턴 동작
1. 사용자의 Action은 View를 통해 들어오게 된다.
2. View에 Action이 들어오면, Command 패턴으로 View Model에 Action을 전달한다.
3. View Model은 Model에게 데이터를 요청한다.
4. Model은 View Model에게 요청받은 데이터를 응답해준다.
5. View Model은 응답 받은 데이터를 가공해서 저장한다.
6. View는 View Model과 Data Binding하여 화면에 나타내준다.

## MVVM 패턴의 장/단점


<br><br>

# Command Pattern 이란?

`Command = 명령어`
실행될 기능을 추상화, 캡슐화하여 한 클래스에서 여러 기능을 실행할 수 있도록 하는 패턴

# Data Binding 이란?




# MVC vs MVVM Pattern

<br>

<!-- > 참고
- https://beomy.tistory.com/43
- https://velog.io/@sso0022/iOS-MVC-%EC%99%80-MVVM -->