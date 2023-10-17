import sys
input = sys.stdin.readline

num_tree, target_length = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
max_height_of_tree = max(tree)

def simulate_cut(tree, height_to_cut):
    sum = 0
    for tree_height in tree:
        if (height_to_cut < tree_height):
            sum += tree_height - height_to_cut
    return sum

def bsearch(tree, start, end, target):
    if start > end:
        return end
    
    mid = (start + end) // 2
    cutting_length = simulate_cut(tree, mid)
    
    if target > cutting_length:
        return bsearch(tree, start, mid - 1, target)
    else:
        return bsearch(tree, mid + 1, end, target)

result = bsearch(tree, 0, max_height_of_tree, target_length)
print(result)