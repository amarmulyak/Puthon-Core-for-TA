x = []
for a in range(1,10):
    for b in range(0,10):
        if a!=b:
            for c in range(0,10):
                if b!=c and a!=c:
                    for d in range(0,10):
                        if c!=d and d!=b and d!=a:
                            x.append(str(a)+str(b)+str(c)+str(d))
print(x)



