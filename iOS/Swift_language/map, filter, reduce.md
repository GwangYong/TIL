# 고차함수
먼저, 고차함수에 대해 알아보자.

고차함수는 **다른 함수를 전달 인자로 받거나 함수 실행의 결과를 함수로 반환하는 함수**이다.

스위프트에서 제공하는 고차함수는 `map, filter, reduce` 3가지가 있으며, 컨테이너 타입 (Array, Set, Dictionary 등)에 구현되어 있다.

<br>

# map(변형)
`map`은 컨테이너 내부에 **기존 데이터를 변형(transform)하여 새로운 컨테이너를 생성한다.** 

다만, 새로운 컨테이너를 생성한 것이기 때문에, **기존의 데이터는 변하지 않는다.**

map은 for-in 구문과 큰 차이점은 없지만, map을 사용하면 **코드의 간결성, 재사용 용이성, 컴파일러 최적화 성능이 좋다**는 장점이 있다.

<br>

**for-in**
```swift
let numArray = [0, 1, 2, 3]
var forArray = [Int]()
for num in numArray {
    forArray.append(num * 2)
}
print(forArray) // [0, 2, 4, 6]
```

**map**
```swift
let numArray = [0, 1, 2, 3]
let mapArray = numArray.map { (numArray: Int) -> Int in 
    return numArray * 2
}
print("map \(mapArray)") // map [0, 2, 4, 6]
```
map 함수를 사용하면 아래의 코드처럼 원래의 배열인 `numbers`의 값에 2를 곱한 값이 `mapArray`에 새로 생성된다.

<br>

위 코드에서, 매개변수, 반환 타입, 반한 키워드를 생략한 후행 클로저가 아래의 코드이다. 이런식으로 사용할 수 있다는 것도 알아두면 좋을것이다. 
```swift
let numArray = [0, 1, 2, 3]
let mapArray = numArray.map { $0 * 2 }
print(mapArray) // [0, 2, 4, 6]
```

<br>

# filter(추출)
`filter`는 **컨테이너 내부에 값을 걸러서 새로운 컨테이너로 추출한다.**

반환 타입은 `Bool`이며, `true`이면 값을 포함하고, `false`이면 값을 포함하지 않는다.


우선은 for-in문 부터 확인하자
**for-in**
```swift
let numbers: [Int] = [10, 5, 20, 13, 4]

var filter: [Int] = [Int]()

for num in numbers {
    if num > 10 {
        filter.append(num)
    }
}

print(filter)
```

<br>

다음으로는, filter 메소드를 사용해보자

```swift
let intArray = [10, 5, 20, 13, 4]
let filterArray = intArray.filter { (num: Int) -> Bool in 
    return num > 10
}

print(filterArray)
```

이처럼, filter 메소드를 사용하면 코드가 보기쉽고 간략화된 것을 볼 수 있다.

또한, 클로저를 사용했기 때문에, **후행 클로저**를 사용해서 아래와같이 더욱 간단하게 작성할 수 있다.

```swift
let intArray = [10, 5, 20, 13, 4]
let filterArray = intArray.filter { $0 > 10 }

print("filter \(filterArray)") // filter [20, 13]
```

<br>

# reduce(결합)
`reduce`는 컨테이너 내부의 요소를 하나로 통합시켜준다.

첫 번째 매개변수를 통해 초기값을 결정해줄 수 있으며, 정수 배열이라면 연산 결과를 합치고 문자열 배열이라면 문자열을 하나로 통합하는 일을 해준다.

**for-in**
```swift
let someArray: [Int] = [0, 1, 2, 3, 4, 5]
var reduceResult: Int = 0

for arr in someArray {
    reduceResult += arr
}

print(reduceResult)
```


이번에는 reduce 메소드를 사용해보자.

`someArray`배열에 초기값을 만들어준 후, `reduce` 함수 첫 번째 매개변수의 초기값을 0으로 설정해주었으며, 두 번째 매개변수 클로저를 보면 `result`와 `element`를 더해서 반환해준다.

이렇게 되면 `someArray`배열에 있는 각 요소들은 더해지며 `reduceResult` 변수에 대입된다.

여기서 result 매개변수는 누적값을 뜻하며, element 매개변수는 배열의 요소값을 뜻한다. 

```swift
let someArray = [1, 2, 3, 4, 5]
let reduceResult = someArray.reduce(0) {
    (result: Int, element: Int) -> Int in
    print("\(result) + \(element)")
    return result + element
}

print("reduce \(reduceResult)")
//  0 + 1
//  1 + 2
//  3 + 3
//  6 + 4
//  10 + 5
//  reduce 15
```

<br>

만약, 초기값인 `reduce(0)` 값을 `reduce(5)`로 변경해 주었을 경우, 0이 아닌 5로 변경해 주었으므로 출력 결과는 아래와 같이 나오게된다.
```swift
//  5 + 1
//  6 + 2
//  8 + 3
//  11 + 4
//  15 + 5
//  reduce 20
```

그 이유는 reduce 초기값이 0이 아닌 5값으로 someArray의 각 요소들을 차례대로 접근해서 더했기 때문이다.

<br>

> Reference
> - [고차함수 - Map, Filter, Reduce 알아보기](https://shark-sea.kr/entry/Swift-%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98-Map-Filter-Reduce-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)