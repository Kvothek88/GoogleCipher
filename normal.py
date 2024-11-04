import time

start = time.time()

for w in range(1,10):
    for o in range(0,10):
        for t in range(0,10):
            for l in range(0,10):
                for d in range(1,10):
                    for g in range(1,10):
                        for e in range(0,10):
                            for c in range(0,10):
                                for m in range(0,10):
                                    values = {w,o,t,l,d,g,e,c,m}
                                    if len(values)==9:
                                        min_value = str(w) + str(w) +str(w) +str(d) + str(o) + str(t)
                                        sub_value = str(g) + str(o) +str(o) +str(g) + str(l) + str(e)
                                        dif_value = str(d) + str(o) +str(t) +str(c) + str(o) + str(m)
                                        res = int(min_value) - int(sub_value)
                                        if res == int(dif_value):
                                            print(min_value)
                                            print(sub_value)
                                            print(res)
                                            print()

end = time.time()
end = time.time()
elapsed_time = int(end - start)
mins = elapsed_time // 60
secs = elapsed_time % 60
print(f"Elapsed time: {mins} mins {secs} secs")