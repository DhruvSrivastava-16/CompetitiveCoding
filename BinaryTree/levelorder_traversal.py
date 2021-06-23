


class treenode:
    
    
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
ans = []
def levelorder(root):
    h = height(root)
    
    for i in range(1,h+1):
        l = printlevel(root,i,[])
        ans.append(l)
        
    return ans
        
    

def height(root):          #finds the height of the tree
    if not root:
        return 0
    
    else:
        lh = height(root.left)
        rh = height(root.right)
        
        if lh<rh:
            return rh+1
        
        else:
            return lh+1
    

def printlevel(root,level,l):
    
    if root is None:
        return 
    
    if level == 1:
        print(root.val)
        l.append(root.val)
        
    elif level>1:
        printlevel(root.left,level-1,l)
        printlevel(root.right,level-1,l)
        
    return l
        
        
        
    

 
    

root = treenode(8)
n1 = treenode(10)
n2 = treenode(3)

root.left = n1
root.right = n2


n3 = treenode(1)
n4 = treenode(6)
n5 = treenode(14)

n1.left = n3
n1.right = n4
n2.right = n5

n6 = treenode(9)
n4.left = n6
