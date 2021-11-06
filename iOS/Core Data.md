## Core Data

Core Data는 디바이스의 permanent data (영구적인 데이터)를 저장할 수 있음.

간단한 ToDoList를 만들 경우, 앱을 껐다가 다시 켜도 데이터들이 없어지지않고 저장되게 하기위해 사용한 UserDefaults랑도 비슷하지만 조금 다르다.

UserDefaults는 app setting같은 간단한 정보를 저장하는데에 적합한 반면, Core Data는 복잡하고 큰 user data를 저장히기에 적합하다.

<br>

### Core Data는 Database인가?

바로 말하자면, Core Data는 Database가 아니다.

Core Data의 기능 중 하나인 Persistence는, 객체를 저장소에 매핑하는 세부 정보를 추상화하여 데이터베이스를 직접 관리하지 않고도 Swift 언어로 데이터를 쉽게 저장할 수 있도록 해준다.

이 Persistence 기능은 Core Data의 기능 중 하나 일 뿐이지, Core Data == Database가 아니라는 소리이다. 

기억할 것은 **Database가 아니며, 데이터를 유지하기 위한 API도 아니다.** 라는 것을 기억하자는 것이다.

**Core Data는 객체를 관리하는 Framework이다.**

<br>

> Reference
> - [Zeed님의 Core Data (1)](https://zeddios.tistory.com/987)

