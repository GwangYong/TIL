- 내가 쓴 관련 포스팅
    - https://jud00.tistory.com/entry/자료구조-연결-리스트Linked-List?category=1010128
    - 자세한 개념은 위 글을 보자. 여기에는 코드 구현을 위한 설명만을 적어둔다.

<br>

## 2-1. Node를 생성

```swift
class Node<T: Equatable> {
  var data: T?
  var next: Node?

  init(data: T?, next: Node? = nil) {
    self.data = data
    self.next = next
  }
}
```

<br>

## 2-2. head : 가장 첫 노드를 가리키는 프로퍼티

매번 노드를 생성하고 이전 노드랑 연결해주는걸 일일이 매번 할 수 없기에 Node 관리를 해주는 LinkedList라는 클래스를 만들어준다

```swift
// LinkedList

// T: Equatable 프로토콜을 채택해주는 이유는, 아래의 search 단계에서
// node?.data == data를 == 연산하는 코드가 있는데, Equatable 프로토콜이 채택되지 않아있기에
// ==으로 비교할 수 없다! 라고 오류가 뜨기 때문에 Equatable프로토콜을 채택해준것이다.
class LinkedList<T: Equatable> {
  // head : 가장 첫 노드를 가리키는 프로퍼티
  // 즉, 가장 첫번째에 data를 가지고 있는 Node가 head가 된다.
  private var head: Node<T>?
}
```

<br>

## 2-3. append(data:) : 연결 리스트 맨 마지막 노드 추가

추가하는 경우, head 노드부터 끝까지 순회하며 nodex.next가 nil일 경우를 찾아서 추가하면 된다.

```swift
public func append(data: T?) {
    // head가 없는 경우 Node를 생성 후 head로 지정해준다
    if head == nil {
        head = Node(data: data)
        return
    }

    var node = head
    while node?.next != nil {
        node = node?.next
    }
    node?.next = Node(data: data)
}

```

<br>

## 2-4. insert(data: at:) : 연결 리스트 중간에 노드 추가

연결리스트는 중간에 노드를 추가할 수 있지만, index가 없기에 중간에 추가하려면 아래와 같은 insert로 직접 구현해서 추가가 가능하다.

또한, index는 알겠지만 0부터 시작이다.

```swift
// 아래의 index는 0부터 시작한다.
 public func insert(data: T?, at index: Int) {
      if index == 0 {
        // 인덱스가 0일 때의 처리. 0번째에 넣기 때문에, 기존 첫 번째 data값인 head를 next 값으로 넣어 연결해준다.
          let newNode = Node(data: data, next: head)  
          head = newNode
          return
      }

      if head == nil {
          head = Node(data: data)
          return
      }

      var node = head
      for _ in 0..<(index-1) {
          if node?.next == nil { break }
          node = node?.next
      }

      let nextNode = node?.next
      node?.next = Node(data: data)
      node?.next?.next = nextNode
}
```

<br>

## 2-5. removeLast() : 연결 리스트 맨 마지막 노드 삭제

연결 리스트 맨 마지막 노드 삭제는 removeLast키워드로 직접 구현하면된다.

delet할 노드의 바로 이전 노드를 nil로 바꿔주는걸 잊지 말자.

```swift
public func removeLast() {
        if head == nil { return }

        // head를 삭제하는 경우
        if head?.next == nil {
            head = nil
            return
        }

        var node = head
        while node?.next?.next != nil {
            node = node?.next
        }
        node?.next = node?.next?.next // 맨 마지막 노드의 next는 nil이므로! (nil을 직접 넣어도 괜찮다.)
}
```

<br>

## 2-6. remove(at:) : 연결 리스트 중간 노드 삭제

delete할 노드의 바로 이전 노드의 next를 delete할 노드의 next로 변경해주자

```swift
public func remove(at index: Int) {
        if head == nil { return }

        //head를 삭제하는 경우
        if index == 0 {
            head = head?.next // 인덱스가 0일 때의 처리
            return
        }

        var node = head
        for _ in 0..<(index-1) {
            if node?.next?.next == nil { break }
            node = node?.next
        }

        node?.next = node?.next?.next
}
```

<br>

## 2-7. searchNode(from:) : data로 Node찾기

