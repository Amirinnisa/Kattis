import sys

input = sys.stdin.read()
vals = input.split(" ")

Hour = int(vals[0])
Minute = int(vals[1])

if 0<=Hour<=23 and 0<=Minute<=53 :
	m = Hour*60+Minute
	mNew = m-45
	
	HourNew = int(round(mNew/60))
	MinuteNew = mNew%60
	
	if HourNew == -1 :
		HourNew = 23

print '%d %d' % (HourNew, MinuteNew)
