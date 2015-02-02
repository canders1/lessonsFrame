import xml.etree.ElementTree as etree
tree = etree.parse('short_test.xml')
root = tree.getroot()

#####################################################################

def printLeaves(r):
    if len(r) == 0:
        print(r)
    else:
        for child in r:
            printLeaves(child)

#####################################################################

def getElements(r, keyword):
    return list(r.iter(keyword))

#####################################################################
    
def addAttr(r, keyword, k, v):
    l = getElements(root, keyword)
    for i in l:
        i.set(k, v)
        #print(i.attrib) Prints all attributes of i

#####################################################################

def getAttrV(r, keyword, k):
    l = getElements(root, keyword)
    r = []
    for i in l:
        r.append(i.get(k))
    return r

#####################################################################
addAttr(root, 'unit', 'href', "http://example.com/")
hrefs = getAttrV(root, 'unit', 'href')
#printLeaves(root)
f = open('root', 'w')
s = etree.tostring(root)
f.write(s)
f.close()
f = open('root', 'r')
inputs = f.read()
r = etree.fromstring(inputs)
printLeaves(r)
