#Coded by: QyFashae

# Data for the comprehension
employees = {'Employee_1' : 100000,
             'Employee_2' : 99817,
             'Employee_3' : 122908,
             'Employee_4' : 88123,
             'Employee_5' : 93121}

# One_liner
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]

# Output
print(top_earners)
