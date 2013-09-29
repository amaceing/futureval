__author__ = 'Mace'
import graphics
from graphics import *
princ = eval(input("Enter initial principal: "))
rate = eval(input("Enter the interest rate (%): ")) / 100
timeSpan = eval(input("Enter the amount of years investing: "))
for i in range(timeSpan):
    princ = princ * (1 + rate)
    print(princ)