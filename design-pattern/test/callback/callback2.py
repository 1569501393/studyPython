# -*- coding: utf-8 -*-
# 回调函数2
# 技能抽象类
# 公司新员工
# 唱歌
# 说段子
# 拉Ukulele
# 表演魔术
# 玩滑板
from abc import ABCMeta, abstractmethod


# 技能抽象类
class Skill(metaclass=ABCMeta):
    @abstractmethod
    def performance(self):
        """技能表演"""
        pass


# 公司新员工
class NewEmployee:
    """公司新员工"""

    def __init__(self, name):
        self.name = name

    def doPerformance(self, skill):
        print(self.name + "的表演:", end="")
        skill.performance()


# 唱歌
class Sing(Skill):
    """唱歌"""

    def performance(self):
        print("唱一首歌")


# 说段子
class Joke(Skill):
    """说段子"""

    def performance(self):
        print("说一个段子")


# 拉Ukulele
# 表演魔术
# 玩滑板

helen = NewEmployee("helen")
helen.doPerformance(Sing())
frank = NewEmployee("frank")
frank.doPerformance(Joke())

# 说段子
joke = Joke()
joke.performance()
