#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :dirichlet.py
@Author  :JackHCC
@Date    :2022/2/18 14:58 
@Desc    :dirichlet 分布与多项式分布是共轭的。如果 k=2，则为β分布, 这里以 k=3为例

了解更多：https://baike.baidu.com/item/%E7%8B%84%E5%88%A9%E5%85%8B%E9%9B%B7%E5%88%86%E5%B8%83/12728892
'''
import numpy as np
from random import randint
from matplotlib import pyplot as plt


def normalization(x: list, s: float):
    """
    normalize list x, where sum(x) == s
    :param x:
    :param s:
    :return:
    :return:
    """
    return [(i * s) / sum(x) for i in x]


def sampling():
    return normalization([randint(1, 100), randint(1, 100), randint(1, 100)], s=1)


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


def beta_func(alpha: list) -> float:
    """
    beta_func(alpha_1, ……, alpha_k) = ((gamma_func(alpha_1) * …… * gamma_func(alpha_k)) / gamma_func(alpha_1 + …… + alpha_k))

    :param alpha: list, len(alpha) is k
    :return:
    """
    numerator = 1
    for a in alpha:
        numerator *= gamma_func(a)
    denominator = gamma_func(sum(alpha))
    return numerator / denominator


def dirichlet(x: list, a: list, n: int) -> list:
    """
    form：
    y = f(x) =>
    specific form：
    dirichlet(x, a) = (gamma_func(a_1 + …… + a_k) / (gamma_func(a_1) * …… * gamma_func(a_k))) * (x_1 ^ (a_1 - 1)) * …… * (x_k ^ (a_k - 1))
    :param x: list of [x[1,...,K], x[1,...,K], ...], shape is (n_trial, K)
    :param a:
    :param n:
    :return:
    """
    c = (1 / beta_func(a))
    y = [c * (xn[0] ** (a[0] - 1)) * (xn[1] ** (a[1] - 1)) * (xn[2] ** (a[2] - 1)) for xn in x]
    x = np.arange(n)
    return x, y


if __name__ == "__main__":
    n_experiment = 30
    for ls in [(6, 2, 2), (3, 7, 5), (6, 2, 6), (2, 3, 4)]:
        alpha = list(ls)
        # random sampling [x[1,...,K], x[1,...,K], ...], shape is (n_trial, K)
        # each sum of row should be one.
        x = [sampling() for _ in range(1, n_experiment + 1)]

        x, y = dirichlet(x, alpha, n=n_experiment)
        plt.plot(x, y, label=r'$\alpha=(%d,%d,%d)$' % (ls[0], ls[1], ls[2]))

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("dirichlet")
    plt.savefig('images/dirichlet.png')
    plt.show()
