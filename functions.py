import numpy as np
import math


def power_law(x,a,b):
    return a*np.power(x, b)


def modified_power_law(x,a,b,c):
    return a*np.power(x, b) + c*np.power(x, 2)


def exponential(x,a,b,c):
    return a*np.exp(b*x) + c


def double_exponential(x,a,b,c,d,e):
    return a*np.exp(b*x) + c*np.exp(d*x) + e


def linear(x,a,b):
	return a * x + b


def poly2(x,a,b,c):
	return a * x + b * x**2 + c

def poly3(x,a,b,c,d):
	return a * x + b * x**2 + c * x**3 + d

def poly4(x,a,b,c,d,e):
	return a * x + b * x**2 + c * x**3 + d * x**4 + e

def logarithm(x,a,b):
    return a*np.log(x) + b


def plateau(x,a,b):
    return (a*x)/(b + x)


def logistic(x,a):
    1/(1 + np.exp(a*x))


def logistic2(x,a,b,c):
    b/(c + np.exp(a*x))
    
