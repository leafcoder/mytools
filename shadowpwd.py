#!/usr/bin/python
# coding: utf-8
'''shadow 密码生成工具

在 Ubuntu / Debian 下，密码文件是 /etc/shadow，以下脚本可以生成密码。
'''
import crypt
from sys import argv
from uuid import uuid4
from random import randint

assert len(argv) >= 2, 'please input password'
size = randint(8, 12)
salt = uuid4().hex[:size]
print crypt.crypt(argv[1], '$6$%s' % salt)
