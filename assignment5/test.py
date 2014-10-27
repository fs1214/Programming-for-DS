from interval import *
if False:
	#test for question 1
	#print 'abc'
	i = Interval("(1,4]")
	try:
		assert(i.linclusive and i.rinclusive and i.lower == 1 and i.upper == 4)
	except AssertionError as a:
		print(a)
		
	print i
	for bogus in ["abcd", "{1,1}", "]1,5]", "[2,1]"]:
		try:
			i = Interval(bogus)
		except Exception as e:
			print(e)

if False:
	# Tests for Question 2
    workingtests = [(Interval("[1,4]"), Interval("[3,8]")), \
             (Interval("(1,4)"), Interval("[5,8]")), \
             (Interval("[1,9]"), Interval("[3,8]"))]
    failingtests = [
             (Interval("[1,4)"), Interval("[5,8]")), \
             (Interval("[-100,-3]"), Interval("[5,228]"))]

    for (x,y) in workingtests + failingtests:
        try:
            print("merge {} and {} gives {}".format(x,y,merge_intervals(x,y)))
        except NoOverLapException as e:
            print(e) # print exception message



if False:
	slist = ["[1,5]","[2,10]","[12,13]","[15,19]"]
	ilist = [Interval(s) for s in slist]
	print merge_overlapping(ilist)
	
if True:
	ilist = [Interval('[1,2]')]
	newint = Interval('[3,4]')
	res = insert(ilist,newint)
	print res
	slist = ["[1,5]", "[2,7)", "(8,10]", "[8,18]"]
	ilist = sorted([Interval(s) for s in slist], compare_intervals)
	newint = Interval("[6,9)")
	res = insert(ilist, newint)
	print("insert({},{}) gives {}".format(ilist,newint, res))
	slist = ["[1,3]", "[6,9]"]
	ilist = sorted([Interval(s) for s in slist], compare_intervals)
	newint = Interval("[2,5]")
	res = insert(ilist, newint)
	print("insert({},{}) gives {}".format(ilist,newint, res))
	slist = ["[1,2]", "(3,5)", "[6,7)", "(8,10]", "[12,16]"]
	ilist = sorted([Interval(s) for s in slist], compare_intervals)
	newint = Interval("[4,9]")
	res = insert(ilist, newint)
	print("insert({},{}) gives {}".format(ilist,newint, res))

