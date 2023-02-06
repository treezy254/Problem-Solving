'''Hackerland is a one-dimensional city with houses aligned at integral locations
 along a road. The Mayor wants to install radio transmitters on the roofs of the
  city's houses. Each transmitter has a fixed range meaning it can transmit a signal
   to all houses within that number of units distance away.

Given a map of Hackerland and the transmission range, determine the minimum number of
 transmitters so that every house is within range of at least one transmitter. Each
  transmitter must be installed on top of an existing house.'''

def hackerlandRadioTransmitters(x, k):
	x.sort()

	transmitters = 0
	idx = len(x) -1

	while idx >= 0:

		for _ in range(2):
			remaining = k

			while reamining >= 0 and idx >= 1:
				cur, nxt = x[idx], x[idx - 1]
				diff = cur - nxt
				remaining -= diff

				if remaining >= 0:
					idx -= 1

		transmitters += 1
		idx -= 1

	return transmitters