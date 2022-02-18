#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :student-t.py
@Author  :JackHCC
@Date    :2022/2/18 19:36 
@Desc    :t分布【连续型】是对称的钟形分布，与正态分布类似，但尾部较重，这意味着它更容易产生远低于平均值的值。

了解更多：https://blog.csdn.net/kdazhe/article/details/105378229
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


def student_t(x: list, freedom: int) -> list:
    """
    form：
    y = f(x) =>
    :param x:
    :param freedom:
    :return:
    """
    c = gamma_func((freedom + 1) // 2) / np.sqrt(freedom * np.pi) * gamma_func(freedom // 2)
    y = c * (1 + x ** 2 / freedom) ** (-((freedom + 1) / 2))
    return y


if __name__ == "__main__":
    for freedom in [1, 2, 5]:
        x = np.arange(-10, 10, 0.01, dtype=np.float64)  # define range of x
        y = student_t(x, freedom=freedom)
        plt.plot(x, y, label=r'$v=%d$' % (freedom))

    plt.legend()
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("student_t")
    plt.savefig('images/student_t.png')
    plt.show()
