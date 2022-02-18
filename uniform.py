#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :uniform.py
@Author  :JackHCC
@Date    :2022/2/17 22:20 
@Desc    :均匀分布【连续型】：均匀分布在 [a，b] 上具有相同的概率值，是简单概率分布。

'''
import numpy as np
import logging
from matplotlib import pyplot as plt


def uniform(x: list, a: float, b: float) -> list:
    """
    form：
    y = f(x) =>
    specific form：
    y = 1 / (b - a) , a <= x <= b
    y = 0 , other
    :param x:
    :param a:
    :param b:
    :return:
    """
    if a >= b:
        logging.error("parameter b must greater than parameter a!")
        return None

    y = [1 / (b - a) if b >= val >= a else 0 for val in x]
    return y


def statistic_formula(a: float, b: float):
    """
    get expectation and variance
    :param a:
    :param b:
    :return:
    """
    if a >= b:
        logging.error("parameter b must greater than parameter a!")
    u = (a + b) / 2
    s = (b - 1) ** 2 / 12
    return u, s


if __name__ == "__main__":
    x = np.arange(-100, 100)
    for ls in [(-50, 50), (10, 20)]:
        a, b = ls[0], ls[1]
        y = uniform(x, a, b)
        u, s = statistic_formula(ls[0], ls[1])
        plt.plot(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("uniform")
    plt.legend()
    plt.savefig('images/uniform.png')
    plt.show()

