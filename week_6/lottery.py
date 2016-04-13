#encoding:utf-8

import re

member_id = raw_input('請輸入您的會員卡號 : ')
while re.findall("[A-Z]{1}-\d{6}",member_id)==[]:
  print '輸入格式錯誤 , 卡號格式為1個大寫英文字-6碼數字 , 範例 : [R-502765]'
  member_id = raw_input('請重新輸入您的會員卡號 : ')

if re.findall("E-056790",member_id)!=[]:
  print '恭喜您中了獎金10萬元'
elif re.findall("E-\d{1}56790",member_id)!=[]:
  print '恭喜您中了獎金2萬元'
elif re.findall("[A-Z]{1}-\d{3}790",member_id)!=[]:
  print '恭喜您中了獎金100元'
else:
  print '銘謝惠顧 , 謝謝再聯絡'
