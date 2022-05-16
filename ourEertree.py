from asyncio.windows_events import NULL
from sys import prefix

from requests import NullHandler


class Node:
    def __init__(self, val):
        self.val = val
        self.blackEdge = NULL
        #  Prefix and Suffixnode both combine to make the blue edge.
        self.prefixnode = NULL
        self.suffixnode = NULL

        #  THe middlestring becomes the black edge if it is a palindrome.
        self.middlestring = NULL
    def addBlackEdge(self, node):
        self.blackEdge = node
    def addBlueEdge(self, suffixnode, prefixnode = NULL):
        self.suffixnode = suffixnode
        self.prefixnode = prefixnode
    def addMiddleString(self, node):
        self.middlestring = node

class Eertree:
    def __init__(self):
        self.imaginaryString = Node("I")
        self.emptyString = Node("")
        self.imaginaryString.addBlueEdge(self.emptyString)

    def isPalindrome(self, string):
        if string == string[::-1]:
            return True
        return False    
         
    def addStringToTree(self, string):
        string  = string.upper()

        root = Node(string)
        
        stack = [root]
        visited = []

        while stack != []:
            visiting = stack.pop()
            if visiting != self.imaginaryString and visiting != self.emptyString and visiting.val not in visited:
                    if self.isPalindrome(visiting.val):
                        visited.append(visiting.val)

                    self.getSuffixandPrefix(visiting, visited)
                    self.getMiddleString(visiting, visited)

                    if self.isPalindrome(visiting.middlestring.val):
                        visiting.addBlackEdge(Node(visiting.middlestring.val))

                    neighbors = [visiting.middlestring, visiting.suffixnode, visiting.prefixnode]

                    for neighbor in neighbors:
                        if neighbor != NULL and neighbor.val not in visited:
                            stack.append(neighbor)

        if self.isPalindrome(root.val):
            self.root = root
        else:
            self.root = root.blackEdge
                        
        self.visited = visited
        

    def getMiddleString(self, node, visited):
        if len(node.val) == 1:
            node.addMiddleString(self.imaginaryString)  
        elif len(node.val) == 2:
            node.addMiddleString(self.emptyString) 
        else:
            node.addMiddleString(Node(node.val[1:(len(node.val)-1)])) 
            
       
    def getSuffixandPrefix(self, node, visited):
        
        if len(node.val) == 1:
            node.addBlueEdge(self.emptyString)
        else:
            end = len(node.val)

            prefix = node.val[0:end]
            
            while self.isPalindrome(prefix) != True:
                end -= 1
                prefix = node.val[0:end]
            
            start = 0
            suffix = node.val[start:len(node.val)]
            
            while self.isPalindrome(suffix) != True:
                start += 1
                suffix = node.val[start:len(node.val)]  
                
            node.addBlueEdge(Node(suffix), Node(prefix))

        
    def getPalindromes(self):
        return self.visited

eertree = Eertree()
eertree.addStringToTree("abbaeaeaabbeertreeaaeertreeesaasbaas")
lst = eertree.getPalindromes()

print(lst)
print(len(lst))