**Format:- arranging things in a port.**
Like,

1] x="is"
   y="my"
   z="name"
   c=y+x+z
   print(c)
 
 Output:
  mynameis
                           [or]
                           
   x="is"
   y="my"
   z="name"
   c=y+" "+x+" "+z
   print(c)
   
Output:
  my name is
 
 ** 2 METHODS.**
 
 METHOD 1:- 
 -----------  
 1] x='my name is"
    z="alex"
    y="my name is {}".format(z)
    print(y)
    
Output:
  my name is alex
  
 2] can also use this way..
      
      x="my name is"
      z="alex"
      y="my name is"+z
      print(y)
      
   Output:
    my name is alex
3] x=34
   y="alex"
   z="my name is {} and my age is {}".format(y,z)
   print(z)
   
Output:
  my name is alex and my age is 34
  
4] x=34
   y="alex"
   z="my name is {1} and my age is {0}".format(x,y)
   print(z)
 
 Output:
   my name is alex and my age is 34
#if 3 inputs then use index {2}.

METHOD 2:-
--------- 
1] x="alex"
   y=f"my name is {x}"
   print(y)
   
Output:
  my name is alex
  
 2] x="alex"
    y="33"
    z=f"my name is {x} and my age is {y}"
    print(z) 

Output:
  my name is alex and my age is 33
  
  4] #if we have,
       x={"dev","sports","34"}
     #we need to use indexing
       z=f"my name is {x[0]} and my hobbie is playing {x[1]}and my age is {x[2]}"
       print(z)
     
  Output:
    my name is dev and my hobbie is playing sports and my age is 34.
  
  
  
  
  
  
  
  
  
  
  
  
  
 
  
  
  
  
  
    
