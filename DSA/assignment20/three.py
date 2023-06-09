

INT_MIN, INT_MAX = float('-inf'), float('inf')


class NodeDetails:

	def __init__(self, data, min, max):
		self.data = data
		self.min = min
		self.max = max


def levelOrderIsOfBST(arr, n):

	# if tree is empty
	if n == 0:
		return True
	
	# queue to store NodeDetails
	q = []
	
	# index variable to access array elements
	i = 0

	newNode = NodeDetails(arr[i], INT_MIN, INT_MAX)
	i += 1
	q.append(newNode)
	

	while i != n and len(q) != 0:	
	
		temp = q.pop(0)
		
		if i < n and (arr[i] < temp.data and
					arr[i] > temp.min):
		
			newNode = NodeDetails(arr[i], temp.min, temp.data)
			i += 1
			q.append(newNode)			
		
	
		if i < n and (arr[i] > temp.data and
					arr[i] < temp.max):
		
			
			newNode = NodeDetails(arr[i], temp.data, temp.max)
			i += 1
			q.append(newNode)		
				

	if i == n:
		return True
		
	
	return False	


if __name__ == "__main__":

	arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
	n = len(arr)	
	if levelOrderIsOfBST(arr, n):
		print("Yes")
	else:
		print("No")

# This code is contributed by Rituraj Jain
