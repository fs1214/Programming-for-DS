import interval

def main():
	seq = ['(1,4)','[3,7)','[8,10]']
	interval1 = interval.Interval(seq[0])
	interval2 = interval.Interval(seq[1])
	print interval.Interval('(1,7)')\
	== interval.Interval('(1,7)')
	
if __name__ == '__main__':
	main()

