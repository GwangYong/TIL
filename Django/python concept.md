## 이스케이프 코드

<table>

| 코드 | 설명 | 
|:---:|:---:|
| `\n` | 개행 (줄 바꿈) |
| `\t` | 수평 탭  |
| `\r` | 캐리지 리턴 |
| `\a` | 벨 소리 |
| `\b` | 백스페이스 |
| `\000` | 널 문자 |
</table>

<br>

## 불(bool) 자료형

- 불(bool) 자료형이랑 참(True) 또는 거짓(Flase)을 값으로 가지는 자료형이다.
 

<pre>
>>> 1 == 1
True
>>> 1 > 2
False
>>> 100 > 99
True
>>> 'aa' == 'ab'
False
>>> True == True
True
>>> True == False
Flase
</pre>

<br>

## 리스트 자료형

<pre>
>>> list1 = [123,987,532, 492, 593]
>>> list2 = ['This', 'is', 'list']
>>> list3 = []
>>> list4 = [42, 39, 593,['List', 'in', 'list']]
</pre>

<br>

## 튜플 자료형

- 대괄호가 아닌 소괄호를 이용한다.
- 리스트 자료형과 달리 내부 요소에 대한 추가, 수정, 삭제가 불가능하다.

<pre>
>>> tuple1 = (123, 35, 341, 390)
>>> tuple2 = ('This', 'is', 'tuple')
>>> tuple3 = ()
>>> tuple4 = (4943, 482, 494,('Tuple', 'in', 'tuple'))
</pre>

<br>

## 딕셔너리 자료형

- Key1:value1, Key2:value2, Key3:value3,...
- 여러 개의 Key-value쌍이 있으면 중괄호({})로 묶여있다.
- key에는 문자열이나 숫자형, 튜플 자료형이 들어갈 수 있다.
- value에는 어떠한 자료형도 들어갈 수 있다. 심지어 value에는 딕셔너리 자료형도 넣을 수 있다.

<table>

| `Key` | No | Name | Phone | Birth |
|:---:|:---:|:---:|:---:|:---:|
| `value` | A001 | beomwoo | 010-1111-2222 | 0722|

</table>

<br>

<pre>
>>> dic1 = {'NO':'A001', 'Name':'beomwoo', 'phone':'010-1111-2222', 
'Birth':'0722'}
>>> dic1
{'NO':'A001', 'Name':'beomwoo', 'phone':'010-1111-2222', 
'Birth':'0722'}
</pre>

<br>

> 딕셔너리 자료형이 가진 모든 키 값을 얻으려면 keys() 함수를 이용한다.


<pre>
>>> dic1.keys()
dict_keys(['No', 'Name', 'Phone', 'Birth'])
</pre>

<br>

> 딕셔너리 자료형이 가진 모든 value 값을 얻으려면 values() 함수를 이용한다.

<pre>
>>> dic1.values()
dict_values(['A001', 'beomwoo', '010-1111-2222', '0722'])
</pre>

<br>

> 대응되는 key와 value 쌍 모두를 얻으려면 items() 함수를 사용한다.

<pre>
>>> dic1.items()
dict_items([('No', 'A001'), ('Name', 'beomwoo'), ('phone', '010-1111-2222'), ('Birth', '0722')])
</pre>

<br>

> 딕셔너리 자료형에 key-value 쌍을 추가하려면, 단순히 추가할 key값을 입력한 후, "="기호를 이용해 넣을 value 값을 입력해주면 된다.

<pre>
>>> dic1['hobby'] = 'programming'
>>> dic1
{'NO':'A001', 'Name':'beomwoo', 'phone':'010-1111-2222', 'Birth':'0722', 'hobby':'programming'}
</pre>

<br>

> 딕셔너리 자료형에 key-value 쌍을 삭제하려면 del 함수를 이용한다.

<pre>
>>> del dic1['No']
>>> dic1
{'Name':'beomwoo', 'phone':'010-1111-2222', 'Birth':'0722', 'hobby':'programming'}
</pre>

<br>

## 인덱싱(Indexing)

-  말 그대로 하나의 무언가를 '카리킨다' 라는 의미.

> 참고용 이미지

