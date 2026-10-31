#file size conversion
# def convert_bytes(size):
#     """Convert bytes to KB, MB, GB, or TB"""
#     for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
#         if size < 1024.0:
#             return f"{size:.2f} {unit}"
#         size /= 1024.0
#     return f"{size:.2f} PB"
# MB=convert_bytes(5242880)
# print(MB)

#pending records count and percentage calculation
total_records=10000
pending_records=250
percentage_pending=(pending_records/total_records)*100
print(f"Pending Records: {pending_records} ({percentage_pending:.2f}%)")
#print(f"pending records percentage: {percentage_pending:.2f}%")