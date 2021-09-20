from request import req
from get_greate import great_img

def a():
    r = req()
    #c = great_img(r[0],r[1])
    return r

b = a()
print(b[0])
print(b[1])