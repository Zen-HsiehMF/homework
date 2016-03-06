#encoding:utf-8

sys_name='Zen-HsiehMF'
print'歡迎光臨 %s 系統'%sys_name
found = 5000
money = raw_input('請輸入提款金額：');
money = int(money) 
found -= money
if found>0:
	print'您的存款還剩%d元'%found
elif found==0:
	print'您的存款無剩餘存款囉!!'
elif found<0:
	print'您的存款不足,多賺點錢吧!!'
f = open("ATM.txt","w")
f.write("經使用者提款後,最終存款為%d元"%found)
f.close()
