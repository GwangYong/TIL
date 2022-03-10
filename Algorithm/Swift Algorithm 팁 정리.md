## 값 입력 프로젝트 생성

swift 언어로 알고리즘을 풀 경우(특히 백준 알고리즘에서 값을 입력받는 경우)에는 `readLine()`을 사용해야한다.

<img src="https://user-images.githubusercontent.com/59376200/135711221-4e25e334-b883-4843-9569-5f148176acbb.png" width="550" height="400">

## 키보드 값 입력받기
```swift
let input = readLine() // return 값은 Optional String 형식

let input = readLine()! // return 값은 String 형식
```

## Int 값 입력받기
```swift
let input = Int(readLine()!)! // return 값은 Int

let input = Int(String(readLine()!))! // 위보다 조금 더 속도가 빠르다고함.
```

<br>

## 키보드 입력받은 값 공백으로 구분하기

1. **split( )** 으로 구분 (예시: 1 2 3 4)
```swift
let nums = readLine()!.split(seperator: " ") // ["1", "2", "3", "4"]
```

2. **component( )** 로 구분 (예시: 1 2 3 4)
```swift
let nums = readLine()!.components(seperatedBy: " ") // ["1", "2", "3", "4"]
```

split를 사용할 경우에는 Foundation을 import 해주어야한다.
자세한 내용은 다음에 따로 정리할 예정이다.

<br>

## 배열(Array) 사용

1. 배열 만들기
```swift
let arr = [Int]() // 빈 배열
let arr : Array<Int>

let arr = [Int](repeating: 2, count: 5) // 원하는 데이터 타입으로
let arr = Array(repeating: 2, count: 5)
// repeating에 들어간 요소를 count만큼 반복하여 만듦.
// ex) [2, 2, 2, 2, 2]
```

2. 2차원 배열 만들기
```swift
let arr = [[Int]]() // 빈 2차원 배열

let arr = [[Int]](repeating: Array(repeating: 2, count: 3), count: 4)
let arr: [[Int]] = Array(repeating: Array(repeating: 2, count: 3), count: 4) 
// ex) [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]
```

3. 임의의 Data 넣어서 만들기
```swift
let arr = Array(1...5)  // [1, 2, 3, 4, 5]
```

4. 배열 역순으로 출력
```swift
arr.reversed()
arr = arr.reversed()
```

5. 배열 정렬하기
```swift
// 오름차순. default도 오름차순 (1, 2, 3, 4...)
arr.sort()
arr.sort(by: <)
arr.sorted(by: <) 


// 내림차순 (..., 4, 3, 2, 1)
arr.sort(by: >)
arr.sorted(by: >) 
```

6. 배열 다룰 때 가장 중요한 **map, filter, reduce 고차함수!!**

**map**
```swift
let string = ["1", "2", "3", "4"]
string.map { Int($0)! } // [1, 2, 3, 4] 각 원소를 전부 Int로 맵핑
```

**filter**
```swift
let array = [1, 2, 3, 4]
array.filter { $0 % 2 == 0 } // [2, 4] 조건에 맞는 수만 뽑아냄
```

**reduce**
```swift
let array = [1, 2, 3, 4]
array.reduce(0, +) // 숫자 합이 나타남. 문자열 합치기도 가능
```
[고차함수 자세히 정리](https://jud00.tistory.com/entry/%EC%98%A4%EB%8A%98%EC%9D%98-Swift-%EC%A7%80%EC%8B%9D-%EA%B3%A0%EC%B0%A8-%ED%95%A8%EC%88%98-map-filter-reduce?category=1010119)

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




