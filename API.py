
from Config import *

        
def 多账号登陆(data):
    t = []
    for i in data:
        if i[:4] == "qgqp":
            t.append(DCTD(i))
        else:
            t.append(Tonghuashun(i))
    return t
