#Python program to find height of full binary tree
# using preorder
	
# function to return max of left subtree height
# or right subtree height
def findDepthRec(tree, n, index) :

	if (index[0] >= n or tree[index[0]] == 'l'):
		return 0

	# calc height of left subtree (In preorder
	# left subtree is processed before right)
	index[0] += 1
	left = findDepthRec(tree, n, index)

	# calc height of right subtree
	index[0] += 1
	right = findDepthRec(tree, n, index)
	return (max(left, right) + 1)

# Wrapper over findDepthRec()
def findDepth(tree, n) :

	index = [0]
	return findDepthRec(tree, n, index)

		
# Driver program to test above functions
if __name__ == '__main__':
	tree= "nlnnlll"
	n = len(tree)

	print(findDepth(tree, n))

# This code is contributed by SHUBHAMSINGH10
