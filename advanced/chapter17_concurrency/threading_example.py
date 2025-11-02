# threading_example.py
# Examples and explanations for threading

import threading

def worker():
    print('Worker thread is running')

threads = []
for i in range(2):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('All threads finished')
