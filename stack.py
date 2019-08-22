import time

# Initial Stack Contents

myStack = ['One', 'Two', 'Three']

# Show Stack Function


def showStack():
    print('-----------')
    print 'Stack Count:', len(myStack)
    print('-----------')
    time.sleep(2)
    for item in myStack:
        print(item)
        time.sleep(2)
    print('-----------')
    time.sleep(2)

# Append Stack Function


def appendStack(item):
    myStack.append(item)
    print(' ')
    print('###############################')
    print '# Adding [', item, '] to Stack!'
    print('###############################')
    print(' ')
    time.sleep(2)
    showStack()

# Pop Stack Function


def popStack():
    completed = myStack.pop()
    print(' ')
    print('###############################')
    print '# Removing [', completed, '] from Stack!'
    print('###############################')
    print(' ')
    time.sleep(2)
    showStack()


# Start

showStack()
appendStack('Four')
popStack()
popStack()
popStack()
popStack()
