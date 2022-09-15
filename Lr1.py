import math
def integrate(f, a, b, n=1000):
    h = (b - a) / n
    x = a
    s = f(x) - f(b)
    for k in range(1, n+1):
        x += h
        s += 2 * f(x)    
    result = (h / 2) * s
    print(round(result, 8))
if __name__ == "__main__":
    f1 = lambda x: math.sqrt(x)
    integrate(f1, 5, 10)
