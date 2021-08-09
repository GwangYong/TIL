# 타입 캐스팅이란?

타입 캐스팅이란, 인스턴스의 타입을 확인하거나 어떠한 클래스의 인스턴스를 해당 클래스 계층 구조의 슈퍼 클래스나 서브 클래스로 취급 하는 방법이다.

"is"와 "as"라는 연산자를 사용하여, 값의 타입을 확인하거나 값을 다른 타입으로 변환하는데 사용함.

<br>

## 타입 확인(Checking Type)
타입 확인은 "is" 키워드를 사용해서 특정 클래스의 인스턴스의 타입을 확인할 수 있다.

Swift Language Guide에 있는 예제를 살펴보자.

```swift
class MediaItem {
    var name: String
    init(name: String) {
        self.name = name
    }
}
```
우선 String 형식의 name 프로퍼티와 생성자를 하나 가지는 `MediaItem` 이라는 클래스를 선언해준다.

```swift
class Movie: MediaItem {
    var director: String
    init(name: String, director: String) {
        self.director = director
        super.init(name: name)
    }
}

class Song: MediaItem {
    var artist: String
    init(name: String, artist: String) {
        self.artist = artist
        super.init(name: name)
    }
}
```
`MediaItem` 클래스를 상속받는 서브 클래스인 `Movie`와 `Song` 두 개의 클래스를 선언해준다.


```swift
let library = [
    Movie(name: "기생충", director: "봉준호"),
    Song(name: "Six Feet Under", artist: "Billie Eilish"),
    Movie(name: "올드보이", director: "박찬욱"),
    Song(name: "Closure", artist: "Faime"),
    Song(name: "If I Die Young", artist: "The Band Perry")
]
```
그리고 위의 코드와 같이 배열을 하나 만들어준다. 이 안에 처음 정의해준 `MediaItem` 클래스의 상속을 받는 `Movie`와 `Song` 타입 인스턴스를 넣어준다.
그러면 `library`배열은 타입 추론에 의해 `[MediaItem]` 배열의 형태를 가지게 된다.

<br>

이제 "is" 연산자를 사용한 `타입 확인(Checking Type)`을 사용해보자.

아래 코드는 `library` 배열을 순회하여 `item`이 특정 타입일 때마다 그에 맞는 숫자를 증가시키는 코드이다. 

```swift
var movieCount = 0
var songCount = 0

for item in library {
    if item is Movie {
        movieCount += 1
    } else if item is Song {
        songCount += 1
    }
}

print("Media library에는 \(movieCount)개의 영화와 \(songCount)개의 노래가 있다.")
// Media library에는 2개의 영화와 3개의 노래가 있다.
```

`library`배열에서 정의해준 `Movie`는 2개이며, `Song`은 3개이므로, `movieCount`에는 2가 더해지고, `songCount`에는 3이 더해져서 **Media library에는 2개의 영화와 3개의 노래가 있다.** 라는 출력이 나오게된다.

<br>


## 다운캐스팅(Downcasting)

다운 캐스팅은 `부모 클래스`에서 `자식 클래스`로 `형 변환` 하는것을 의미한다. 쉽게 말하자면 자식 클래스의 프로퍼티와 메소드를 사용하기 위해서 다운캐스팅을 하는 것이다.

특정 클래스 타입의 상수나 변수는 하위 클래스의 인스턴스를 참조하고 있을 수 있다. 이런 경우에 "as?"와 "as!"를 사용하여 서브 클래스 타입으로 "다운캐스팅"을 진행할 수 있다.

다운캐스팅은 실패할 수 있기 때문에, 형 변환 연산자는 두 개의 형식으로 나뉘어진다.

Optional 조건부 형식 `as?`는 다운캐스트를 시도하여 타입의 옵셔널 값을 반환하며, 강제 형식인 `as!`를 사용하면 강제 언래핑(Forced-Unwrap)을 하여 강제로 값을 반환하게 된다.

Optional Binding에서 `!`를 사용하면 값이 없는 경우에도 값을 가져오려다가 런타임 에러가 발생하므로, 가능하면 사용하지 말고 값이 확실히 있을때만 사용하라고 주의했었다. 
그러므로 다운캐스팅도 마찬가지로 확실히 성공한다는 확신이 있을때만 `!`를 사용하자.

<br>

```swift
for item in library {
    if let movie = item as? Movie {
        print("Movie: \(movie.name), dir. \(movie.director)")
    } else if let song = item as? Song {
        print("Song: \(song.name), by \(song.artist)")
    }
}

// Movie: 기생충, dir. 봉준호
// Song: Six Feet Under, by Billie Eilish
// Movie: 올드보이, dir. 박찬욱
// Song: Closure, by Faime
// Song: If I Die Young, by The Band Perry
```

위의 예제를 보면 if let을 사용하였으며 `as?`로 조건부 형식을 사용하였다.

`library`는 `MediaItem`타입 배열이며, `as?` 조건부 형식 뒤에 있는 `Movie`와 `Song` 모두 `MediaItem`의 서브클래스이기 때문에, 차례대로 Movie와 Song의 이름과 감독/아티스트 이름을 출력하게 된다.





<br>

<!-- 

더 정리해서 TIL 마무리하고, 블로그 포스팅으로 준비

************가능하면 밑에 Reference에 적어둔 스위프트 가이드만 보고 정리하자. 참고한곳 늘리고싶지않아...************************

- 다운 캐스팅 개념 간단하게 설명
- Any와 AnyObject 정리하기


> Reference
> - [The Swift Language Guide - Type Casting](https://docs.swift.org/swift-book/LanguageGuide/TypeCasting.html)
 -->