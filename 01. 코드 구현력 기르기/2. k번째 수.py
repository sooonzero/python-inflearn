testcase = int(input())

def solution (n,s,e,k,numbers):
    #오름차순 정렬
    result = numbers[s-1:e]
    result.sort()
    return result[k-1]


for i in range (1, (testcase+1)):
    #첫번째줄 입력받아서 n s e에 넣기
    n, s, e, k = map(int, input().split())

    #두번째줄 입력받아서 numbers에 넣기
    numbers = list(map(int,input().split()))
    print('#', end='')
    print(i,solution(n,s,e,k,numbers))




'''
[K번째 수:강의답안]
T=int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split())
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t, a[k-1]))


'''
    
    
