from time import time

start_time = time()
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print('a=%d,b=%d,c=%d'%(a,b,c))

print('over')
end_time = time()
print('elapse:%f'%(end_time-start_time))
