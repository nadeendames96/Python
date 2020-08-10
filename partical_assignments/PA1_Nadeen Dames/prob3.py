# # Prob 3
# # Mars Rover 
x=0
y=0

# Define Tuple and add x,y to position variable 
position=()
print("Enter dicoration and value  of dicoration : ")
dic=" "
dic_value=" "
for i in range(1,7):
     dic,dic_value=input().split()
#dic_value=int(input())
     if(dic=="U"):
          y+=int(dic_value)
          position=(x,y)   
     if(dic=="R"):
               x+=int(dic_value)
               position=(x,y)   
     if(dic=="L"):
          x=abs(x-int(dic_value))
          position=(x,y)   
     if(dic=="lo"):
          y=abs(y-int(dic_value))  
          position=(x,y)      
          
print(f"Current position: {position}"),
