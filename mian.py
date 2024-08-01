"""This is the main script for the Mathematics Specialist Investigation"""
import random 

# define the array that you will use to store information 
array = []

# population size
n = int(input("How large would your population sample size be? "))
# number of trials 
trials = int(input("How many trials would you like to conduct? "))
# the constriants random loop that generates a random number between the trials and the sample size
for i in range(trials):
    result = random.randint(1, n)
    array.append(result)

print("Trial results: ", ", ".join(map(str, array)))