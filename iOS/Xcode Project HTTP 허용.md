아래는, iOS에서 Server에 POST 요청을 보낼 때 발생한 에러문이다.
```
The resource could not be loaded because the App Transport Security 
policy requires the use of a secure connection.
```

https를 사용해야하지만, 테스트이기 때문에 http로 사용했다가 에러가 발생해서 해결하였다.

<br>

자, 이 에러는 Xcode 프로젝트에서 http 통신이 허용되지 않아서 발생하는 오류이다. 이는 디폴트값인듯 하다.

http 통신을 허용하기위해 내가 찾아서 에러를 고친 방법은 `Info.plist`에서 허용해주는 방법이다.

![스크린샷 2021-11-29 오후 4 26 18](https://user-images.githubusercontent.com/59376200/143825454-f880e0dd-d7a9-4c87-9268-3d53b8c2cc5b.png)

위의 이미지처럼, `Info.plist`의 `App Transport Security Settings`에 마우스를 가져가면 +버튼이 나오는데, 이 + 버튼을 눌러서 하위 항목(?)을 생성해주고, `Allow Arbittrary Loads`를 추가해주고 Value를 `YES`로 해주면 된다.