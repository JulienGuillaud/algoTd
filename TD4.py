# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:39:32 2021

@author: Julien
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.hauteurDroit = None
        self.hauteurGauche = None
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
    
    def getHauteur(self, side = ""):
        if(side == "left"):
            return self.hauteurLeft(self.racine) - 1
        elif(side == "right"):
            return self.hauteurRight(self.racine) - 1
        else:
            return self.hauteur(self.racine) - 1
    
    def hauteur(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.hauteur(node.left), self.hauteur(node.right))
        
    def hauteurLeft(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.hauteurLeft(node.left)
        
    def hauteurRight(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.hauteurRight(node.right)
        
    def isEquilibrated(self):
        equilibre = self.getHauteur("left") - self.getHauteur("right")
        print("Equilibre "+str(equilibre))
        if( -1 <= equilibre <= 1):
            return True
        else:
            return False
        
    def rotate_node_left(self, node):
        if node.right is not None:
            node.right.left = Node(node.value)
        return node.right
    


# Fonctions
def parcoursProfondeurInfix(node):
  left = node.getLeft()
  right = node.getRight()
  if left!=None:
      parcoursProfondeurInfix(left)
  print(node.getValue())
  if right!=None:
      parcoursProfondeurInfix(right)


# Exercice 1
arbre = Tree()
arbreList = [11,8,14,5,10,13,15]
for elem in arbreList:
    arbre.add(elem)

arbreNonEquilibre = Tree()
arbreNonEquilibreList = [11,8,14,5,10,13,15,12,15,18]
for elem in arbreNonEquilibreList:
    arbreNonEquilibre.add(elem)


parcoursProfondeurInfix(arbreNonEquilibre.getRacine())
print("Hauteur : "+str(arbreNonEquilibre.getHauteur()))
print("Equilibre : "+str(arbreNonEquilibre.isEquilibrated()))

parcoursProfondeurInfix(arbre.getRacine())
print("Hauteur : "+str(arbre.getHauteur()))
print("Equilibre : "+str(arbre.isEquilibrated()))