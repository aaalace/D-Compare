import threading


def func1():
    rocket = 0
    print('start func2')
    while rocket < 100000000:
        rocket += 1
    print('end func2')


def func2():
    rocket = 0
    print('start func1')
    while rocket < 100000000:
        rocket += 1
    print('end func1')


if __name__ == '__main__':
    my_thread = threading.Thread(target=func1)
    my_thread1 = threading.Thread(target=func2)
    my_thread.start()
    my_thread1.start()