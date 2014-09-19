'''Delete Final Line'''

import os, sys

def delete_final_line(path):
    last = None
    file = open(path, "r+")
    file.seek(0, os.SEEK_END)
    pos  = file.tell() - 1
    while pos >= 0:
        char = file.read(1)
        if char == '\n':
            if last !='\n':
                pos += 1
            break
        pos -= 1
        if pos < 0:
            pos = 0
            break
        file.seek(pos, os.SEEK_SET)
        last = char
    if pos >= 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()
    file.close()

if __name__ == '__main__':
    path = 'm.py'
    open(path, 'w').write('\nHello\n\n\nstranger.\n\nThis is a demo.')
    while 1:
        data = open(path).read()
        sys.stdout.write(`data`)
        sys.stdout.write('\n')
        if not data:
            break
        delete_final_line(path)
