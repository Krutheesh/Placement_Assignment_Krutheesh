class DataStream:
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.stream = []

    def consec(self, num):
        self.stream.append(num)
        if len(self.stream) < self.k:
            return False

        return all(val == self.value for val in self.stream[-self.k:])
dataStream = DataStream(4, 3)
print(dataStream.consec(4))  # Output: False
print(dataStream.consec(4))  # Output: False
print(dataStream.consec(4))  # Output: True
print(dataStream.consec(3))  # Output: False
