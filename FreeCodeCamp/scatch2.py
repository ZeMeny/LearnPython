import statistics

data2 = [i for i in range(1, 11)]
print(data2)

x = statistics.mean(data2)
print(x)


def recursive(num):
    if num == 0:
        return 1
    else:
        return num * recursive(num - 1)


print(recursive(6))
