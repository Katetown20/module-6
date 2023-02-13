import time
from datetime import datetime
from threading import Thread

def get_thread(thread_name):
    time.sleep(1.0)
    print(f'thread name {thread_name }')

for i in range(5):
    get_thread(i+1)

t1 = datetime.now()

print('time', (datetime.now() - t1).microseconds)
threads = [Thread(target= get_thread, args= (i +1,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print('time', (datetime.now() - t1).microseconds)