def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000
	down_payment = 0.25 * cost_of_dream_home
	months = 36
	amount_saved = 0
	
	upper_bound = 1.0
	lower_bound = 0.0
	r = lower_bound
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	steps = 0
	
	
	
	possible = down_payment < initial_deposit * (1 + upper_bound/12)**months
	while possible:
		amount_saved = initial_deposit * (1 + r/12) ** months
		if down_payment - 100 <= amount_saved <= down_payment + 100:
			break
		elif amount_saved < down_payment:
			lower_bound = r
		elif amount_saved > down_payment:
			upper_bound = r
		
		r = (upper_bound + lower_bound) / 2
		steps += 1
	else:
		r = None
	
	print("Best savings rate:",r)
	print("Steps in bisection search:",steps)
	return r, steps