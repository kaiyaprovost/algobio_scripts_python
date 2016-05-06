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
adjList["lungfish"] = ("tetrapods",[])
adjList["coelacanths"] = ("lobeFinnedFishes",[])
adjList["rayFinnedFish"] = ("bonyFishes",[])
adjList["cartilanginousFishes"] = ("jawedFishes",[])
adjList["lampreys"] = ("vertebrates",[])
adjList["conodonts"] = ("diapsids",[])
adjList["hagfishes"] = ("craniates",[])

#Next the internal nodes:
adjList["archsaurs"] = ("diapsids",["birds", "crodolilians"])
adjList["unnamed1"] = ("diapsids",["lepidosaurs", "marineReptiles"])
adjList["diapsids"] = ("reptiles",["unnamed1", "archsaurs"])
adjList["reptiles"] = ("amniotes",["turtles", "diapsids"])
adjList["amniotes"] = ("tetrapods",["mammals", "reptiles"])
adjList["tetrapods"] = ("lobeFinnedFishes",["amniotes", "amphibians"])
adjList["lobeFinnedFishes"] = ("bonyFishes",["coelacanths", "tetrapods"])
adjList["bonyFishes"] = ("jawedFishes",["rayFinnedFish", "lobeFinnedFishes"])
adjList["jawedFishes"] = ("vertebrates",["bonyFishes", "cartilanginousFishes"])
adjList["vertebrates"] = ("craniates",["lampreys", "jawedFishes"])
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


printLeaves("bonyFishes")
