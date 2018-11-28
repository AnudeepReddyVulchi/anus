a=int(input(" "))
h=0
v=a
for i in range(0,a+1):
		if(i%60==0 and i>=60):
				h+=1
				v-=60
print(h,v)
