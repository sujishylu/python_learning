# tip calculator
total_bill = input(" Hi\n Plese endter the toatal bill amount in INR :")
split = input ( " please input the the number of peple its needs to be split by : ")
percentage = input(" tell me what percentage you want to tip 10, 12, 15 % :")

tips = (int(total_bill)/int(split) * (float(percentage) /100))
print ("the tipe per head is =" , tips, " rs" )

