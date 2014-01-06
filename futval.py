__author__ = 'Mace'

from graphics import *

#introduction
print("This program plots the growth of a ten year investment.")

#investment information
principal = eval(input("Enter the principal interest: "))
rate = eval(input("Enter the interest rate: "))

#window setup
win = GraphWin('Investment Growth Chart', 370, 300)
win.setBackground("white")

#y-axis label
Text(Point(8, 100), 'a').draw(win)
Text(Point(8, 115), 'm').draw(win)
Text(Point(8, 130), 'o').draw(win)
Text(Point(8, 145), 'u').draw(win)
Text(Point(8, 160), 'n').draw(win)
Text(Point(8, 175), 't').draw(win)

#x-axis label
Text(Point(185, 260), 'years').draw(win)

#y-axis values
Text(Point(40, 230), '0.0K').draw(win)
Text(Point(40, 180), '2.5K').draw(win)
Text(Point(40, 130), '5.0K').draw(win)
Text(Point(40, 80), '7.5K').draw(win)
Text(Point(40, 30), '10.0K').draw(win)

#x-axis values
Text(Point(70, 240), '0').draw(win)
Text(Point(95, 240), '1').draw(win)
Text(Point(120, 240), '2').draw(win)
Text(Point(145, 240), '3').draw(win)
Text(Point(170, 240), '4').draw(win)
Text(Point(195, 240), '5').draw(win)
Text(Point(220, 240), '6').draw(win)
Text(Point(245, 240), '7').draw(win)
Text(Point(270, 240), '8').draw(win)
Text(Point(295, 240), '9').draw(win)
Text(Point(320, 240), '10').draw(win)

#first bar setup
height = principal * 0.02
bar = Rectangle(Point(60, 230), Point(85, 230 - height))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

#bars 1-10 setup
for year in range(1, 11):
    principal *= (1 + rate)
    xll = year * 25 + 60
    height = principal * 0.02
    bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

#allows the window to stay on screen until user hits enter
wait = input("Enter: ")

#closes window
win.close()