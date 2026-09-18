def is_triangle(a,b,c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def area(a,b,c):
    if is_triangle:
        p=(a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**0.5
    return 0

def perimiter(a,b,c):
    return a+b+c


