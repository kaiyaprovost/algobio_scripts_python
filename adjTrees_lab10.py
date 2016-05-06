"""
Template for second part of Lab 10 (trees stored as adjacency lists)
RGGS 670:  Algorithmic Approaches for Biological Data
Spring 2016
"""

adjList = {}
#Add in leaves first:
adjList["birds"] = ("archsaurs",[])
adjList["crodolilians"] = ("archsaurs",[])
adjList["lepidosaurs"] = ("unnamed1",[])
adjList["marineReptiles"] = ("unnamed1",[])
adjList["turtles"] = ("reptiles",[])
adjList["mammals"] = ("amniotes",[])
adjList["amphibians"] = ("tetrapods",[])
adjList["lungfish"] = ("unnamed2",[])
adjList["coelacanths"] = ("lobeFinnedFishes",[])
adjList["rayFinnedFish"] = ("bonyFishes",[])
adjList["cartilanginousFishes"] = ("jawedFishes",[])
adjList["lampreys"] = ("unnamed3",[])
adjList["conodonts"] = ("vertebrates",[])
adjList["hagfishes"] = ("craniates",[])

#Next the internal nodes:
adjList["archsaurs"] = ("diapsids",["birds", "crodolilians"])
adjList["unnamed1"] = ("diapsids",["lepidosaurs", "marineReptiles"])
adjList["diapsids"] = ("reptiles",["unnamed1", "archsaurs"])
adjList["reptiles"] = ("amniotes",["turtles", "diapsids"])
adjList["amniotes"] = ("tetrapods",["mammals", "reptiles"])
adjList["tetrapods"] = ("unnamed2",["amniotes", "amphibians"])
adjList["unnamed2"] = ("lobeFinnedFishes",["lungfish", "tetrapods"])
adjList["lobeFinnedFishes"] = ("bonyFishes",["coelacanths", "unnamed2"])
adjList["bonyFishes"] = ("jawedFishes",["rayFinnedFish", "lobeFinnedFishes"])
adjList["jawedFishes"] = ("unnamed3",["bonyFishes", "cartilanginousFishes"])
adjList["unnamed3"] = ("vertebrates",["lampreys", "jawedFishes"])
adjList["vertebrates"] = ("craniates",["conodonts", "unnamed3"])
adjList["craniates"] = ("",["hagfishes", "vertebrates"])

"""
Given a vertex in the tree, prints out all leaves below it (its clade):
"""
def printLeaves(v):
     if len(adjList[v][1]) == 0:
          print v
     else:
          for child in adjList[v][1]:
               printLeaves(child)

def numLeaves(v,count):
     if len(adjList[v][1]) == 0:
          count += 1
          return count
     else:
          for child in adjList[v][1]:
               #print count
               count = numLeaves(child,count)
     return count

def leafPath(v):
     if len(adjList[v][1]) == 0:
          maxLevel = 0 ## leaves get level 0
          #print adjList[v][1],maxLevel
          return maxLevel
     else:
          childLevel = []
          for child in adjList[v][1]:
               childLevel.append(leafPath(child))
          maxLevel = max(childLevel) + 1
          #print adjList[v][1],maxLevel
          return maxLevel
     return maxLevel


print "PRINT LEAVES------------------------"          
printLeaves("bonyFishes")
print "NUM LEAVES--------------------------"
print numLeaves("bonyFishes",0)
print "LEAF PATH---------------------------"
print leafPath("bonyFishes")
print
#print leafPath("birds")
#print numLeaves("birds",0)
