#encoding:utf-8

import random
guess_num = random.randint(1,100)

global small
small = 1
global large
large = 100
count = 1

num = input('�п�J�Ʀr : ')
while num != guess_num:
  if num <= guess_num and num > small:
    small = num
    print "�{�b���d��",small,"~",large
  if num >= guess_num and num < large:
    large = num
    print "�{�b���d��",small,"~",large
  num = input('�п�J�Ʀr : ')
  count = count + 1
print ""
print "���ߧA�q��!�׷��K�X�O%d,�A��F%d���q��"%(num,count)