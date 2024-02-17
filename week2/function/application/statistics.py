import math

def ptp(data):
    """求級差(全距)"""
    return max(data) -min(data)

def average(data):
    """求平均"""
    return sum(data)/len(data)

def variance(data):
    """求方差"""
    x_bar=average(data)
    temp=[(num-x_bar)**2 for num in data]
    return sum(temp)/(len(temp)-1)

def standard_deviation(data):
    """求標準差"""