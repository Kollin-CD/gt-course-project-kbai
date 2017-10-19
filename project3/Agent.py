# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
import random
from PIL import Image

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        
        self.answer = "-1"
        

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        if problem.hasVerbal == True or "Challenge" in problem.name:
            return '-1'
        
        figureList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '1', '2', '3', '4', '5', '6', '7', '8']
        answers = ['1', '2', '3', '4', '5', '6', '7', '8']
        pDict= {}
        sz = 0
        for i in range(len(figureList)):
            figure = problem.figures[figureList[i]]
            image = Image.open(figure.visualFilename)
            pixel = image.load()
            pDict[figureList[i]] = pixel
        sz = image.size[0]
        
        #identical operations
        compare = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                   ['A', 'D', 'G', 'B', 'E', 'H', 'C', 'F'],
                   ['B', 'F', 'G', 'C', 'D', 'H', 'A', 'E'],
                   ['A', 'F', 'H', 'C', 'E', 'G', 'B', 'D']]
        for i in range(len(compare)):
            if self.identical(pDict[compare[i][0]], pDict[compare[i][1]], sz) and self.identical(pDict[compare[i][1]], pDict[compare[i][2]], sz):
                if self.identical(pDict[compare[i][3]], pDict[compare[i][4]], sz) and self.identical(pDict[compare[i][4]], pDict[compare[i][5]], sz):
                    update = []
                    
                    for j in range(len(answers)):
                        if self.identical(pDict[compare[i][6]], pDict[answers[j]], sz) and self.identical(pDict[compare[i][7]], pDict[answers[j]], sz):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0]
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        

        
                            
        #id_core operation
        compare2 = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                   ['A', 'D', 'G', 'B', 'E', 'H', 'C', 'F'],
                   ['B', 'F', 'G', 'C', 'D', 'H', 'A', 'E'],
                   ['C', 'D', 'H', 'A', 'H', 'E',  'A', 'E'],
                   ['A', 'F', 'H', 'C', 'E', 'G', 'B', 'D'],
                   ['C', 'E', 'G', 'A', 'H', 'F', 'B', 'D']]
        for n in range(40, 80, 5): 
            sc = (n, 184 - n)
            for i in range(len(compare2)):
                if self.id_core(pDict[compare2[i][0]], pDict[compare2[i][2]], sz, sc) and self.id_core(pDict[compare2[i][0]], pDict[compare2[i][1]], sz, sc):
                    if self.id_core(pDict[compare2[i][3]], pDict[compare2[i][5]], sz, sc):
                        update = []
                        
                        for j in range(len(answers)):
                            if self.id_core(pDict[compare2[i][6]], pDict[answers[j]], sz, sc) or self.id_core(pDict[compare2[i][7]], pDict[answers[j]], sz, sc):
                                update.append(answers[j])
                        if len(update) == 1:
                            print problem.name + " X.D. Sheldon's answer: " + update[0] 
                            return update[0]
                        elif len(update) > 1:
                            answers = update
                            

        #id_edge operation
        for n in range(10, 50, 5): 
            se = (n, 184 - n)
            for i in range(len(compare)):
                if self.id_edge(pDict[compare[i][0]], pDict[compare[i][1]], sz, se) and self.id_edge(pDict[compare[i][1]], pDict[compare[i][2]], sz, se):
                    if self.id_edge(pDict[compare[i][3]], pDict[compare[i][4]], sz, se) and self.id_edge(pDict[compare[i][4]], pDict[compare[i][5]], sz, se):
                        update = []
                        
                        for j in range(len(answers)):
                            if self.id_edge(pDict[compare[i][6]], pDict[answers[j]], sz, se) and self.id_edge(pDict[compare[i][7]], pDict[answers[j]], sz, se):
                                update.append(answers[j])
                        if len(update) == 1:
                            print problem.name + " X.D. Sheldon's answer: " + update[0] 
                            return update[0]
                        elif len(update) > 1:
                            answers = update
                            
        #pmerge operation 
        for i in range(len(compare)):
            if (self.pmerge(pDict[compare[i][0]], pDict[compare[i][1]], pDict[compare[i][2]], sz)
            or self.pmerge(pDict[compare[i][0]], pDict[compare[i][2]], pDict[compare[i][1]], sz)
            or self.pmerge(pDict[compare[i][1]], pDict[compare[i][2]], pDict[compare[i][0]], sz)):
                if (self.pmerge(pDict[compare[i][3]], pDict[compare[i][4]], pDict[compare[i][5]], sz)
                or self.pmerge(pDict[compare[i][3]], pDict[compare[i][5]], pDict[compare[i][4]], sz)
                or self.pmerge(pDict[compare[i][4]], pDict[compare[i][5]], pDict[compare[i][3]], sz)):
                    update = []
                   
                    for j in range(len(answers)):
                        if (self.pmerge(pDict[compare[i][6]], pDict[answers[j]], pDict[compare[i][7]], sz)
                        or self.pmerge(pDict[compare[i][6]], pDict[compare[i][7]], pDict[answers[j]],sz)
                        or self.pmerge(pDict[compare[i][7]], pDict[answers[j]], pDict[compare[i][6]], sz)):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0] 
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        

        #pmerge2 operation
        for i in range(len(compare)):
            if (self.pmerge2(pDict[compare[i][0]], pDict[compare[i][1]], pDict[compare[i][2]], sz)
            or self.pmerge2(pDict[compare[i][0]], pDict[compare[i][2]], pDict[compare[i][1]], sz)
            or self.pmerge2(pDict[compare[i][1]], pDict[compare[i][2]], pDict[compare[i][0]], sz)):
                if (self.pmerge2(pDict[compare[i][3]], pDict[compare[i][4]], pDict[compare[i][5]], sz)
                or self.pmerge2(pDict[compare[i][3]], pDict[compare[i][5]], pDict[compare[i][4]], sz)
                or self.pmerge2(pDict[compare[i][4]], pDict[compare[i][5]], pDict[compare[i][3]], sz)):
                    update = []
                    
                    for j in range(len(answers)):
                        if (self.pmerge2(pDict[compare[i][6]], pDict[answers[j]], pDict[compare[i][7]], sz)
                        or self.pmerge2(pDict[compare[i][7]], pDict[answers[j]], pDict[compare[i][6]], sz)
                        or self.pmerge2(pDict[compare[i][6]],  pDict[compare[i][7]], pDict[answers[j]], sz)):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0] 
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        



        #poverlap operation
        for i in range(len(compare)):
            if (self.poverlap(pDict[compare[i][0]], pDict[compare[i][1]], pDict[compare[i][2]], sz)
            or self.poverlap(pDict[compare[i][0]], pDict[compare[i][2]], pDict[compare[i][1]], sz)
            or self.poverlap(pDict[compare[i][1]], pDict[compare[i][2]], pDict[compare[i][0]], sz)):
                if (self.poverlap(pDict[compare[i][3]], pDict[compare[i][4]], pDict[compare[i][5]], sz)
                or self.poverlap(pDict[compare[i][3]], pDict[compare[i][5]], pDict[compare[i][4]], sz)
                or self.poverlap(pDict[compare[i][4]], pDict[compare[i][5]], pDict[compare[i][3]], sz)):
                    update = []
                    
                    for j in range(len(answers)):
                        if (self.poverlap(pDict[compare[i][6]], pDict[answers[j]], pDict[compare[i][7]], sz)
                        or self.poverlap(pDict[compare[i][7]], pDict[answers[j]], pDict[compare[i][6]], sz)
                        or self.poverlap(pDict[compare[i][6]], pDict[compare[i][7]], pDict[answers[j]], sz)):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0] 
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        
                       

                                
        #pincr operation
        for i in range(len(compare)):
            if (self.pincr(pDict[compare[i][0]], pDict[compare[i][1]], pDict[compare[i][2]], sz)
            or self.pincr(pDict[compare[i][0]], pDict[compare[i][2]], pDict[compare[i][1]], sz)
            or self.pincr(pDict[compare[i][1]], pDict[compare[i][0]], pDict[compare[i][2]], sz)):
                if (self.pincr(pDict[compare[i][3]], pDict[compare[i][4]], pDict[compare[i][5]], sz)
                or self.pincr(pDict[compare[i][3]], pDict[compare[i][5]], pDict[compare[i][4]], sz)
                or self.pincr(pDict[compare[i][4]], pDict[compare[i][3]], pDict[compare[i][5]], sz)):
                    update = []
                    
                    for j in range(len(answers)):
                        if (self.pincr(pDict[answers[j]], pDict[compare[i][6]], pDict[compare[i][7]], sz)
                        or self.pincr(pDict[answers[j]], pDict[compare[i][7]], pDict[compare[i][6]], sz)
                        or self.pincr(pDict[compare[i][6]], pDict[answers[j]], pDict[compare[i][7]], sz)):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0] 
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        

       
                        
        

        #up and down operation
        compare4 = [['A', 'C', 'B', 'C', 'D', 'F', 'E', 'F', 'G', 'H']]
        for i in range(len(compare4)):
            if self.id_up(pDict[compare4[i][0]], pDict[compare4[i][1]], sz) and self.id_down(pDict[compare4[i][2]], pDict[compare4[i][3]], sz):
                if self.id_up(pDict[compare4[i][4]], pDict[compare4[i][5]], sz) and self.id_down(pDict[compare4[i][6]], pDict[compare4[i][7]], sz):
                    update = []
                    
                    for j in range(len(answers)):
                        if self.id_up(pDict[compare4[i][8]], pDict[answers[j]], sz) and self.id_down(pDict[compare4[i][9]], pDict[answers[j]], sz):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0] 
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        

        #remove identical items
        update = []    
        for i in range(len(answers)):
            find = False
            for j in range(len(compare[0])):
                if self.identical(pDict[answers[i]], pDict[compare[0][j]], sz):
                    find = True
                    break
            if not find:
                update.append(answers[i])
        answers = update

        #padd operation
        for i in range(len(compare)):
            if (self.padd(pDict[compare[i][0]], pDict[compare[i][1]], pDict[compare[i][2]], sz)
            or self.padd(pDict[compare[i][0]], pDict[compare[i][2]], pDict[compare[i][1]], sz)
            or self.padd(pDict[compare[i][1]], pDict[compare[i][2]], pDict[compare[i][0]], sz)):
                if (self.padd(pDict[compare[i][3]], pDict[compare[i][4]], pDict[compare[i][5]], sz)
                or self.padd(pDict[compare[i][3]], pDict[compare[i][5]], pDict[compare[i][4]], sz)
                or self.padd(pDict[compare[i][4]], pDict[compare[i][5]], pDict[compare[i][3]], sz)):
                    update = []
                    
                    for j in range(len(answers)):
                        if (self.padd(pDict[compare[i][6]], pDict[answers[j]], pDict[compare[i][7]], sz)
                        or self.padd(pDict[compare[i][7]], pDict[answers[j]], pDict[compare[i][6]], sz)
                        or self.padd(pDict[compare[i][6]], pDict[compare[i][7]], pDict[answers[j]], sz)):
                            update.append(answers[j])
                    if len(update) == 1:
                        print problem.name + " X.D. Sheldon's answer: " + update[0] 
                        return update[0]
                    elif len(update) > 1:
                        answers = update
                        
                        
        if len(answers) > 0 and len(answers) < 3 :
            print problem.name + " X.D. Sheldon's answer: " + answers[0] 
            return answers[0]

        
        print problem.name + " X.D. Sheldon has No answer! "  
        return '-1'



                
    def findUL(self, pixel, sz):
        for i in range(0, sz):
            for j in range(0, sz):
                if pixel[i, j][0] < 10:
                    return (i, j)
        return (sz/2, sz/2)

    def findLR(self, pixel, sz):
        
        for i in range(sz-1, -1, -1):
            for j in range(sz-1, -1, -1):
                if pixel[i, j][0] < 10:
                    
                    return (i, j)
        return (sz/2, sz/2)

    def pnum(self, pixel, sz):
        pnum = 0
        for i in range(sz):
            for j in range(sz):
                if pixel[i, j][0] == 0:
                    pnum += 1
        return pnum
        
    def identical(self, pixel_1, pixel_2, sz):
        difs = 0
        
        sp1a = self.findUL(pixel_1, sz)
        sp1b = self.findLR(pixel_1, sz)
        sp2a = self.findUL(pixel_2, sz)
        sp2b = self.findLR(pixel_2, sz)
        dy = (sp2a[0] + sp2b[0] - sp1a[0] - sp1b[0]) /2
        dx = (sp2a[1] + sp2b[1] - sp1a[1] - sp1b[1]) /2

        for i in range(0, sz ):
            for j in range(0, sz):
                if i + dy < 0 or i + dy >= sz:
                    continue
                elif j + dx < 0 or j + dx >=sz:
                    continue
                elif pixel_1[i, j][0] != pixel_2[i + dy, j + dx][0]:
                    difs += 1
           
        
        if difs > 400:
            return False
        else:
            return True

    def id_core(self, pixel_1, pixel_2, sz, sc):
        difs = 0
        blank = True
            
        for i in range(sc[0], sc[1]):
            for j in range(sc[0], sc[1]):
                if pixel_1[i, j][0] == 0 or pixel_2[i, j][0] == 0:
                    blank = False
                if abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                    difs += 1
                
         
       
        if blank or difs > 500:
            return False
        
        else:
            return True
        
    def id_edge(self, pixel_1, pixel_2, sz, se):
        difs = 0
            
        for i in range(sz):
            for j in range(sz):
                if i > se[0] and i < se[1] and j > se[0] and j < se[1]:
                    continue
                elif abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                    difs += 1
                
         
        
        if difs > 400:
            return False
        
        else:
            return True

    def id_up(self, pixel_1, pixel_2, sz):
        difs = 0
            
        for i in range(0, sz/2):
            for j in range(0, sz):
                if abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                    difs += 1
                
         
        
        if difs > 1000:
            return False
        
        else:
            return True

    def id_down(self, pixel_1, pixel_2, sz):
        difs = 0
            
        for i in range(sz/2, sz):
            for j in range(0, sz):
                if abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                    difs += 1
                
         
        
        if difs > 1000:
            return False
        
        else:
            return True
        
    def pmerge(self, pixel_1, pixel_2, pixel_3, sz):
        difs = 0
        for i in range(sz):
            for j in range(sz):
                if pixel_3[i, j][0] < 5:
                    if (pixel_1[i, j][0] < 250 or pixel_2[i, j][0] < 250):
                        continue
                    difs += 1
                elif pixel_3[i, j][0] > 250:
                    if (pixel_1[i, j][0] < 5 or pixel_2[i, j][0] < 5):
                        difs += 1
        
        if difs > 500:
            return False
        
        else:
            return True                

    def pmerge2(self, pixel_1, pixel_2, pixel_3, sz):
        difs = 0
        for i in range(sz):
            for j in range(sz):
                if pixel_3[i, j][0] < 5:
                    if pixel_1[i, j][0] < 5 and pixel_2[i, j][0] < 5:
                        difs += 1

                    elif pixel_1[i, j][0] < 250 or pixel_2[i, j][0] < 250:
                        continue
                    else:
                        difs += 1
                elif pixel_3[i, j][0] > 250:
                    if pixel_1[i, j][0] < 5 and pixel_2[i, j][0] < 5:
                        continue
                    elif pixel_1[i, j][0] < 5 or pixel_2[i, j][0] < 5:
                        difs += 1
        
        if difs > 1100:
            return False
        
        else:
            return True  
    def poverlap(self, pixel_1, pixel_2, pixel_3, sz):
        difs = 0
        for i in range(sz):
            for j in range(sz):
                if pixel_3[i, j][0] < 5:
                    if (pixel_1[i, j][0] < 250 and pixel_2[i, j][0] < 250):
                        continue
                    difs += 1
                elif pixel_3[i, j][0] > 250:
                    if (pixel_1[i, j][0] < 5 and pixel_2[i, j][0] < 5):
                        difs += 1
        
        if difs > 500:
            return False
        
        else:
            return True  

    def padd(self, pixel_1, pixel_2, pixel_3, sz):
        p1num = self.pnum(pixel_1, sz)
        p2num = self.pnum(pixel_2, sz)
        p3num = self.pnum(pixel_3, sz)
        
        if abs(p3num - p1num - p2num) < 450:
            return True
        return False

    def pincr(self, pixel_1, pixel_2, pixel_3, sz):
        p1num = self.pnum(pixel_1, sz)
        p2num = self.pnum(pixel_2, sz)
        p3num = self.pnum(pixel_3, sz)
        
        if abs((p3num - p2num) - (p2num - p1num)) < 200 :
            return True
        return False           
                
                   
