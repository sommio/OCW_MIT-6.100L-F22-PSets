def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	return months