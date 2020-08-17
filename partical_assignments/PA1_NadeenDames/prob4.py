# Prob 4
# Come again the program to calculate number of count word in the statement if cout of word greater than or equals 2

stat=input("Enter Statement :")
list1=stat.split()
list1.sort()
list1.reverse()
unique_words=set(list1)
for word in unique_words:     
         if stat.count(word) >= 2 :
             print(f"The {word} : {stat.count(word)} counter")