00 生活中的设计模式：启程之前，请不要错过我
两年前 CSDN 出了一个产品叫 ink，旨在提供一个高质量的写作环境，那时就有写设计模式这一系列的想法了，而且也确实写了，在 ink 里写了三篇文章，后来不知道什么原因这个产品下架了，写的三篇文章也没了，这事也就一直被搁置了；直到今天，我想重新开始，以全新的方式和思路重新写这一系列内容！

文章的特点： 从生活的小故事开始，由浅入深，逐步阐述设计模式的思想，并抽象出代码模型（骨架）。
追求的境界： 用最通俗的语言阐述最难懂的概念；用最简单的语法实现最复杂的逻辑；用最短小的代码写出最强悍的程序！
为什么叫设计模式
什么是设计模式
设计模式最初是被 GoF 于 1995 年提出的，GoF（Gang of Four，四人帮）即 Erich Gamma、Richard Helm、Ralph Johnson和John Vlissides。他们四人于 1995 年出版了一本书《Design Patterns：Elements of Reusable Object-Oriented Software》（翻译成中文是《设计模式 可复用面向对象软件的基础》），第一次将设计模式提升到理论高度，并将之规范化，该书提出了 23 种经典的设计模式。

设计模式（Design Pattern）是一套被反复使用、多数人知晓的、无数工程师实践的代码设计经验的总结，它是面向对象思想的高度提炼和模板化，使用设计模式是为了让代码具有更高的可重用性，更好的灵活性和可拓展性，更易被人阅读和理解。GoF 提到的模式有四个基本要素：

模式名称：助记名，方便讨论、交流、传播；
问题：该模式是用来解决哪类实际问题，即它的应用场景；
解决方案：设计的组成部分，它们之间的相互关系及各自的职责和协作方式；
效果：使用模式能达到的效果，即对使用条件的权衡取舍。
设计模式与生活有什么联系
我一直坚信：程序源于生活，又高于生活！程序的灵魂在于思维的方式，而思维的灵感来源于生活的精彩。互联网是一个虚拟的世界，而程序本身就是对生活场景的虚拟和抽象，每一个模式我都能在生活中找到他的影子。比如，说到状态模式我能想到水有冰、水、气三种状态，而人也有少、壮、老三个不同的阶段；提起中介模式我能立马想到房产中介；看到单例模式，脑海中会即刻浮现心目中的那个她……

设计模式是面向对象的高度抽象和总结，而越抽象的东西越难以理解。本系列文章的目地就是为了降低设计模式的阅读门槛，以生活中的小故事开始，用风趣的方式，由浅入深地讲述每一个模式。让你再次看到设计模式时不只是一个模式，还是生活中的一个个小确幸！程序不是冷冰冰的代码，它还有生活的乐趣和特殊意义。

为什么要学设计模式
设计模式是软件开发人员在软件开发过程中面临的一般问题的解决方案，这些解决方案是众多软件开发人员经过相当长的一段时间的试验和错误总结出来的。所以不管你是新手还是老手，学习设计模式将对你都有莫大的帮助。

学习设计模式的理由有很多，这里只列出几个最实现的：

摆脱面试的窘境，不管是前端工程师还是后端工程师，亦或是全端工程师，设计模式是面试时必问的一道题。
让程序设计能力有一个质的提升，不再是写一堆结构复杂、难以维护的烂代码。
对面向对象的思想有一个更高层次的理解。
如何进行学习
熟悉一门面向对象语言

首先，至少要熟悉一门面向对象的计算机语言。如果没有，请根据自己的学习爱好，或希望从事的工作，先选择一门面向对象语言（C++、Java、Python、Go 等都可以）进行学习和实战，对抽象、继承、多态、封装有一定的基础之后，再来看本系列的文章内容。

了解 Python 的基本语法

对 Python 的基本语法有一个简单了解。Python 语法非常简单，只要有一定的编程语言基础，通过下文的介绍很快就能理解的。

学会阅读 UML 图

UML（Unified Modeling Language）称为统一建模语言或标准建模语言，是面向对象软件的标准化建模语言。UML 规范用来描述建模的概念有：类（对象的）、对象、关联、职责、行为、接口、用例、包、顺序、协作以及状态。

UML 类图表示不同的实体（人、事物和数据）如何彼此相关；换句话说，它显示了系统的静态结构。想进一步了解类图中的各种关系，可参考以下文章：

UML 类图关系大全
UML 类图关系（泛化 、继承、实现、依赖、关联、聚合、组合）
阅读本系列文章

通过阅读本系列文章，以轻松愉快的方式学习设计模式和编程思想。本系列文章没有阅读的先后顺序，每一章都是单独成文，可从任意一篇文章开始。

为什么选择 Python
虽然说设计模式与编程语言没有关系，它是对面向对象思想的灵活应用和高度概括，可以用任何一种语言来实现它，但总归是需要用一种语言进行举例的。本系列文章的所有示例代码均使用 Python 语言编写，为什么选择 Python，主要是基于以下两个原因。

