def random():
    list = [1, 3, 'heello']

    print(list)

    list.append("poopstains")
    print(list)

    list.insert(2, "first")

    print(list)

    item = list.pop(2)
    print(item)
    print(list)

    print(list.index('heello'))

    print("list as stack")
    # using a list as a stack
    stack = [1, 4, 8, 4]

    print(stack)
    stack.append(3)
    stack.append(5)

    print(stack)
    print(stack.pop())
    print(stack.pop())

    print(stack)

    print("Queue example")

    from collections import deque

    q = deque([1, 2, 3])

    print(q)
    q.append(4)
    q.append(5)
    print(q)

    print(q.popleft())
    print(q.popleft())
    print(q)

    print("Q my way")
    q = [1, 2, 3]
    print(q)
    q.pop(0)
    q.pop(0)
    print(q)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def fib(x):
    s = {}
    if x <= 0:
        return 0
    elif x is 1:
        return 1
    else:
        return fib(x - 1) + fib(x -2)

def printrec(list):
    if len(list) > 0:
        print(list[0])


def multiples3(n):
    #f(n) = 3 * n
    pass

