# hello_one.py

def hello_world():
    print('Hello!, world')


def good_morning(x):
    print(x)
    msg = str(input('Type here: '))
    print('We say : \' %s \'' % msg)


if __name__ == '__main__':
    hello_world()
    print('Prints only here')
