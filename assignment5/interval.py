class NotAnIntervalExceptions(Exception):
	#print "NotAnInterval"
	pass
class IllegalIntervalException(Exception):
	#print "IllegalInterval"
	pass
class NoOverLapException(Exception):
	pass

class Interval:
	def __init__(self, s):
		lbrack, middle, rbrack = s[0], s[1:-1], s[-1]
		try:
			lower,upper = middle.split(',')
			assert(lbrack in ["[", "("])
			assert(rbrack in ["]", ")"])
			self.lower = int(lower)
			self.upper = int(upper)
		except:
			raise NotAnIntervalExceptions(s + "  not an interval!")
		self.linclusive = (lbrack == "[")
		self.rinclusive = (rbrack == "]")		
	
		if self.real_lower() > self.real_upper():
			raise IllegalIntervalException(s + "  illegal interval!")
			
	def real_upper(self):
		return self.upper if self.rinclusive else self.upper - 1
	def real_lower(self):
		return self.lower if self.linclusive else self.lower + 1
	def __repr__(self):
		return self.linclusive*'[' + (not self.linclusive)*'('+\
		str(self.lower)+','+str(self.upper)+self.rinclusive*']'+\
		 (not self.rinclusive)*')'
	
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	
def merge_intervals(x,y):
	if x.real_upper() < y.real_lower()-1 or x.real_lower() > y.real_upper()+1:
		raise NoOverLapException(str(x) + str(y) + " do not overlap!")
	result = Interval("[0,1]")
	if x.real_lower() < y.real_lower():
		result.lower = x.lower
		result.linclusive = x.linclusive
	else:
		result.lower = y.lower
		result.linclusive = y.linclusive
	
	if x.real_upper() > y.real_upper():
		result.upper = x.upper
		result.rinclusive = x.rinclusive
	else:
		result.upper = y.upper
		result.rinclusive = y.rinclusive
	return result

def merge_overlapping(intervallist):
	intervallist.sort(key = lambda x:x.real_lower)
	result = []
	temp = intervallist[0]
	for i in range(len(intervallist)-1):
		try:
			temp = merge_intervals(temp, intervallist[i+1])
		except:
			#print "break"
			result.append(temp)
			temp = intervallist[i+1]
	result.append(temp)
	return result


def compare_intervals(x, y):
	return x.real_lower() - y.real_lower()


def insert(ilist, newint):
	newlist = ilist[:]
	for interval in newlist:
		if newint.lower <= interval.lower:
			newlist.insert(newlist.index(interval), newint)
			break
	if len(newlist) == len(ilist):
		newlist.append(newint)
	return newlist

