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
        
         
        
                
        pType = problem.problemType
        
        if pType == "2x2":
            compares = [["A", "B", "C"], ["A", "C", "B"], ["B", "C", "A"]]
            answers = [ "1", "2", "3", "4", "5", "6"] 
            cycle = 3
        elif pType == "3x3":
            compares = [["A", "C", "G"], ["A", "G", "C"], ["C", "G", "A"], ["D", "F", "G"], ["D", "G", "F"], ["B", "C", "H"], ["B", "H", "C"], ["E", "F", "H"], ["E", "H", "F"], ["A", "H", "B"], ["B", "G", "A"], ["D", "H", "E"], ["E", "G", "D"] ]
            answers = [ "1", "2", "3", "4", "5", "6", "7", "8"] 
            cycle = 13
        
        n = 0
        #print "*******************************************************************************"
        while n < cycle:
            score = self.pairUp(objectLists[compares[n][0]], objectLists[compares[n][1]])
            #print score
            scoreList = []
            for i in range(len(answers)):
                scoreList.append(self.pairUp(objectLists[compares[n][2]], objectLists[answers[i]]))
            #print scoreList
            
            matchList = []
            for i in range(len(scoreList)):
                if len(scoreList[i]) != len(score):
                    continue

                for j in range(len(scoreList[i])):
                    if abs(scoreList[i][j] - score[j]) < 0.00001:
                        matchList.append(answers[i])
                        break
                
            
            if len(matchList) == 1:
                return matchList[0]
            if len(matchList) > 1:
                answers = matchList
            #print answers
            #print"************************"
            
            n += 1

        if self.answer == "-1":
            n = 0
            
            #print ' ---------------------------------------------------------------------------------------------------------'
            while n < cycle:
                score = self.pairUpL(objectLists[compares[n][0]], objectLists[compares[n][1]])
                #print score
                scoreList = []
                for i in range(len(answers)):
                    scoreList.append(self.pairUpL(objectLists[compares[n][2]], objectLists[answers[i]]))
                #print scoreList
            
                matchList = []
                for i in range(len(scoreList)):
                    if len(scoreList[i]) != len(score):
                        continue

                    for j in range(len(scoreList[i])):
                        if abs(scoreList[i][j] - score[j]) < 0.0001:
                            matchList.append(answers[i])
                            break
                
            
                if len(matchList) == 1:
                    return matchList[0]
                if len(matchList) > 1:
                    answers = matchList
            
                #print answers
                #print '--------------------------------'
                n += 1

        return self.answer
        
        
        
        

        
    def Operation(self, obj1, obj2):
                    
        if obj1 == None or obj2 == None:
            return 1
              
               
        score = 5
        rotated = False
        
        if ("shape" in obj1.attributes) and ("shape" in obj2.attributes) and (obj1.attributes["shape"] != obj2.attributes["shape"]):
            if obj1.attributes["shape"] in ["square", "rectangle"] and obj2.attributes["shape"] in ["square", "rectangle"]:
                score = 4
            else:
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
        if ("size" in obj1.attributes or ("width" in obj1.attributes and "height" in obj1.attributes)) and ("size" in obj2.attributes or ("width" in obj2.attributes and "height" in obj2.attributes)) :
            sizeList = ["very small", "small", "medium", "large", "very large", "huge"]
            
            if ("size" in obj1.attributes) and ("size" in obj2.attributes):
                sa = 0
                sb = 0
                for i in range(len(sizeList)):
                    if obj1.attributes["size"][0] == sizeList[i][0] and obj1.attributes["size"][-1] == sizeList[i][-1]:
                        sa = i
                    if obj2.attributes["size"][0] == sizeList[i][0] and obj2.attributes["size"][-1] == sizeList[i][-1]:
                        sb = i
                score -= (sa - sb) * 0.4
            elif ("size" in obj1.attributes) and not ("size" in obj2.attributes):
                si = 0
                sw = 0
                sh = 0
                for i in range(len(sizeList)):
                    if obj1.attributes["size"][0] == sizeList[i][0] and obj1.attributes["size"][-1] == sizeList[i][-1]:
                        si = i
                    if obj2.attributes["width"][0] == sizeList[i][0] and obj2.attributes["width"][-1] == sizeList[i][-1]:
                        sw = i
                    if obj2.attributes["height"][0] == sizeList[i][0] and obj2.attributes["height"][-1] == sizeList[i][-1]:
                        sh = i
                score -= ((si - sw)  + (si - sh) * 1.1) * 0.2
            elif not ("size" in obj1.attributes) and ("size" in obj2.attributes):
                si = 0
                sw = 0
                sh = 0
                for i in range(len(sizeList)):
                    if obj2.attributes["size"][0] == sizeList[i][0] and obj2.attributes["size"][-1] == sizeList[i][-1]:
                        si = i
                    if obj1.attributes["width"][0] == sizeList[i][0] and obj1.attributes["width"][-1] == sizeList[i][-1]:
                        sw = i
                    if obj1.attributes["height"][0] == sizeList[i][0] and obj1.attributes["height"][-1] == sizeList[i][-1]:
                        sh = i
                score -= ((sw - si)  + (sh - si) * 1.1) * 0.2
            else:
                sw = 0
                sh = 0
                sw2 = 0
                sh2 = 0
                for i in range(len(sizeList)):
                    if obj1.attributes["width"][0] == sizeList[i][0] and obj1.attributes["width"][-1] == sizeList[i][-1]:
                        sw = i
                    if obj1.attributes["height"][0] == sizeList[i][0] and obj1.attributes["height"][-1] == sizeList[i][-1]:
                        sh = i
                    if obj2.attributes["width"][0] == sizeList[i][0] and obj2.attributes["width"][-1] == sizeList[i][-1]:
                        sw2 = i
                    if obj2.attributes["height"][0] == sizeList[i][0] and obj2.attributes["height"][-1] == sizeList[i][-1]:
                        sh2 = i
                score -= ((sw - sw2)  + (sh - sh2) * 1.1) * 0.2
            
        if ("fill" in obj1.attributes) and ("fill" in obj2.attributes) and (obj1.attributes["fill"] != obj2.attributes["fill"]):
            score -= 3.5
                                    
                
        return score


    def OperationL(self, obj1, obj2):
                    
        if obj1 == None or obj2 == None:
            return 1
              
               
        score = 5
        rotated = False
        
        if ("shape" in obj1.attributes) and ("shape" in obj2.attributes) and (obj1.attributes["shape"] != obj2.attributes["shape"]):
            if obj1.attributes["shape"] in ["square", "rectangle"] and obj2.attributes["shape"] in ["square", "rectangle"]:
                score = 4
            else:
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
        if ("size" in obj1.attributes or ("width" in obj1.attributes and "height" in obj1.attributes)) and ("size" in obj2.attributes or ("width" in obj2.attributes and "height" in obj2.attributes)) :
            sizeList = ["very small", "small", "medium", "large", "very large", "huge"]
            
            if ("size" in obj1.attributes) and ("size" in obj2.attributes):
                sa = 0
                sb = 0
                for i in range(len(sizeList)):
                    if obj1.attributes["size"][0] == sizeList[i][0] and obj1.attributes["size"][-1] == sizeList[i][-1]:
                        sa = i
                    if obj2.attributes["size"][0] == sizeList[i][0] and obj2.attributes["size"][-1] == sizeList[i][-1]:
                        sb = i
                score -= (sa - sb) * 0.4
            elif ("size" in obj1.attributes) and not ("size" in obj2.attributes):
                si = 0
                sw = 0
                sh = 0
                for i in range(len(sizeList)):
                    if obj1.attributes["size"][0] == sizeList[i][0] and obj1.attributes["size"][-1] == sizeList[i][-1]:
                        si = i
                    if obj2.attributes["width"][0] == sizeList[i][0] and obj2.attributes["width"][-1] == sizeList[i][-1]:
                        sw = i
                    if obj2.attributes["height"][0] == sizeList[i][0] and obj2.attributes["height"][-1] == sizeList[i][-1]:
                        sh = i
                score -= ((si - sw)  + (si - sh) * 1.1) * 0.2
            elif not ("size" in obj1.attributes) and ("size" in obj2.attributes):
                si = 0
                sw = 0
                sh = 0
                for i in range(len(sizeList)):
                    if obj2.attributes["size"][0] == sizeList[i][0] and obj2.attributes["size"][-1] == sizeList[i][-1]:
                        si = i
                    if obj1.attributes["width"][0] == sizeList[i][0] and obj1.attributes["width"][-1] == sizeList[i][-1]:
                        sw = i
                    if obj1.attributes["height"][0] == sizeList[i][0] and obj1.attributes["height"][-1] == sizeList[i][-1]:
                        sh = i
                score -= ((sw - si)  + (sh - si) * 1.1) * 0.2
            else:
                sw = 0
                sh = 0
                sw2 = 0
                sh2 = 0
                for i in range(len(sizeList)):
                    if obj1.attributes["width"][0] == sizeList[i][0] and obj1.attributes["width"][-1] == sizeList[i][-1]:
                        sw = i
                    if obj1.attributes["height"][0] == sizeList[i][0] and obj1.attributes["height"][-1] == sizeList[i][-1]:
                        sh = i
                    if obj2.attributes["width"][0] == sizeList[i][0] and obj2.attributes["width"][-1] == sizeList[i][-1]:
                        sw2 = i
                    if obj2.attributes["height"][0] == sizeList[i][0] and obj2.attributes["height"][-1] == sizeList[i][-1]:
                        sh2 = i
                score -= ((sw - sw2)  + (sh - sh2) * 1.1) * 0.2
            
        if ("fill" in obj1.attributes) and ("fill" in obj2.attributes) and (obj1.attributes["fill"] != obj2.attributes["fill"]):
            score -= 3.5

        if "above" in obj1.attributes or "left-of" in obj1.attributes or "overlaps" in obj1.attributes or "above" in obj2.attributes or "left-of" in obj2.attributes or "overlaps" in obj2.attributes:
            lc1 = [0, 0, 0]
            lc2 = [0, 0, 0]
            if "above" in obj1.attributes:
                lc1[0] = len(obj1.attributes["above"].split(","))
            if "left-of" in obj1.attributes:
                lc1[1] = len(obj1.attributes["left-of"].split(","))
            if "overlaps" in obj1.attributes:
                lc1[2] = len(obj1.attributes["overlaps"].split(","))
            if "above" in obj2.attributes:
                lc2[0] = len(obj2.attributes["above"].split(","))
            if "left-of" in obj2.attributes:
                lc2[1] = len(obj2.attributes["left-of"].split(","))
            if "overlaps" in obj2.attributes:
                lc2[2] = len(obj2.attributes["overlaps"].split(","))

            score -= abs(lc1[0] - lc2[0]) * 0.01 + abs(lc1[1] - lc2[1]) * 0.03 + abs(lc1[2] - lc2[2]) * 0.05

        return score
    
    def pairUp(self, A, B):  # A, B are two list of objects with different length
                    
        scoreList = []   # a list to store operation scores between A and B
        copyB = []           # a copy of B
        leftA = []           #temp list to store A objects that not identical to B
                
        for i in range(len(B)):
            copyB.append(B[i])
            
        # the following loop find identical objects between A and B
        # unidentified A objects store in leftA 
        for i in range(len(A)):
            find = False
            for j in range(len(copyB)):
                ops = self.Operation(A[i], copyB[j]) 
                if ops == 5:
                    find = True
                    break
                
            if find:
                scoreList.append(ops)
                copyB.pop(j)
            else:
                leftA.append(A[i])

        
        ts1 = float(sum(scoreList))/ max(1, len(scoreList))
        if len(leftA) == 0 and len(copyB) == 0:
            return [ts1 + 5, sum(scoreList)]
        
        elif len(leftA) == 0:
            sl2 = []
            for i in range(len(copyB)):
                tempScore = 1.5
                for j in range(len(A)):
                    if self.Operation(copyB[i], A[j]) == 5:
                        tempScore = 10
                        break
                sl2.append(tempScore)
            return [ts1 + float(sum(sl2))/ len(copyB), ts1 + sum(sl2)]
            
        elif len(copyB) == 0:
            sl2 = []
            for i in range(len(leftA)):
                sl2.append(1.0)
            return [ts1 + 1.0, ts1 + sum(sl2)]    
                    
        
        else:
            maxLen = max(len(leftA), len(copyB))
            while len(leftA) < maxLen:
                leftA.append(None)
            while len(copyB) < maxLen:
                copyB.append(None)    
            newSL = []
            for i in range(len(leftA)):
                tempScore = -100
                tempIndex = 0
            
                for j in range(len(copyB)):
                    score = self.Operation(leftA[i], copyB[j])
                    if score > tempScore:
                        tempScore = score
                        tempIndex = j
                newSL.append(tempScore)
                copyB.pop(tempIndex)
                
            return [ts1 + float(sum(newSL)) / len(newSL), ts1 + sum(newSL) ]         

    def pairUpL(self, A, B):  
                    
        scoreList = []   
        copyB = []           
        leftA = []          
                
        for i in range(len(B)):
            copyB.append(B[i])
            
        
        for i in range(len(A)):
            find = False
            for j in range(len(copyB)):
                ops = self.OperationL(A[i], copyB[j]) 
                if abs(ops - 5) == 0:
                    find = True
                    break
                
            if find:
                scoreList.append(ops)
                copyB.pop(j)
            else:
                leftA.append(A[i])

        tempLeftA = []
        for i in range(len(leftA)):
            find = False
            for j in range(len(copyB)):
                ops = self.OperationL(leftA[i], copyB[j]) 
                if abs(ops - 5) < 0.1:
                    find = True
                    break
                
            if find:
                scoreList.append(ops)
                copyB.pop(j)
            else:
                tempLeftA.append(leftA[i])

        leftA = tempLeftA

        ts1 = float(sum(scoreList))/ max(1, len(scoreList))
        ts2 = 5
        if len(leftA) == 0 and len(copyB) == 0:
            return [ts1 + 5, sum(scoreList)]
        
        elif len(leftA) == 0:
            sl2 = []
            for i in range(len(copyB)):
                tempScore = 1.0
                for j in range(len(A)):
                    if abs(self.OperationL(copyB[i], A[j]) - 5) < 0.1:
                        tempScore = self.OperationL(copyB[i], A[j])
                        break
                sl2.append(tempScore)
            return [ts2 + float(sum(sl2))/ len(copyB), ts2 + sum(sl2)]
            
        elif len(copyB) == 0:
            sl2 = []
            for i in range(len(leftA)):
                 sl2.append(1.0)
            return [ts1 + 1.0, ts1 + sum(sl2)]    
                    
        
        else:
            maxLen = max(len(leftA), len(copyB))
            while len(leftA) < maxLen:
                leftA.append(None)
            while len(copyB) < maxLen:
                copyB.append(None)    
            sl3 = []
            for i in range(len(leftA)):
                tempScore = -100
                tempIndex = 0
            
                for j in range(len(copyB)):
                    score = self.OperationL(leftA[i], copyB[j])
                    if score > tempScore:
                        tempScore = score
                        tempIndex = j
                sl3.append(tempScore)
                copyB.pop(tempIndex)
                
            return [ts1 + float(sum(sl3)) / len(sl3), ts1 + sum(sl3) ]        
        
