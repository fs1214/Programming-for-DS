from interval import *
def main():
	s = raw_input('List of intervals ')
	parts = s.split(', ')
	intervals = [Interval(i) for i in parts]
	while True:
		s = raw_input('Interval? ')
		if s == 'quit':
			break
		try:
			intervals = insert(intervals, Interval(s))
			print intervals
		except:
			print 'Invalid interval'
	return 0

if __name__ == '__main__':
	main()

