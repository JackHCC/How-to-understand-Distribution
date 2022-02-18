#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :gamma.py
@Author  :JackHCC
@Date    :2022/2/18 18:03 
@Desc    :伽马分布【连续型】：假设随机变量X为等到第 a 件事发生所需的等候时间, b 为事情发生一次的概率, 指数分布和卡方分布是伽马分布的特例。

了解更多：https://zhuanlan.zhihu.com/p/105482657
'''
import numpy as np
from matplotlib import pyplot as plt


def gamma_func(n: int) -> int:
    """
    if n is int: gamma_func(n) = (n - 1)!
    :param n:
    :return:
    """
    val = 1
    for i in range(2, n):
        val *= i
    return val


def gamma(x: list, a: float, b: float) -> list:
    """
    form：
    y = f(x) =>
    specific form：
    y = ((b ^ a) * (x ^ (a - 1)) * (exp(-b * x))) / gamma_func(a)
    :param x:
    :param a:
    :param b:
    :return:
    """
    c = (b ** a) / gamma_func(a)
    y = c * (x ** (a - 1)) * np.exp(-b * x)
    return y


def statistic_formula(a: int, b: int):
    """
    special method: get expectation and variance by using formula
    :param a:
    :param b:
    :return:
    """
    u = a / b
    s = a / (b ** 2)
    return u, s


if __name__ == "__main__":
    for ls in [(1, 1), (2, 1), (3, 1), (2, 2)]:
        a, b = ls[0], ls[1]

        x = np.arange(0, 20, 0.01, dtype=np.float64)
        y = gamma(x, a=a, b=b)
        u, s = statistic_formula(a, b)
        plt.plot(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f,'
                             r'\ \alpha=%d,\ \beta=%d$' % (u, s, a, b))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("gamma")
    plt.savefig('images/gamma.png')
    plt.show()
