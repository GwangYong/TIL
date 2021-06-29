## Optional이란??

애플에서 swift언어는 type-safety한 언어라고 주장한 대로, optional은 그 중요한 요소 중 하나이다.<br>
optional은 "?"를 통해 표현되며, 그 의미는 `이 변수에는 값이 들어갈 수도 있고, 아닐 수도 있어` 라는 뜻이다.


## Optional 예시

일단 아래의 예시를 보자.
```swift
var name: String = "Jack"   // OK
name = nil                  // Error ('nil' cannot be assigned to type 'String')
```

아래와같이 변수에 값을 넣어주고, 그 값에 다시 nil로 지정을 해줬는데 오류가 났다. 이유가 뭘까?

기본적으로 Swift 에서 변수를 선언할 경우에는 optional이 아닌 값(non-optional)을 지정해주어야 한다.
즉, 변수를 선언할 경우 nil이 아닌 값(non-nil)을 할당해주어야 한다는 뜻이다.
만약, 옵셔널이 아닌 변수에 nil을 설정해주면, 위와 같이 컴파일러는 nil 값을 할당할 수 없다며 오류를 발생시킬 것 이다.

이 오류를 없애보자!
```swift
var name: String? = "Jack"   // OK
name = nil                   // OK
```

String타입의 뒤에 ?을 붙여주니 오류가 사라졌다. ?와 같이 !를 사용해도 오류가 사라진다.
이유는 optional 기호를 사용하여, 이 변수의 안에는 값이 있을 수도, 없을 수도 있다는 것을 명시해주었기 때문이다.<br>
변수에 ?가 붙으면 그 안에 값이 있는지 물어보게되고, 그 안에 값이 있으면 값을 얻게되지만, 아무것도 없으면 nil을 얻게 되는것이다.
(참고로 optional 변수는 초기화하지 않으면 값이 자동으로 nil로 초기화가 된다.)

<br>

## !은 뭐지?

?는 optional의 기호라는건 알겠다. 하지만 위에서 말했듯이 !를 써도 오류가 사라진다. !은 무엇일까?
!는 강제 언래핑(Unwrapping)이라고 부른다. ?와 다르게 친절하게 물어보는 느낌이 아닌, 값이 있든 말든 다 무시하고 부수고 값을 가져온다.

<br>


## 그렇다면 nil은 무엇인가?

nil은 value가 없는 것 이라는 의미라고 생각하면 된다.
swift에서 nil은 optional 변수 이외에서 사용할 수 없다.


<br>

## Wrapping & Unwrapping
