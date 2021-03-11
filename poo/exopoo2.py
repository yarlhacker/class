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
    
    def __init__(self,nom,sexe,adresses):
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



class ListePersonnes:
    def __init__(self,personne):
        self.personne = personne

    @property
    def personne(self):
        return self.__personne
    
    @personne.setter
    def personne(self,a):
        self.__personne = a
    
    def __str__(self):
        return self.personne

    def find_by_nom(self,s:str):
        if self.personne[0] == s:
            return self.personne[0]
        else:
            print('null')





p1 =Personne('ismael','M',545416)

print(p1.sexe)
