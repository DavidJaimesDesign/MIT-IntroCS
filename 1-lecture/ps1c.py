annual_salary = input("Your yearly salary: ")
total_cost = 1000000.0
portion_down_payment = total_cost/4.0

epsilon = 0.01
high = 1.0
low = 0
num_steps = 0

guess = (high + low)/2.0

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


while (amountSaved(guess, annual_salary - portion_down_payment)) >= epsilon:
    if amountSaved(guess, annual_salary) < portion_down_payment:
        print(amountSaved(guess, annual_salary) - portion_down_payment)
        low = guess
    else: 
        print(amountSaved(guess, annual_salary) - portion_down_payment)
        high = guess
    guess = (high + low)/2.0
    num_steps +=1
    
print 'Best savings rate:', guess
print 'Steps in bisection search:', num_steps
