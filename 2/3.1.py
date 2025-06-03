# 符号计算(方程组求解)
from sympy import symbols,Eq,solve

# 定义符号
x,y = symbols('x y')

# 定义方程组 (二元一次方程组)
eq1 = Eq(2*x+y,3)
eq2 = Eq(x-2*y,-1)

# 求解
solution  = solve((eq1,eq2),(x,y))

print(solution)