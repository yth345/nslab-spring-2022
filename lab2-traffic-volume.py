# task: count the number of packets that are TCP, UDP, and other

# terminal command:
# tcpdump -q -t -N -r lab1.tr > lab1_all.txt
# data format:
# src > dst: <protocol> <packet length>

tcp_cnt = 0
udp_cnt = 0
other_cnt = 0

f = open('./lab1_all.txt', 'r')

# each row is a packet
for aline in f:
    second_half = aline.split(':')[1]
    if 'tcp' in second_half:
        tcp_cnt += 1
    elif 'UDP' in second_half:
        udp_cnt += 1
    else:
        other_cnt += 1
f.close()

ttl_cnt = tcp_cnt + udp_cnt + other_cnt

print(f'total: {ttl_cnt}, TCP: {tcp_cnt}, UDP: {udp_cnt}, other: {other_cnt}')