![indexing_image](https://media.vlpt.us/post-images/ceres/6b72ebd0-4336-11ea-bda0-8d09ce94fe71/%EC%BA%A1%EC%B2%98.PNG)

<pre>
>>> str = "Hello, world!"
>>> str
"Hello, world!"
</pre>

<pre>
>>> str[7]
'w'
>>> str[0]
'H'
>>> str[12]
'!'
>>> str[-10]
'l'
</pre>

<br>

## 슬라이싱(Slicing)

- 슬라이싱은 특정 범위를 가리키는 것, 잘라 내는 것을 의미한다.

> 참고용 이미지

![Slicing_image](https://media.vlpt.us/post-images/ceres/617c4870-4349-11ea-9cc9-bd6fa31ea7d5/%EC%BA%A1%EC%B2%98.PNG)

<pre>
>>> str = 'Hello, python! Welcome~'
>>> str
'Hello, python! Welcome~'
>>> str[7]+str[8]+str[9]+str[10]+str[11]+str[12]
'python'
</pre>

> 슬라이싱 활용

<pre>
>>> str[7:13]
'python'
</pre>

- 즉, 슬라이싱 하려는 문자열 뒤에 대괄호를 통해 슬라이싱의 시작 지점과 끝 지점을 지정해주면 된다.
- 예를 들어, str[start : end]와 같이 했다면 str이라는 문자열(또는 리스트 자료형)에서 start 번째 요소부터 end 직전 요소까지 슬라이싱한다.
- end 번째까지 슬라이싱 하는 것이 아니라, 그 직전 요소까지 슬라이싱 한다는 것에 유의하자.

> 추가 예시
<pre>
>>> str
'Hello, python! Welcome~'
>>> str[4:10]
'o, pyt'
>>> str[4:]
'o, python! Welcome~'
>>> str[:10]
'Hello, pyt'
</pre>

<br>

## if문

- "~이면, ~해라."

<br>

> 사용형식
<pre>
if (조건식1):
    (실행할 코드1)
else:
    (실행할 코드2)
</pre>

> 사용형식
<pre>
if (조건식1):
    (조건식1이 참일 때 실행되는 코드1)
    (조건식1이 참일 때 실행되는 코드2)
    ...
elif (조건식2):
    (조건식2가 참일 때 실행되는 코드1)
    (조건식2가 참일 때 실행되는 코드2)
    ...
elif (조건식3):
    (조건식3이 참일 때 실행되는 코드1)
    (조건식3이 참일 때 실행되는 코드2)
    ...
else:
    (조건식1, 조건식2, 조건식3이 모두 거짓일때 실행되는 코드1)
    (조건식1, 조건식2, 조건식3이 모두 거짓일때 실행되는 코드2)
</pre>

<br>

## for문

- 특정 리스트나 튜플, 문자열등의 요소들을 반복하는 구문
- 리스트나 튜플, 문자열 등에 대해서 내부 요소를 순차적으로 하나씩 꺼내고, 꺼낸 요소를 지정한 변수로 사용한다.

> 사용형식

<pre>
for (변수) in (리스트/튜플/문자열 등 iterable 객체):
    (실행되는 코드1)
    (실행되는 코드2)
</pre>

<br>

## while문

- 특정 조건이 만족하는 동안만 반복하게 하는 구문이다.

> 사용형식

<pre>
>>> var = 3
>>> while var > 1:
        print("현재 var의 값:", var)
        var = var - 1

현재 var의 값: 3
현재 var의 값: 2
</pre>

<br>

> 무한반복(while의 조건에 True를 넣어줌)

<pre>
>>> var = 0
>>> while True:
        print("계속 반복될 문장",var)
        var = var + 1
        
계속 반복될 문장 0
계속 반복될 문장 1
계속 반복될 문장 2
계속 반복될 문장 3
.....
</pre>

> 위의 코드를 동작시키면 "계속 반복될 문장(숫자)"가 끊임없이 출력되고, 숫자는 1씩 증가한다.
>즉, while의 조건이 항상 참이므로 그 내부 코드가 무한대로 반복된다.

<br>

## break문과 continue문

- 이들은 for문이나 while문에서 함께 사용되는 구문들이다.
- break문과 continue문은 while문에서 무한루프를 컨트롤하는데 많이 사용된다.

> break문 사용형식

<pre>
>>> var = 0
>>> while True:
        print("var의 값:", var)
        var = var + 1
        if var > 3:
            break
            
var의 값: 0
var의 값: 1
var의 값: 2
var의 값: 3
</pre>

> 이와같이 while문의 조건식이 항상 참인 무한루프지만, 프로그램은 중간에 var 값이 3을 넘어가면
> break문을 만나서 프로그램은 종료된다.

<br>

## continue

- 반복문의 맨 처음으로 돌아가게하는 기능이 있다.
- continue문은 continue문을 만나면 이하의 코드를 실행시키지 않고 다시 반복문의 맨 처음으로 돌아간다.

> continue문 사용 형식
<pre>
>>> var = 10
>>> while var > 0:
        var = var - 1
        if var % 2 == 0:
            print("짝수:", var)
        else:
            continue
            
짝수: 8
짝수: 6
짝수: 4
짝수: 2
짝수: 0
</pre>

<br>

## 함수

![함수 사진](https://wikidocs.net/images/page/24/mixer.png)
> 믹서는 과일을 입력받아 주스를 출력하는 함수와 같다

<br>

- 함수란 단순하게 특정 기능을 하는 것에 대해 반복적인 작업을 단순화시키려는 것이다.
- 프로그램에서는 특정 기능이 반복적으로 기능해야 하는 경우가 많이 존재하기 때문에, 그때마다 동일한 코드를 작성하지 않고, 함수로 만들어두어서 필요할 때 마다 함수를 호출해서 사용한다.

<br>

> 함수 사용형식

<pre>
def 함수 이름(매개변수1, 매개변수2, ...):
    (실행되는 코드1)
    (실행되는 코드2)
    return 반환 값
</pre>
> def는 함수를 만들겠다는 의미를 가진 "예약어"이며, return은 함수의 결괏값을 돌려주는 명령어이다.

<br>

> 함수 사용예시

<pre>
>>> def simple_adder(a,b,c):
        result = a+b+c
        return result
        
>>> answer = simple_adder(10,3,9)
>>> print(answer)

22
</pre>
