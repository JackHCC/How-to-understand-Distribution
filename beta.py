#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :beta.py
@Author  :JackHCC
@Date    :2022/2/18 14:08 
@Desc    :β分布【连续型】与二项分布和伯努利分布共轭。利用共轭，利用已知的先验分布可以更容易地得到后验分布。

了解更多：https://zhuanlan.zhihu.com/p/69606875

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


def beta(x: list, a: int, b: int) -> list:
    """
    form：
    y = f(x) =>
    specific form：
    beta(x, a, b) = (gamma_func(a + b) / (gamma_func(a) * gamma_func(b))) * (x ^ (a - 1)) * ((1 - x) ^ (b - 1))
    :param x:
    :param a:
    :param b:
    :return:
    """
    beta_func = gamma_func(a) * gamma_func(b) / gamma_func(a + b)
    y = (1 / beta_func) * (x ** (a - 1)) * ((1 - x) ** (b - 1))
    return y


def statistic_formula(a: int, b: int):
    """
    special method: get expectation and variance by using formula
    :param a:
    :param b:
    :return:
    """
    u = a / (a + b)
    s = (a * b) / ((a + b + 1) * ((a + b) ** 2))
    return u, s


if __name__ == "__main__":
    for ls in [(1, 3), (5, 1), (2, 2), (2, 5)]:
        a, b = ls[0], ls[1]

        # x in [0, 1], trial is 1/0.001 = 1000
        x = np.arange(0, 1, 0.001, dtype=np.float64)
        y = beta(x, a=a, b=b)
        u, s = statistic_formula(a, b)
        plt.plot(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f,'
                             r'\ \alpha=%d,\ \beta=%d$' % (u, s, a, b))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("beta")
    plt.savefig('images/beta.png')
    plt.show()
