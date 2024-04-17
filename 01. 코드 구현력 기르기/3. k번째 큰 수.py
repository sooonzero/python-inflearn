'''
n, k = map(int, input().split())
cards = list(map(int,input().split()))
sumcards = []

for i in range(n):
    for j in range(i+1,n):
        for t in range(j+1,n):
            result = cards[i] + cards[j] + cards[t]
            sumcards.append(result)

sumcards.sort(reverse=True)
print(sumcards[k-1])

'''
#강의 답안( set을 사용해서 중복 제거)

n, k = map(int, input().split())
a = list(map(int, input().split()))
res=set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])


             
