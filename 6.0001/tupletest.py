


def get_data(aTuple):
	nums = ()
	words = ()
	for t in aTuple:
		nums = nums+(t[0],)
		if t[1] not in words:
			words = words+(t[1],)
	min_n = min(nums)
	max_n = max(nums)
	unique_words = len(words)
	return (min_n,max_n, unique_words)
		
testtuple = ((1,"doug"),(2,"kim"),(3,"doug"))
(a,b,c) = get_data(testtuple)
print("min num="+str(a)+" max num="+str(b)+" num unique words="+str(c))
print(testtuple[0][1])

 
