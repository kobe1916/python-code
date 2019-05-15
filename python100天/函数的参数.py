# 参数默认值
def f1(a, b=5, c=10):
	return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


# 可变参数  *args--元组  参数个数可任意
def f2(*args):
	sum = 0
	for num in args:
		sum += num
	return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数    **kw--字典
def f3(**kw):
	if 'name' in kw:
		print('欢迎你%s!' % kw['name'])
	elif 'tel' in kw:
		print('你的联系电话是: %s!' % kw['tel'])
	else:
		print('没找到你的个人信息!')


param = {'name': '骆昊', 'age': 38}
f3(**param)
f3(name='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, mobile='13866778899')


def foo(*args, **kwargs):    

    print 'args = ', args    

    print 'kwargs = ', kwargs    

    print '---------------------------------------'

if __name__ == '__main__':
   foo(1,2,3,4)
   foo(a=1,b=2,c=3)
   foo(1,2,3,4, a=1,b=2,c=3)
   foo('a', 1, None, a=1, b='2', c=3)
   #可以看到，这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；
   #**kwargs表示关键字参数，它是一个dict。
   #并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，
   #像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。
