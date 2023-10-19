import sys
input = sys.stdin.readline

num_nodes = int(input())
tree = dict()

for i in range(num_nodes):
    parent, left, right = input().split()
    tree[parent] = (left, right)

def preorder(node):
    left, right = tree[node]
    print(node, end='')

    if left != '.':
        preorder(left)
    
    if right != '.':
        preorder(right)

def inorder(node):
    left, right = tree[node]
    if left != '.':
        inorder(left)

    print(node, end='')

    if right != '.':
        inorder(right)

def postorder(node):
    left, right = tree[node]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)

    print(node, end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')