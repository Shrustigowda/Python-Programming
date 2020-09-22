*In dictionaries we have the curly brackets {},like  x={}.
*Dictionaries can be manipulated.
*In dictionaries we define indexing in terms with particular names as we call it as 'keys'.

x={"numbers":1,"name":"blue","age":200}
#Here "numbers"--> key
#and : --> to define the value in key.

#And to access any element.

1] x={"numbers":1,"name":"blue","age":200}
   x["name"]
 
 Output:
   'blue'
   
 2]  x={"numbers":1,"name":"blue","age":200}
     x["age"]
 
 Output:
   200
   
 3] #If need to change element then,
      x={"numbers":1,"name":"blue","age":200}
      x["age"]=300
      print(x)
 
 Output:
   {'numbers':1,'name':'blue','age':300}
   
  4]  #If need to change element then,
      x={"numbers":1,"name":"blue","age":200}
      x["name"]=alex
      print(x)
 
 Output:
   {'numbers':1,'name':'alex','age':300}
   
5] #Need to know length,then  
    x={"numbers":1,"name":"blue","age":300}
    len(x)
    
  Output:
    3
 *Here we have 6 things ,but only 3 we get bcoz 3 are indexes(keys).
 
 
 **ADDING DICTIONARIES**
    x={"numbers":1,"name":"blue","age":300}
    x["year"]=2019
   #we need to add a key while adding a new element.
    print(x)
   
Output:
   {'numbers':1,'name':'blue','age':300,'year':2019}
   
 #If need to remove element from dictionaries ,then 
    x={"numbers":1,"name":"blue","age":300}
    x.pop("age")
   #make sure to pass the parameters.
    print(x)
    
 Output:
   {'numbers':1,'name':'blue'}
   
   
   
  
   
     

      
