import sys
if __name__ == '__main__':
		city = []
		listk = []
		input = sys.stdin.read(5000)
		inx = [a for a in input.split("\n")]
		trip = inx[0]	
		inx.pop(0)
		m = 0
		for a in inx:
				listc = []
				if a.isdigit():
						listk = inx[m+1:m+int(a)+1]
						for b in listk:
								if not b in listc:
										listc.append(b)
						print len(listc)
				m += 1