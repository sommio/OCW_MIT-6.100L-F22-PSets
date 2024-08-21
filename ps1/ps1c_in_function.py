def part_c(initial_deposit):
	#########################################################################
	portion_down_payment = 200000 # 25% * $800,000
	months = 36
	min, max = 0, 1
	r = (min+max)/2 
	steps = 0
	epsilon = 100
	cint = lambda money,r,months: money*((1+r/12)**months)
	
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	
	if initial_deposit > portion_down_payment:
	    r = 0
	elif cint(initial_deposit, max, months) >= portion_down_payment:
	    steps += 1
	    while abs(cint(initial_deposit, r, months) - portion_down_payment) >= epsilon:
	        if cint(initial_deposit, r, months) < portion_down_payment:
	            min = r
	        else:
	            max = r
	        steps += 1
	        r = (min+max)/2 
	else:
	    r = None
	
	print(f'Best savings rate: {r}')
	print(f'Steps in bisection search: {steps}')
	return r, steps