# [nslab] Spring-2022 Special Topics

This is my first semester of Special Project in NTU Network and Systems Lab aiming to exploring Twitch's CDN. I spent the first half semester reading background papers, and spent the second half learning to use tcpdump and access databases.

## 1. Schedule

| Date         | Assignment                                                                                                                                                         |
| ------------ |:------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Winter Break | Readings: (past projects) <br> 1. Towards Cost Effective Server Population Estimation: A Case Study of Twitch <br> 2. Twitch's CDN as an Open Population Ecosystem |
| 3/1          | Readings: (background papers) <br> 1. Internet Scale User-Generated Live Video Streaming: The Twitch Case                                                          |
| 3/8          | 2. Vantage: Optimizing Video Upload for Time-shifted Viewing of Social Live Streams <br> 3. Zooming in on Wide-area Latencies to a Global Cloud Provider (BlameIt) |
| 3/15         | Ubuntu installation on mbox-02                                                                                                                                     |
| 3/22         | 4. On the Origin of Scanning: The Impact of Location on Internet-Wide Scans (ZMap)                                                                                 |
| 3/29         | Readings: (Caleb's thesis) <br> Discovering Twitch's Video Delivery Infrastucture Utilizing Cloud Services and VPNs                                                |
| 4/5          | Spring Break                                                                                                                                                       |
| 4/12         | Learn to access 2019, 2021 database                                                                                                                                |
| 4/19         | Complete tcpdump lab 1 & 2                                                                                                                                         |
| 4/26         | Complete tcpdump lab 3 & 4                                                                                                                                         |
| 5/3          | Explore 2019 database (influxDB, Azure)                                                                                                                            |
| 5/10         | Recreate graphs in "Twitch's CDN as an Open Population Ecosystem" using 2019 database                                                                              |
| 5/17         | Explore 2021 database (MongoDB, VPN)                                                                                                                               |
| 5/24         | Summary of the semester


## 2. tcpdump

### 2.1. Instructions
https://homepage.ntu.edu.tw/~pollyhuang/teach/net-simtest-spring-08/labs/tcpdump.html

### 2.2. Lab 1
1. Run the following command in terminal to record trace.
`sudo tcpdump -w lab1.tr -Z root`
2. Follow the instructions to upload lab1.tr to homepage.ntu.edu.tw via FTP.
3. Use `ctrl+c` to end the capture.

### 2.3. Lab 2
1. Run the following command in terminal to process the trace and write it to a txt file.
`sudo tcpdump -q -t -N -r lab1.tr > lab2.txt`
2. Each row of the processed data we get in step 1. will be in the format of 
`src > dst: <protocol> <packet length>`.
3. Run the python code `lab2-traffic-volume.py` to count number of (1) TCP, (2) UDP, (3)other packets.
4. Output:
`total: 107002, TCP: 53487, UDP: 53512, other: 3`

### 2.4. Lab 3
1. Run the following command in terminal.
`sudo tcpdump -q -r lab1.tr > lab3.txt`
2. Each row will be in the format of
`time src > dst: <protocol> <pkt length>`.
3. Run the python code `lab3-traffic-burstiness.py` to plot the packets count per second.
4. The result is as follows.
<img src="https://i.imgur.com/2X1XdBL.png" width="40%">

### 2.5. Lab 4
1. Run the following command in terminal.
`sudo tcpdump -r lab1.tr src or dst homepage.ntu.edu.tw and tcp > lab4.txt`
2. Each row will be in the format of 
`time IP src > dst: Flags [<tcpflags>], seq <data-seqno>, ack <ackno>, win <window>, options [<opts>], length <len>`
3. Run the python code `lab4-delay.py` to plot the end-to-end delay of packets.
4. The result is as follows.
<img src="https://i.imgur.com/DprVDb3.png" width="40%">


## 3. Access Databases

### 3.1. 2019 InfluxDB

#### 3.1.1. Access
```python
from influxdb import InfluxDBClient
client = InfluxDBClient(host='140.112.42.161', port=23234, database='test_2')
```

#### 3.1.2. Summary
1. Columns in the database:
 - time: client request time (string)
 - client_ip: (string)
 - client_location: (string)
 - fq_count: (int)
 - ip_list: (list or string)
 - num_edge: (float)
 - stream_language: (string)
 - viewer: viewer count (float)

2. Options in column 'client_location':
`'north-eu', 'southeast-asia', 'tw', 'west-eu', 'west-us', 'ko', 'central-au'`
3. Options in column 'stream_language':
`'ko', 'es', 'ja', 'fr', 'ru', 'zh-tw', 'en', 'en-gb', 'es-mx'`

### 3.2. 2021 MongoDB

#### 3.2.1 Access
```python
from pymongo import MongoClient
client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')
```

#### 3.2.2 Summary
[Summary Excel file](https://docs.google.com/spreadsheets/d/1_yi8a4zauQSFX8l6Vt5lr3SO0fcoJTNL/edit?usp=sharing&ouid=112952391443444590602&rtpof=true&sd=true)
