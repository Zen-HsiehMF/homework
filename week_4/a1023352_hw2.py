<<<<<<< HEAD
#encoding:utf-8

import random
guess_num = random.randint(1,100)

global small
small = 1
global large
large = 100
count = 1

num = input('è«‹è¼¸å…¥æ•¸å­— : ')
while num != guess_num:
  if num <= guess_num and num > small:
    small = num
    print "ç¾åœ¨çš„ç¯„åœç‚º",small,"~",large 
  if num >= guess_num and num < large:
    large = num
    print "ç¾åœ¨çš„ç¯„åœç‚º",small,"~",large  
  num = input('è«‹è¼¸å…¥æ•¸å­— : ')
  count = count + 1
print ""
print "æ­å–œä½ çŒœä¸­!çµ‚æ¥µå¯†ç¢¼æ˜¯%d,ä½ èŠ±äº†%dæ¬¡çŒœä¸­"%(num,count)
=======
#encoding:utf-8

import random
guess_num = random.randint(1,100)

global small
small = 1
global large
large = 100
count = 1

num = input('½Ğ¿é¤J¼Æ¦r : ')
while num != guess_num:
  if num <= guess_num and num > small:
    small = num
    print "²{¦bªº½d³ò¬°",small,"~",large
  if num >= guess_num and num < large:
    large = num
    print "²{¦bªº½d³ò¬°",small,"~",large
  num = input('½Ğ¿é¤J¼Æ¦r : ')
  count = count + 1
print ""
print "®¥³ß§A²q¤¤!²×·¥±K½X¬O%d,§Aªá¤F%d¦¸²q¤¤"%(num,count)
>>>>>>> 3ca72c46a17871ec33a168bbd349ce66192f153f
