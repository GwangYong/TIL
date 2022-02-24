[블로그 포스팅 주소](https://jud00.tistory.com/entry/iOS-Push-Present-%ED%99%94%EB%A9%B4-%EC%A0%84%ED%99%98%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90)

iOS에는 크게 code를 통해 화면을 전환하는 방식과, 소스 코드를 필요로 하지 않는 세그웨이 방법을 통한 화면 전환 방식이 있다.

Stack을 쌓는 것처럼 Push 하는 방법과, 화면 위에 띄우는 Present 방식을 세그웨이와 소스 코드를 작성하여 만드는 2가지 방법에 대해서 알아보자.

<br>

## 기본 세팅

처음에는, Navigation Controller를 생성해서 이미자와 같이 만들어준다.

![기본 세팅](https://user-images.githubusercontent.com/59376200/152902229-b508d8de-cd1e-45b0-8e03-2911fea099cd.png)

여기에 보이는 버튼 4가지의 화면 전환 방식을 해 볼 것이며, Push, Present 방식들을 해보겠다.


<br>

## Segue Push 방식

첫 방법은 **Segue로 Push**하는 방법이다. 

> 세그웨이는 소스코드와 다르게 화면과 화면을 연결하기 위해서 소스 코드를 전혀 사용하지 않는다는 특징이 있다. 다만, 연결된 화면끼리는 스토리보드상에서 화살표로 연결되어있어 화면이 많아지면 보기 불편하다는 단점이 있다.

먼저 Main.storyboard에 ViewController를 하나 생성해주고 아래 영상과 같이 `우클릭`을 누르고 드래그하여, 마우스 포인터를 만들어준 ViewController에 `Show` 로 연결해주면 끝이다. 이제 Segue로 Push 버튼을 누르면 화면 전환이 될 것이다.

![Segue로 Push 방법](https://user-images.githubusercontent.com/59376200/152904009-de2bf9a1-8b26-4fb7-a325-764e935673f1.gif)

<br>

### Segue Push 뒤로가기

이번에는 뒤로가기 버튼도 만들어보자. 아래의 사진과 같이 `command + N`을 눌러서 **Cocoa Touch Class** 파일을 생성해준다. 

<img width="728" alt="스크린샷 2022-02-11 오후 7 00 55" src="https://user-images.githubusercontent.com/59376200/153572074-9a9d31f2-bb1f-4e3a-9aca-7b00c2406c03.png">

<img width="727" alt="스크린샷 2022-02-11 오후 7 06 04" src="https://user-images.githubusercontent.com/59376200/153572810-7df12554-2f6b-4408-a588-4e5e2391c85a.png">

<br>

그리고, 화면 전환을 하려는 ViewController를 아래의 사진처럼 storyboard에서 파일명으로 매칭해준다. (이러면 SeguePushViewController이라는 파일이 이 ViewController에 매칭된다.)

<img width="908" alt="스크린샷 2022-02-11 오후 7 03 53" src="https://user-images.githubusercontent.com/59376200/153572444-92413b29-d7fd-418a-bfae-67473758c365.png">

그 후, 뒤로가기 버튼을 `Control + 클릭`를 통해서 SeguePushViewController 파일에 **액션 함수(Action)** 로 정의해준다. 그리고 그 안에 아래의 코드를 작성하면 뒤로가기 버튼을 눌렀을 때, **push하기 전의 화면**으로 돌아가게된다.

```swift
self.navigationController?.popViewController(animated: true)
```

이제 아래의 영상과 같이 Segue로 Push 버튼을 눌렀을 경우 화면 전환이 되며 **상단의 Back 버튼, 오른쪽으로 스와이프, 만들어준 뒤로가기 버튼 3가지 방법**으로 뒤로가기가 된다.

![Segue로 Push, pop 시연](https://user-images.githubusercontent.com/59376200/153574768-d54d90af-d18c-4c5d-b55d-13be7600a285.gif)

<br>

## Segue Present 방식

이번에도 ViewController 를 하나 생성해주고, 똑같이 `우클릭`을 누른 상태로 방금 생성한 ViewController 에 `Present Modally`로 연결해주면 된다.

![Segue로 Present 방법](https://user-images.githubusercontent.com/59376200/152903474-90504bfd-7040-403d-a138-aac910e82998.gif)

이렇게되면 Segue로 Present 버튼을 클릭했을 경우에 화면 전환이 이루어질 것이다. 이제 뒤로가기 기능도 추가해보자! 위에와 준비하는 방법은 똑같다. 

<br>

### Segue Present 뒤로가기

1. Segue로 Push와 동일하게 **Cocoa Touch Class 파일을 생성**해준다. (여기서는 임의로 `SeguePresentViewController`로 임의로 정했다.)
2. Storyboard에서 화면 전환할 ViewController에 **"뒤로가기"** 버튼을 생성해주고, Class에 파일 이름을 먼저 만들어준 **Cocoa Touch Class 파일 이름과 동일하게 맞춘다.** (임의로 정한 `SeguePresentViewController`로 이름을 맞춰줌)
3. Assistant를 켜서 만들어준 뒤로가기 버튼을 `우클릭 + 드래그`해서 **액션함수로 정의**해준다.

마지막으로 들어갈 코드는 Push방법이 아닌, Present 방법으로 화면전환을 하였기에 아래의 코드를 작성해주면 된다.

```swift
self.presentingViewController?.dismiss(animated: true,completion: nil)
```

이제 아래처럼 화면 전환이 잘 되는걸 볼 수 있다.

![Segue로 Present 시연](https://user-images.githubusercontent.com/59376200/153577936-071bce85-e477-43a1-8133-f7b72f8a1fd6.gif)

<br>

## Code Push 방식

이번에는 Segue가 아닌, **코드를 이용하여 Push**를 해보자. 

우선 동일하게 ViewController를 하나 생성해준다. 그리고 그 ViewController에 이미지와 같이 **Storyboard ID에 값을 지정**해준다. (여기서는 Code로 Push하기 때문에, CodePush라고 임의로 지정해 주었다.)

![CodePush Storyboard ID Value](https://user-images.githubusercontent.com/59376200/152977985-557bd9e6-7ae0-47eb-ae25-ffb6625f0a12.png)

그리고 맨 처음 Storyboard에 만들어둔 `Code로 Push` 버튼을 아래와 같이 **ViewController.swift**에 `우클릭 + 드래그`를 통해서 **액션 함수(Action)** 로 정의해준다. 그러면 **@IBAction ...** 형식의 소스가 나타나게된다.

![CodePush 방법](https://user-images.githubusercontent.com/59376200/153128967-43d99578-65ef-4b37-aaa2-ba995d6dbec8.gif)


그리고 그 안에 아래와 같은 코드를 작성해주자.
```Swift
guard let viewController = self.storyboard?.instantiateViewController(withIdentifier: "자신이 만들어준 Storyboard ID값") else { return }
self.navigationController?.pushViewController(viewController, animated: true)
```

위의 코드는 **Storyboard에서 정의한 View Controller에 해당하는 ID값을 찾아서 인스턴스화**를 해주는 역할을 한다. 그리고, 2번째 코드를 통해 인스턴스화를 해준 viewController를 navigation 스택에 새로운 화면이 push된다.

추가로 **identifier**란, 스토리보드에서 뷰 컨트롤러를 구분할 수 있게 만들어주는 별명(?) 이라고 생각하면 된다.

이번에도 뒤로가기 버튼을 만들어보자.

<br>

### Code Push 뒤로가기

(이 방법은 Segue로 Push에서 설명한 뒤로가기와 방법이 동일하다. 하지만, 혹시 몰라서 조금 길게 다시 설명을 적어두었다.)

이번에는 설명할 내용도 없다. 왜냐하면 **Segue로 Push한 방법과 같기 때문**이다.

이유로는 연결만 Segue와 Code로 하는 방식이 다른거지 **화면 전환 방식은 Push로 같기 때문**에 pop만 해주면 된다.

1. Cocoa Touch Class 파일을 만든다.
2. 뒤로가기 버튼을 만들어주고, ViewController와 1번에 만들어준 파일 명을 동일하게 맞춰서 코드 작성이 가능하도록 한다.
3. 만들어준 뒤로가기 버튼을 액션함수로 정의해준다.
4. 아래의 코드를 액션함수 안에 정의하여, 버튼을 누르면 코드가 실행되도록한다.

```swift
self.navigationController?.popViewController(animated: true)
```

이제 실행하면 아래와같이 잘 되는것을 볼 수 있다.

![CodePush 시뮬레이션](https://user-images.githubusercontent.com/59376200/153580382-7eafb678-beb4-4daf-a452-9ebc86854c39.gif)


<br>

## Code Present 방식

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

이렇게하면, 화면이 제대로 Present 되는걸 볼 수 있다. 마지막으로 뒤로가는 방법도 알아보자!

<br>

### Code Present 뒤로가기

이 역시 Segue, Code 방식이 다른거지, 위의 Segue로 Present와 동일하기 때문에 **Segue로 Present 뒤로가기** 방식과 동일하다.

3번이나 했으니 이번에는 설명을 적지 않아도 괜찮을거같아 마지막에 액션 함수에 들어갈 코드만 적어두겠다.

```swift
self.presentingViewController?.dismiss(animated: true,completion: nil)
```

이렇게 하면 Present로 잘 나오는 모습을 볼 수 있다.

![CodePresent 시뮬레이터](https://user-images.githubusercontent.com/59376200/153581312-91c0d043-58d1-4167-a3c9-8bb991ccb9ae.gif)
