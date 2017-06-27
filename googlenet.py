#!/usr/bin/python
# coding: utf-8

'''查询 Google 可用 IP 段

分析字符串，输出所有网段；主要提供给 google-hosts 的 find.sh 作为参数。
'''

import os, re, math
findall = re.compile(r'ip4:(?:\d+.){3}\d+\/\d{1,2}').findall
cmd = 'nslookup -q=TXT _netblocks.google.com 8.8.8.8'
with os.popen(cmd) as p:
    s = p.read()
for s in findall(s):
    seg = s.split(':')[1]
    ip, mask = seg.split('/')
    mask = int(mask)
    count = int(math.ceil(mask / 8.0))
    elems = ip.split('.')[:count]
    assert 1 < count < 4, 'out of limit'
    size = pow(2, (count * 8) - mask)
    elem = int(elems.pop(-1))
    for i in range(elem, elem + size + 1):
        print '.'.join(elems + [str(i)])
