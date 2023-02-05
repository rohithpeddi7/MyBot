from threading import Thread

def func1():
    for i in range(1000):
        print(f"1 {i}")

def func2():
    for i in range(1000):
        print(f"2 {i}")

if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2).start()