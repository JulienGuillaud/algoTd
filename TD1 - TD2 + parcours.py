class Tree:
  def __init__(self, letter, parent):
    self.letter = letter
    self.parent = parent
    self.children = None
    self.leftChild = None
    self.rightChild = None
  def getLetter(self):
    return self.letter
  def getChild(self):
    return self.children
  def getParent(self):
    return self.parent
  def getLeftChild(self):
    return self.leftChild
  def getRightChild(self):
    return self.rightChild
  def setChilds(self, childrens):
      if 0 <= 0 < len(childrens):
          self.leftChild = childrens[0]
      else:
          self.leftChild = None
      if 0 <= 1 < len(childrens):
          self.rightChild = childrens[1]
      else:
          self.rightChild = None
      self.children = childrens
# Fonctions
def parcoursLargeur(node):
  tabNoeuds = []
  tabNoeuds.append(node)
  resultat = []
  while len(tabNoeuds) >= 1:
    currentNode = tabNoeuds.pop(0)
    resultat.append(currentNode)
    currentNodeChilds =currentNode.getChild() 
    if currentNodeChilds != None:
      for i in currentNodeChilds:
        tabNoeuds.append(i)
  for j in resultat:
    print(j.getLetter())

def parcoursProfondeurPrefix(node):
  print(node.getLetter())
  childs = node.getChild()
  if childs!=None:
    for i in childs:
      parcoursProfondeurPrefix(i)

def parcoursProfondeurSuffix(node):
  childs = node.getChild()
  if childs!=None:
    for i in childs:
      parcoursProfondeurSuffix(i)
  print(node.getLetter())

def parcoursProfondeurInfix(node):
  left = node.getLeftChild()
  right = node.getRightChild()
  if left!=None:
      parcoursProfondeurInfix(left)
  print(node.getLetter())
  if right!=None:
      parcoursProfondeurInfix(right)

# Données exercice 1

a = Tree("a",None)
b = Tree("b",a)
c = Tree("c",a)
d = Tree("d",a)
e = Tree("e",b)
f = Tree("f",b)
g = Tree("g",d)
h = Tree("h",d)
i = Tree("i",d)
j = Tree("j",e)
k = Tree("k",e)
l = Tree("l",e)
m = Tree("m",g)
n = Tree("n",i)
o = Tree("o",i)
p = Tree("p",m)

a.setChilds([b,c,d])
b.setChilds([e,f])
d.setChilds([g,h,i])
e.setChilds([j,k,l])
g.setChilds([m])
i.setChilds([n,o])
m.setChilds([p])

# Données exercice 2
_20 = Tree("20",None)
_5 = Tree("5",_20)
_25 = Tree("25",_20)
_3 = Tree("3",_5)
_12 = Tree("12",_5)
_21 = Tree("21",_25)
_28 = Tree("28",_25)
_8 = Tree("8",_12)
_13 = Tree("13",_12)
_6 = Tree("6",_8)

_20.setChilds([_5, _25])
_5.setChilds([_3, _12])
_25.setChilds([_21, _28])
_12.setChilds([_8, _13])
_8.setChilds([_6])

# Print exercice 1

print("Parcours largeur : ")
parcoursLargeur(a)

print("Parcours Profondeur préfix: ")
parcoursProfondeurPrefix(a)

print("Parcours Profondeur suffix: ")
parcoursProfondeurSuffix(a)

# Print exercice 2

print("Parcours largeur : ")
parcoursLargeur(_20)

print("Parcours Profondeur préfix: ")
parcoursProfondeurPrefix(_20)

print("Parcours Profondeur suffix: ")
parcoursProfondeurSuffix(_20)

print("Parcours Profondeur infix: ")
parcoursProfondeurInfix(_20)