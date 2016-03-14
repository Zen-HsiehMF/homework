#encoding:utf-8

number = input('請輸入質數：')
if number==1:				#使用者不能輸入小於等於1的數值
  print '1不是質數'
  exit() 				#終止程式
elif number<1:
  print '請輸入大於1的數字'
  exit()

for number in range(number,number+1):
  count=1
  for y in range(2,number):
    if(number%y==0):
      count=0
      break
  if count:
    print '%d是質數'%number
  if count==0:
    print '%d不是質數'%number
