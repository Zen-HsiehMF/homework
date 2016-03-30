#encoding:utf-8
import random
guess_num = random.randint(1,100)
 
global small
small = 1
global large
large = 100
count = 1

num = input('請輸入數字 : ')
while num != guess_num:
  if num <= guess_num and num > small:
    small = num
    print "現在的範圍為",small,"~",large
  if num >= guess_num and num < large:
    large = num
    print "現在的範圍為",small,"~",large
  num = input('請輸入數字 : ')
  count = count + 1
print ""
print "恭喜你猜中!終極密碼是%d,你花了%d次猜中"%(num,count)
