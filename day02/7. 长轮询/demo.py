from queue import Queue,Empty

q = Queue()
q.put({'id':1,'count':1})
try:
    v = q.get(timeout=5)
    print(v,type(v))
except Empty as e:
    pass

