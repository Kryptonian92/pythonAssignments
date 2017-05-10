import random
def CoinToss():
    head = 0
    tail = 0
    for count in range(1,5001):
        toss = random.randint(0,1)
        if toss == 1:
            head += 1
            print "Attempt #", count, "It's a head! ... Got", head, " heads and", tail, "tails so far."
        elif toss == 0:
            tail += 1
            print "Attempt #", count, "It's a tail! ... Got", head, " heads and", tail, "tails so far."
CoinToss()
