#encoding:utf-8

import random

str="Honey, you are always on my mind. Your love makes me blind .When I first met you I knew it was a sign."

g_friend={'Mary':'Honey','Lynn':'Baby','jannie':'Little sweetie'}

which_num=random.randint(1,3)
print "今天你的第%d號女朋友來見你了"%which_num

if which_num==1:
  print str
elif which_num==2:
    print str.replace("Honey",g_friend['Lynn'])
elif which_num==3:
      print str.replace("Honey",g_friend['jannie'])
