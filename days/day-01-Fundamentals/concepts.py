# #Variables
# employee_name="John Doe" #String
# employee_age=30 #Integer
# salary=50000.0 #Float
# is_data_engineer=True   #Boolean

# #Print the variables
# print(f"Employee Name: {employee_name}")
# print(f"Employee Age: {employee_age}")
# print(f"Salary: {salary}")
# print(f"Is Data Engineer: {is_data_engineer}")

# #Type checking and conversion 
# print(f"Type of employee_name: {type(employee_name)}")
# print(f"Type of employee_age: {type(employee_age)}")    
# print(f"Type of salary: {type(salary)}")
# print(f"Type of is_data_engineer: {type(is_data_engineer)}")

# #Type conversion
# salary="200000.0" #String
# print(f"Updated Salary: {salary}")
# salary=float(salary) #Convert to Float
# print(f"Converted Salary: {salary}")
# bonus="10000" #String
# bonus=int(bonus) #Convert to Integer
# total_compensation=salary+bonus #Float
# print(f"Total Compensation: {total_compensation}")

#Operators
total_record_count=1000
processed_record_count=800
unprocessed_record_count=200

success_rate=(processed_record_count/total_record_count)*100
print(f"Success Rate: {success_rate}%")

if processed_record_count+unprocessed_record_count==total_record_count:
    print("Data validation successful.")
else:
    print("Data validation failed. Record count mismatch.")