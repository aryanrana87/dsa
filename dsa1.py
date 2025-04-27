# class Student:
#     school = "Newton"

#     def __init__(self,val):
#         self.name = val
#     def addsurname(self,val):
#         self.surname = val
#     def fullname(self,val):
#         self.fullname = val

# s1=Student("Adityta")
# print(s1.name)


# s2 = Student("Nishi")
# print(s2.name)

# s2.addsurname("Gupta")
# print(s2.surname)

# s2.fullname("Nishi Gupta")
# print(s2.fullname)

# print(s1.school)
# print(s2.school)
# print(Student.school)
# print(Student.name)

# class fractional:
#     def __init__(self,numerator,denominator):
#         self.numerator=numerator
#         self.denominator=denominator
#     def print(self):
#         print(self.numerator,"/",self.denominator)
# s1=fractional(2,5)
# s1.print()
# s2=fractional(3,4)
# s2.print()
# fibonacci series
# def fibonacci (n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else :
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(14))
#sets
# s={3,4,5,3}
# t={"hii",23,4,34.55}
# print(t)
# f=set()
# print(type (f))
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         s=0
#         d=[]
#         for i in nums:
#             if i == s:
#                 print(d)
#             else:
#                 s+=i
#                 d.append(i)
# print(11)
# print(11,end=" ")
# print(11)
# s = input()
# t = input()

# if s == t[::-1]:
#     print("YES")
# else:
#     print("NO")
# s=input()
# d=0
# t=0
# for i in s:
#     if i == i.upper():
#         d+=1
#     else:
#         t+=1
# if d>t:
#     print(s.upper())
# else:
#     print(s.lower())
# s1 = input().lower()
# s2 = input().lower()
# if s1 < s2:
#     print(-1)
# elif s1 > s2:
#     print(1)
# else:
#     print(0)
# class Dog:
#     def __init__(self,intro,name,age,breed,gender,colour,owner):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.gender = gender
#         self.colour = colour
#         self.owner = owner
#         print("i am initialized")
#     def introduce(self):
#         print(f"i am {self.name} and my age is {self.friend.name}")
#     def bark(self):
#         print("woof woof")
#     def Name(self):
#         return self.name
#     def Age(self):
#         return self.age
#     def Breed(self):
#         return self.breed
#     def Gender(self):
#         return self.gender
#     def color(self):
#         return self.colour
#     def Owner(self):
#         return self.owner

    
# bark = Dog("sahil",3,"notdefine","bisexual","Brown","Pommerian")
# print(bark.name)
# print(bark.age)
# print(bark.breed)
# print(bark.gender)
# print(bark.colour)
# print(bark.owner)
# t= int(input())
# for i in range(t):
#     n=int(input())
#     a=list(map(int,input().split()))
#     l,r=0,n-1
#     b=[]
#     for i in range(n):
#         if i%2==0:
#             b.append(a[l])
#             l+=1
#         else:
#             b.append(a[r])
#             r-=1
            
#     print(*b)
a=input().lower()
b=input().lower()
# d=a.split()
# c=b.split()
x=0
y=0
for i in a:
    x+=ord(i)
for j in b:
    y+=ord(j)
if x==y:
    print("0")
elif x>y:
    print("1")
else:
    print("-1")
