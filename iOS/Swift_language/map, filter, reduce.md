# 고차함수
먼저, 고차함수에 대해 알아보자.

고차함수는 **다른 함수를 전달 인자로 받거나 함수 실행의 결과를 함수로 반환하는 함수**이다.

스위프트에서 제공하는 고차함수는 `map, filter, reduce` 3가지가 있으며, 컨테이너 타입 (Array, Set, Dictionary 등)에 구현되어 있다.

<br>

# map(변형)
`map`은 컨테이너 내부에 **기존 데이터를 변형(transform)하여 새로운 컨테이너를 생성한다.** 다만, 기존의 데이터는 변하지 않는다.

map 함수를 사용하면 아래의 코드처럼 원래의 배열인 `numbers`의 값에 2를 곱한 값이 `mapArray`에 새로 생성된다.
```swift
let numbers = [0, 1, 2, 3]
let mapArray = numbers.map { (number) -> Int in 
    return number * 2
}
print("map \(mapArray)") // map [0, 2, 4, 6]
```

<br>

# filter(추출)
`filter`는 컨테이너 내부에 값을 걸러서 새로운 컨테이너로 추출한다.

아래 예시를 보면 초기 배열의 `intArray`를 생성해주었다. 그리고 filter함수를 사용하여 배열의 요소에 접근하여 10보다 큰 값들을 걸러내고, `filterArray`에 걸러내준 10보다 큰 값들만 들어있는 새로운 배열이 대입된다. 
```swift
let intArray = [10, 5, 20, 13 ,4]
let filterArray = intArray.filter { $0 > 10 }

print("filter \(filterArray)") // filter [20, 13]
```

<br>

# reduce(결합)
`reduce`는 컨테이너 내부의 요소를 하나로 통합시켜준다.

이번에도 코드를 보자. 

`someArray`배열에 초기값을 만들어준 후, `reduce` 함수 첫 번째 매개변수의 초기값을 0으로 설정해주었으며, 두 번쨰 매개변수 클로저를 보면 `result`와 `element`를 더해서 반환해준다.
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
위 코드를 실행하면, 배열의 요소값을 다 더한 15값이 출력된다.

만약, `reduce(0)` 값을 `reduce(5)`로 변경해 주었을 경우, 0이 아닌 5로 변경해 주었으므로 출력 결과는 
```swift
//  5 + 1
//  6 + 2
//  8 + 3
//  11 + 4
//  15 + 5
//  reduce 20
```
이렇게 나오게 된다.

그 이유는 reduce 초기값이 0이 아닌 5값으로 someArray의 각 요소들을 차례대로 접근해서 더했기 때문이다.