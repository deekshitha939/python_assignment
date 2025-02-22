
# 1,100 numbers
for i in range(1,101):
    print(i)
#all even numbers from 1,50
i=1
while i<=50:
    if i%2==0:
        print(i)
    i=i+1

#multiplication table
num=int(input("enter a number"))
for i in range(1,21):
       print("{}*{}={}".format(num,i,num*i))
       
#finding factorial of given number
num=int(input("enter a number"))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i=i+1
print(fact)
#all numbers from 1 to 100 that are divisible by 3 and 5
for i in range(1, 101):  
    if i % 3 == 0 and i % 5 == 0:  
        print(i)