弥补市场空缺
设计模式于 1995 被 GoF 提出，被广泛应用于热门的面对象语言。目前用 Java、C++ 描述的设计模式的书籍和资料已经非常多了，但用 Python 来描述的真是太少了；我在当当上搜索了一下“Python 设计模式”关键字，发现只有那零星的几本书。而作为已经挤进 Top4 的 Python 语言，这明示是不够的。Python 已经越来越成熟，也越来越多地被使用，作为一个有技术追求的 IT 儿有必要了解一下基于 Python 代码设计。

大势所趋，Python 已然成风
C 语言诞生于 1972 年，确随着 Unix 的诞生才深深植根于各大操作系统；
C++ 语言诞生于 1983 年，确因微软的可视化桌面操作系统才得以广泛传播；
Java 语言诞生于 1995 年，确因互联网的迅速崛起才变得家喻户晓；
Python 语言诞生于 1991 年，而下一场技术革命已然开始，AI 时代已然成风。在 AI 领域中已经被广泛使用的 Python 语言必将成为下一个时代的第一开发语言！
最热门的 AI 开源框架 PyTorch 和 TensorFlow 都已经采用了 Python 作为接口和开发语言。除此之外，还有一堆的 AI 相关的框架库，也都纷纷采用，如 AIMA、pyDatalog、SimpleAI、PyBrain、PyML 等。

作为这么一门有前途的语言，必然是要去学习和使用的。

简单的 Python 基础
如果已经熟悉 Python 语言，这一部分的内容可直接跳过！

Python 的特点
Python 崇尚优美、清晰、简单，是一个优秀并广泛使用的语言。

与 Java 和 C++ 这些语言相比，Python 最大的两个特点是：

语句结束不用分号“;”。
代码块用缩进来控制，而不用大括号“{}”。
刚转过来的时候可能会有点不适，用一段时间就好了！

个人觉得，在所有的高级计算机语言中，Python 是最接近人类自然语言的。Python 的语法、风格都与英文的书写习惯非常接近，Python 的这种风格被称为 Pythonic，如条件表达式，在 Java 和 C++ 中是这样的：

int min = x < y ? x : y

而 Python 是这样的：

min = x if x < y else y

有没有觉得第二种方式更接近人类的自然思维？

基本语法
数据类型

Python 是一种弱类型的语言，变量的定义不需要在前面加类型说明，而且不同类型之间可以方便地相互转换。Python 有五个标准的数据类型：

Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
其中 List、Tuple、Dictionary 为容器，将在下一部分介绍。Python 支持四种不同的数字类型：int（有符号整型）、long（长整型）、float（浮点型）、complex（复数）。

每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

Demo：

age = 18        # int
weight = 62.51  # float
name = "Tony"    # string
print("age:", age)
print("weight:", weight)
print("name:", name)
# 变量的类型可以直接改变
age = name
print("age:", age)

a = b = c = 5
# a,b,c三个变量指向相同的内存空间，具有相同的值
print("a:", a, "b:", b, "c:", c)
print("id(a):", id(a), "id(b):", id(b), "id(c):", id(c))

结果：

age: 18
weight: 62.51
name: Tony
age: Tony
a: 5 b: 5 c: 5
id(a): 1457772400 id(b): 1457772400 id(c): 1457772400

常用容器
List（列表）
List（列表）是 Python 中使用最频繁的数据类型，用 [ ] 标识。

列表可以完成大多数集合类的数据结构实现。类似于 Java 中的 ArrayList，C++ 中的 Vector。此外，一个 List 中还可以同时包含不同类型的数据，支持字符、数字、字符串，甚至可以包含列表（即嵌套）。

列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
加号（+）是列表连接运算符，星号（*）是重复操作。
Demo：

list = ['Thomson', 78, 12.58, 'Sunny', 180.2]
tinylist = [123, 'Tony']
print(list)             # 输出完整列表
print(list[0])          # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个元素
print(list[2:])          # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)      # 输出列表两次
print(list + tinylist)  # 打印组合的列表
list[1] = 100            # 修改第二个元素的值
print(list)              # 输出完整列表
list.append("added data")
print(list)              # 输出增加后的列表

结果：

['Thomson', 78, 12.58, 'Sunny', 180.2]
Thomson
[78, 12.58]
[12.58, 'Sunny', 180.2]
[123, 'Tony', 123, 'Tony']
['Thomson', 78, 12.58, 'Sunny', 180.2, 123, 'Tony']
['Thomson', 100, 12.58, 'Sunny', 180.2]
['Thomson', 100, 12.58, 'Sunny', 180.2, 'added data']

Tuple（元组）
Tuple（元组）是另一个数据类型，元组用“()”标识，内部元素用逗号隔开。元组不能二次赋值，相当于只读列表，用法与 List 类似。Tuple 相当于 Java 中的 final 数组，C++ 中的 const 数组。

Demo：

