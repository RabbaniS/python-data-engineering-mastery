# #Convert employee salary "75000.50" into float and calculate a 15% increment.
# salary=str(input("Enter your salary: "))
# con_salary=float(salary)
# bonus=15
# new_salary=con_salary+(con_salary*bonus/100)
# print(f"Your new salary after {bonus}% bonus is: {new_salary:.2f}")

#Calculate success and failure percentages
# total_records=10000
# success_records=700
# failure_records=9200
# percentage_success=(success_records/total_records)*100
# percentage_failure=(failure_records/total_records)*100
# print(f"Success Records: {success_records} ({percentage_success:.2f}%)")
# print(f"Failure Records: {failure_records} ({percentage_failure:.2f}%)")

#convert gb to mb and kb
gb=float(input("Enter size in GB: "))
mb=gb*1024
kb=mb*1024
print(f"{gb} GB is equal to {mb:.2f} MB and {kb:.2f} KB")