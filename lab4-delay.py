# task: find pairs of data-ack packets and calculate the end-to-end delay

# terminal command:
# sudo tcpdump -r lab1.tr src or dst homepage.ntu.edu.tw and tcp > lab4_full.txt
# data format:
# time IP src > dst: Flags [<tcpflags>], seq <data-seqno>, ack <ackno>, win <window>, options [<opts>], length <len>

from datetime import datetime, timedelta
import matplotlib.pyplot as plt

f = open('./lab4_full.txt', 'r')

# the first few packets are for handshaking
for i in range(4):
    f.readline()

# how to distinguish data packets and ack packets?
# data packets have 'seq' while ack packets don't

# check the src and dst
# ignore the ack data pair when there is retransmission
data_dict = dict()
x_time = []
y_delay = []
for aline in f:
    seg_1 = aline.split(',')[0].split()
    time = datetime.strptime(seg_1[0], '%H:%M:%S.%f') 
    seg_2 = aline.split(',')[1].strip()

    # data packet
    if seg_2.find('seq') != -1:
        seqno = seg_2.split()[1]
        if seqno.find(':') != -1:
            seqno = int(seqno.split(':')[1])
        else:
            seqno = int(seqno)
        data_dict[seqno] = time

    # ack packet
    else:
        ackno = int(seg_2.strip().split()[1])
        if ackno in data_dict:
            delay = (time - data_dict[ackno]) / timedelta(seconds=1)
            x_time.append(data_dict[ackno])
            y_delay.append(delay)

f.close()

plt.plot(x_time, y_delay)
plt.title('End-to-End Delay')
plt.xlabel('time')
plt.ylabel('delay (seconds)')
plt.show()
