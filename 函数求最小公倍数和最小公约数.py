#求最大公约数
'''
辗转相除法：
有两整数a和b：

① a%b得余数c

② 若c=0，则b即为两数的最大公约数

③ 若c≠0，则a=b，b=c，再回去执行①

例如求27和15的最大公约数过程为：

27÷15 余12  15÷12余3   12÷3余0因此，3即为最大公约数
'''
def gcd(x, y):
	if x > y:
		(x, y) = (y, x)
	for factor in range(x, 1, -1):
		if x % factor == 0 and y % factor == 0:
			return factor
	return 1


#最小公倍数=两整数的乘积÷最大公约数
def lcm(x, y):          
	return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
