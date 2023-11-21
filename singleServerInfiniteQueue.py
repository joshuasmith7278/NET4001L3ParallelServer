from matplotlib import pyplot as plt
import numpy as np


def getIntArrivalTime(lam, s):
    np.random.seed(5)
    interArrival = np.random.exponential(scale=lam, size=s-1)
    return interArrival


def getServiceTime(new, s):
    np.random.seed(13)
    serviceTime = np.random.exponential(scale=new, size=s)
    return serviceTime


def getArrivalTime(intArr):
    cumsum = 0
    arrTime = []
    arrTime.append(0)
    for i in intArr:
        cumsum += i
        arrTime.append(cumsum)
    return arrTime



def getServerStats(lam, mew):
    bigL = lam/mew
    bigW = bigL/lam
    print("The Average Number of Packets in the System (L) is lambda/mew since K is infinite:" + str(bigL))
    print("The Average Delay using Little THeorem : " + str(bigW))
  





print("M/M/2 System ")
lam = 1
mew = 8
print("Lambda = 1packet / s, Inter-arrival time = 1s")
print("Mew = 8 packet /s since Two Server (4 each)")
server1_available_time = 0
server2_available_time = 0
clock_time = 0
interarrival_times = getIntArrivalTime(lam, 100000)
arrival_times = getArrivalTime(interarrival_times)
service_times = getServiceTime(mew, 100000)
departure_times = []

for i in range(99999):
    clock_time = clock_time + interarrival_times[i]
    ##Both Servers are BUSY, choose the one available next
    if arrival_times[i] <= server1_available_time and arrival_times[i] <= server2_available_time:
        if server1_available_time <= server2_available_time:
            departure_times.append(clock_time + service_times[i])
            server_to_use = 1
        else:
            departure_times.append(clock_time + service_times[i])

            server_to_use = 2


    ##Server 2 is FREE
    elif arrival_times[i] <= server1_available_time:
        departure_times.append(clock_time + service_times[i])
        server_to_use = 1

    ##Server 1 is FREE
    elif arrival_times[i] <= server2_available_time:
        departure_times.append(clock_time + service_times[i])

        server_to_use = 2

    ##Both Servers are FREE, choose server 1
    else:
        departure_times.append(clock_time + service_times[i])

        server_to_use = 1 



print(len(departure_times))





