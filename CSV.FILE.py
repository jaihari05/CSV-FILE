import csv
import os
data = [
    {'NAME': 'HARI', 'DEPT': 'B.COM', 'REG.NO': 'BU211204'},
    {'NAME': 'RAMESH', 'DEPT': 'B.COM.CA', 'REG.NO': 'BU211201'},
    {'NAME': 'RAM', 'DEPT': 'MCA', 'REG.NO': 'BU211203'}
    ]
# File path to save
file_path = file_path = os.path.join(os.path.expanduser('~'), 'Desktop','SAMPLETEST.CSV')
# Write data to CSV file
with open(file_path, mode='w', newline='') as csvfile:
    fieldnames = ['NAME', 'DEPT', 'REG.NO']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for SAMPLETEST in data:
        writer.writerow(SAMPLETEST)
print(f"Data has been written to '{file_path}' successfully.")