import os

# 1. تحديد المسار الديناميكي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(BASE_DIR, "server.log")

file = open(log_path, "r")
failed_count = 0
success_count = 0

for line in file:
    if "Failed" in line:
        failed_count += 1
    elif "successfully" in line:
        success_count += 1
    else:
        pass    
file.close()

print(f"Failed attempts {failed_count}, success attempts {success_count}")        
