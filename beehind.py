import sys

input = sys.stdin.read()
line = input.split("\n")

for i in range(len(line)) :
	row = line[i].split(' ')
	sweet = int(row[0])
	sour = int(row[1])
	super = sweet+sour

	if sweet >= 0 and sour <= 1000:
		if sweet == 0 and sour == 0 :
			break	
		else :
			if super != 13 :
				if sour > sweet :
					print "Left beehind."
				elif sour < sweet :
					print "To the convention."
				else :
					print "Undecided."
			else :
				print "Never speak again."