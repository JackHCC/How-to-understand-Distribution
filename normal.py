#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :normal.py
@Author  :JackHCC
@Date    :2022/2/18 19:05 
@Desc    :正态分布【连续型】为标准高斯分布，平均值为0，标准差为1

'''
import numpy as np
from matplotlib import pyplot as plt


def normal(x: list):
    """
    form：
    y = f(x) =>
    specific form：
    y = (1 / (sqrt(2 * pi)) * exp(-(x ^ 2 / 2))
    :param x:
    :return:
    """
    u = np.mean(x)
    s = np.std(x)
    x = (x - u) / s
    a = ((x - 0) ** 2) / (2 * (1 ** 2))
    y = (1 / (1 * np.sqrt(2 * np.pi))) * np.exp(-a)
    return x, y, np.mean(x), np.std(x)


if __name__ == "__main__":
    x = np.arange(-100, 101)    # define range of x
    x, y, u, s = normal(x)

    plt.plot(x, y, label=r'$\mu=%.d,\ \sigma=%.d$' % (u, s))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("normal")
    plt.savefig('images/normal.png')
    plt.show()
