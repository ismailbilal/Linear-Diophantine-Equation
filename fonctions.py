#this fonction is for calculate the greatest common divisor of tow integrs
def fGCD(a,b) :
    if abs(a) < abs(b) :
        q=b
        r=a
    else:
        q=a
        r=b
    while q%r != 0 :
        l=q%r
        q=r
        r=l
    return r 


#to calculate an initial solution
def initial_solution(a,b,c) :
    #~~~~find an initial integer solution
    y=1
    gcd=fGCD(a,b)
    n=abs(gcd-(b*y))
    ci=int(c/gcd)
    while n%a != 0 :
        if y>0 :
            y=-y
        else:
            y=-y+1
        n=abs(gcd-(b*y))
    n=gcd-(b*y)
    x=n/a
    #~~~~~~


    y=int(y*ci)
    x=int(x*ci)
    return (x,y)


#to make solution looks better
def write_x(x, op) :
    wr_var = {True : f'{x}{op}', False : ""}
    return wr_var[
        x != 0
    ]


def write_coef(x) :
    wr_coef = {True : f'{x}', False : ""}
    return wr_coef[
        x != 1
    ]
