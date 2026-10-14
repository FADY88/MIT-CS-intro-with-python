def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	monthly_salary = yearly_salary / 12
	down_payment = portion_down_payment * cost_of_dream_home
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	months = 0
	while amount_saved < down_payment:
		amount_saved += portion_saved * monthly_salary + amount_saved * (r/12)
		
		if months % 6 == 0 and months != 0:
			yearly_salary *= 1 + semi_annual_raise
			monthly_salary = yearly_salary / 12
		
		months += 1
	
	print("Number of months:", months)
	return months