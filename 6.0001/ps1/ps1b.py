portion_down_payment = 0.25
current_savings = 0
float(current_savings)
r = 0.04


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of the house: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))



month_counter = 0
saved_enough_flag = False


while saved_enough_flag != True:
	monthly_salary = annual_salary/12

	if month_counter % 6 == 0 and month_counter != 0:
		annual_salary *= 1+semi_annual_raise 

	current_savings = current_savings*(1+r/12)+portion_saved*monthly_salary
	month_counter += 1
	
	if current_savings >= (total_cost*portion_down_payment):
		saved_enough_flag = True

print("Number of months: ",month_counter)	