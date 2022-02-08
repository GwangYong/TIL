iOS에는 크게 소스코드를 통해 전환하는 방식과, Storyboard를 통해 전환하는 방식이 있다.

Stack을 쌓는 것처럼 Push 하는 방법과, 화면 위에 띄우는 Present 방식을 Segue와 Code로 알아보자.

<br>

### 기본 세팅

처음에는, Navigation Controller를 생성해서 이미자와 같이 만들어준다.

![기본 세팅](https://user-images.githubusercontent.com/59376200/152902229-b508d8de-cd1e-45b0-8e03-2911fea099cd.png)

여기에 보이는 버튼 4가지의 화면 전환 방식을 해 볼 것이며, Push, Present 방식들을 해보겠다.


<br>

## Segue로 Push

첫 방법은 **Segue로 Push**하는 방법이다. 

먼저 Main.storyboard에 ViewController를 하나 생성해주고 아래 영상과 같이 `control`을 누르고 클릭해준 후, 마우스 포인터로 만들어준 ViewController에 `Show` 로 연결해준다.

![Segue로 Push 방법](https://user-images.githubusercontent.com/59376200/152904009-de2bf9a1-8b26-4fb7-a325-764e935673f1.gif)

그러면 아래의 영상과 같이 Segue로 Push 버튼을 눌렀을 경우 화면 전환이 되며, 상단의 Back 버튼과 오른쪽으로 스와이프를 통해서 뒤로가기가 된다.

![Segue로 Push 시연](https://user-images.githubusercontent.com/59376200/152904155-0efdad49-f6ab-438b-9588-15edfa5e2cf3.gif)

<br>

## Segue로 Present

이번에도 ViewController 를 하나 생성해주고, 똑같이 `Control`을 누른 상태로 방금 생성한 ViewController 에 `Present Modally`로 연결해주면 된다.

![Segue로 Present 방법](https://user-images.githubusercontent.com/59376200/152903474-90504bfd-7040-403d-a138-aac910e82998.gif)

그러면 이번에는 영상과같이 마지막에 ViewController의 모습이 아래서 위로 화면이 생기는 Present 방식으로 된 것이 보인다.

![Segue로 Present 시연](https://user-images.githubusercontent.com/59376200/152903742-f52eeb6b-fc13-4bc1-bb1b-96a1b1ae5978.gif)

<br>

## Code로 Push


<br>

## Code로 Present

<!-- 

# 업데이트할 항목

전부 아래와같이 파일을 생성해주고, 그에맞게 연결해주고 각각 작성해야하는 pop, dismiss 코드들을 넣자.

나중에 이렇게 파일 추가해서, 코드 사용할 수 있도록 하고 popViewController나 dismiss 사용해서 뒤로 가는 버튼 기능 만드는 내용 추가하자

`command + N`을 눌러서 `Cocoa Touch Class`를 생성해준다. (이름은 자유지만, 여기서는 SeguePushViewController로 해주었다.)




 -->
