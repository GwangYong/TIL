# 클래스와 구조체 비교 (Comparing Classes and Structures)

구조체로는 가능하지 않고 클래스만 가능한 기능은 아래와 같다.
- 상속 (Inheritance) : 클래스의 여러 속성을 다른 클래스에 물려 줌
- 타입 캐스팅 (Type casting) : 런타임에 클래스 인스턴스의 타입을 확인
- 소멸자 (Deinitializers) : 할당된 자원을 해재 시킴
- 참조 카운트 (Reference counting) : 클래스 인스턴스에 하나 이상의 참조가 가능
<br>

## 선언 문법 (Definition Syntax)
```swift
class SomeClass {
  // 클래스 내용
}

struct SomeStructure {
  // 구조체 내용
}
```

<br>

아래는 각각 구조체 선언과 클래스 선언의 예이다.
```swift
struct Resolution {
  var width = 0
  var height = 0
}

class VideoMode {
  var resolution = Resolution() // 위 Resolution 구조체를 값으로 사용
  var interlaced = false
  var frameRate = 0.0
  var name : String?
}
```

<br>

## 클래스와 구조체의 선택 

클래스와 구조체 모두 프로그램의 코드를 조직화하고 특정 타입을 선언하는데 사용된다.
그리고 클래스 인스턴스가 인자로 사용될 때는 참조가 넘어가고, 구조체는 값이 넘어간다.
그러면 언제 클래스를 사용하고 언제 구조체를 사용해야할까?

일반적으로 다음의 조건 중 1개 이상을 만족하면 구조체를 사용하는 것을 고려해볼 수 있다고 한다.
- 구조체의 주 목적이 관계된 간단한 값을 캡슐화(encapsulate) 하기 위한 경우
- 구조체의 인스턴스가 참조되기 보다 복사되기를 기대하는 경우
- 구조체에 의해 저장된 어떠한 프로퍼티가 참조되기 보다 복사되기를 기대하는 경우
- 구조체가 프로퍼티나 메소드 등을 상속할 필요가 없는 경우

예를 들면 다음과 같다. `double`형을 같는 `width`와 `height`를 캡슐화해 특정 지형의 크기로 사용하는 경우, `Int`형을 같는 `start`와 `length`를
캡슐화해 특정 값의 범위를 나타내는 경우 `Double`형으로 구성된 x, y, z를 캡슐화해 3D좌표 시스템의 point로 사용되는 경우

이러한 경우를 제외한 다른 모든 경우에는 구조체가 아닌, 클래스를 사용화면 된다.