class RecentCounter:
    def __init__(self):
        self.requests = []
    
    def ping(self, t):
        self.requests.append(t)
        start_time = t - 3000
        
        while self.requests[0] < start_time:
            self.requests.pop(0)
        
        return len(self.requests)
recentCounter = RecentCounter()
output = []
output.append(None)
output.append(recentCounter.ping(1))
output.append(recentCounter.ping(100))
output.append(recentCounter.ping(3001))
output.append(recentCounter.ping(3002))

print(output)
