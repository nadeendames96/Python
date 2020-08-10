# Prob 5
# Problem to print sequars 2.0 for numbers in the range start and end form user
# print("Enter Start And End Number :")

# From User
# start=int(input())
# end=int(input())

start=5
end=12
mult=[]
for i in range(start,end+1):
    mult.append(start**2)
    start+=1
    if start==end+1:
            break
print(mult)