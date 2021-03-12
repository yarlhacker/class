class Adresse: 
    def __init__(self,rue,ville,code_postale):
        self.rue = rue
        self.ville = ville
        self.code_postale = code_postale
    
    @property
    def rue(self):
        return self.__rue
    
    @property
    def ville(self):
        return self.__ville

    @property
    def code_postale(self):
        return self.__code_postale

    @rue.setter
    def rue(self,a):
        self.__rue=a
    
    @ville.setter
    def ville(self,a):
        self.__ville=a
    
    @code_postale.setter
    def code_postale(self,a):
        self.__code_postale=a
    
    def __str__(self):
        return f'{self.rue} {self.ville} {self.code_postale}'

class Personne:
    
    def __init__(self,nom,sexe,adresses = []):
        self.nom = nom
        self.sexe = sexe
        self.adresses = adresses
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def sexe(self):
        return self.__sexe
    
    @property
    def adresses(self):
        return self.__adresses
    
    @nom.setter
    def nom(self,b):
        self.__nom = b
    
    @sexe.setter
    def sexe(self,b):
        self.__sexe = b
    
    @adresses.setter
    def adresses(self,b):
        self.__adresses = b
    
    def __getitem__(self,index):
        return self.adresses[index]
    
    def __setitem__(self,index,value):
        self.adresses[index]=value

    def __delitem__(self,index):
        del self.adresses[index]

    def __str__(self):
        return f'{self.nom} {self.sexe}'


class ListePersonnes:
    def __init__(self,personnes = []):
        self.personnes = personnes

    @property
    def personnes(self):
        return self.__personnes
    
    @personnes.setter
    def personnes(self,a):
        self.__personnes = a


    def find_by_nom(self,s:str):
        for personne in self.personnes:
            if personne.nom == s:
                return personne 
    def exists_code_postale(self,cp):
        for personne in self.personnes:
            for adresse in personne.adresses:
                if adresse.code_postale == cp:
                    return True
        return False 
    
    def count_personne_ville(self,ville):
        nombre_personne = 0
        for personne in self.personnes:
            for adresse in personne.adresses:
                if adresse.ville == ville:
                    nombre_personne+=1
                    break
            continue
    
    def edit_personne_ville(self,oldnom,newville):
        for personne in self.personnes:
            if personne.nom == oldnom:
                personne.nom = newville #personne.nom.replace(oldnom,newville)
    
    def edit_personne_ville(self,nom,newville):
        for personne in self.personnes:
            for adresse in personne.adresses:
                if nom == adresse.ville:
                    adresse.ville = newville 
    def __getitem__(self,index):
        return self.personnes[index]
    
    def __setitem__(self,index,value):
        self.personnes[index]=value

    def __delitem__(self,index):
        del self.personnes[index]
        

    def __str__(self):
        return str(self.personnes)
        
    

p1 = Personne('ismael','M')
p2 = Personne('aziz','F')
lp1 = ListePersonnes([p1,p2])

print(lp1[0])
lp1[0] = p2
del lp1[0]


