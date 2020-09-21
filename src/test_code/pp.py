import pp
import time

def f(x, t0):
    ans = 1
    x0 = x
    t = time.time() - t0
    print('factorial of %d: start@%.2fs' % (x0, t))
    while x > 1:
        ans *= x
        time.sleep(0.5)
        x -= 1
    t = time.time() - t0
    print('factorial of %d: finish@%.2fs, res = %d' %(x0, t, ans))
    return ans

def main():
    res = []
    var = (4, 8, 12, 20, 16)
    ppservers=()
    p = pp.Server(2, ppservers=ppservers)
    t0 = time.time()
    for i in var:
        res.append(p.submit(f, args = (i, t0), modules = ('time', )))
        
    print('output:')
    for i in range(len(res)):
        res[i] = res[i]()
    t = time.time() - t0
    print('factorial of %s@%.2fs: %s' % (var, t, res))

if __name__ == '__main__':
    main()
