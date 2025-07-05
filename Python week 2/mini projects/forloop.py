# count down

# import time

# print ("counting down..... \n")
# for i in range(10,0,-1):
#     print (i)
#     time.sleep(1)

#List all prime numbers 1 to 100

print ("Prime numbers between 1 to 100 are:")

for num in range(2,101):
    is_prime = True
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
