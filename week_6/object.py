#encoding:utf-8

class Hanwei:
  mantra = '我一點都不會介意XD'
  def skill(self,name):
    print name+'專長為C語言'
    print name+'專長為電腦網路'

class Student(Hanwei):
  def interest(self,name):
    self.name = name
    print name+'興趣為Python'    

hanwei = Hanwei()
mingfeng = Student()
hanwei.skill('教授')
mingfeng.skill('學生')
mingfeng.interest('學生')
print hanwei.mantra
print mingfeng.mantra
