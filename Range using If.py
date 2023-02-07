starting_input_value=int(input("Enter your Starting value:"))
ending_input_value=int(input("Enter your Ending value:"))
step_input_value=int(input("Enter your Step value:"))
enter_divide_value=int(input("Enter your Divide value:"))



for x in range(starting_input_value,ending_input_value,step_input_value):
    if x%enter_divide_value ==0:
        print("The values are :",x)
    
