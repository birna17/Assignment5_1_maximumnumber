#1. asks for a number and sets as max.. 
#2 asks for another number, 
#3 if second number is negative then stop  and print max 
#4 otherwise continue: compare second number to max number,
# and if second number is bigger than max , then second number
# is set as max. 
#5 go back to step 2 and so on .. 

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0 

while num_int > -1:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line