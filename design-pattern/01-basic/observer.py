# observer pattern
# 观察者模式
# 定义对象间的一种一对多的依赖关系，使得每当一个对象改变状态，则所有依赖于它的对象都会得到通知并自动更新。


# class WaterHeater
class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("temperature:", self.__temperature)
        self.__notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def __notifies(self):
        for observer in self.__observers:
            observer.update(self)


# class Observer
class Observer:
    "The Parent class of WashingMode and DrinkingMode"

    def update(self, waterHeater):
        pass


# class WashingMode
class WashingMode(Observer):
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 100:
            print("Washing Mode")


# class DrinkingMode
class DrinkingMode(Observer):
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 60:
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
