import numpy as np

#prices = [float(x) for x in open("data5500_spring2023/week6_queues_stacks/zoomsession2/KSS.txt").readlines()]
fil = open("data5500_spring2023/week6_queues_stacks/zoomsession2/KSS.txt")

prices = []


prices.append(float(fil.readline())) for i in range(6)
    # line = fil.readline()
    # prices.append(float(line))


days= 5
buy = 0
profit = 0.0
while line:
# for i in range(len(prices)):
    p = prices[-1]
    avg = np.mean(prices[0:days])
    
    if p < avg * 0.87 and buy == 0: #buy
        buy = p
    elif p > avg * 1.13 and buy != 0: #sell
        profit += p - buy
        buy = 0
    else:
        pass # do nothing today, except hopefully my position is becoming more profitable
    # append a new price
    # pop off the first price, prices[0]

print("profit: ", profit)
print("returns%: ", 100 * (profit/prices[0]))

