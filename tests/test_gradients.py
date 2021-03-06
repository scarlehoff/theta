"""Python Unit testing for gradients"""

import numpy as np
from theta.model import Model
from theta.layers import ThetaUnitLayer, DiagExpectationUnitLayer, Linear, NonLinear, SoftMaxLayer


def run_check(mdl, diffepsilon=1e-5, epsilon=1e-5):
    n = 1000
    data = np.random.random_sample(n).reshape(1, n)
    for p in range(len(mdl.get_parameters())):
        num, back = mdl.gradient_check(p, data, epsilon)
        assert np.abs(num - back) < diffepsilon


def test_thetaunitlayer_1():
    mdl = Model()
    mdl.add(ThetaUnitLayer(1, 1, diagonal_T=True))
    run_check(mdl)


def test_thetaunitlayer_2():
    mdl = Model()
    mdl.add(ThetaUnitLayer(1, 1, Nhidden=2, diagonal_T=True))
    run_check(mdl, 1e-2)


def test_diagexpectationunitlayer():
    mdl = Model()
    mdl.add(DiagExpectationUnitLayer(1, 1))
    run_check(mdl)


def test_linear():
    mdl = Model()
    mdl.add(Linear(1,1))
    run_check(mdl)


def test_nonlinear():
    mdl = Model()
    mdl.add(NonLinear(1,1))
    run_check(mdl)


def test_softmax():
    mdl = Model()
    mdl.add(SoftMaxLayer(1))
    run_check(mdl)
