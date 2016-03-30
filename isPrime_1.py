#encoding:utf-8

def isPrime(start,end):
  sum=0
  for x in range(start,end):
    count=1
    for y in range(2,x):
      if x%y==0:
        count=0
        break
    if count==1:
      sum=sum+x
  return sum
print isPrime(2,1000)