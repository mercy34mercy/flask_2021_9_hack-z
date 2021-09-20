from request import req
from get_greate import great_img

r = req()
print(r[0]) 
print(r[1])

c = great_img(r[0],r[1])