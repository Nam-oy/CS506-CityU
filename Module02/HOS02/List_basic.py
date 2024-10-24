

list1 = ['physics', 'chemistry', 1997, 2000] #define list1
list2 = [1, 2, 3, 4, 5, 6, 7] #define list2
#accessing
print ("list1[0]: ", list1[0]) #show data inside list1 of position [0]
print ("list[1:5] ", list2[1:5]) #show data inside list2 starting from position1 to position4 (not including position5)
#updating
print ("Value available at index 2 : ")#show string
print (list1[2]) #show data in list1 at position 2
list1[2] = 2001 #set data in list1 at position 2 to 2001
print("New value available at index 2 : ") # show string
print(list1[2]) #show list1 position2 after the change

#Adding
list1.append(2020) #add data to the end of list1
print("New List: " ,list1) #show the updated list1

#Insert
list1.insert(0,'Python') #insert 'Python' at the position 0 in the list1
print("After inserting: ", list1) # show the update list

