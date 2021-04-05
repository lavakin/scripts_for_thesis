import numpy as np
import math


def power_law(x,a,b):
    return a*np.power(x, b)


def exponential(x,a,b,c):
    return a*np.exp(b*x) + c


def double_exponential(x,a,b,c,d,e):
    return a*np.exp(b*x) + c*np.exp(d*x) + e


def linear(x,a,b):
	return a * x + b


def poly2(x,a,b,c):
	return a * x + b * x**2 + c


def logarithm(x,a,b):
    return a*math.log(x) + b


def plateau(x,a,b):
    return (a*x)/(b + x)


def logistic(x,a):
    1/(1 + np.exp(a*x))


def logistic2(x,a,b,c):
    b/(c + np.exp(a*x))
    
