# print("1+1=", 1 + 1)
# 观察者模式
# 定义对象间的一种一对多的依赖关系，使得每当一个对象改变状态，则所有依赖于它的对象都会得到通知并自动更新。
class Observer:
    def update(self, message):
        raise NotImplementedError


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("ConcreteObserver:", message)


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# 使用
subject = Subject()
observer1 = ConcreteObserver("observer1")
observer2 = ConcreteObserver("observer2")
subject.add_observer(observer1)
subject.add_observer(observer2)
subject.notify_observers("hello world")
