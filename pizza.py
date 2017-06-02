import sys

input = sys.stdin.read()
vals = input.split(" ")

radius = float(vals[0])
crust = float(vals[1])

AreaPizza = radius*radius*22/7
AreaCheese = (radius-crust)*(radius-crust)*22/7

cheese = 100*AreaCheese/AreaPizza
print cheese
	
