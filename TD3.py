# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:52:18 2021

@author: jgu
"""
import random
import time

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getValue(self):
        return self.value

class Tree:
    def __init__(self):
        self.racine = None
        
    def getRacine(self):
        return self.racine

    def add(self, value):
        if(self.racine == None):
            self.racine = Node(value)
        else:
            self.appendChild(value, self.racine)

    def appendChild(self, value, node):
        if(value < node.value):
            if(node.left != None):
                self.appendChild(value, node.left)
            else:
                node.left = Node(value)
        else:
            if(node.right != None):
                self.appendChild(value, node.right)
            else:
                node.right= Node(value)

    def search(self, value):
        node = self.racine
        while node != None:
            if node.value == value:
                return node
            if node.value > value:
                node = node.left
            else:
                node = node.right
        return None
   

# Fonctions
def parcoursProfondeurInfix(node):
  left = node.getLeft()
  right = node.getRight()
  if left!=None:
      parcoursProfondeurInfix(left)
  # décommenter pour débug
  #print(node.getValue())
  if right!=None:
      parcoursProfondeurInfix(right)


# Exercice 1
arbre = Tree()
arbreList = [25,10,60,5,20,35,65,15,30,45,70,40,50,55]
for elem in arbreList:
    arbre.add(elem)

parcoursProfondeurInfix(arbre.getRacine())

# Exercice 2
grandArbreList = list(range(1,10001))
random.shuffle(grandArbreList)
grandArbre = Tree()
for elem in grandArbreList:
    grandArbre.add(elem)
    
# Valeurs a rechercher
listRecherche = []
for i in range(0, 100):
    listRecherche.append(random.randint(0,10001))


#+------------------------------------------------+
#| Mesure temps recherche parcour normal          |
#+------------------------------------------------+
indexResult = []
startNormal = time.time()
compteurNormal=0
for elemRecherche in listRecherche:
    for elemParcouru in grandArbreList:
        if elemRecherche == elemParcouru:
            indexResult.append([elemRecherche,grandArbreList.index(elemParcouru)])
            compteurNormal = compteurNormal+1
            break

endNormal = time.time()
elapsedNormal = endNormal - startNormal
# décommenter pour débug
#for elem in indexResult:
    #print(f'{elem[0]} Trouvé a l\'index {elem[1]}')
print('\n')
print(f'Temps de recherche (methode parcours classique) : {elapsedNormal}ms : {compteurNormal} elements trouvés')

#+------------------------------------------------+
#| Mesure temps recherche parcour Arbre binaire   |
#+------------------------------------------------+
indexResultGrandArbre = []    
startTree = time.time()

compteur = 0
for elemRecherche in listRecherche:
    if grandArbre.search(elemRecherche) != None:
        compteur=compteur+1

endTree = time.time()
elapsedTree = endTree - startTree
print('\n')
print(f'Temps de recherche (methode binaryTree) : {elapsedTree}ms : {compteur} elements trouvés')


#+------------------------------------------------+
#| Mesure temps Tri methode sort                  |
#+------------------------------------------------+ 
startTri = time.time()

grandArbreList.sort()

endTri = time.time()
elapsedTri = endTri - startTri

#+------------------------------------------------+
#| Mesure temps Tri methode profondeur infix      |
#+------------------------------------------------+  
startTriArbre = time.time()

parcoursProfondeurInfix(grandArbre.getRacine())

endTriArbre = time.time()
elapsedTriArbre = endTriArbre - startTriArbre

# Debug comparaison
print('\n')
print(f'Temps de tri (methode sort) : {elapsedTri}ms')
print('\n')
print(f'Temps de tri (methode profondeurInfix) : {elapsedTriArbre}ms')