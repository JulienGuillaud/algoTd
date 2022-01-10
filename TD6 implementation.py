# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:39:32 2021

@author: Julien
"""
import numpy as np

class Node:
    def __init__(self, val):
        self.value = val
        self.antecedent = []
    def getValue(self):
        return self.value
    def setAntecedent(self,antecedent):
        self.antecedent.append(antecedent)
    def getAntecedent(self):
        return self.antecedent

class Graph:
    def __init__(self, matrix):
        self.racine = None
        self.node = []
        alphabet = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        num_rows, num_cols = matrix.shape
        for i in range(0, num_rows):
            alphabetLetter = alphabet[i]
            self.node.append(Node(alphabetLetter))
        nbRow = 0
        for row in matrix:
            rowLetter = alphabet[nbRow]
            nodeRow = self.findNode(rowLetter)
            #print("Row = "+rowLetter)
            nbAntecedent = 0
            for antecedent in row:
                antecedentLetter = alphabet[nbAntecedent]
                antecedentNodeRow = self.findNode(antecedentLetter)
                if(antecedent == 1):
                    #print("> "+antecedentLetter)
                    nodeRow.setAntecedent(antecedentNodeRow)
                nbAntecedent+=1
            nbRow+=1

    def findNode(self, value):
        for currentNode in self.node:
            if(currentNode.getValue()==value):
                return currentNode

    def showDegre(self, value):
        noeud = self.findNode(value)
        degre = len(noeud.getAntecedent())
        print("Degre de "+str(value)+" : "+str(degre))
    
    def show(self):
        for noeud in self.node:
            nodeVal = noeud.getValue()
            nodeAntecedents = noeud.getAntecedent()
            print(nodeVal)
            for antecedents in nodeAntecedents:
                print(" > "+antecedents.getValue())
        print("\n")
    

# Exercice 2 question 3

graphMatrix1 = np.array([
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,0,1,0],
    [0,1,0,0,0,0],
    [0,0,0,1,0,1],
    [0,0,0,0,0,0]
])

num_rows, num_cols = graphMatrix1.shape

graph1 = Graph(graphMatrix1)
graph1.show()

graph1.showDegre("A")
graph1.showDegre("E")
graph1.showDegre("F")