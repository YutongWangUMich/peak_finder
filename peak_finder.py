from isotonic_regression_l1_total_order import isotonic_regression_l1_total_order
import numpy as np
import random

def isotonic_regression_l1_total_order_decrease(y,w):
    return -isotonic_regression_l1_total_order(-y,w)


def solve_minimization(y, S):

    increase = True
    j = 0
    s = len(S)
    x = np.zeros_like(y)
    x[:S[j]] = isotonic_regression_l1_total_order(y[:S[j]], np.ones(S[j]))
    for j in range(0,s-1):
        increase = not increase
        if increase:
            x[S[j]:S[j+1]] = isotonic_regression_l1_total_order(y[S[j]:S[j+1]], np.ones(S[j+1]-S[j]))
        else:
            x[S[j]:S[j+1]] = isotonic_regression_l1_total_order_decrease(y[S[j]:S[j+1]], np.ones(S[j+1]-S[j]))
    x[S[-1]:] = isotonic_regression_l1_total_order_decrease(y[S[-1]:], np.ones(len(y)-S[-1]))
    return x, np.sum(np.abs(x-y))

def peak_finder_random_search(y,n_peaks,n_trials = 1000):
    n = len(y)
    x_best = []
    S_best = []
    opt_best = np.Inf
    for _ in range(n_trials):
        S = sorted(random.sample(range(n), 2*n_peaks-1))
        x, opt = solve_minimization(y,S)
        if opt < opt_best:
            x_best = x
            S_best = S
            opt_best = opt
    return x_best, S_best, opt_best

def peak_finder_improve(y, S_best, opt_best):
    n = len(y)
    s = len(S_best)
    for j in range(s):
        S = [S_best[k] for k in range(s)]
        if (S[j]-1 >= 0):
            if (j == 0) or (S[j]-1 > S[j-1]):
                S[j] -= 1
                x_test, opt_test = solve_minimization(y,S)
                if opt_test < opt_best:
                    return x_test, S, opt_test
        S = [S_best[k] for k in range(s)]
        if (S[j] + 1 < n):
            if (j==s-1) or (S[j]+1 < S[j+1]):
                S[j] += 1
                x_test, opt_test = solve_minimization(y,S)
                if opt_test < opt_best:
                    return x_test, S, opt_test
    return [], S_best, opt_best

def peak_finder(y,n_peaks,n_trials= 1000):
    if n_peaks == 1:
        S = [0]
        x,opt = solve_minimization(y, [0])
        for i in range(1,len(y)):
            x_imp,opt_imp = solve_minimization(y, [i])
            if opt_imp < opt:
                x,opt = x_imp,opt_imp
                S = [i]
        return S,x,opt
    else:
        x,S,opt = peak_finder_random_search(y, n_peaks, n_trials)
        x_imp, S_imp, opt_imp = peak_finder_improve(y, S, opt)
        j = 0
        while opt_imp < opt:
            j += 1
            x,S,opt = x_imp, S_imp, opt_imp
            x_imp, S_imp, opt_imp = peak_finder_improve(y, S, opt)
        return S[::2],x,opt
