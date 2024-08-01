import random 

# define the array that you will use to store information 
array = []

# population size
n = int(input("How large would your population sample size be? "))
# trial size
# trials = int(input("How many trials do you want to record "))
# generate random numbers for each person in the population
while len(array) < n:
    result = random.randint(1, n)
    array.append(result)

# print the array in the desired format
print("Trial results:", ", ".join(map(str, array)))
