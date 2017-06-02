import sys

input = sys.stdin.read()
vals = input.split(" ")

orang = int(vals[0])
ayam = int(vals[1])
sisa = ayam - orang
kurang = orang - ayam

if orang > ayam and kurang == 1 :	
	print "Dr. Chaz needs",kurang,"more piece of chicken!"
elif orang > ayam and kurang > 1 :
	print "Dr. Chaz needs",kurang,"more pieces of chicken!"
elif orang < ayam and sisa == 1 :
	print "Dr. Chaz will have",sisa,"piece of chicken left over!"
else :
	print "Dr. Chaz will have",sisa,"pieces of chicken left over!"

	
