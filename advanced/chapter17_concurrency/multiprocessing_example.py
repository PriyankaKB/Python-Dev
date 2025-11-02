# multiprocessing_example.py
# Examples and explanations for multiprocessing

import multiprocessing

def worker(num):
    print(f'Worker {num} is running')

if __name__ == '__main__':
    processes = []
    for i in range(2):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print('All processes finished')
