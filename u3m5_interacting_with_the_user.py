print("hello")
print(5*2+3**5)
print("new"+"ton")

top = 22
bottom = 7
pi_approx = top/bottom
print(pi_approx)
print(top,"/",bottom,"=",pi_approx)
to_print = str(top)+"/"+str(bottom)+"="+str(pi_approx)
print(to_print)

# input stored as a string - concatenate
a = input("Enter one number: ")
b = input("Enter another number: ")
print(a+b)

# input stored as a string - convert to int
a = int(input("Enter one number: "))
b = int(input("Enter another number: "))
print(a+b)

#############
# quick check
#############

# get user input
day = input("What day of the week? ")
num = int(input("How many times? "))

# show the phrase
print("It's", day*num)
