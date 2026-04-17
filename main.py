# 1-mashq
from collections import defaultdict, deque

edges = [(1,2),(1,3),(3,4)]

graph = defaultdict(list)
indeg = defaultdict(int)

for u,v in edges:
    graph[u].append(v)
    indeg[v]+=1

q = deque([n for n in graph if indeg[n]==0])
res = []

while q:
    node = q.popleft()
    res.append(node)
    for nei in graph[node]:
        indeg[nei]-=1
        if indeg[nei]==0:
            q.append(nei)

print(res)
# 2-mashq
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c,{})
        node["#"] = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "#" in node
# 3-mashq
parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    parent[find(a)] = find(b)
# 4-mashq
import heapq

low = []
high = []

def add(num):
    heapq.heappush(low, -num)
    heapq.heappush(high, -heapq.heappop(low))
    
    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))

def median():
    if len(low) > len(high):
        return -low[0]
    return (-low[0] + high[0]) / 2
# 5-mashq
def serialize(root):
    if not root:
        return "None,"
    return str(root.val)+","+serialize(root.left)+serialize(root.right)

def deserialize(data):
    vals = data.split(",")
    
    def dfs():
        val = vals.pop(0)
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    
    return dfs()
