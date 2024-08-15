## 6.100A PSet 1: Part A
## Name: sommio
## Time Spent: ~20m
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input('Starting yearly salary: '))
portion_saved = float(input('Portion of salary to be saved: '))
cost_of_dream_home = float(input('Cost of dream home: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
amount_saved = 0
portion_down_payment = 0.25
months = 0
r = 0.05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < cost_of_dream_home*portion_down_payment:
    months += 1
    amount_saved += amount_saved * (r/12)
    amount_saved += (yearly_salary/12)*portion_saved
print(f'Number of months: {months}')
