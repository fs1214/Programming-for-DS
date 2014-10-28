import unittest 
import interval

class TestIntervalFunctions(unittest.TestCase):
	def setUp(self):
		self.seq = ['(1,4)','[3,7)','[8,10]']

	def test_merge_interval(self):
		interval1 = interval.Interval(self.seq[0])
		interval2 = interval.Interval(self.seq[1])
		self.assertEqual(interval.merge_intervals(interval1, interval2),\
		interval.Interval('(1,7)'))
		
	def test_merge_overlappings(self):
		self.intseq = [interval.Interval(s) for s in self.seq]
		self.assertEqual(interval.merge_overlapping(self.intseq),[interval.\
		Interval(s) for s in ['(1,7)','[8,10]']])
		
	def test_insert(self):
		

if __name__ == '__main__':
	unittest.main()

