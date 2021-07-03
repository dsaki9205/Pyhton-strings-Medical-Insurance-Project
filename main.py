medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   $4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#task 1
print (medical_data)

#task 2 replacing # with $
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data) 

#task 3 creating variable for calculating the number of medical records
num_records = 0

#task 4 for loop
for character in updated_medical_data:
  if character == "$":
    num_records += 1
#task 5
print("There are " + str(num_records) + " medical records in the data." )

#task 6 splitting Strings
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

#Task 7
medical_record = []

#Task 8
for record in medical_data_split:
  medical_record.append(record.split(','))
print(medical_record)

#Task 9 Cleaning data
medical_records_clean = []
#task 10
for record in medical_record:
  record_clean = []
for item in record:
  record_clean.append(item.strip())
  #task 11
for item in record:
    record_clean.append(item.strip())
#task 12
medical_records_clean.append(record_clean)
print(medical_records_clean)
for record in medical_records_clean:
  print(record[0])
#task 15
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])
#task 16
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
  print("names: " + str(names))
  print("ages: " + str(ages))
  print("bmis: " + str(bmis))
  print("insurance costs: " + str(insurance_costs))

  #task 19
  total_bmi = 0
  # task 20
  for bmi in bmis:
    total_bmi += float(bmi)
  average_bmi = total_bmi/len(bmis)
print("Average BMI: " + str(average_bmi))
