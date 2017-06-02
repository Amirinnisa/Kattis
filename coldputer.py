import sys

input = sys.stdin.read()
vals = input.split('\n')
vals2 = vals[1].split(' ')

n = int(vals[0])

if 1 <= n <= 100 :
	belowZero = []
	for m in range(n) :
		temp = int(vals2[m])
		if -1000000 <= temp <= 1000000 and temp < 0 :
			belowZero.append(temp)
	print len(belowZero)