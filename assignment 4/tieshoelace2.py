from random import randint

class Eyelets(object):
    def __init__(self, name):
        self.name = name
        self.filled = False
 
def connect(eyelet1, eyelet2, initial):
    if initial == True:
        eyelet1.filled = True
        eyelet2.filled = True        
        print 'connects: ' + eyelet1.name + ' + ' + eyelet2.name
        return True
    elif eyelet1.filled == True:        
        eyelet2.filled = True        
        print 'connects: ' + eyelet1.name + ' + ' + eyelet2.name
        return True
    elif eyelet2.filled == True:
        eyelet1.filled = True     
        print 'connects: ' + eyelet2.name + ' + ' + eyelet1.name
        return True
    else:        
        return False

def tieShoelace(style):
    #create Eyelets objects and stored in a dict: {name: eyelet}
    eyelets = {}
    for i in range(len(style)):
        for j in range(len(style[0])):
            eyelets[style[i][j]] = Eyelets(style[i][j])
    
    #create list of tuples of Eyelets objects
    goal =[]
    for i in range(len(style)):
        goal.append((eyelets[style[i][0]], eyelets[style[i][1]]))

    print 'The style is: ', style, '\n'
    print "My robot's plan: "
    print '------------------'
    #randomly pick the initial step
    init = randint(0, len(goal) - 1)
    connect(goal[init][0], goal[init][1], True)
    goal.pop(init)
    
    while len(goal) > 0:
        temp = []
        for i in range(len(goal)):            
            op = connect(goal[i][0], goal[i][1], False)
            if op != True:
                temp.append(goal[i])
        goal = temp
    print '------------------'    


 
style1 = [('a', 'd'), ('b', 'c'), ('c', 'd')]
style2 = [('a', 'd'), ('b', 'c'), ('e', 'd'), ('c', 'f'), ('e', 'f')]
style3 = [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'f'), ('e', 'f'), ('e', 'h'), ('g', 'j'), ('i', 'j'), ('i', 'l'), ('k', 'l'), ('k', 'n'), ('m', 'n'), ('m', 'b')]

tieShoelace(style1)
tieShoelace(style2)
tieShoelace(style3)

