class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        complete_count = 0
        
        # Step 2: Find connected components
        for i in range(n):
            if i not in visited:
                # Use a stack for DFS to collect all nodes in the current component
                comp = []
                stack = [i]
                visited.add(i)
                
                while stack:
                    node = stack.pop()
                    comp.append(node)
                    
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                            
                # Step 3: Check if the component is complete
                # In a complete graph, every node is connected to every other node.
                # Hence, every node's degree must equal the total number of nodes in the component minus 1.
                is_complete = True
                for node in comp:
                    if len(adj[node]) != len(comp) - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    complete_count += 1
                    
        return complete_count