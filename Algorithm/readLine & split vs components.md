백준 문제를 풀다가 값을 입력받아야하는데, Python과 하는 방식이 달라서 공부하기 시작함.
입력 받고 파이썬에서는 split로만 나눴었는데, 여기에는 components라는 방식이 하나 더 있어서 공부하고 정리.



## readLine()

swift로 알고리즘 문제를 풀 경우(특히 백준 알고리즘 입력 받을 경우)에는 `readLine()` 함수를 사용해야한다.

<img width="743" alt="스크린샷 2021-10-02 오후 4 22 22" src="https://user-images.githubusercontent.com/59376200/135711221-4e25e334-b883-4843-9569-5f148176acbb.png">

Playground에서는 이 함수를 사용할 수 없고 위의 사진처럼 Xcode에서 프로젝트를 생성할 때, `Command Line Tool`로 프로젝트를 생성해야한다.

readLine() 함수를 사용하면 콘솔창에 텍스트를 입력할 수 있다.

<br>

### 1. 한 줄만 입력받는 경우
```swift
let num = readLine()!
// 물론, 두 줄을 입력받을 경우에는 위의 코드를 2번 작성해주면 된다.

// Int형태로 받는 경우
let num = Int(readLine()!)!
```

<br>

### 2. 한 줄에 2개 이상의 값을 입력받는 경우
```swift
let num = readLine()!.split(separator: " ") // 매개변수로 받아서 해당 인자를 기준으로 쪼개준다.
let num = readLine()!.components(separatedBy: " ") // 위와 동일

// map 함수를 이용해서 Int형태로
let num = readLine()!.split(separator: " ").map { Int($0)! }
let num = readLine()!.components(separatedBy: " ").map { Int($0)! }

// 위에서 split와 components 2가지 방식을 하였고 출력도 동일하다. 하지만 다른점이 있어서 밑에서 설명할 것이다.
```

<br>

<!-- ## split VS components

split와 components 두 가지 경우를 위에서 다 예시를 들었으니, 이 두가지 경우에 대해 알아보자.

1. 타입이 다르다.

split와 components의 다른점 중 하나는 타입이 다르다는 점이다. 

아래 사진을 확인해보자
<img width="455" alt="스크린샷 2021-10-02 오후 7 20 23" src="https://user-images.githubusercontent.com/59376200/135712245-abfb32a9-7545-4661-a767-c3bd24cb8c8d.png">

<img width="219" alt="스크린샷 2021-10-02 오후 7 21 14" src="https://user-images.githubusercontent.com/59376200/135712265-29c67e6d-670c-4da6-87d1-f3cee273dbeb.png">

이렇게 결과만 확인했을 경우에 값이 다른점은 보이지 않는다. 그러면 이제 타입을 확인해보자

<img width="217" alt="스크린샷 2021-10-02 오후 7 27 11" src="https://user-images.githubusercontent.com/59376200/135712410-e6168cb4-d5f2-4ebf-9393-5b3f806098bc.png">


위의 사진과 같이, 값은 똑같을지 몰라도 타입이 다른것이 보인다. **split로 출력한 값은 "Substring" 타입이며, components로 출력한 값은 "String" 타입이다.**

2. Foundata -->









<!--  

# 업데이트
- components, split 두개 더 공부하고 작성
    - split와 components 두개 각각 설명하고 마지막에 VS로 해서 정리하기
- 둘 다 공식문서 읽어보기

# 수정 
- 맨 위에 작성한글 수정 (삭제 or 업데이트)
- 참고한것들 있으면 작성하기

-->