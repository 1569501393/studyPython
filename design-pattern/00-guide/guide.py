import pprint
import sys
import os

# print hello
print("hello, world!")


x = 1
y = 2
min = x if x < y else y

min2 = x < y and x or y
# print min
print("min =", min)
print("min2 =", min2)

# basic grammar

# data types
# numbers
# string
# list
# tuple
# dictionary

# numbers
# string
age = 18
weight = 62.51
name = "Tony"
# print age
print("age =", age)
# print weight
print("weight =", weight)
# print name
print("name =", name)
print("name:{}, age:{}, weight:{}".format(name, age, weight))

# type conversion
age = name
print("age:", age)

a = b = c = 5
# a,b,c三个变量指向相同的内存空间，具有相同的值
# a: 5 b: 5 c: 5
# id(a): 140197053792624 id(b): 140197053792624 id(c): 140197053792624
print("a:", a, "b:", b, "c:", c)
print("id(a):", id(a), "id(b):", id(b), "id(c):", id(c))

c = 1
# a: 5 b: 5 c: 1
# id(a): 140197053792624 id(b): 140197053792624 id(c): 140197053792496
print("a:", a, "b:", b, "c:", c)
print("id(a):", id(a), "id(b):", id(b), "id(c):", id(c))


# list
list = ["Thomson", 78, 12.58, "Sunny", 180.2]
tinylist = [123, "Tony"]
print("list:", "-" * 120)
print("list:", list)
print("tinylist:", tinylist)
print("list[0]:", list[0])
print("list[1:3]:", list[1:3])
print("list[2:]:", list[2:])
print(tinylist * 2)
print(list + tinylist)
list[1] = 100
print("list:", list)
list.append("added data")
print("list:", list)


# tuple
print("tuple:", "-" * 120)
tuple = ("Thomson", 78, 12.58, "Sunny", 180.2)
tinytuple = (123, "Tony")
print("tuple:", tuple)
print("tinytuple:", tinytuple)
print("tuple[0]:", tuple[0])
print("tuple[1:3]:", tuple[1:3])
print("tuple[2:]:", tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)
# tuple[1] = 100
print("tuple:", tuple)
# tuple.append("added data")
# tuple.index("Sunny")
# tuple: ('Thomson', 78, 12.58, 'Sunny', 180.2) 3
print("tuple:", tuple, tuple.index("Sunny"))

# tuple: ('Thomson', 78, 12.58, 'Sunny', 180.2) 1
print("tuple:", tuple, tuple.count("Sunny"))


# dictionary
print("dict:", "-" * 120)
dict = {}
print("dict:", dict, type(dict))
dict["one"] = "This is one"
dict[2] = "This is two"
tinydict = {"name": "Tony", "age": 24, "height": 177}
print("dict:", dict)
print("tinydict:", tinydict)
print("dict[one]:", dict["one"])
print("dict[2]:", dict[2])
print("tinydict:", tinydict)
print("tinydict.keys():", tinydict.keys())

# tinydict.values(): dict_values(['Tony', 24, 177]) <class 'dict_values'>
print("tinydict.values():", tinydict.values(), type(tinydict.values()))
# {2: "This is two", "one": "This is one"}
pprint.pprint(dict)


# class
print("class:", "-" * 120)


class ClassName:
    "类的帮助信息"
    # class_suite


print("ClassName:", ClassName)
print("ClassName:", ClassName.__doc__, help(ClassName))


class Test:
    "这是一个测试类"

    def __init__(self):
        self.__ivalue = 5

    def getvalue(self):
        return self.__ivalue


# class Person
class Person:
    "人类"
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
        print("visited", self.visited)
        Person.visited += 1


# class Teacher
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


# testPerson
def testPerson():
    "测试方法"
    tony = Person("Tony", 25, 1.77)
    tony.showInfo()
    print()

    jenny = Teacher("Jenny", 34, 1.68)
    jenny.setTitle("教授")
    jenny.showInfo()


print("testPerson:", "-" * 120)
testPerson()

# operators
# + - * / % ** // << >> & | ^ ~


# control flow
# if
# if-else
# elif
# while
# for

# function


# exception

# design pattern

# other
print("other:", "-" * 120)
# print("hello, world!")
print("hello, world!")
