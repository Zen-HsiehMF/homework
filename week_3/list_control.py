#encoding:utf-8

f = open("input.txt")
line = f.readline()
print ''
print '文字檔內容如下：'
print line
x = line.count(' ')	#計算e出現次數
y = line.count('e')	#計算空白
z = len(line)		#計算字元

print '在input.txt文字檔中：空白出現的次數為%d次,而e出現次數則為%d次'%(x,y)
x = float(x)
y = float(y)
z = float(z)

n=round((x/z),3)*100
m=round((y/z),3)*100

print '空白字元佔了%f percent ,e字元佔了%f percent '%(n,m)
f.close

