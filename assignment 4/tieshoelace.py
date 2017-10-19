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
    copy = []
    for i in range(len(style)):
        copy.append(style[i])    
    connect(copy[0][0], copy[0][1], True)
    copy.pop(0)
    while len(copy) > 0:
        temp = []
        for i in range(len(copy)):            
            op = connect(copy[i][0], copy[i][1], False)
            if op != True:
                temp.append(copy[i])
        copy = temp
        

a = Eyelets('a')
b = Eyelets('b')
c = Eyelets('c')
d = Eyelets('d')
e = Eyelets('e')
f = Eyelets('f')
g = Eyelets('g')
h = Eyelets('h')
i = Eyelets('i')
j = Eyelets('j')
k = Eyelets('k')
l = Eyelets('l')
m = Eyelets('m')
n = Eyelets('n')

style = [(a, b), (a, d), (c, d), (c, f), (e, f), (e, h), (g, j), (i, j), (i, l), (k, l), (k, n), (m, n), (m, b)]

tieShoelace(style)


