annual_salary = input("Your yearly salary: ")
total_cost = 1000000.0
portion_down_payment = total_cost/4.0

epsilon = 100
high = 1.0
low = 0
num_steps = 0

guess = (high + low)/2

def amountSaved(guess, salary):
    annual_salary = salary
    portion_saved = guess
    semi_annual_rate = 0.07
    months_to_save = 36
    r = 0.04
    total_saved = 0
    
    for months in range(months_to_save):
        if months%6 == 0:
            annual_salary = annual_salary + annual_salary*semi_annual_rate
        monthly_savings = annual_salary*portion_saved/12
        total_saved += monthly_savings + total_saved*r/12
    #print total_saved
    return total_saved

saved = amountSaved(guess, annual_salary)

if (saved < portion_down_payment):
    print 'There is no way you could save enough in 3 years'
else:
    while abs(saved - portion_down_payment) >= epsilon:  
        if  saved < portion_down_payment:
            low = guess
        else: 
            high = guess
        guess = (high + low)/2.0
        saved = amountSaved(guess, annual_salary)
        num_steps +=1
    
    print 'Best savings rate:', round(guess,2)
    print 'Steps in bisection search:', num_steps
