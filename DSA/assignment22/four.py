def is_same_tree(inorder, preorder, postorder):
    if len(inorder) != len(preorder) or len(inorder) != len(postorder):
        return False

    if len(inorder) == 0:
        return True

    if len(inorder) == 1:
        return inorder[0] == preorder[0] == postorder[0]

    if set(inorder) != set(preorder) or set(inorder) != set(postorder):
        return False

    root = preorder[0]
    root_index = inorder.index(root)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]

    left_postorder = postorder[:root_index]
    right_postorder = postorder[root_index:-1]

    return is_same_tree(left_inorder, left_preorder, left_postorder) and \
           is_same_tree(right_inorder, right_preorder, right_postorder)


# Test Case 1
inorder1 = [4, 2, 5, 1, 3]
preorder1 = [1, 2, 4, 5, 3]
postorder1 = [4, 5, 2, 3, 1]
print(is_same_tree(inorder1, preorder1, postorder1))  # Output: True

# Test Case 2
inorder2 = [4, 2, 5, 1, 3]
preorder2 = [1, 5, 4, 2, 3]
postorder2 = [4, 1, 2, 3, 5]
print(is_same_tree(inorder2, preorder2, postorder2))  # Output: False
