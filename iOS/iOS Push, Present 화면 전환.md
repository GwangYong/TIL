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

이번에는 Segue가 아닌, **코드를 이용하여 Push**를 해보자. 

우선 동일하게 ViewController를 하나 생성해준다. 그리고 그 ViewController에 이미지와 같이 **Storyboard ID에 값을 지정**해준다. (여기서는 Code로 Push하기 때문에, CodePush라고 임의로 지정해 주었다.)

![CodePush Storyboard ID Value](https://user-images.githubusercontent.com/59376200/152977985-557bd9e6-7ae0-47eb-ae25-ffb6625f0a12.png)

그리고 맨 처음 Storyboard에 만들어둔 `Code로 Push` 버튼을 아래와 같이 **ViewController.swift**에 `Control + 드래그`를 통해서 **액션 함수(Action)** 로 정의해준다. 그러면 **@IBAction ...** 형식의 소스가 나타나게된다.

![CodePush 방법](https://user-images.githubusercontent.com/59376200/153128967-43d99578-65ef-4b37-aaa2-ba995d6dbec8.gif)


그리고 그 안에 아래와 같은 코드를 작성해주자.
```Swift
guard let viewController = self.storyboard?.instantiateViewController(withIdentifier: "자신이 만들어준 Storyboard ID값") else { return }
self.navigationController?.pushViewController(viewController, animated: true)
```

위의 코드는 **Storyboard에서 정의한 View Controller에 해당하는 ID값을 찾아서 인스턴스화**를 해주는 역할을 한다. 그리고, 2번째 코드를 통해 인스턴스화를 해준 viewController를 navigation 스택에 새로운 화면이 push된다.

추가로 **identifier**란, 스토리보드에서 뷰 컨트롤러를 구분할 수 있게 만들어주는 별명(?) 이라고 생각하면 된다.

이제 실행하면 아래와같이 잘 되는것을 볼 수 있다.

![CodePush 시뮬레이션](https://user-images.githubusercontent.com/59376200/152978356-ab343b4b-8f2d-495e-b82c-b6ec08fff3ad.gif)


<br>

## Code로 Present

이 방법은 위의 Code로 Push하는 많이 동일하다.

새로운 ViewController을 생성해준 후, 이 ViewController의 **Storyboard ID 값을 지정**해준다 (여기서는 Code로 Present하기 때문에, CodePresent로 임의로 지정해주었다.)

![CodePresent Storyboard ID Value](https://user-images.githubusercontent.com/59376200/152978459-d71bdd37-e0df-4db5-b029-8b9db5589f07.png)

이번에도 마찬가지로 Storyboard에 만들어둔 `Code로 Present` 버튼을 **ViewController.swift**에 액션 함수로 정의해주고

![CodePresent 방법](https://user-images.githubusercontent.com/59376200/153128816-7990a5d9-9065-4c77-8c76-c21ba857714c.gif)

그 액션 함수 안에 아래의 코드를 작성하면 된다.

```swift
guard let viewController = self.storyboard?.instantiateViewController(withIdentifier: "자신이 만들어준 Stroyboard ID의 값") else { return }
self.present(viewController, animated: true, completion: nil)
```

이렇게 하면 Present로 잘 나오는 모습을 볼 수 있다.

![CodePresent 시뮬레이터](https://user-images.githubusercontent.com/59376200/152978886-66b3eafa-dd7b-48a2-a8b7-c605410e7cab.gif)

<br>

Code로 Present와 Push는 ViewController에 Storyboard ID 값을 지정하고 액션함수로 정의하고 하는 방식은 동일하며, 그 안에 들어가는 코드 부분만이 다르다.

<!-- 

# 업데이트할 항목

전부 아래와같이 파일을 생성해주고, 그에맞게 연결해주고 각각 작성해야하는 pop, dismiss 코드들을 넣자.

나중에 이렇게 파일 추가해서, 코드 사용할 수 있도록 하고 popViewController나 dismiss 사용해서 뒤로 가는 버튼 기능 만드는 내용 추가하자

`command + N`을 눌러서 `Cocoa Touch Class`를 생성해준다. (이름은 자유지만, 여기서는 SeguePushViewController로 해주었다.)




 -->
