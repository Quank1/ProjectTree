class Peopls:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []
        self.parents = []
        self.spouses = []

    def AppendSpouses(self, spouse):
        if spouse is not self.spouses:
            self.spouses.append(spouse)

    def AppendChild(self, child):
        if child is not self.children:
            self.children.append(child)

    def AppendParent(self, parent):
        if parent is not self.parents:
            self.parents.append(parent)

    def GetChild(self):
        return self.children
    
    def GetParent(self):
        return self.parents
    
    def GetPeople(self):
        return f"{self.name} | {self.age}"
        
    
class Tree:
    def __init__(self):
        self.AllPerson = []

    def FindPers(self, person):
        for person1 in self.AllPerson:
            if person1.lower() == person.lower():
                return True
            else:
                return False
            

    def AppendPerson(self, person):
        self.AllPerson.append(person)

    def PrintFamalyTree(self):
        for i in self.AllPerson:
            print(i)

def FindPerson(person):
    if FindPerson(person) == True:
        print("Есть")
    else:
        print("Нету")





FirstPerson = Peopls("Righard", 27)
SecondPerson = Peopls("Lev", 12)
ThirdPerson = Peopls("Svitlana", 26)

FirstPerson.AppendChild(SecondPerson.GetPeople())
FirstPerson.AppendSpouses(ThirdPerson.GetPeople())
SecondPerson.AppendParent(FirstPerson.GetPeople())
SecondPerson.AppendParent(ThirdPerson.GetPeople())
ThirdPerson.AppendChild(SecondPerson.GetPeople())
ThirdPerson.AppendSpouses(FirstPerson.GetPeople())

famaly = Tree()

famaly.AppendPerson(FirstPerson.GetPeople())
famaly.AppendPerson(SecondPerson.GetPeople())
famaly.AppendPerson(ThirdPerson.GetPeople())

famaly.PrintFamalyTree()

