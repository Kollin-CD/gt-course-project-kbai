import random

class Atom(object):
    def __init__(self, name, element):
        valence = {'C':4, 'H':1}
        self.name = name
        self.val = valence[element]   #total valences
        self.lval = valence[element]  #open valences
        self.adjacent = []
    def __repr__(self):
        return self.name
    
def connect(atom1, atom2):
    if atom1.lval == 0 or atom2.lval == 0:
        return False
    else:
        atom1.lval -= 1
        atom1.adjacent.append(atom2)
        atom2.lval -= 1
        atom2.adjacent.append(atom1)
        return True

def hydrocarbon(formula):  # formula = {'C':4, 'H':10}
    carbonList = []   
    hydrogenList = []
    molecule = []
    
    #transfer formula into lists of carbon/hydrogen atoms
    for i in range(formula['C']):
        carbonList.append(Atom('C'+str(i+1), 'C'))
    for j in range(formula['H']):
        hydrogenList.append(Atom('H'+str(j+1), 'H'))

    #molecule start with one carbon atom
    molecule.append(carbonList[0])

    #connect carbons in molecule in a random order
    for i in range(1, len(carbonList)):
        switch = True
        while switch:
            if connect(carbonList[i], random.choice(molecule)):
                molecule.append(carbonList[i])
                switch = False

    #calculate total open valences
    lv_sum = 0
    for carbon in molecule:
        lv_sum += carbon.lval

    while True:
        if lv_sum < len(hydrogenList):
            print '------------------------------------------'
            print 'No structure fits formula: ' + 'C' + str(formula['C']) + 'H' + str(formula['H'])
            return None
        elif lv_sum > len(hydrogenList):
            r1 = random.randint(0, len(molecule)-1)
            r2 = random.randint(0, len(molecule)-1)
            if r1 != r2:
                if connect(molecule[r1],molecule[r2]):
                    lv_sum -= 2
        else:
            #connect hydrogen in molecules
            for hydrogen in hydrogenList:
                for carbon in molecule:
                    if connect(hydrogen, carbon):
                        break 
    
            #print connections between carbon and hydrogen
            print '------------------------------------------'
            print 'There is a structure fits formula: ' + 'C' + str(formula['C']) + 'H' + str(formula['H'])
            for carbon in molecule:
                print carbon.name, ' connects: ', carbon.adjacent
            return None

formula1 = {'C':4, 'H':10}
formula2 = {'C':6, 'H':6}
formula3 = {'C':2, 'H':4}
formula4 = {'C':2, 'H':2}
formula5 = {'C':2, 'H':3}
hydrocarbon(formula1)
hydrocarbon(formula2)
hydrocarbon(formula3)
hydrocarbon(formula4)
hydrocarbon(formula5)
            
