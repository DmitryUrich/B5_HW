import time


def time_this(num_runs):
    def decorator(f):
        def wrapper():
            sum_num = 0
            for i in range(num_runs):
                t1 = time.time()

                f()

                t2 = time.time()
                sum_num += (t2 - t1)
            return "Время цикла в среднем %.5f секунд." % (sum_num / num_runs)

        return wrapper

    return decorator


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


print(f())
