#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :bernoulli.py
@Author  :JackHCC
@Date    :2022/2/17 22:47 
@Desc    :伯努利分布（0-1分布）【离散型】：先验概率 p（x）不考虑伯努利分布。因此，如果我们对最大似然进行优化，那么我们很容易被过度拟合。

'''
import numpy as np
import random
import logging
from matplotlib import pyplot as plt


def bernoulli(p: float, k: bool) -> float:
    """
    form：
    y = f(k) =>
    specific form：
    y = p ^ k * (1 - p) ^ (1 - k) , k = 0 or 1
    =>
    y = p, k = 1
    y = 1 - p, k = 0
    :param p:
    :param k:
    :return:
    """
    if p <= 0 or p >= 1:
        logging.error("parameter p must be between 0 and 1!")
    return p if k else 1 - p


def statistic_formula(p: float):
    """
    get expectation and variance
    :param p:
    :return:
    """
    if p <= 0 or p >= 1:
        logging.error("parameter p must be between 0 and 1!")
    u = p
    s = p * (1 - p)
    return u, s


if __name__ == "__main__":
    n_experiment = 100
    p = 0.6
    x = np.arange(n_experiment)
    y = []
    for _ in range(n_experiment):
        # getrandbits()方法返回指定大小（以位为单位）的整数。
        pick = bernoulli(p, k=bool(random.getrandbits(1)))
        y.append(pick)

    u, s = statistic_formula(p)
    plt.scatter(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("bernoulli")
    plt.legend()
    plt.savefig('images/bernoulli.png')
    plt.show()
