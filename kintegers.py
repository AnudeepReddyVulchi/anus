n,k=map(int,raw_input().split())
n = list(map(int,raw_input().split()))
a=0
for i in range(0,(k+1)):
	a = a+i
	n.append(a)
print(a)
