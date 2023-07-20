'''
identify the problem domain : search
identify the problem subdomain : greedy search
come up with a soludtion for it
'''
def minimumPasses(m, w, p, n):
	# m - machines
	# w - workers
	# p - purchase price of new machine or worker
	# n - target

	passes = 0
	current = 0
	while current < n:

		# calculate current production
		produced = m * w 

		# calculate steps until next decision is possible (enough to buy machines/workers) or finished
		steps = max(math.floor((min(p, n) - current) / produced), 1)

		# jump to the calculated decision point
		passes += steps 
		current += steps * produced

		# calculate if saving or buying is better (compare saving from now or saving from next round to save calculation time)
		wait = math.ceil((n - current) / produced)
		not_wait = calcNext(m, w, p, current)

		print(current, m, w)

		# if buying is faster bu and go to the next iteration, else calculate result and finish preemptively
		if not_wait <= wait:
			m, w, p, current = buyOnce(m, w, p, current)
		else: 
			return passes + wait

	return passes

def buyOnce(m, w, p, current):
	# buy new stuff. always greedy and try to keep m and w as close to each other as possible
	buy = current // p
	difference = m - w
	if difference < 0:
		m += min(buy, abs(difference))
	else:
		w += min(buy, abs(difference))
	buy -= min(buy, abs(difference))
	lower = buy // 2 
	higher = buy - lower
	if m < w:
		w += lower
		m += higher
	else:
		w += higher
		m += lower
	current = current % p 
	return m, w, p, current

def calcNext(m, w, p, current):
	# calculate how long waiting from next would take
	m, w, p, current = buyOnce(m, w, p, current)
	return (math.ceil((n - current) / (m * w)))
