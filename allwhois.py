import os, re, sqlite3

conn = sqlite3.connect('whois.db')
conn.executescript('''\
CREATE TABLE IF NOT EXISTS i (i INTEGER, n VARCHAR, s BOOLEAN,
PRIMARY KEY (i), UNIQUE (n));
''')
conn.commit()

size = 0
chars = 'abcdefghijklmnopqrstuvwxyz'
findall = re.compile(r'No\smatch\sfor').findall

def getname(name=None, level=6, ext='com'):
    curr = ''
    if level > 0:
        for c in chars:
            if name is None:
                sub = c
            else:
                sub = c + name
            if len(sub) - len(set(sub)) >= 2:
                continue
            yield '%s.%s' % (sub, ext)
        for c in chars:
            if name is None:
                for c in getname(c, level=level-1, ext=ext):
                    yield c
            else:
                for c in getname(c+name, level=level-1, ext=ext):
                    yield c

for name in getname(level=3):
    cur = conn.cursor()
    cur.execute('''\
SELECT COUNT(i) FROM i WHERE n=?;''', (name, ))
    c = cur.fetchone()[0]
    if 0 != c:
        continue
    p = os.popen('whois %s' % name)
    s = p.read()
    p.close()
    status = True 
    if findall(s):
        status = False
    print '%s' % name, status
    conn.execute('''\
INSERT INTO i (n, s) VALUES (?, ?);''', (name, status))
    if size == 10:
        conn.commit()
        size = 0
    else:
        size += 1
