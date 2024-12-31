# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(n):
    print('l.acquire()')
    if n==0:
        result=1
    else:
        result=n*print_hi(n-1)
    print("l.release()")
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(print_hi(1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
