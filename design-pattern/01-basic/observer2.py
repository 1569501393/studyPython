# observer pattern
# 观察者模式
# 定义对象间的一种一对多的依赖关系，使得每当一个对象改变状态，则所有依赖于它的对象都会得到通知并自动更新。


# class Observable
class Observable:
    "The Basic class of observable"

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for observer in self.__observers:
            observer.update(self, object)


# class WaterHeater
class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("temperature:", self.__temperature)
        self.notifyObservers()


# class WashingMode
class WashingMode(Observable):
    def update(self, observable, object):
        if (
            isinstance(observable, WaterHeater)
            and observable.getTemperature() >= 50
            and observable.getTemperature() < 70
        ):
            print("Washing Mode")


# class DrinkingMode
class DrinkingMode(Observable):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 60:
            print("Drinking Mode")


# test
def testWaterHeater():
    heater = WaterHeater()
    washingObserver = WashingMode()
    drinkingObserver = DrinkingMode()
    heater.addObserver(washingObserver)
    heater.addObserver(drinkingObserver)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


testWaterHeater()
