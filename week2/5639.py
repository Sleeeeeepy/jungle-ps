import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
    
    def from_key(self, key):
        ret = Node(key, None, None)
        return ret
    
    def insert(self, key):
        node = self
        while True:
            if node.key > key:
                if node.left != None:
                    node = node.left
                else: 
                    node.left = self.from_key(key)
                    break
            else:
                if node.right != None:
                    node = node.right
                else:
                    node.right = self.from_key(key)
                    break
    
numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

root = Node(numbers[0], None, None)

for i in range(1, len(numbers)):
    root.insert(numbers[i])

def post_order(node):
    if node is None:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node.key)

post_order(root)