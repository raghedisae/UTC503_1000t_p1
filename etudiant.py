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
        data.ajouterEtudiant(self)    
    
    def set_niveau(self, value):
      if value not in ('A', 'B', 'C'):
         raise ValueError()
      self.niveau = value
    
    def edit_etudiant(self,nom,prenom,niveau):
        self.nom =nom
        self.prenom = prenom
        self.set_niveau(niveau)
    
    def __repr__(self):
        return ("numero:"+self.numero+"\tnom:"+self.nom+"\tprenom:"+self.prenom+"\tniveau: "+self.niveau)
    

class cours(object):
    
    def __init__(self,code,intitule,niveau):
        self.code = code
        self.intitule = intitule
        self.set_niveau(niveau)
        data.ajouterCours(self)
        
    def set_niveau(self, value):
      if value not in ('A', 'B', 'C'):
         raise ValueError()
      self.niveau = value
      
    def edit_cours(self,intitule,niveau):
        self.intitule=intitule
        self.set_niveau(niveau)
    
    def __repr__(self):
        return ("code:"+self.code+"\tintitule:"+self.intitule+"\tniveau: "+self.niveau)

class note(object):
    
    def __init__(self,numEtudiant,codeCours,note):
        try:
            numEtudiant
            codeCours
        except ValueError:
            print("Course mark should be between 0 and 100")
        else:    
            self.numEtudiant = numEtudiant
            self.codeCours = codeCours
            self.setNote(note)
            data.ajouterNote(self)
            
    def setNote(self, value):
      if value <0 or value >100:
         raise ValueError()
      self.note = value
      
    def __repr__(self):
        return ("cours:"+self.codeCours+"\tEtudiant:"+self.numEtudiant+"\tnote: "+str(self.note))

class BD(object):
    
    def __init__(self):    
        self.listEtudiant=[]
        self.listCours=[]
        self.listNotes=[]
    
    def ajouterEtudiant(self,e):
        self.listEtudiant.append(e)
    
    def supprimerEtudiant(self,num):
        for x in self.listEtudiant:
            if x.numero == num :
               self.listEtudiant.remove(x)
               print("etudiant ",num," has been deleted")
            break
        
    def ajouterNote(self,n):
        self.listNotes.append(n)
    
    def supprimerNote(self,e,c):
        for x in self.listNotes:
            if x.numEtudiant == e and x.codeCours==c :
               self.listNotes.remove(x)
               print("note  etudiant ",e," en cours ",c," has been deleted")
            break
    
    def ajouterCours(self,c):
        self.listCours.append(c)
    
    def supprimerCours(self,num):
        for x in self.listCours:
            if x.code == num :
               self.listCours.remove(x)
               print("cours ",num," has been deleted")
            break
    
    def moyenne_classe(self,c):
        n_sum= 0
        n_count= 0
        for n in self.listNotes:
            if n.codeCours == c:
                n_sum+= n.note
                n_count+=1
        return (n_sum/n_count)
    
    def moyenne_etudiant(self,e):
        n_sum= 0
        n_count= 0
        for n in self.listNotes:
            if n.numEtudiant == e:
                n_sum+= n.note
                n_count+=1
        return (n_sum/n_count)
    
    def consulter_classnote(self,c):
        print("notes class: ",c.code)
        print("-----------------------")
        print("Etudiant \tNote")
        print("-----------------------")
        for n in self.listNotes:
            if n.codeCours == c.code:
                print(n.numEtudiant,"\t",n.note)
    
    def consulter_etudianNote(self,e):
        print("notes Etudiant: ",e.numero)
        print("-----------------------")
        print("Cours \tNote")
        print("-----------------------")
        for n in self.listNotes:
            if n.numEtudiant == e.numero:
                print(n.codeCours,"\t",n.note)
    
    
    
    def __repr__(self):
        
            print (self.listEtudiant)
    
data=BD()
e1 = etudiant("1000","raghed","idris","A")
e2 = etudiant("1001","sami","sam","B")

print(e1)
print(e2)

c1=cours("GDN100","Projet INformatique","A")
c2=cours("UTC503","Paradigme","B")
print(c1)

note_e1=note(e1.numero,c1.code,100)
note_e1=note(e1.numero,c2.code,80)
note_e2=note(e2.numero,c1.code,91)
note_e2=note(e2.numero,c2.code,95)

print(note_e1)
print(note_e2)

print("--------")
print("lists before deletion")
print(data.listNotes)
print(data.listEtudiant)
print(data.listCours)

print("--------")
print("moyenne class ",c1.code,":", data.moyenne_classe(c1.code))
print("moyenne etudiant ",e1.numero,":", data.moyenne_etudiant(e1.numero))
print("--------")

data.consulter_classnote(c2)
print("--------")
data.consulter_etudianNote(e1)


print("--------SupprimerNote---------------")
#use studient ID
data.supprimerEtudiant("1000")

data.supprimerNote("1000","GDN100")



print("--------")
print("lists after deletion")
print(data.listNotes)
print(data.listEtudiant)
print(data.listCours)
#print(data)