앞에서 계속 봐왔듯이 head부터 순차적으로 순회하며 찾아야한다.

```swift
public func searchNode(from data: T?) -> Node<T>? {
        if head == nil { return nil }

        var node = head
        while node?.next != nil {
            if node?.data == data { break }
            node = node?.next
        }
        return node
}
```

<br>

## 2-8. printAllNodes() : 모든 노드 출력

노드가 어떻게 되어있는지 확인 가능하게 출력하는 코드이다.

```swift
public func printAllNodes() {
      var node = head
      while node != nil {
          if let data = node?.data {
              print(data, terminator: " -> ")
          }
          node = node?.next
      }
      print("nil")
}
```

<br>

## 2-9. 완성된 코드 & 시현

- 완성된 코드

    ```swift
    class Node<T: Equatable> {
      var data: T?
      var next: Node?

      init(data: T?, next: Node? = nil) {
        self.data = data
        self.next = next
      }
    }

    /// head: 연결 리스트는 특정 데이터에 연결하려면 첫 번째 노드부터 순차적으로 접근해야 함
    class LinkedList<T: Equatable> {
        private var head: Node<T>?

        /// append(data:) : 연결 리스트 맨 마지막 노드 추가
        public func append(data: T?) {

          // head가 없는 경우 Node를 생성 후 head로 지정해준다
            if head == nil {
                head = Node(data: data)
                return
            }

            var node = head
            while node?.next != nil {
                node = node?.next
            }
            node?.next = Node(data: data)
        }

        /// insert(data: at:) : 연결 리스트 중간에 노드 추가
        // 아래의 index는 0부터 시작한다.
        public func insert(data: T?, at index: Int) {
          if index == 0 {
            // 인덱스가 0일 때의 처리. 0번째에 넣기 때문에, 기존 첫 번째 data값인 head를 next 값으로 넣어 연결해준다.
              let newNode = Node(data: data, next: head)  
              head = newNode
              return
          }

            if head == nil {
                head = Node(data: data)
                return
            }

            var node = head
            for _ in 0..<(index-1) {
                if node?.next == nil { break }
                node = node?.next
            }

            let nextNode = node?.next
            node?.next = Node(data: data)
            node?.next?.next = nextNode
        }

        /// removeLast() : 연결 리스트 맨 마지막 노드 삭제
        public func removeLast() {
            if head == nil { return }

            // head를 삭제하는 경우
            if head?.next == nil {
                head = nil
                return
            }

            var node = head
            while node?.next?.next != nil {
                node = node?.next
            }
            node?.next = node?.next?.next // 맨 마지막 노드의 next는 nil이므로! (nil을 직접 넣어도 괜찮다.)
        }

        /// remove(at:) : 연결 리스트 중간 노드 삭제
        public func remove(at index: Int) {
            if head == nil { return }

            //head를 삭제하는 경우
            if index == 0 {
                head = head?.next // 인덱스가 0일 때의 처리
                return
            }

            var node = head
            for _ in 0..<(index-1) {
                if node?.next?.next == nil { break }
                node = node?.next
            }

            node?.next = node?.next?.next
        }

        /// searchNode(from:) : data로 Node찾기
        public func searchNode(from data: T?) -> Node<T>? {
            if head == nil { return nil }

            var node = head
            while node?.next != nil {
                if node?.data == data { break }
                node = node?.next
            }
            return node
        }

      // printAllNodes() :  모든 노드 출력
      public func printAllNodes() {
          var node = head
          while node != nil {
              if let data = node?.data {
                  print(data, terminator: " -> ")
              }
              node = node?.next
          }
          print("nil")
      }

    }

    // 사용

    let list = LinkedList<Int>()
    list.append(data: 1)
    list.append(data: 2)
    list.append(data: 3)
    list.append(data: 4)

    list.printAllNodes() // 1 -> 2 -> 3 -> 4 -> nil

    // 0번째 index에 값 추가
    list.insert(data: 30, at: 0)
    list.printAllNodes() // 0 -> 1 -> 2 -> 3 -> 4 -> nil

    // 0번째 index 값 제거
    list.remove(at: 0)
    list.printAllNodes() // 1 -> 2 -> 3 -> 4 -> nil
    ```

<br>

 
<!-- 
## Reference

- https://babbab2.tistory.com/86 -->

