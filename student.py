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
  
  class Personne :
      #constructeur
      def __init__(self,name,age):
          self.name = name
          self.age = age
          
      def __str__(self) -> str:
          return f"{self.name} ({self.age})"
      
      def showPerson(self) :
          print(self.name ,self.age)
          
    ##### la classe derivee
  class student(Personne) :
      s=Personne("Matty", 23)
      s.showPerson()
          
  

 
  