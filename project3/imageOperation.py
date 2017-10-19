from PIL import Image


def findUL(pixel, sz):
    
    for i in range(0, sz):
        for j in range(0, sz):
            if pixel[i, j][0] < 10:
                
                return (i, j)
    return None

def findLR(pixel, sz):
    
    for i in range(sz-1, -1, -1):
        for j in range(sz-1, -1, -1):
            if pixel[i, j][0] < 10:
                
                return (i, j)
    return None

def pnum(pixel, sz):
    pnum = 0
    for i in range(sz):
        for j in range(sz):
            if pixel[i, j][0] == 0:
                pnum += 1
    return pnum
    
def identical(pixel_1, pixel_2, sz):
    difs = 0
    
    sp1a = findUL(pixel_1, sz)
    sp1b = findLR(pixel_1, sz)
    sp2a = findUL(pixel_2, sz)
    sp2b = findLR(pixel_2, sz)
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
       
    print 'Operation identical difs: ', difs
    if difs > 100:
        return False
    else:
        return True

def m_id(m1, m2):
    difs = 0
    
    for i in range(18):
        for j in range(18):
            if m1[i][j] != m2[i][j]:
                difs += 1
       
    print 'Operation identical difs: ', difs
    if difs > 36:
        return False
    else:
        return True

def id_core(pixel_1, pixel_2, sz, sc):
    difs = 0
        
    for i in range(sc[0], sc[1]):
        for j in range(sc[0], sc[1]):
            if abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                difs += 1
            
     
    print 'Operation id_core difs: ', difs
    if difs > 100:
        return False
    
    else:
        return True
    
def id_edge(pixel_1, pixel_2, sz, se):
    difs = 0
        
    for i in range(sz):
        for j in range(sz):
            if i > se[0] and i < se[1] and j > se[0] and j < se[1]:
                continue
            elif abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                difs += 1
            
     
    print 'Operation id_edge difs: ', difs
    if difs > 100:
        return False
    
    else:
        return True

def id_up(pixel_1, pixel_2, sz):
    difs = 0
        
    for i in range(0, sz/2 - 20):
        for j in range(0, sz):
            if abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                difs += 1
            
     
    print 'Operation id_up difs: ', difs
    if difs > 500:
        return False
    
    else:
        return True

def id_down(pixel_1, pixel_2, sz):
    difs = 0
        
    for i in range(sz/2 + 20, sz):
        for j in range(0, sz):
            if abs(pixel_1[i, j][0] - pixel_2[i, j][0]) > 200:
                difs += 1
            
     
    print 'Operation id_down difs: ', difs
    if difs > 500:
        return False
    
    else:
        return True
    
def pmerge(pixel_1, pixel_2, pixel_3, sz):
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
    print 'Operation pmerge difs: ', difs
    if difs > 500:
        return False
    
    else:
        return True                

def pmerge2(pixel_1, pixel_2, pixel_3, sz):
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
    print 'Operation pmerge2 difs: ', difs
    if difs > 500:
        return False
    
    else:
        return True  
def poverlap(pixel_1, pixel_2, pixel_3, sz):
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
    print 'Operation poverlap difs: ', difs
    if difs > 500:
        return False
    
    else:
        return True  

def padd(pixel_1, pixel_2, pixel_3, sz):
    p1num = pnum(pixel_1, sz)
    p2num = pnum(pixel_2, sz)
    p3num = pnum(pixel_3, sz)
    print 'padd p1, p2 p1+p2, p3: ', p1num, p2num, p1num + p2num, p3num
    if abs(p3num - p1num - p2num) < 500:
        return True
    return False

def convert(pixel):
    m = []
    for i in range(18):
        temp = []
        for j in range(18):
            switch = False
            for l in range(12):
                for n in range(12):
                    if pixel[i*10+l, j*10+n][0] < 250:
                        switch = True
                        break
                if switch:
                    break
            if switch:
                temp.append(1)
            else:
                temp.append(0)
                        
        m.append(temp)
    return m
    
pdict = {}    
image1 = Image.open("C:\\XiaodongGu\\KBAI assignments\\project3\\Problems\\Basic Problems D\\Basic Problem D-01\\e.png", "r")
image2 = Image.open("C:\\XiaodongGu\\KBAI assignments\\project3\\Problems\\Basic Problems D\\Basic Problem D-01\\h.png", "r")
image3 = Image.open("C:\\XiaodongGu\\KBAI assignments\\project3\\Problems\\Basic Problems E\\Basic Problem E-12\\d.png", "r")
image4 = Image.open("C:\\XiaodongGu\\KBAI assignments\\project3\\Problems\\Basic Problems E\\Basic Problem E-04\\1.png", "r")

p1 = image1.load()
m1 = convert(p1)

'''
for i in range(len(m1)):
    print m1[i]
'''    

p2 = image2.load()
m2 = convert(p2)


'''
for i in range(len(m2)):
    print m2[i]
'''    
'''
p3 = image3.load()

p4 = image4.load()
sz = image1.size[0]
sc = (69, 115)
se = (46, 138)

func = [identical, id_core]
print func[0](p1, p2, sz)
print func[1](p1, p2, sz, sc)
print id_edge(p1, p2, sz, se)
print pmerge(p1, p2, p3, sz)
print padd(p1, p2, p3, sz)
print pmerge2(p1, p2, p3, sz)
print poverlap(p1, p2, p3, sz)

'''
print m_id(m1, m2)
