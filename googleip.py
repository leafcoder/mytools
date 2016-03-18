#!/usr/bin/python
import sys
import socket
from cStringIO import StringIO

input_ips = '''
216.58.214.244	0%	264.8	*.google.com
108.177.9.113	0%	265.4	*.google.com
108.177.9.139	0%	276.6	*.google.com
216.58.214.51	0%	291	*.google.com
216.58.212.24	0%	295.4	*.google.com
216.58.214.181	0%	299.4	*.google.com
216.58.212.23	0%	299.8	*.google.com
216.58.214.115	0%	316.4	*.google.com
108.177.15.138	0%	325.8	*.google.com
216.58.214.14	0%	329.4	*.google.com
216.58.214.192	0%	329.6	*.google.com
108.177.15.113	0%	331	*.google.com
108.177.10.114	0%	343	*.google.com
216.58.222.148	0%	363.6	*.google.com
216.58.222.90	0%	369.6	*.google.com
108.177.10.31	0%	370.6	*.google.com
216.58.214.24	0%	385.6	*.google.com
108.177.15.100	0%	393.8	*.google.com
216.58.214.57	0%	394.2	*.google.com
108.177.9.91	0%	406.4	*.google.com
216.58.222.123	0%	418.4	*.google.com
216.58.222.185	0%	422.4	*.google.com
216.58.222.87	0%	441.2	*.google.com
216.58.214.32	0%	452.6	*.google.com
216.58.222.122	0%	465	*.google.com
216.58.214.142	0%	466.2	*.google.com
216.58.222.91	0%	469.4	*.google.com
64.233.189.100	20%	58.075	*.google.com
64.233.189.188	20%	62.35	*.google.com
216.58.214.146	20%	324.75	*.google.com
216.58.214.214	20%	341.25	*.google.com
216.58.214.60	20%	352.5	*.google.com
108.177.10.190	20%	365.25	*.google.com
216.58.222.160	20%	372.75	*.google.com
216.58.214.191	20%	377.5	*.google.com
216.58.222.155	20%	435.5	*.google.com
216.58.222.151	20%	480.25	*.google.com
216.58.214.116	33%	347.5	*.google.com
64.233.188.188	40%	59.8	*.google.com
216.58.198.153	40%	331.667	*.google.com
216.58.222.174	40%	452.667	*.google.com
216.58.214.110	40%	457	*.google.com
216.58.214.153	40%	478	*.google.com
216.239.38.121	60%	34.25	*.google.com
216.58.203.78	60%	112	*.google.com
216.58.193.96	60%	165.5	*.google.com
216.58.193.88	60%	170	*.google.com
216.58.199.92	60%	176	*.google.com
216.58.193.123	60%	194	*.google.com
216.58.193.20	60%	222.5	*.google.com
216.58.195.54	60%	226	*.google.com
216.58.195.60	60%	235	*.google.com
216.58.195.55	60%	237.5	*.google.com
216.58.193.21	60%	248.5	*.google.com
216.58.198.218	60%	297	*.google.com
216.58.198.148	60%	299.5	*.google.com
216.58.202.96	60%	325	*.google.com
216.58.202.121	60%	326	*.google.com
216.58.201.248	60%	332	*.google.com
216.58.201.253	60%	350	*.google.com
216.58.198.122	60%	368.5	*.google.com
216.58.201.250	60%	370.5	*.google.com
216.58.198.118	60%	383	*.google.com
216.58.201.155	60%	407.5	*.google.com
216.58.201.191	60%	431	*.google.com
216.58.195.157	60%	451	*.google.com
216.58.201.174	60%	476.5	*.google.com
216.58.214.121	60%	482.5	*.google.com
216.58.195.53	66%	229	*.google.com
216.58.195.148	66%	230	*.google.com
216.58.201.251	66%	378.5	*.google.com
216.58.197.243	80%	56.2	*.google.com
216.58.203.93	80%	65.2	*.google.com
216.58.203.121	80%	65.5	*.google.com
216.58.199.219	80%	67.1	*.google.com
216.58.203.90	80%	67.5	*.google.com
216.58.203.110	80%	68.2	*.google.com
216.58.203.88	80%	68.4	*.google.com
216.58.203.64	80%	69.2	*.google.com
216.58.203.83	80%	70	*.google.com
216.58.203.115	80%	93.2	*.google.com
216.58.203.118	80%	111	*.google.com
216.58.203.96	80%	112	*.google.com
216.58.203.94	80%	113	*.google.com
216.58.203.126	80%	114	*.google.com
216.58.203.84	80%	115	*.google.com
216.58.203.123	80%	117	*.google.com
216.58.203.82	80%	118	*.google.com
216.58.203.116	80%	121	*.google.com
216.58.199.182	80%	125	*.google.com
216.58.203.114	80%	131	*.google.com
216.58.199.190	80%	140	*.google.com
216.58.193.116	80%	160	*.google.com
216.58.193.64	80%	164	*.google.com
216.58.199.78	80%	176	*.google.com
216.58.199.94	80%	177	*.google.com
216.58.195.56	80%	197	*.google.com
216.58.193.117	80%	198	*.google.com
216.58.195.62	80%	203	*.google.com
216.58.193.55	80%	204	*.google.com
216.58.195.51	80%	224	*.google.com
216.58.193.0	80%	226	*.google.com
216.58.195.50	80%	228	*.google.com
216.58.202.87	80%	230	*.google.com
216.58.193.24	80%	234	*.google.com
216.58.202.116	80%	243	*.google.com
216.58.195.61	80%	251	*.google.com
216.58.195.158	80%	257	*.google.com
216.58.202.86	80%	257	*.google.com
216.58.195.147	80%	258	*.google.com
216.58.195.59	80%	265	*.google.com
216.58.195.142	80%	268	*.google.com
216.58.195.52	80%	276	*.google.com
216.58.195.58	80%	276	*.google.com
216.58.198.220	80%	294	*.google.com
216.58.201.245	80%	297	*.google.com
216.58.202.85	80%	303	*.google.com
216.58.198.146	80%	312	*.google.com
216.58.201.147	80%	318	*.google.com
216.58.201.224	80%	337	*.google.com
216.58.201.252	80%	350	*.google.com
216.58.202.126	80%	351	*.google.com
216.58.202.119	80%	352	*.google.com
216.58.198.158	80%	353	*.google.com
216.58.202.115	80%	359	*.google.com
216.58.202.123	80%	368	*.google.com
216.58.201.214	80%	370	*.google.com
216.58.201.238	80%	376	*.google.com
216.58.201.211	80%	382	*.google.com
216.58.201.151	80%	383	*.google.com
216.58.201.158	80%	383	*.google.com
216.58.201.186	80%	388	*.google.com
216.58.201.243	80%	388	*.google.com
216.58.201.149	80%	393	*.google.com
216.58.201.179	80%	393	*.google.com
216.58.201.206	80%	397	*.google.com
216.58.201.254	80%	400	*.google.com
216.58.201.188	80%	401	*.google.com
216.58.201.210	80%	402	*.google.com
108.177.15.190	80%	407	*.google.com
216.58.201.187	80%	408	*.google.com
216.58.201.249	80%	415	*.google.com
216.58.201.128	80%	416	*.google.com
216.58.201.185	80%	416	*.google.com
216.58.201.150	80%	417	*.google.com
216.58.214.128	80%	418	*.google.com
216.58.201.216	80%	429	*.google.com
216.58.201.152	80%	439	*.google.com
216.58.201.218	80%	440	*.google.com
216.58.195.153	80%	449	*.google.com
216.58.201.148	80%	450	*.google.com
216.58.201.189	80%	451	*.google.com
216.58.201.220	80%	474	*.google.com
216.58.214.123	80%	477	*.google.com
216.58.201.219	80%	498	*.google.com
216.58.214.152	80%	518	*.google.com
216.58.195.63	83%	226	*.google.com
216.58.202.83	83%	278	*.google.com
216.58.198.251	83%	320	*.google.com
216.58.198.151	83%	341	*.google.com
216.58.195.155	83%	365	*.google.com
216.58.198.116	83%	387	*.google.com
216.58.201.246	83%	400	*.google.com
216.58.201.180	83%	432	*.google.com
108.177.9.100	100%	NO	*.google.com
216.58.193.87	100%	NO	*.google.com
216.58.193.90	100%	NO	*.google.com
216.58.195.128	100%	NO	*.google.com
216.58.195.146	100%	NO	*.google.com
216.58.195.149	100%	NO	*.google.com
216.58.195.150	100%	NO	*.google.com
216.58.195.151	100%	NO	*.google.com
216.58.195.154	100%	NO	*.google.com
216.58.195.156	100%	NO	*.google.com
216.58.195.32	100%	NO	*.google.com
216.58.195.46	100%	NO	*.google.com
216.58.195.57	100%	NO	*.google.com
216.58.197.160	100%	NO	*.google.com
216.58.197.213	100%	NO	*.google.com
216.58.197.218	100%	NO	*.google.com
216.58.197.251	100%	NO	*.google.com
216.58.198.110	100%	NO	*.google.com
216.58.198.155	100%	NO	*.google.com
216.58.198.211	100%	NO	*.google.com
216.58.198.222	100%	NO	*.google.com
216.58.198.243	100%	NO	*.google.com
216.58.198.245	100%	NO	*.google.com
216.58.199.116	100%	NO	*.google.com
216.58.199.210	100%	NO	*.google.com
216.58.199.222	100%	NO	*.google.com
216.58.199.56	100%	NO	*.google.com
216.58.199.84	100%	NO	*.google.com
216.58.199.96	100%	NO	*.google.com
216.58.201.142	100%	NO	*.google.com
216.58.201.146	100%	NO	*.google.com
216.58.201.153	100%	NO	*.google.com
216.58.201.154	100%	NO	*.google.com
216.58.201.157	100%	NO	*.google.com
216.58.201.160	100%	NO	*.google.com
216.58.201.178	100%	NO	*.google.com
216.58.201.181	100%	NO	*.google.com
216.58.201.182	100%	NO	*.google.com
216.58.201.183	100%	NO	*.google.com
216.58.201.184	100%	NO	*.google.com
216.58.201.190	100%	NO	*.google.com
216.58.201.192	100%	NO	*.google.com
216.58.201.212	100%	NO	*.google.com
216.58.201.213	100%	NO	*.google.com
216.58.201.215	100%	NO	*.google.com
216.58.201.217	100%	NO	*.google.com
216.58.201.221	100%	NO	*.google.com
216.58.201.222	100%	NO	*.google.com
216.58.201.223	100%	NO	*.google.com
216.58.201.242	100%	NO	*.google.com
216.58.201.244	100%	NO	*.google.com
216.58.201.247	100%	NO	*.google.com
216.58.202.110	100%	NO	*.google.com
216.58.202.114	100%	NO	*.google.com
216.58.202.117	100%	NO	*.google.com
216.58.202.118	100%	NO	*.google.com
216.58.202.120	100%	NO	*.google.com
216.58.202.122	100%	NO	*.google.com
216.58.202.124	100%	NO	*.google.com
216.58.202.127	100%	NO	*.google.com
216.58.202.25	100%	NO	*.google.com
216.58.202.82	100%	NO	*.google.com
216.58.202.91	100%	NO	*.google.com
216.58.202.95	100%	NO	*.google.com
216.58.203.117	100%	NO	*.google.com
216.58.203.119	100%	NO	*.google.com
216.58.203.120	100%	NO	*.google.com
216.58.203.122	100%	NO	*.google.com
216.58.203.124	100%	NO	*.google.com
216.58.203.127	100%	NO	*.google.com
216.58.203.85	100%	NO	*.google.com
216.58.203.86	100%	NO	*.google.com
216.58.203.87	100%	NO	*.google.com
216.58.203.89	100%	NO	*.google.com
216.58.203.91	100%	NO	*.google.com
216.58.203.92	100%	NO	*.google.com
216.58.203.95	100%	NO	*.google.com
'''

def connect(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect(addr)
    finally:
        sock.close()

def find_ip():
    m = StringIO(input_ips)
    for s in m.readlines():
        s = s.strip()
        if not s:
            continue
        host = s.split(None)[0]
        try:
            connect((host, 5222))
            print 'host: %s closed' % host
            continue
        except socket.error:
            pass
        try:
            connect((host, 443))
            connect((host, 80))
            print host
        except socket.error:
            print 'host: %s closed' % host
            continue

if '__main__' == __name__:
    find_ip()
