from random import randint
import time,sys

#定义玩家为一个类A，玩家拥有灵石和战士
class A:
	def __init__(self,stone):#构造方法
		self.stone=stone#灵石数量
		self.B={}#B代表战士，包含弓箭兵、斧头兵

#定义战士为类B,战士的类为父类
class B:
	def __init__(self,life_length):#构造方法，初始化生命值
		self.life_length=life_length#生命值
	def recovery(self,stone_count):
		if self.life_length==self.maxlife_length:
			print("the soldier already died...")
			return
		self.life_length=stone_count+self.life_length
		if self.life_length>self.maxlife_length:
			self.life_length=self.maxlife_length

class B1(B):
	typename='Archer'#弓箭兵
	employment_price=100
	maxlife_length=100
	#初始化生命值和名字
	def __init__(self,name,life_length=maxlife_length):
		B.__init__(self,life_length)#生命值
		self.name=name#名字
	#打怪
	def fight(self,demon):
		#鹰妖
		if demon.typename=='eagle_demon':
			self.life_length=self.life_length-20
		#狼妖
		else:
			demon.typename=='wolf_demon'
			self.life_length=self.life_length-80

class B2(B):
	typename='Axeman'#斧头兵
	employment_price=120
	maxlife_length=120
	#初始化生命值和名字
	def __init__(self,name,life_length=maxlife_length):
		B.__init__(self,life_length)#生命值
		self.name=name#名字
	#打怪
	def fight(self,demon):
		#鹰妖
		if demon.typename=='eagle_demon':
			self.life_length=self.life_length-80
		#狼妖
		else:
			demon.typename=='wolf_demon'
			self.life_length=self.life_length-20

class eagle():
	typename='eagle_demon'#鹰妖

class wolf():
	typename='wolf_demon'#狼妖

#森林
class forest():   
	def __init__(self,demon):
		self.demon=demon#森林里的妖怪
print("game start...")
forest_number=7#森林数量
forest_List=[]#森林列表
notification='the demon in the forest ahead is：'#显示在屏幕上的内容
for i in range(forest_number):
	typename=randint(0,1)
	if typename==0:
		forest_List.append(forest(eagle()))
	else:
		forest_List.append(forest(wolf()))
	notification+=f'the {i+1} forest is{forest_List[i].demon.typename}'

print(notification,end=' ')#显示妖怪信息

#20秒后删除屏幕信息
time.sleep(20)
for i in range(len(notification)):
	sys.stdout.write('\b')
	time.sleep(0.06)

#创建玩家
A=A(1000)
print(f'you have{A.stone}stone')

#雇佣战士
def hireB():
	menu='''
	please select mercenary type
	a-Archer
	b-Axeman
	c-complete the hire and opt out
	:'''

	while True:
		choice=input(menu)
		if choice not in['a','b','c']:
			print('input error！')
			continue
		if choice=='c':
			return#退出雇佣流程
			#斧头兵和弓箭兵
		if choice=='a':
			hireClass=B1
		else:
			hireClass=B2
		if hireClass.employment_price>A.stone:
			print(f'lock of stone，you only have{A.stone}stone')
			continue
		break

	#给战士命名
	while True:
		Bname=input('please input his name:')#没有输入内容
		if not Bname:
			continue
		if Bname in A.B:
			print('the name is already in use!')
			continue
		break

	#调用战士
	A.B[Bname]=hireClass(Bname)

	#支付灵石
	A.stone=A.stone-hireClass.employment_price
	print(f'employment success，you have some stone left now{A.stone}')

#雇佣弓箭兵和斧头兵
hireB()

#输出灵石和战士的信息
def printInfo():
	print('\n the men under his command are as follows：')
	for name ,B in A.B.items():
		print(f'{name}:{B.typename}life_length{B.life_length}')
printInfo()

for name, B in A.B.items():
    print(f"{B.typename}:{name}")

print('\ngame start...')

#森林关卡
for no,forest in enumerate(forest_List):
    #如果战士队列为空，游戏没有通关，就失败了
    if not A.B:
        print('there are no soldier left!')
        exit()

print(f'\nnow, we alread get the {no+1} forest...')

#派出战士，开始进入森林打怪
while True:
    while True:
        Bname=input('the soldier you are sending are: ')
        if Bname not in A.B:
            print('the soldier does not exit')
            continue
        break
    B=A.B[Bname]

    print(f"now in the forest is:{forest.demon.typename}")

    B.fight(forest.demon)#打怪

    print(f'by fighting，your soldier {Bname},the life_length have {B.life_length}')

    #如果生命值<=0，该战士牺牲，从队列中消失
    if B.life_length<=0:
        print('the soldier died!')
        A.B.pop(Bname)
        #打怪失败，通关失败
        continue
    #打怪成功，通关成功
    else:
        break
input('\n finish the game, press Enter to continue')
#通关后，选择是否给战士疗伤
while True:
    printInfo()
    op=input('''\nplease enter the name of the wounded soldier and the number of stone，
    	the format is：name+20
    	directly enter to exit headling''')

    if not op:
        break
    if op.count('+')!=True:
        print('input format error!')
        continue
    name,stone_count=op.split('+')
    name=name.strip()