# Function for nth Fibonacci number 
  
def get_fibonacci_number(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return get_fibonacci_number(n-1)+get_fibonacci_number(n-2) 
  
# Driver Program 
  
print(get_fibonacci_number(9)) 


# Sourced and modified from: https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/