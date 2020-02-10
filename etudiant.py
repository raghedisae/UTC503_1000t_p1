# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:35:36 2020

@author: raghed
"""

class etudiant(object):
    
    def __init__(self,numero,prenom,nom,niveau):
        self.numero = numero
        self.prenom = prenom
        self.nom = nom
        self.set_niveau(niveau)
    
    def set_niveau(self, value):
      if value not in ('A', 'B', 'C'):
         raise ValueError()
      self.niveau = value
    
    def __repr__(self):
        return ("numero:"+self.numero+"\tnom:"+self.nom+"\tprenom:"+self.prenom+"\tniveau: "+self.niveau)
    

class cours(object):
    
    def __init__(self,code,intitule,niveau):
        self.code = code
        self.intitule = intitule
        self.set_niveau(niveau)
    
    def set_niveau(self, value):
      if value not in ('A', 'B', 'C'):
         raise ValueError()
      self.niveau = value
    
    def __repr__(self):
        return ("code:"+self.code+"\tintitule:"+self.intitule+"\tniveau: "+self.niveau)

class note(object):
    
    def __init__(self,numEtudiant,codeCours,note):
        self.numEtudiant = numEtudiant
        self.codeCours = codeCours
        self.setNote(note)
    
    def setNote(self, value):
      if value <0 or value >100:
         raise ValueError()
      self.note = value
      
    def __repr__(self):
        return ("cours:"+self.codeCours+"\tEtudiant:"+self.numEtudiant+"\tnote: "+str(self.note))



e1 = etudiant("1000","raghed","idris","A")
e2 = etudiant("1001","sami","sam","B")
print(e1)
print(e2)

c1=cours("GDN100","Projet INformatique","A")
print(c1)

note_e1=note(e1.numero,c1.code,100)
note_e2=note(e2.numero,c1.code,90)

print(note_e1)
print(note_e2)