tuple = ('Thomson', 78, 12.58, 'Sunny', 180.2)
tinytuple = (123, 'Tony')
print(tuple)              # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第三个的元素
print(tuple[2:])          # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)      # 输出元组两次
print(tuple + tinytuple)# 打印组合的元组
# tuple[1] = 100         # 不能修改元组内的元素

结果：

('Thomson', 78, 12.58, 'Sunny', 180.2)
Thomson
(78, 12.58)
(12.58, 'Sunny', 180.2)
(123, 'Tony', 123, 'Tony')
('Thomson', 78, 12.58, 'Sunny', 180.2, 123, 'Tony')

Dictionary（字典）
Dictionary（字典）是 Python 中除列表以外最灵活的内置数据结构类型。字典用“{ }”标识，字典由索引（key）和它对应的值 value 组成，相当于 Java 和 C++ 中的 Map。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

Demo：

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'Tony', 'age': 24, 'height': 177}
print(dict['one'])      # 输出键为'one' 的值
print(dict[2])          # 输出键为 2 的值
print(tinydict)         # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())# 输出所有值

结果：

This is one
This is two
{'name': 'Tony', 'age': 24, 'height': 177}
dict_keys(['name', 'age', 'height'])
dict_values(['Tony', 24, 177])

类的定义
使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾，如下实例：

class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体

类的帮助信息可以通过 ClassName.__doc__ 查看，class_suite 由类成员，方法，数据属性组成。如：

class Test:
    "这是一个测试类"

    def __init__(self):
        self.__ivalue = 5

    def getvalue(self):
        return self.__ivalue

其中，__init__ 为初始化函数，相当于构造函数。

访问权限：

__foo__：定义的是特殊方法，一般是系统定义名字，类似 __init__() 之类的。
_foo：以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *。
__foo：双下划线的表示的是私有类型（private）的变量，只能是允许这个类本身进行访问了。
类的继承：

继承的语法结构如下：

class 派生类名（基类名）：
    类体

Python 中继承中的一些特点：

在继承中基类的构造（__init__() 方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
在调用基类的方法时，需要使用 super() 前缀。
Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作“多重继承”。

基础重载方法

Python 的类中有很多内置的方法，我们可以通过重写这些方法来实现一些特殊的功能，这些方法有：

序号	方法	描述	简单的调用
1	__init__(self [,args…] )	构造函数	obj = className(args)
2	__del__(self)	析构方法, 删除一个对象	del obj
3	__repr__(self)	转化为供解释器读取的形式	repr(obj)
4	__str__(self)	用于将值转化为适于人阅读的形式	str(obj)
5	__cmp__(self, x)	对象比较	cmp(obj, x)
Demo 让你顿悟
我们将一段 Java 的代码对应到 Python 中来实现，进行对比阅读，相信很快就能明白其中的用法。Java 代码如下：

class Person {
    public static int visited;

    Person(String name, int age, float height) {
        this.name = name;
        this.age = age;
        this.height = height;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void showInfo() {
        System.out.println("name:" + name);
        System.out.println("age:" + age);
        System.out.println("height:" + height);
        System.out.println("visited:" + visited);
        Person.visited ++;
    }

    private String name;
    protected int age;
    public  float height;
}

class Teacher extends Person {

    Teacher(String name, int age, float height) {
        super(name, age, height);
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void showInfo() {
        System.out.println("title:" + title);
        super.showInfo();
    }

    private String title;

}
public class Test {
    public static void main(String args[]) {
        Person tony = new Person("Tony", 25, 1.77f);
        tony.showInfo();
        System.out.println();
        Teacher jenny = new Teacher("Jenny", 34, 1.68f);
        jenny.setTitle("教授");
        jenny.showInfo();
    }
}

对应的 Python 代码：

class Person:
    "人"
    visited = 0

    def __init__(self, name, age, height):
        self.__name = name
        self._age = age
        self.height = height

    def getName(self):
        return self.__name

    def getAge(self):
        return self._age

    def showInfo(self):
        print("name:", self.__name)
        print("age:", self._age)
        print("height:", self.height)
        print("visited:", self.visited)
        Person.visited = Person.visited +1

class Teacher(Person):
    "老师"

    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.__title = None

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def showInfo(self):
        print("title:", self.__title)
        super().showInfo()

def testPerson():
    "测试方法"
    tony = Person("Tony", 25, 1.77)
    tony.showInfo()
    print();

    jenny = Teacher("Jenny", 34, 1.68);
    jenny.setTitle("教授");
    jenny.showInfo();

testPerson()

自己测试一下，会发现结果是一样的：

name: Tony
age: 25
height: 1.77
visited: 0

title: 教授
name: Jenny
age: 34
height: 1.68
visited: 1

重要说明
为了降低程序复杂度，本系列文章中用到的所有示例代码均不考虑多线程安全，望借鉴 Demo 的读者注意。
本系列所有 Demo 均是在 Python 3.6.3 下编写的，Python 3.0 以上应该都可以正常运行。