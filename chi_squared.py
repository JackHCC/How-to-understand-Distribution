#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :chi_squared.py
@Author  :JackHCC
@Date    :2022/2/18 19:13 
@Desc    :卡方分布【连续型】是 β 分布的特例。k 自由度的卡方分布是 k 个独立标准正态随机变量的平方和的分布。

了解更多：https://www.zhihu.com/question/304500591
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


def chi_squared(x: list, k: int):
    """
    form：
    y = f(x) =>
    specific form：
    beta distribution -> a = k / 2, b = 1 / 2
    :param x:
    :param k:
    :return:
    """
    c = (1 / (2 ** (k / 2))) * gamma_func(k // 2)
    y = c * (x ** (k / 2 - 1)) * np.exp(-x / 2)
    return y


def statistic_formula(k: int):
    """
    special method: get expectation and variance by using formula
    :param k:
    :return:
    """
    u = k
    s = 2 * k
    return u, s


if __name__ == "__main__":
    for k in [2, 3, 4, 6]:
        x = np.arange(0, 10, 0.01, dtype=np.float64)
        y = chi_squared(x, k)
        u, s = statistic_formula(k)
        plt.plot(x, y, label=r'$k=%d, \mu=%.2f, \sigma=%.2f$' % (k, u, s))

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("chi-squared")
    plt.savefig('images/chi-squared.png')
    plt.show()
