# #calculate datapipeline cost
# compute_cost=500
# storage_cost=200
# network_cost=100
# tax_rate=18
# total_cost=compute_cost+storage_cost+network_cost
# tax_amount=total_cost*tax_rate/100
# final_cost=total_cost+tax_amount
# print("Total Cost: ", total_cost)
# print("Tax Amount: ", tax_amount)
# print("Final Cost: ", final_cost)

#calculate invalid records,data quality percentage, nullpercentage, duplicate percentage, data completeness percentage
total_records=10000
invalid_records=500
invalid_percentage=invalid_records/total_records*100
data_quality_percentage=(total_records-invalid_records)/total_records*100
null_records=200
null_percentage=null_records/total_records*100
duplicate_records=100
duplicate_percentage=duplicate_records/total_records*100
print("Data Quality Percentage: ", data_quality_percentage)
print("Null Percentage: ", null_percentage)
print("Duplicate Percentage: ", duplicate_percentage)
print("Data Completeness Percentage: ", 100 - data_quality_percentage)
print("Invalid Percentage: ", invalid_percentage)