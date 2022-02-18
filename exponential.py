#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :exponential.py
@Author  :JackHCC
@Date    :2022/2/18 18:30 
@Desc    :指数分布【连续型】是 α 为 1 时 gamma 分布的特例

'''
import numpy as np
from matplotlib import pyplot as plt


def exponential(x: list, lamb: float) -> list:
    """
    form：
    y = f(x) =>
    specific form：
    y = lamb * exp(-lamb * x) , where  x >= 0
    :param x:
    :param lamb:
    :return:
    """
    y = [lamb * np.exp(-lamb * xn) if xn >= 0 else 0 for xn in x]
    return y


def statistic_formula(lamb: int):
    """
    special method: get expectation and variance by using formula
    :param lamb:
    :return:
    """
    u = 1 / lamb
    s = 1 / (lamb ** 2)
    return u, s


if __name__ == "__main__":
    for lamb in [0.5, 1, 1.5]:
        x = np.arange(0, 20, 0.01, dtype=np.float64)
        y = exponential(x, lamb=lamb)
        u, s = statistic_formula(lamb)
        plt.plot(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f,'
                             r'\ \lambda=%.1f$' % (u, s, lamb))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("exponential")
    plt.savefig('images/exponential.png')
    plt.show()
