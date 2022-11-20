### 📍 Core Data
---
- Core Data는 데이터를 저장하고 관리하기 위한 ORM(Object Relational Mapping) 프레임워크이다. (Database는 아니다.)
- 해당 기기에 데이터를 저장하므로 오프라인에서도 동작이 가능하며, Cloud를 제외하고는 데이터 공유가 불가능하다
- SQL을 쓸 일 없이 Object-Oriented 방식으로만 데이터를 다룰 수 있다.
- 데이터는 Object로 표현되며, NSManagedObjectModel의 인스턴스로 구현된다. 
- 이러한 Object가 관계를 형성하여 Object Graphs를 이루고 이를 관리하는 프레임워크가 바로 Core Data이다.

<br>

### 📍 SQLite
---
- 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스
- Apple에서 제공되는 것이 아닌, 외부 라이브러리로 비교적 가벼운 데아터 처리가 필요할 때 사용하기 좋다.

<br>

### 📍 SQLite VS Core Data
---
- 보통 SQLite는 lightweight solution(경량 솔루션)이 필요한 경우에, Core Data는 complex object graph(복잡한 개체 그래프)가 필요한 경우에 사용.
- Core Data가 SQLite바도 빠르게 기록을 가져올 수 있지만, 그에 반해서 더 많은 메모리와 저장 공간을 사용함
- 속도 : Core Data > SQLite
- 메모리 및 저장 공간 사용 : Core Data > SQLite
- 결론 : 빠르고 좀 더 다양하고 많은 데이터를 저장하며, 특성 및 관계가 있는 복잡한 개체 그래프를 관리하는 경우라면 Core Data를 사용하고, 그것이 아니라면 SQLite를 사용하는 것이 좋아보인다.

<br> 

### 📍 Realm
---
- Core Data와 같은 객체 데이터베이스 관리 시스템
- 무료에 설치가 쉽고 무제한 사용이 가능하다. (많은 데이터를 저장할 수 있음)
- Core Data보다 속도가 빠름

<br>

### 📍 UserDefaults
---
- iOS로 데이터를 저장할 때 사람들이 처음에 가장 많이 사용하는 방법
- User Default는 앱을 런치(Launch)하거나 재가동시에 간단한, 적은 양의 데이터를 저장하는데 사용된다. (id, pw, 자동 로그인 설정 정도)
- 위와 같이 사용될 때, key-value 쌍을 영구적으로 저장하는 사용자의 기본 DataBase에 대한 인터페이스이다.
- 사용이 쉽고, Thread Safe하다.
- 하지만 암호화되지 않고, 동일한 키의 값을 쉽게 재정의 할 수 있다. (키 충돌 가능성 O)

<br>

### 📍 UserDefaults VS Core Data
---
- 앱 내부에 데이터를 저장할 때 외부 라이브러리를 사용하지 않고 저장하는 방법은 “User Defaults”와 “Core Data” 의 2가지가 있다.
- User Defaults의 모든 데이터가 key-value 형태로 짝을 이루기 때문에 Core Data보다 빠르지만, 말 그대로 유저 정보와 같이 작은 데이터를 저장하는데 사용된다.
- UserDefaults는 사용자 기본 설정과 같은 단일 데이터 값에 적합하다.

<br>

### 📍 FileManager
---
- iOS 내에서 파일과 디렉토리의 생성, 이동, 읽기, 쓰기 행위와 같은 기본적인 동작과 제어를 할 때 사용한다.
- 파일을 단일 엔티티로 조작하는데 사용된다. 파일은 구조화되지 않은 데이터에 가장 적합하다.
- FileManager는 iCloud 스토리지와 함께 사용할 수 있으므로 모든 iOS 및 MacOS 사용자 기기간에 앱 데이터가 동기화된다.
- 디렉토리 내용 나열, 디렉토리 생성, 파일 이동, 복사 또는 제거와 같은 다양한 방법으로 사용이 가능하다.
- 다만, URL Path 생성은 오류가 발생할 수 있으며, 디스크에서 파일 읽기 / 저장 속도가 매우 느릴 수 있다.


<!-- 

> Reference
> - https://devmjun.github.io/archive/iOS_Databases-SQLLite_vs_Core_Data_vs_Realm
> - https://velog.io/@rnfxl92/UserDefaults-FileManger-CoreData에대한-간단한-설명
> - https://cocoacasts.com/what-is-the-difference-between-core-data-and-sqlite/ 

-->
