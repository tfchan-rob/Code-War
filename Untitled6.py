#!/usr/bin/env python
# coding: utf-8

# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
# 
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
# 
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# 
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# In[ ]:


def zero(a=None): return int(0) if not a else a(0)
def one(a=None): return int(1)if not a else a(1)
def two(a=None): return int(2)if not a else a(2)
def three(a=None): return int(3)if not a else a(3)
def four(a=None): return int(4)if not a else a(4)
def five(a=None): return int(5)if not a else a(5)
def six(a=None): return int(6)if not a else a(6)
def seven(a=None): return int(7)if not a else a(7)
def eight(a=None): return int(8)if not a else a(8)
def nine(a=None): return int(9)if not a else a(9)

def plus(y): return lambda x:x+y
def minus(y): return lambda x:x-y
def times(y): return lambda x:x*y
def divided_by(y): return lambda x:x//y

