# task: process the trace and obtain a time series of packet counts per second

# terminal command:
# sudo tcpdump -q -r lab1.tr > lab3.txt
# data format:
# time src > dst: <protocol> <pkt length>

from datetime import datetime
import matplotlib.pyplot as plt

f = open('./lab3.txt', 'r')

pkts_in_sec = []
first = True
for aline in f:
    time = datetime.strptime(aline.split()[0], '%H:%M:%S.%f')
    second = time.second
    if first:
        cnt = 1
        first = False
        curr_sec = second
    elif second == curr_sec:
        cnt += 1
    else:
        pkts_in_sec.append(cnt)
        cnt = 0
        curr_sec = second
pkts_in_sec.append(cnt)
f.close()

seconds = [i+1 for i in range(len(pkts_in_sec))]

plt.plot(seconds, pkts_in_sec)
plt.title('Packet Counts per Second')
plt.xlabel('time (seconds)')
plt.ylabel('packet count')
plt.show()
