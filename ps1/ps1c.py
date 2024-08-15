## 6.100A PSet 1: Part C
## Name: sommio
## Time Spent: ~45min
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 200000 # 25% * $800,000
months = 36
min, max = 0, 1
r = (min+max)/2 
steps = 0
epsilon = 100


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

def compound_interest(money, r, months):
    '''
    money: An integer or float
    r: Rate of return, a float
    mothers: An integer
    Returns the result of the compound interest
    '''
    return money*((1+r/12)**months)

if initial_deposit > portion_down_payment:
    r = 0
elif compound_interest(initial_deposit, max, months) >= portion_down_payment:
    steps += 1
    while abs(compound_interest(initial_deposit, r, months) - portion_down_payment) >= epsilon:
        if compound_interest(initial_deposit, r, months) < portion_down_payment:
            min = r
        else:
            max = r
        steps += 1
        r = (min+max)/2 
else:
    r = None

print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')
