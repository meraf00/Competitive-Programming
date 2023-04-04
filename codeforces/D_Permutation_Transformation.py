# https://codeforces.com/problemset/problem/1490/D


from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  


    def __str__(self):
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"        
    
    __repr__ = __str__


def max_index(nums, start, end):
    max_idx = start

    for idx in range(start, end + 1):
        if nums[idx] > nums[max_idx]:
            max_idx = idx
    
    return max_idx


def build_tree(nums, start, end):    
    if start > end:
        return
    
    if start == end:
        return TreeNode(nums[start])
    
    max_idx = max_index(nums, start, end)

    left_child = build_tree(nums, start, max_idx - 1)
    right_child = build_tree(nums, max_idx + 1, end)

    root = TreeNode(nums[max_idx])
    root.left = left_child
    root.right = right_child

    return root



def calculate_node_level(root):
    
    levels = {root.val : 0}

    queue = deque([root])

    while queue:        
        current_node = queue.popleft()

        left_child = current_node.left
        
        right_child = current_node.right


        if left_child:
            levels[left_child.val] = levels[current_node.val] + 1
            queue.append(left_child)


        if right_child:
            levels[right_child.val] = levels[current_node.val] + 1
            queue.append(right_child)
        
    
    return levels
        



test_cases = int(input())

for _ in range(test_cases):
    nums_length = int(input())

    nums = list(map(int, input().split()))

    tree_root = build_tree(nums, 0, nums_length - 1)

    node_levels = calculate_node_level(tree_root)

    for i, num in enumerate(nums):
        nums[i] = node_levels[num]

    print(*nums)
