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
        
        objectLists = {} # {figureName : [list of RavenObject]}
        for figureName in problem.figures:
            thisFigure = problem.figures[figureName]
            thisFigureObjectList = []
            for objectName in thisFigure.objects:
                thisFigureObjectList.append(thisFigure.objects[objectName])
            objectLists[figureName] = thisFigureObjectList
        
        maxObj = 0
        for figureName in objectLists:
            if len(objectLists[figureName]) > maxObj:
                maxObj = len(objectLists[figureName])
                
        for figureName in objectLists:        
            while len(objectLists[figureName]) < maxObj:
                objectLists[figureName].append(None)
                
        compares = [["A", "B", "C"], ["A", "C", "B"], ["B", "C", "A"]]
        answers = [ "1", "2", "3", "4", "5", "6"] 
        
        n = 0
        
        while n < 3:
            scoreList = self.pairUp(objectLists[compares[n][0]], objectLists[compares[n][1]])
            
            scoreListOfProducts = []
            for i in range(len(answers)):
                scoreListOfProducts.append(self.pairUp(objectLists[compares[n][2]], objectLists[answers[i]]))
        
            diffList = []
            indexList = []
            for i in range(len(answers)):
                diff = 0
                for j in range(maxObj):
                    diff += (scoreListOfProducts[i][j] - scoreList[j])**2
                
                diffList.append(diff) 
                 
             
            diffMin = min(diffList)     
            for i in range(len(answers)):
                if diffList[i] == diffMin:
                    indexList.append(answers[i])       
            
            
            if len(indexList) == 1:
                return indexList[0]
            answers = indexList
            n += 1
                
        return self.answer
        
        
        
        

        
    def Operation(self, obj1, obj2):
        if obj1 == None and obj2 == None:
            return 5
            
        if obj2 == None:
            return 1   
              
        if obj1 == None:
            return 0
            
        score = 5
        rotated = False
        if ("shape" in obj1.attributes) and ("shape" in obj2.attributes) and (obj1.attributes["shape"] != obj2.attributes["shape"]):
            return 0
        if ("angle" in obj1.attributes) and ("angle" in obj2.attributes) and (obj1.attributes["angle"] != obj2.attributes["angle"]):
            if  (int(obj1.attributes["angle"]) - int(obj2.attributes["angle"])) % 180 == 0:
                rotated = True
                score -= 1
            elif  (int(obj1.attributes["angle"]) - int(obj2.attributes["angle"])) % 90 == 0:
                rotated = True
                score -= 1.5
            else:
                rotated = True
                score -= 2
        if ("alignment" in obj1.attributes) and ("alignment" in obj2.attributes) and (obj1.attributes["alignment"] != obj2.attributes["alignment"]):
            if  obj1.attributes["alignment"][0] == obj2.attributes["alignment"][0] and not rotated:
                score -= 1.5
            elif obj1.attributes["alignment"][-2] == obj2.attributes["alignment"][-2] and not rotated:
                score -= 1.5
            elif not rotated:
                score -= 1
        if ("size" in obj1.attributes) and ("size" in obj2.attributes) and (obj1.attributes["size"] != obj2.attributes["size"]):
            score -= 3
            
        if ("fill" in obj1.attributes) and ("fill" in obj2.attributes) and (obj1.attributes["fill"] != obj2.attributes["fill"]):
            score -= 4
        
        if score >= 0:
            return score
        else:
            return 0
            
    def pairUp(self, A, B):  # A, B are two list of objects with same length
        scoreList = []   # a list to store operation scores between A and B
        tempB = []           # a copy of B
        tempA = []           #temp list to store A objects that not identical to B
        tempLen = len(A)
        
        for i in range(tempLen):
            tempB.append(B[i])
            
        # the following loop find identical objects between A and B
        # identified B objects store in tempList
        # unidentified A objects store in tempA 
        for i in range(tempLen):
            find = False
            for j in range(tempLen):
                if self.Operation(A[i], tempB[j]) == 5:
                    find = True
                    break
            if find:
                scoreList.append(5)
                tempB.pop(j)
                tempLen -= 1
            else:
                tempA.append(A[i])
        
        # the following loop compute operateions between AB objects
        # objects in tempA will look its pair objects in B based on max score
        for i in range(tempLen):
            tempScore = -100
            tempIndex = 0
            
            for j in range(tempLen):
                score = self.Operation(tempA[i], tempB[j])
                if score > tempScore:
                    tempScore = score
                    tempIndex = j
            scoreList.append(tempScore)
            tempB.pop(tempIndex)
            tempLen -= 1
                     
        scoreList.sort()    # keep operation score in order
        
        return scoreList