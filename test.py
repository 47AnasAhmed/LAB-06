print("Anas Ahmed(18b-116-cs),CS-A")
print("LAB QUIZ")
print("Q.NO:5")

print("Enter the task you want to perform:")
def simple(principal_investment,interst_rate,number_of_years):
    p = principal_investment
    r = interst_rate/100
    t = number_of_years
    
    i = (p*r*t)/100
    a = p+i

    print("The simple interest is:",i)
    print("The total amount of money earned plus interst is:",a)

def compound(principal_investment,interst_rate,number_of_years):
    p = principal_investment
    r = interst_rate/100
    t = number_of_years

    a = p*((1+(r/100))**t)
    i = a - p

    print("The compound interest is:",i)
    print("The total amount of money earned plus compound interst is:",a)

def compoundedmonthly(principal_investment,interst_rate,number_of_years,monthly_or_quarterly):
    p = principal_investment
    r = interst_rate/100
    t = number_of_years
    n = t*12
    m = monthly_or_quarterly

    if m == 1:
        k = 12 

    else:         
        k = 4

    s = p*((1+(r/k))*n)

    print("The final value of investment after",t,"years:",s)
        
