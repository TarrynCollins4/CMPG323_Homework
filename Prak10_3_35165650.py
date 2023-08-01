
print("For the calculation of prime numbers;")
start_number = int(input("Enter a positive starting number: "))
end_value = int(input("Enter a positive ending number: "))

print("Prime numbers between" , start_number, "and", end_value, "are:")
for num in range (start_number,end_value +1):
    if num>1:
        for i in range (2,num):
            if(num%i)==0:
               break
        else:
            print(num)
     
