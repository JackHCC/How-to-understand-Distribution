#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :gaussian.py
@Author  :JackHCC
@Date    :2022/2/18 18:50 
@Desc    :高斯分布【连续型】是一种非常常见的连续概率分布。

'''
import numpy as np
from matplotlib import pyplot as plt


def gaussian(x: list):
    """
    form：
    y = f(x) =>
    specific form：
    y = (1 / (std(x) * sqrt(2 * pi))) * exp(-((x - mean(x)) ^ 2 / (2 * (std(x) ^ 2)))
    :param x:
    :return:
    """
    u = np.mean(x)
    s = np.std(x)

    a = ((x - u) ** 2) / (2 * (s ** 2))
    y = (1 / (s * np.sqrt(2 * np.pi))) * np.exp(-a)
    return y, u, s


if __name__ == "__main__":
    x = np.arange(-100, 101)    # define range of x
    y, u, s = gaussian(x)

    plt.plot(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("gaussian")
    plt.savefig('images/gaussian.png')
    plt.show()
