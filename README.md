# 선수지식

## 변수명 정하기
1. 영문과, 숫자, _ 로 이뤄진다.
2. 대소문자를 구분한다.
3. 문자나, _ 로 시작한다.
4. 특수문자를 사용하면 안된다
5. 키워드를 사용하면 안된다.

## 변수 입력과 연산자
a = input()
a,b = input().split()
map(int, input().split())

## 반복문(for, while)
range
a = range(10)  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(1, 11) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
print(”hello”)
for i in range(10, 0, -1):
print(”hello”)
i = 1
while i ≤ 10:
print(i)
i += 1
break
continue 밑에 생략하고 지나가버림
continue 를 활용한 홀수 출력
for i in range(1, 11):
if i % 2 == 0:
continue
print(i)
for else 문
for i in range(1, 11):
print(i)
if i == 5:
break
else:
print(11)
for else, while else는 break 조건이 있는 경우 사용

## 반복문을 이용한 문제풀이
1. 1 부터 n 까지 홀수 출력
2. 1부터 n 까지의 합
3. n의 약수 출력

## 중첩 반복문(2중 for 문)

## 문자열과 내장함수
.upper() 대문자로 만들기
.find(’ ’) 해당하는 문자의 인덱스 번호
.count(’ ‘) 해당하는 문자의 갯수 출력
[:2] 0, 1, 2, 출력(슬라이스)
len() 공백포함 길이 출력
for x in msg:
print(x, end=’ ‘)
.isupper() 대문자일경우 참
.islower() 소문자일경우 참
.isalpha() 알파벳일경우 참
ord() 아스키 넘버 출력
chr() 아스키넘버를 문자로 출력

## 리스트와 내장함수 1
import random as r
list(range(1, 11))
1 부터 10까지 리스트 초기화
리스트끼리 + 해서 더할 수 있다.
a.append(4) a 리스트 뒤에 4 추가
a.insert(3, 7) 3번 인덱스에 7 넣어주기(삭제아님)
a.pop() a 인덱스 맨 뒤에 제거
a.pop(3) a 의 3 번 인덱스 제거
a.remove(3) a 리스트에 3 이라는 값을 찾아서 삭제
print(a.index(4)) a 리스트에 4번이라는 값의 인덱스 번호 출력
sum(a) 리스트 a 의 모든 값을 더한다.
max(a)
min(a)
a 리스트의 최댓값 최솟값 구하기
r.shuffle(a) a 리스트 랜덤으로 섞기
a.sort() 오름차순정렬
a.sort(reverse = True) 내림차순정렬
a.clear() 빈 리스트로 만들기

### 리스트와 내장함수2
for i in range(len(a)):
print(a[i], end = ‘ ‘)
이거랑
아래의
for x in a:
pirnt(a[x], end=’ ‘)
랑 같다
enumerate(a) 튜플 형태로 대입
for x in enumerate(a):
print(x)
단, 튜플값은 변경이 불가능하다.
for index, value in enumerate(a):
print(index, value)
모든 결과가 참일때 거짓일때: all()
if all(60>x for x in a):
print(”yes”)
else:
print(” no”)
한번이라도 결과가 참일때: any()
if any()

## 리스트 생성과 접근
1차원 리스트 초기화
a = [0]*3
2차원 리스트 초기화, for 문에 _ 는 변수 없이 반복문만 돈다는 의미
a[[0]*3 for *in range(3*)]

## 함수 만들기
def add(a,b):
함수는 가장 위에 만들기
python에서 함수는 여러개의 값을 반환할 수 있다.

## 람다 함수
함수에 이름이 없다.
표현식, 내장함수의 인자로 사용할 때 장점
일반 함수와 비교해보기
def plus_one(x):
return x + 1
plus_two = lambda x: x+2
a = [1,2,3]

print(list(map(pluse_one,a)))

print(list(map(lambda x: x+1, a)))
