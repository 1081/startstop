from startstop import t


def run_a():
    for i in range(100000):
        i**2


def run_b():
    for i in range(100000):
        i**2


t()
run_a()
t()

t()
run_b()
t()
