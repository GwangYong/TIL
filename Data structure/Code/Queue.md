- 내가 쓴 관련 포스팅
    - https://jud00.tistory.com/entry/자료구조-스택Stack과-큐Queue에-대해서-알아보자

<br>

## 1. Swift로 Queue 구현


```swift
struct Queue<T> {
  private var queue: [T] = []

  public var count: Int {
    return queue.count
  }

  public var isEmpty: Bool {
    return queue.isEmpty
  }

  // struct는 참조타입인데, 내부의 값을 변경해야할 경우, mutating 메서드를 명시하여 값을 변경할 수 있음.
  public mutating func enqueue(_ element: T) {
    queue.append(element)
  }

  public mutating func dequeue() -> T? {
    return isEmpty ? nil : queue.removeFirst()
  }
}
```

Swift에서는 Queue를 따로 지원해주지 않기에 구조체와 배열을 사용하여 구현이 가능

```swift
// 아래와 같이 사용이 가능
var myQueue = Queue<Int>()
myQueue.enqueue(10)
myQueue.enqueue(30)
myQueue.dequeue()
```

여기서 문제가 하나 있는데 Queue는 FIFO으로, 처음 element가 삭제되기에 앞에있는 element가 삭제된다면 한 칸씩 앞으로 당겨지는 과정이 발생하면서 시간복잡도가 O(n)이 되는 것이다.

그래서 좀 더 효율적으로 개선한 Queue를 찾아보았다. 

<br>

## 2. 개선된 Queue

```swift
struct Queue<T> {
    private var queue: [T?] = []
    private var front: Int = 0

    public var count: Int {
        return queue.count
    }

    public var isEmpty: Bool {
        return queue.isEmpty
    }

    public mutating func enqueue(_ element: T) {
        queue.append(element)
    }

    // return값이 Optional인 이유는, Queue가 비어있을때 dequeue를 실행한다면 nil이 리턴되기 때문
    public mutating func dequeue() -> T? {
        guard front <= queue.count, let element = queue[front] else { return nil }
        queue[front] = nil
        front += 1

        if front > 50 {
            queue.removeFirst(front)
            front = 0
        }
        return element
    }
}
```

개선된 버전은 dequeue에서 removeFirst()를 하지않고, front를 이용해 dequeue시 반환되어야 할 element의 index를 가지고 있는것이다.

이렇게 된다면 dequeue를 할 때, element를 삭제하고 한 칸씩 당기는 과정이 없기에 시간복잡도가 O(1)이 된다.

다만, enqueue를 계속 하는데 삭제되지 않고 nil로 할당된 element를 계속 가지고 있을 수는 없으니, 적당한 때에 nil로 할당된 element를 제거해주는 작업이 필요하다. 그래서 대략 50개쯤으로 설정한 것 이지만, 필요에 따라 개수를 바꿔서 사용하면 될거같다.

나중에 직접 코드를 돌리면서 속도차이를 느껴보면 좋을거같다.


<br>

<!-- 
### Reference

---

https://jeong9216.tistory.com/350

https://babbab2.tistory.com/84 -->