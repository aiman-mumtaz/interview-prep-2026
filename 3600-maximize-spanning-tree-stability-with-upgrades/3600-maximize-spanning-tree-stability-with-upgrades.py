class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n, edges, k):
        def can_form_tree(min_s):
            dsu = DSU(n)
            edges_used = 0
            
            for u, v, s, must in edges:
                if must == 1:
                    if s < min_s: return False
                    if not dsu.union(u, v): return False
                    edges_used += 1
            
            for u, v, s, must in edges:
                if must == 0 and s >= min_s:
                    if dsu.union(u, v):
                        edges_used += 1
            
            upgrades = 0
            for u, v, s, must in edges:
                if must == 0 and s < min_s and s * 2 >= min_s:
                    if upgrades < k and dsu.union(u, v):
                        upgrades += 1
                        edges_used += 1
            
            return edges_used == n - 1

        ans = -1
        low, high = 0, 2 * 10**9 
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_tree(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans