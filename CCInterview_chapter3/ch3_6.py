
# chapter 3 question 6



from ch3_SetUp import QueueNode, Queue
class PetQue(object):
    def __init__(self):
        self.DOG = Queue() 
        self.CAT = Queue()
        self.nextDOG = None
        self.nextCAT = None 

    def shelterpet(self, family, id):
        if family == 'canine':
            self.DOG.add(id)
        elif family == 'feline':
            self.CAT.add(id)
        else:
            message = "I'm sorry we only accept canine, or feline."
            print(message)

    def get_pet(self, family):
        default = "The shelter is empty, Hurray!"
        if family == 'canine':
            pet = self.DOG.remove()
            if pet == None:
                message = "I'm sorry but we don't have any puppers at the moment."
                print(message)
                return None
            else:
                return pet 
        elif family == 'feline':
            pet = self.CAT.remove() 
            if pet == None:
                message = "I'm sorry but we don't have any kitters at the moment."
                print(message)
                return None
            else:
                return pet
        elif family == 'any':
            pet1 = self.DOG.peek() 
            pet2 = self.CAT.peek() 
            if pet1 == None:
                if pet2 == None:                    
                    print(default)
                    return None 
                else:
                    newpet = self.CAT.remove()
                    return newpet
            if pet2 == None:
                if pet1 == None:
                    print(default)
                    return None
                else:
                    newpet = self.DOG.remove()
                    return newpet 
            if pet1 != None and pet2 != None:
                # for the comparison, the lower the id set, the older the 'time stamp'.
                if pet1 <= pet2:
                    newpet = self.DOG.remove() 
                    return newpet 
                else:
                    newpet = self.CAT.remove()
                    return newpet 
        else:
            message = f"I'm sorry but the requested pet: {family} is not available here. We have canine, feline or 'any' for either of those."
            print(message)
            return None



def getpet(shelter, selection):
    types = ['any', 'feline', 'canine']
    if selection in types:
        newpet = shelter.get_pet(selection)
        return newpet
    else:
        messsage = "The arguement options are: 'any', 'canine' or 'feline'. "
        print(message)

def test1():
    SHELTER = PetQue() 
    for id in range(20):
        if id % 2 == 0:
            SHELTER.shelterpet('canine', id)
        else:
            SHELTER.shelterpet('feline', id)

    for num in range(21):
        newpet = SHELTER.get_pet('any')
        print(newpet)

test1()