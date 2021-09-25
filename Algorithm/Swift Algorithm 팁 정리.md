여기에 적는 내용들은 다른 블로그들과 구글링을 통해서 Swift로 알고리즘을 할 때, 도움이 되는 내용들을 적어둠.

## 키보드 입력받는 방법.
```swift
let value = readLine()
```

readLine() 리턴값은 Optional String이다.

<br>

## 키보드 입력받은 값 공백으로 구분하기

1. .split()으로 구분하기 (예시 1, 2, 3, 4)
```swift
let nums = readLine()!.split(seperator: " ") // ["1", "2", "3", "4"]
```

2. component()를 이용 (예시 동일)
```swift
let nums = readLine()!.components(seperatedBy: " ") // ["1", "2", "3", "4"]
```

### 두 방법의 차이점
1. import Foundation
component의 경우에는 Foundation에 있는 instance method이기 떄문에, 반드시 import Foundation을 해주어야한다.

또한 용량이 늘어나며, split의 경우에는 import Foundation을 해주지 않아도 괜찮다.

이만 보면 split를 해주어야 하겠지만, 2번째 차이를 보면 이해를 할 수 있을것이다.

2. 리턴값이 다르다.
그냥 결과만 보면 별 다를것은 없다. 하지만, 리턴되는 타입이 다르다.

components로 나눈 것은 리턴값이 `String`이지만, split로 나눈 것은 리턴값이 `String.SubSequence`이다. 이로인해 split로 쪼개면 String으로 바로 사용할 수 없다. (물론, map 함수를 사용하면 가능하다.)


<br>

## 배열(Array) 사용

1. 빈 배열 만들기
```swift
var empty : [Int] = []
var empty = [Int]()
var empty : Array<Int> = []
```

2. 임의의 Data 넣어서 만들기
```swift
var array = Array(1...5)  // [1, 2, 3, 4, 5]
```

3. 2차원 배열(Matrix) 만들기
```swift
let matrix = [[Int]]()
let arr: [[Int]] = Array(repeating: Array(repeating: 1, count: 5), count: 3) // 안쪽 count가 행, 바깥 count가 열

// 다룰때는 아래와 같이
arr[i][j]
```

4. 배열 거꾸로 출력
```swift
array.reversed()
```

5. 배열 정렬하기
```swift
array.sorted() // 오름차순. default도 오름차순 (1, 2, 3, 4...)
array.sorted(by: >) // 내림차순
```

6. 배열 다룰 때 가장 중요한 **map, filter, reduce 고차함수!!**

**map**
```swift
var string = ["1", "2", "3", "4"]
string.map { Int($0)! } // [1, 2, 3, 4] 각 원소를 전부 Int로 맵핑
```

**filter**
```swift
var array = [1, 2, 3, 4]
array.filter { $0 % 2 == 0 } // [2, 4] 조건에 맞는 수만 뽑아냄
```

**reduce**
```swift
var array = [1, 2, 3, 4]
array.reduce(0, +) // 숫자 합이 나타남. 문자열 합치기도 가능
```

<br>

## Dictionary 사용

1. 생성
```swift
var dic: [Int:String] = [:]
var dic = [Int:String]()

var dic = [1: "a", 2: "b', 3: "c"]
```

2. 값 수정
```swift
dic.updateValue("c", forKey: 3)
dic[3] = "d"
```

3. 값 추가
```swift
dic[4] = "5"
dic.update("5", forKey: 4) // 4라는 키가 있을경우 수정이 가능함.
```

4. 접근
```swift
dic[4]! // Unwraopping을 해줌
```

5. for문 돌기
```swift
for (key, value) in dic {
    print(key)   // 1, 2, 3
    print(value) // a, b, c 
}

// 단, Dictionary는 순서가 없으므로 순서는 뒤죽박죽
```

6. 값 삭제
```swift
dic.removeValue(forKey: 4) // 특정 키값 삭제
dic.removeAll()            // 전체 삭제
```

7. Dictionary Key로 sort 정렬 하기
```swift
let sort = dic.sorted(by: { $0.key < %1.key }) // value로 정렬할 경우 $0.value
```

8. Key를 바꿀 경우, 지우고 다시 넣어줘야함

<br>

## Plus Tip!


1. 앱 종료
```swift
exit(0)
```

2. 무한 루프
```swift
while true {
    ...
}
```

3. 타입 범위
```swift
Int, Int64 = 2의 8승 - 1 (9223372036854775807) // 19자리
Int32      = 2의 6승 - 1 (2147483647)          // 10자리
Float      = 소수점 6자리까지 표현 가능
Double     = 소수점 15자리까지 표현 가능
```

4. 문자를 ASCII 코드로 변환
```swift
Character("a").asciiValue!
```

5. 절대값 변환
```swift
abs(-29) // 29
```






<br>

<!-- 블로그에는 작성 X -->
> Reference 
> [알고리즘에 필요한 Swift Basic 총정리](https://twih1203.medium.com/swift-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%97%90-%ED%95%84%EC%9A%94%ED%95%9C-swift-basic-%EC%B4%9D%EC%A0%95%EB%A6%AC-d86453bbeaa5)