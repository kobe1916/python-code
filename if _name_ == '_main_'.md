1. 摘要
通俗的理解__name__ == '__main__'：假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；在你自己眼中，你是你自己(__name__ == '__main__')。

if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
2. 程序入口
对于很多编程语言来说，程序都必须要有一个入口，比如C，C++，以及完全面向对象的编程语言Java，C#等。如果你接触过这些语言，对于程序入口这个概念应该很好理解，C，C++都需要有一个main函数作为程序的入口，也就是程序的运行会从main函数开始。同样，Java，C#必须要有一个包含Main方法的主类，作为程序入口。

而Python则不同，它属于脚本语言，不像编译型语言那样先将程序编译成二进制再运行，而是动态的逐行解释运行。也就是从脚本第一行开始运行，没有统一的入口。

一个Python源码文件（.py）除了可以被直接运行外，还可以作为模块（也就是库），被其他.py文件导入。不管是直接运行还是被导入，.py文件的最顶层代码都会被运行（Python用缩进来区分代码层次），而当一个.py文件作为模块被导入时，我们可能不希望一部分代码被运行。
2.1 一个.py文件被其他.py文件引用
假设我们有一个const.py文件，内容如下：
'''
PI = 3.14

def main():
    print("PI:", PI)

main()

# 运行结果：PI: 3.14
'''
现在，我们写一个用于计算圆面积的area.py文件，area.py文件需要用到const.py文件中的PI变量。从const.py中，我们把PI变量导入area.py：
'''
from const import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print("round area: ", calc_round_area(2))

main()

'''
运行结果：
PI: 3.14
round area:  12.56
'''
'''
2.2 修改const.py，添加if __name__ == "__main__"
我们看到const.py中的main函数也被运行了，实际上我们不希望它被运行，因为const.py提供的main函数只是为了测试常量定义。这时if __name__ == '__main__'派上了用场，我们把const.py改一下，添加if __name__ == "__main__"：
'''
PI = 3.14

def main():
    print("PI:", PI)

if __name__ == "__main__":
    main() 
'''
运行const.py，输出如下：
PI: 3.14
运行area.py，输出如下：
round area:  12.56
如上，我们可以看到if __name__ == '__main__'相当于Python模拟的程序入口，Python本身并没有这么规定，这只是一种编码习惯。由于模块之间相互引用，不同模块可能有这样的定义，而程序入口只有一个。到底哪个程序入口被选中，这取决于__name__的值。 
3. __name__
3.1 __name__反映一个包的结构
__name__是内置变量，可用于反映一个包的结构。假设我们有一个包a，包的结构如下：
a
├── b
│   ├── c.py
│   └── __init__.py
└── __init__.py
在包a中，文件c.py，__init__.py，__init__.py的内容都为：
print(__name__)
当一个.py文件（模块）被其他.py文件（模块）导入时，我们在命令行执行
python -c "import a.b.c"
结果：
a
a.b
a.b.c




















