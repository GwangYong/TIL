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

> 말 그대로 하나의 무언가를 '카리킨다' 라는 의미.

- 참고용 이미지

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

> 슬라이싱은 특정 범위를 가리키는 것, 잘라 내는 것을 의미한다.

- 참고용 이미지

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

## 제어문