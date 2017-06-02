import sys
import math   # This will import math module

input = sys.stdin.read()
line = input.split(' ')

H = int(line[0])
path = line[1].split(' ')
TotalNode = 0
paths = str(path[0])
print paths

if 1 <= H <= 30 :
	for i in range(H+1):
		if path == '':
			TotalNode = TotalNode + int(math.pow(2,i))
	print TotalNode