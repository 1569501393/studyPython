# 写一个斐波那契数列
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 写一个递归函数，计算n的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:	
        return n * factorial(n - 1)	
    
# 写一个测试用例