def euler(G):#O(V+E)
	n=len(G)
	edge_count=[len(G[i]) for i in range(n)]

	if n==0:
		return []

	curr_path=[]
	circuit=[]

	curr_path.append(0)
	curr_v=0

	while len(curr_path):
		if edge_count[curr_v]:
			next_v=G[curr_v][-1]

			curr_path.append(curr_v)
			edge_count[curr_v]-=1
			G[curr_v].pop()
			curr_v = next_v

		else:
			circuit.append(curr_v)
			curr_v=curr_path[-1]
			curr_path.pop()


	circuit.reverse()
	return circuit

"""
do dopisania w domu w notatki: 
zadanie 4a
słowniki
"""