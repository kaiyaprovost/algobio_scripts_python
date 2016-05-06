
# Lab 14: Small Parsimony Problem (Fitch's Algorithm)
# RGGS 670:  Algorithmic Approaches to Biological Data
# Spring 2016


#Use a simple adjacency list for trees:
#    Nodes of trees have: [parent, label, children]


def newLabel(l1,l2):
     """
     Takes two labels and returns the label of their parent.
     """
     
     #Split up the labels into separate positions:
     b1 = l1.split(" ")
     b2 = l2.split(" ")
     #Create a new list to store the parent labels:
     newL = []
     for i in range(len(b1)):
          if b1[i] == b2[i]:
               newL.append(b1[i])
          else:
               s1 = set(b1[i])
               s2 = set(b2[i])
               intersect = s1.intersection(s2)
               if len(intersect) == 0:
                    union = s1.union(s2)
                    newL.append("".join(union))
               else:
                    newL.append("".join(intersect))
          
     return " ".join(newL)

def firstPass(t, n):
     #Assumes all leaves have labels
     #Check if there's a label for the node
     #print n,"TREE",
     #print t[n]
     if t[n][1] != "":
          return t[n][1]
     else:
          #If not, get the label of it's kids:
          #Assumes binary trees
          kid1 = t[n][2][0]
          kid2 = t[n][2][1]
          newL = newLabel(firstPass(t,kid1),firstPass(t,kid2))
          t[n][1] = newL
          return newL

def score(l1, l2):
     w1 = l1.split(" ")
     w2 = l2.split(" ")
     diff = 0
     for i in range(len(w1)):
          if w1[i] != w2[i]:
               diff += 1
     return diff

def forceLabels(t, labels, kid):
     kLabels = t[kid][1].split(" ")
     score = 0
     for i in range(len(labels)):
          if kLabels[i] != labels[i]:
               s1 = set(kLabels[i])
               s2 = set(labels[i])
               intersect = s1.intersection(s2)
               if len(intersect) == 0:
                    #No overlap, so, just choose one
                    kLabels[i] = kLabels[i][:1]
                    score += 1
               else:
                    #Overlap, choose one to use as label:
                    kLabels[i] = intersect.pop()
     t[kid][1] = " ".join(kLabels)
     return score

def secondPass(t, n):
     #Assumes all leaves have labels
     #Check if there's a label for the node
     score = 0
     labels = t[n][1].split(" ")
     if n == "root":
          for i in range(len(labels)):
               #For root, if more than one label, use just the first one:
               labels[i] = labels[i][:1]
          t[n][1] = " ".join(labels)
     if len(t[n][2]) > 0:
          #There's children, so, not a leaf
          #Assumes binary trees
          kid1 = t[n][2][0]
          kid2 = t[n][2][1]          
          #Force the labels for the kids:
          score += forceLabels(t, labels, kid1)
          score += forceLabels(t, labels, kid2)
          #Repeat for the kids
          score += secondPass(t, kid1)
          score += secondPass(t, kid2)
     return score
    


def printTree(t,n,indent):
     """Simple print for trees """

     #n is a leaf:
     if len(t[n][2]) == 0:
          print "\t"*indent+n+": "+t[n][1]
     else:
          print "\t"*indent+n+": "+t[n][1]
          for c in t[n][2]:
               printTree(t,c,indent+1)


def scoreTree(t):
    firstPass(t, "root")
    score = secondPass(t,"root")
    return score


if __name__ == "__main__":
    tree = {"root" : ["","",["i1","i2"]],
        "i1": ["root","", ["a", "i3"]], 
        "i2": ["root","", ["b", "c"]],
        "i3": ["i1","", ["d","e"]],
        "a": ["i1","T A A A A", []],
        "b": ["i2","A A A A G", []],
        "c": ["i2","C A A A T", []],
        "d": ["i3","A A A A A", []],
        "e": ["i3","T A A A A", []]}

    print tree

    s = scoreTree(tree)
    print "Score is", s
    

