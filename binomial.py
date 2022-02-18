#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :binomial.py
@Author  :JackHCC
@Date    :2022/2/18 10:48 
@Desc    :二项分布【离散型】：参数为 n 和 p 的二项分布是一系列 n 个独立实验中成功次数的离散概率分布。二项式分布是指通过指定要提前挑选的数量而考虑先验概率的分布。

'''
import numpy as np
import logging
from matplotlib import pyplot as plt
from functools import reduce


def c(n: int, k: int) -> int:
    """
    C(n , k) = n! / (n - k)! * k!
    :param n:
    :param k:
    :return:
    """
    if n < k:
        logging.error("parameter n must greater than parameter k!")
    k = min(k, n - k)
    numerator = reduce(int.__mul__, range(n, n - k, -1), 1)
    denominator = reduce(int.__mul__, range(1, k + 1), 1)
    return numerator / denominator


def binomial(n: int, p: float) -> list:
    """
    form：
    y = f(k) =>
    specific form：
    y = C(n, k) * p ^ k * (1 - p) ^ (n - k) , 0 <= k <= n
    :param n:
    :param p:
    :param k:
    """
    if p <= 0 or p >= 1:
        logging.error("parameter p must be between 0 and 1!")

    y = [c(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n)]
    return y


def statistic(x: float, y: float):
    """
    common method: get expectation and variance by using statistical method
    :param x:
    :param y:
    :return:
    """
    u = np.sum(np.multiply(x, y))
    s = np.sum(np.multiply((x - u) ** 2, y))
    return u, s


def statistic_formula(n: int, p: float):
    """
    special method: get expectation and variance by using formula
    :param n:
    :param p:
    :return:
    """
    if p <= 0 or p >= 1:
        logging.error("parameter p must be between 0 and 1!")
    u = n * p
    s = n * p * (1 - p)
    return u, s


if __name__ == "__main__":
    for ls in [(0.5, 20), (0.7, 40), (0.5, 40)]:
        p, n = ls[0], ls[1]
        x = np.arange(n)
        y = binomial(n, p)
        # 这里对比公式计算均值方差和统计方法计算均值方差
        u, s = statistic(x, y)
        # u, s = statistic_formula(n, p)
        plt.scatter(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("binomial")
    plt.legend()
    plt.savefig('images/binomial.png')
    plt.show()

