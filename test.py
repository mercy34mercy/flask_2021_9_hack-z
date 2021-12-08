from request import req
from get_greate import great_img
from concurrent.futures import ThreadPoolExecutor

r = req("美女",3)
print(r[0])
print(r[1])

excutor = ThreadPoolExecutor(max_workers=3)
futures = []
futures2 = []
future  = []
future2 = []

for i in range(3):
    future, future2 = excutor.submit(great_img, r[0], r[1], 3)
    futures.append(future)
    futures2.append(future2)

    c = []
    d = []

for i in futures:
        c.append(futures[i].result())
        d.append(futures2[i].result())

jsonify = ({
        "data": []
    })

for i in range(len(c)):
        print(c[i])
        add_data = {
            "url": c[i],
            "alt": d[i]
        }
        jsonify["data"].append(add_data)

print(jsonify)


