portion_down_payment = 0.25
r = 0.04
total_cost = 1000000.0
semi_annual_raise = 0.07

starting_annual_salary = float(input("Enter your starting annual salary: "))


search_flag = False
bisection_search_counter = 0
up_bound = 10000
low_bound = 0
savings_rate = up_bound

while search_flag == False:
	current_savings = 0.0
	annual_salary = starting_annual_salary
	for month in range(36):
		monthly_salary = annual_salary/12

		if month % 6 == 0 and month != 0:
			annual_salary *= 1+semi_annual_raise 

		portion_saved = savings_rate/10000
		current_savings = current_savings*(1+r/12)+portion_saved*monthly_salary


	if savings_rate == 10000 and total_cost*portion_down_payment > current_savings+100:
		print("It is not possible to pay the down payment in three years")
		search_flag = True
	elif current_savings-total_cost*portion_down_payment > 100:
		up_bound = savings_rate
		savings_rate = low_bound+(up_bound-low_bound)/2
		bisection_search_counter += 1
	elif current_savings-total_cost*portion_down_payment < -100:
		low_bound = savings_rate
		savings_rate = low_bound+(up_bound-low_bound)/2
		bisection_search_counter += 1
	else:
		bisection_search_counter += 1
		print("Best savings rate:", savings_rate/10000)
		print("Steps in bisection search:", bisection_search_counter)
		search_flag = True



