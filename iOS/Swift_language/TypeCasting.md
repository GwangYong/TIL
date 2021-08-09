# 타입 캐스팅이란?

타입 캐스팅이란, 인스턴스의 타입을 확인하거나 어떠한 클래스의 인스턴스를 해당 클래스 계층 구조의 슈퍼 클래스나 서브 클래스로 취급 하는 방법

"is"와 "as"라는 연산자를 사용하여, 값의 타입을 확인하거나 값을 다른 타입으로 변환하는데 사용함.


## 타입 확인(Checking Type)
"is" 키워드를 사용해서 특정 클래스의 인스턴스의 타입을 확인할 수 있다.

```swift
class Person {
    var name: String
    init(name: String) {
        self.name = name
    }
}

var person = Person(name: "Jud")

if person is Person {
    print(true) // true
}
```

위의 코드에서 "person" 이라는 인스턴스를 생성해주고, 이 "person" 인스턴스가 Person의 인스턴스인가? 하고 확인하는 것이다.

이렇게 타입을 확인할 경우에 "is"키워드를 사용할 수 있다.


## 다운캐스팅(Downcasting)

특정 클래스 타입의 상수나 변수는 하위 클래스의 인스턴스를 참조하고 있을 수 있다.

이런 경우에 "as?"와 "as!"를 사용하여 서브 클래스 타입으로 "다운캐스팅"을 진행할 수 있다.

다운캐스팅은 실패할 수 있기 때문에, Optional Binding에서 보았듯이 **조건부 형식인 `?`와 강제 형식인 `!`를 사용한다.**

조건부 형식인 `?`는 다운캐스팅 하려는 타입의 Optional 값을 반환하며, 강제 형식인 `!`는 강제 언래핑을 하여 강제로 값을 반환한다.

Optional Binding에서 `!`를 사용하면 값이 없는 경우에도 값을 가져오려다가 에러가 발생하므로, 가능하면 사용하지 말고 값이 확실히 있을때만 사용하라고 주의했었다.
다운캐스팅도 마찬가지로 확실히 성공한다는 확신이 있을때만 `!`를 사용하자.


<!-- 

더 정리해서 TIL 마무리하고, 블로그 포스팅으로 준비



> Reference
> - [The Swift Language Guide - Type Casting](https://jusung.gitbook.io/the-swift-language-guide/language-guide/18-type-casting)
> - [Type Casting](https://zeddios.tistory.com/265)
 -->