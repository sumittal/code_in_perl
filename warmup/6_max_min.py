import operator
N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
def get_unfairness(N,K,n):
	r={}
	K=K-1
	for x in range(0,N-1):
        	if x+K < N:
	        	r[x]=n[x+K]-n[x]

	sorted_x = sorted(r.items(), key=operator.itemgetter(1))
	return sorted_x[0][1]

min_diff = get_unfairness(N,K,lists)

print min_diff
