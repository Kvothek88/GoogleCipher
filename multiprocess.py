import time
from multiprocessing import Pool

def check_combinations(args):
    w, d, g = args
    results = []
    for o in range(0, 10):
        for t in range(0, 10):
            for l in range(0, 10):
                for e in range(0, 10):
                    for c in range(0, 10):
                        for m in range(0, 10):
                            values = {w, o, t, l, d, g, e, c, m}
                            if len(values) == 9:
                                min_value = str(w) + str(w) + str(w) + str(d) + str(o) + str(t)
                                sub_value = str(g) + str(o) + str(o) + str(g) + str(l) + str(e)
                                dif_value = str(d) + str(o) + str(t) + str(c) + str(o) + str(m)
                                res = int(min_value) - int(sub_value)
                                if res == int(dif_value):
                                    results.append((min_value, sub_value, res))
    return results if results else None

if __name__ == '__main__':
    start = time.time()

    # Prepare input arguments for all combinations
    args_list = [
        (w, d, g)
        for w in range(1, 10)
        for d in range(1, 10)
        for g in range(1, 10)
    ]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(check_combinations, args_list, chunksize=10)

    # Filter out None results and print valid ones
    for result in results:
        if result is not None:
            for min_value, sub_value, res in result:
                print(min_value)
                print(sub_value)
                print(res)
                print()

    end = time.time()
    elapsed_time = int(end - start)
    mins = elapsed_time // 60
    secs = elapsed_time % 60
    print(f"Elapsed time: {mins} mins {secs} secs")
