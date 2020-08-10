
# prob 1
# The problem will be print after coma in pi [( , )] tuple insde list  
pi = "3.14159265"
after_coma=pi[2:10]
#print(after_coma)
print("After Print Is Equals :")
print("[",end=" ")
for i in  range(len(after_coma)):
     print("(",i,",",after_coma[i],") , ",end=" ")

print("]")

# Nadeen Dames


# Another soluation using enumariteds fnction
#while using enumarite function
#def pi_find(pi):
 #   after_coma=pi[2:10]
  #  for i,v in enumerate(after_coma):
   #     print(i,v),

#pi_find("3.14159265")        
    