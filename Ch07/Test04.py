from urllib.request import urlopen


web = urlopen('http://www.guancha.cn')

first3Bytes = web.read(3)
print(first3Bytes)
line = web.readline()
print(line)
line = str(line, 'latin_1')
print(line)
if 'encoding' in line:
    print('yes!')
else:
    print('no!!')