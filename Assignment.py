# (Q1)
# n=int(input("Enter a Number: "))
# sum=(n*(n+1))//2
# print( f"the sum of first {n} number is {sum}")






# (Q2)
# s="Hello Hello Hello there is an important anouncement for all of you kindly payvattention"
# print(s)
# print(s.count("O"))






# (Q3)
# s1="apple mango apple orange orange apple guava mango mango"
# s2=[]
# s1=s1.split()
# # print(s)
# for i in s1:
#     if i not in s2:
#      s2.append(i)
# for i in range (0 , len(s2)):
#     print(" the frequency of" , s2[i] , "is" , s1.count(s2[i]))






# (Q4)
# def swap(a,b):
#     old_a=print("abc")
#     old_b=print("xyz")
#     new_a=b[:2] + a[2:]
#     new_b=a[:2] + b[2:]
#     return new_a + " " +  new_b
# s=swap("abc" , "xyz")
# print(s)






# (Q5)
# def add(s1):
#     length=len(s1)
#     if length < 3:
#         return s1
#     elif s1.endswith("ing"):
#         print(s1 + "ly")
#     else:
#         print(s1 + "ing")
# a=add("morn")
# print()





# (Q6)
# str1 = "The lyrics are not meant to be that much poor"
# id1 = str1.index("not")
# print(id1)
# id2 = str1.index("poor")
# print(id2)
# print(str1[id1:id2+4])
# str2 = str1.replace(str1[id1:id2+4], "good")
# print(str2)






# (Q7)
# import math
# print("GCD of 40 and 60 is : ", end="")
# print(math.gcd(40,60))






# (Q8)
# l=["1","2","3","4","5","6","[6,6,7]","10"]
# for i in l:
#     if len(i) > 1:
#         print("Yes, sub-list is present")
#         break





# (Q9)
# l=[4,8,0,88,65,45,7,9,12,34,5,6]
# l.sort()
# print(l)
# print("second smallest numer is: ",l[1])





# (Q10)
# a_list = ['apple', 'orage', 'apple', 'banana', 'apple', 'apple', 'orange', 'grape', 'grape', 'apple']
# uniq_value=set(a_list)
# print(uniq_value)





# (Q11)
# t=((1,2),(3,4),(5,6),(7,8))
# print(list(zip(*t)))





# (Q12)
# t=(("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30))
# di=dict(t)
# print(di)





# (Q13)
# di={35: "akash", 31:"gaurav", 5:"suraj", 12:"arjun", 8: "akhil", 29:"dwarkesh"}
# a=sorted(di.items())
# print(a)




# (Q14)
# di={"akash": 10, "gaurav": 12, "anand": 14, "suraj": 20, "akhil": 25, "ashish": 30}
# a=sorted(di.values())
# print(a)
# print(a[5], a[4], a[3])




# (Q15)
# def fib(n):
    
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:    
#             return (fib(n-2) + fib(n-1))
# n=int(input("enter a number :"))
# for n in range(0,n):    
#         print(fib(n), end = " ")




# (Q16)
# i=0
# freq={}   
# l=["1", "1", "1", "5", "5", "3", "1", "3", "3", "1","4","4", "4", "2", "2", "2", "2"]
# d={x:x.count(x) for x in l}
# print(d)





# # (Q17)
# import math
# s=input("Enter the type : Even or odd : ")
# n=int(input("how many sum of numbers you want: "))
# sum=0
# for i in range (n):
#     if s=="odd":
#         sum=sum + ((12+20*i)) / math.factorial(1+2*i)

#     elif s=="even":
#         sum = sum + ((2+20*i)) / math.factorial(2*(i+1))
#     else:
#         print("Please enter the proper number")
# print("the value of sum is " , sum)




# # (Q18)
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact (n-1)    
# s=fact(3)
# print(s)





# (Q19)
# old_l=['apple', 'orage', 'apple', 'banana', 'apple', 'apple', 'orange', 'grape', 'grape', 'apple']
# new_l=list(set(old_l)) 
# print(new_l)

# or

# new_l=[]
# for i in old_l:
#     if i not in new_l:
#         new_l.append(i)
# print(new_l)



# (Q20)
# import random
# from typing import final

# class User:
#     print("Welcome To Automatic Password Generator")
#     def PassDet():
#         while(True):

#             name=input("Enter Your Name: ")
#             year=input("Enter your birth-date(in ddmmyy): ")
#             if len(year) > 6:
#                     print("Kindly enter date in mentioned format")
                    
                     
#             else:
#                 global g
#                 g= name + year[-4:-1]
#                 print(f"Your computer generated username is {g}")
               
                

#             l_chars="abcdefghiklmnopqrstuvwxyz"
#             u_chars="ABCDEFGHIJKLMOPQRSTUVWXYZ"
#             sym="!@#$%^&*)(><?"
#             dig="1234567890"

#             ans=l_chars + u_chars + sym + dig

#             length=int(input("How long you want your password: "))
#             a="".join(random.sample(ans,length))
          
#             if sym in a:
#                 print("Re-enter details again, because Speical character is missing")
#                 break
        
#             if length < 8:
#                 print("Minimum 8 letters are mandatory for password")
            
#             else:
#                 print(f"Your Password is {a}")
#                 break
            
#         l=[]
#         l.append(name)
#         l.append(g)
#         l.append(a)

#         print("Your Details are saved in our System in following manner -->", end=" ")
#         print(tuple(l))
#         print("Enter 1 if you want to see your details")

#         n=int(input("enter number: "))
#         if n==1:
#             d={g:a}
#             print(f"your Username and password is {d}")
            
# u=User
# u.PassDet()
