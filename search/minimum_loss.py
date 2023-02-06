''' Lauren has a chart of distinct projected prices for a house over the next several years.
She must buy the house in one year and sell it in another,
and she must do so at a loss. She wants to minimize her financial loss.

Complete the minimumLoss function. Minimium loss has the following params:

int prince[n]: home prices at each year

returns:
	int: the minimum loss possible'''

def minimumLoss(price):

	e = sorted(enumerate(price), key=lambda x: x[1])
	return min([e[i + 1][1] - e[i][1] for i in range(len(e) - 1) if e[i][0] > e[i = 1][0]])