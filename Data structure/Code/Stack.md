- 내가 쓴 관련 포스팅
    - https://jud00.tistory.com/entry/자료구조-스택Stack과-큐Queue에-대해서-알아보자

<br>

```swift
struct Stack<T> {
    private var stack: [T] = []

    public var count: Int {
        return stack.count
    }

    public var isEmpty: Bool {
        return stack.isEmpty
    }

    public mutating func push(_ element: T) {
        stack.append(element)
    }

    public mutating func pop() -> T? {
        return isEmpty ? nil : stack.popLast()
    }
}

// 아래와 같이 사용 
var myStack = Stack<Int>()
myStack.push(10)
print(myStack) // [10]
myStack.pop()
print(myStack) // []
```

Stack은 Queue와 똑같이 구현해주면 된다.

다만 Queue와 다르게 Stack은 마지막에 element가 추가(append)되어서 O(1)이 되고, 반대로 삭제도 마지막에 element가 삭제(popLast)가 되기 때문에  O(1)이 된다.

그렇기에 Queue에서 발생하는 오버헤드는 Stack에는 없다.

또한, removeLast와 동일한 함수인 popLast라는 함수 자체를 Swift 배열에서 지원해주고 있다. 그렇기에 그냥 배열을 Stack처럼 사용해서 써도 괜찮을거같다.

굳이 Stack를 만들지 않아도 append, popLast 만으로 충분히 배열을 Stack처럼 사용이 가능할 것 같다.