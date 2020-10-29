from fonctions import fGCD,initial_solution,write_y,write_x,write_coef
print('to solve a Linear Diophantine Equation ,ax+by=c')
a=int(input('enter a : '))
b=int(input('enter b : '))
c= int(input('enter c : '))
gcd=fGCD(a, b)
if c%gcd != 0 :
    print("there are no solution.")
else:
    (x,y)=initial_solution(a,b,c)
    bi=int(b/gcd)
    ai=int(a/gcd)
    x=write_x(x)
    y=write_y(y)
    bi=write_coef(bi)
    ai=write_coef(ai)
    print(f'the solutions of {a}x+{b}y={c} is (x,y)=[({x}{bi}k,{y}{ai}k)/ for k integer]')
