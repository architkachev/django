from _datetime import *

a = 2 * (10 ** 500)
b = 10 ** 500

ts = datetime.utcnow()
ww = 0
for i in range(0, 10000000):
    ww = (a * b) + i - ww

ts2 = datetime.utcnow()
print(ww)
print(ts2 - ts)

