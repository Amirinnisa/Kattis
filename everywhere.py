import sys

input = sys.stdin.read()
line = input.split("\n")

TestCase = int(line[0]) #Total travels
if TestCase <= 50:
	for T in range(1, len(line)) :
		if line[T].isdigit():
			Trips = int(line[T])
			Cities = []	#Total different cities in each trip
			for b in range(T+1, T+Trips+1):
				if len(line[b]) <= 20 and not line[b] in Cities:
					Cities.append(line[b])
			print len(Cities)