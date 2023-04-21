basicPay = 74000
houseAllowance = (10 / 100) * 74000
medicalAllowance = (7 / 100) * 74000
transportAllowance = (15 / 100) * 74000
allowances = houseAllowance + medicalAllowance + transportAllowance
grossPay = basicPay + allowances
nh = (10 / 100) * 74000
ns = (18 / 100) * 74000
pa = (30 / 100) * 74000
deductions = nh + ns + pa
netPay = grossPay - deductions
print("The net pay is : ", netPay)

print("The gross pay is : ", grossPay)

print("The deductions are : ", deductions)

print("The allowances are : ", deductions)





