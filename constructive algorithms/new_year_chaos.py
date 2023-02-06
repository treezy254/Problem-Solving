''' It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.'''

def minimumBribes(q):
    t = len(q)
    position_1 = 1
    position_2 = 2
    position_3 = 3
    totalBridges = 0
    for i in range(t):
        if q[i] == position_1:
            position_1 = position_2
            position_2 = position_3
            position_3 += 1
        elif q[i] == position_2:
            totalBridges += 1
            position_2 = position_3
            position_3 += 1
        elif q[i] == position_3:
            totalBridges += 2
            position_3 += 1
        else:
            print('Too chaotic')
            return 

    print(totalBridges)