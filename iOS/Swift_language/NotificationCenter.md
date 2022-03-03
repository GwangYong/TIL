## NotificationCenter(NSNotificationCenter)

NotificationCenter란, 등록된 이벤트가 발생되면 해당 event에 대한 행동을 행하는 데이터 전달 방식 중 하나이다. 간단히 말하면 팀장이 팀원(옵저버)에게 해야할 업무를 필요한 시점에 전달해주는 것이라 생각하면 쉬울 것 같다.

이는 적은 코드로 간단히 구현할 수 있으며, 앱 내의 어떠한 곳에서 메시지를 던져주면 다른 어떠한 곳에서든 이 메시지를 받아서 처리할 수 있다는 장점이 있다.

<br>

## NotificationCenter 발송

NotificationCenter에서는 post가 가장 중요한 핵심이다. 팀원(Name) 에게 일을 맡기는 작업이다.

```swift
NotificationCenter.default.post(name: NSNotification.Name("Example"), object: text)
```

위의 코드는 **Example** 라고 하는 팀원의 이름이 불리면, text 라는 object를 보내준다. Example라는 팀원에게 일을 하라고 말하며, 일을 하는데 필요한 text라는 부가 자료를 주는것이라 생각하자.

- name : 전달하고자 하는 notification의 이름이다. 일을 시킬 팀원의 이름을 부를때 사용되는 이름이라고 생각하면 된다.
- object : 옵저버에게 보내려 하는 객체이다. 전달할 객체가 없다면 nil을 할당해주면 된다. 
- userInfo : Notification과 관련된 값을 뜻한다. (지금 설명에서는 userInfor를 사용하지 않을 것이다.)

<br>

## NotificationCenter 수신

위에서 post를 하여 해야할 일을 보내주었으니, 이번에는 일을 담당할 팀이 "네 알겠습니다." 라고 말하며 자신이 해야할 일을 받는것이다.

여기서 사용하는것이 addObserver이다. 아래의 코드를 보자

```swift
func NotificationAlert() {
    NotificationCenter.default.addObserver(
        self,
        selector: #selector(dataReceivedExample(_:)),
        name: NSNotification.Name("Example"),
        object: nil)
}
```

이 코드는 Example 라는 notification이 생기면, dataReceivedExample(_:) 라는 함수를 실행시키는 것이다.

즉, Example 에게 dataReceivedExample(_:) 라는 함수에 있는 일을 한다는 것이다.



<!-- 

[ ] 글 작성 멈추고, 우선 밑에 참고 블로그들 보면서 확실히 이해하자

[ ] 내가 작성한 팀장, 팀원 일 배분 예시가 맞는지 검토

[ ] 지금 예시 Xcode에 작성해뒀는데, 이거 아래 참고 블로그에 있는거 따라한거니까 __다른 방식__ 으로 내가 예시 생각해서 만들어서 이미지 올리고 하자. 블로그 올리기 좋을듯
즉, 예시 지금만든거 말고 다른 방식으로 내가 생각하고 만들어서 캡쳐해서 `코드랑 설명, 이미지` 다 변경
 
[ ] 발송, 수신 이렇게 적은부분 다시 생각해보고 수정할거면 수정하기

[ ] 글 다 작성하면, 중요한 부분 표시하기

[ ] 이거 글 작성하자마자 Blog에 바로 올리자. 정리해두고 시간 지나면 또 올리기 힘들어지니까 이거 다 작성 열심히해서 3/4일 오늘 posting 하자.

 -->



<!-- 

 > Reference
 > - [Notification, NotificationCenter](https://leeari95.tistory.com/49#%E2%9C%94%EF%B8%8F%C2%A0notificationcenter%EB%A1%9C-post%ED%95%98%EA%B8%B0-%EB%B0%9C%EC%86%A1%ED%95%98%EA%B8%B0)
 > - [Apple Developer Documentation](https://developer.apple.com/documentation/foundation/notificationcenter)
 > - [데이터 직접 전달 방식(4) - NotificationCenter을 통해 전달](https://roniruny.tistory.com/152)

  -->