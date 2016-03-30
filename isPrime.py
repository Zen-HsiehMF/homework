#encoding:utf-8

def isPrime(n):
  for x in range(n,n+1):
    count=1
    for y in range(2,n):
      if x%y==0:
        count=0
        break
    if(count==1):
      return 1
    elif(count==0):
      return 0
sum=0
for n in range(2,1000):
  if isPrime(n)==1:
    sum=sum+n
print sum
