#Collection data types.
#List is between the [].
Examples:-
1] x=["red","blue","green","yellow","black"]
   print(x)
   
 Output:
  ['red','blue','green','yellow','black']
  
#Can also add another data types like,
#Numbers inside the list.
2] x=["red","blue","green","yellow","black",3]
   print(x)
   
 Output:
  ['red','blue','green','yellow','black',3]

  
  #Can also store floating point values like,
  #4.3..etc,..
  3] x=["red","blue","green","yellow","black",3,4.3]
     print(x)
   
 Output:
  ['red','blue','green','yellow','black',3,4.3]
  
  #To know the various methods in list.Use,
    dir(list)
  #Will get lists.
  
  #ACCESSING THE ELEMENTS IN A LIST.
   1] x=["red","blue","green","yellow","black",3,4.3]
      x[2]
      print(x)
      
  Output:
   'green'
   
   2] x=["red","blue","green","yellow","black",3,4.3]
      x[-2]
      print(x)
      
  Output:
   3
   
   3] x=["red","blue","green","yellow","black",3,4.3]
      x[-1]
      print(x)
      
  Output:
   4.3
   
 #If need to find the length of the list,then
 1] x=["red","blue","green","yellow","black",3,4.3]
    len(x)
    
 Output:
   7
   
#Addition and removal of some elements in the list, then
#Removing elements from the list from last,then
1] x=["red","blue","green","yellow","black",3,4.3]
      x.pop(4.3)
      print(x)
      
  Output:
   ['red','blue','green','yellow','black',3]
   #4.3 is removed.
   
   #If we want to add the element to last,then
   1] x=["red","blue","green","yellow","black",3,4.3]
      x.append(9)
      print(x)
      
   Output:
     ['red','blue','green','yellow','black',3,9]
   
   #If we want to remove in middle,like
    1] x=["red","blue","green","yellow","black",3,4.3]
      x.remove("yellow")
      print(x)
      
   Output:
     ['red','blue','green','black',3,9]
     
   #If we want to delete / delete the whole list,then
    1] x=["red","blue","green","yellow","black",3,4.3]
       del x
      print(x)
      
  Output:
    (Nothing)
   
   
   
   
  
  
   
  
  
  

  
