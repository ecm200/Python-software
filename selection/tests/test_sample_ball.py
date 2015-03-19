from __future__ import absolute_import
import nose
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm 
from scipy.stats import chi
import nose.tools as nt
import selection.affine as AC

def test_sample_ball():

    p = 10
    A = np.identity(10)[:3]
    b = np.ones(3)
    initial = np.zeros(p)
    eta = np.ones(p)

    bound = 5
    s = AC.sample_truncnorm_white_ball(A,
                                       b, 
                                       initial,
                                       eta,
                                       lambda state: bound + 0.01 * np.random.sample() * np.linalg.norm(state)**2,
                                       burnin=1000,
                                       ndraw=1000,
                                       how_often=5)
    return s

def test_sample_sphere():

    p = 10
    A = np.identity(10)[:3]
    b = np.ones(3)
    initial = -np.ones(p)
    eta = np.ones(p)

    bound = 5
    s1 = AC.sample_truncnorm_white_sphere(A,
                                         b, 
                                         initial,
                                         eta,
                                         lambda state: bound + 0.01 * np.random.sample() * np.linalg.norm(state)**2,
                                         burnin=1000,
                                         ndraw=1000,
                                         how_often=5)

    con = AC.constraints(A, b)
    s2 = AC.sample_from_sphere(con, initial)
    return s1, s2