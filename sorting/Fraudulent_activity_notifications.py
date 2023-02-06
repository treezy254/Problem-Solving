''' HackerLand National Bank has a simple policy for warning clients about possible fraudulent
 account activity. If the amount spent by a client on a particular day is greater than or equal
  to  the client's median spending for a trailing number of days, they send the client a 
   about potential fraud. The bank doesn't send the client any notifications until they have at
    least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days,
 determine the number of times the client will receive a notification over all  days.'''


from bisect import bisect_left, insort

def activityNotifications(e, d):

	count = 0
	r = [e[i] for i in range(d)]

	r.sort()
	f = e[0]
	med = d//2
	even = 0 if d%2 else 1
	for i in range(len(e) -d):
		m = (r[med] + r[med-even])/2
		g = bisect_left(r, f)
		f = e[i+1]
		r.pop(g)
		insort(r, e[i+d])
		if e[i+d] >= m*2:
			count += 1

	return count