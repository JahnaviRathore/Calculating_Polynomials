from sympy import symbols, Eq, solve
#eq--equate
#eval--evaluate

def solving_equation(equation_str):
    x=symbols("x")
    lhs, rhs = equation_str.split('=')
    equation = Eq(eval(lhs), eval(rhs))
    solution = solve(equation, x)
    return solution
print("*If the equation has any value with it, write it in the following format - number*x")
print()
#Input and Print
equation = str(input("Enter a linear equation "))
solution = solving_equation(equation)
print(f"--Solution of ",equation,"in x is=",solution)

def solving_equation_steps(equation_str):
    x = symbols("x")
    lhs, rhs = equation_str.split('=')
    equation = Eq(eval(lhs), eval(rhs))
    
    #showing the steps
#step 1:(equation)
    print("Step 1 -")
    print("1. The equation: ",equation)

# Step 2: Move terms to one side
    print("Step 2 -")
    step1 = Eq(eval(lhs)- eval(rhs), 0)
    print(f"2. Bringing the constants on one side =",step1)
    
#step3:(solving x)
    print("Step 3 -")
    solution = solve(equation, x)
    print(f"3. Solving X -> x =  ",solution)
    
    return solution
    
#trial

solution = solving_equation_steps(equation)
