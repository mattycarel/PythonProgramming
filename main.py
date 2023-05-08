# commentaire simple 

"""commentaire multiligne
"""
#par : 
#arg :
        
if __name__ == '__main__':
    
 
  students={
     "FirstName" : "Bizindavyi" ,
     "LastName" : "Joe Matty Carel" ,
     "Tel" : "+257 61 989 328" ,
     "email" : "joemattycarelb@gmail.com" ,
     "Address" : "Mutanga Nord"
  }    
 
  print("------affichages des cles---------")
 
  for s in students.keys():
     print(s)
     print("------affichages des valeurs---------")
  for v in students.values():
     print(v)
  
  print("------affichages des cles/valeurs---------")
  for i,v in students.items():
     print(f"{i} : {v}")
     
  print("------FINNN---------")
  
 
  

 
  