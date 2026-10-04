def dfs(mat, start_root=0):
  size=len(mat)
  stack=[(start_root,[])]
  visited=set()
  while stack:
    node,path=stack.pop()
    has_neighbour=False
    if node in visited:
      continue
    visited.add(node)
    for neighbor in range(size-1,-1,-1):
      if mat[node][neighbor]== 1 and neighbor not in visited:
        stack.append((neighbor,path+[(node,neighbor)]))
        has_neighbour=True
    if not has_neighbour and path: 
      print(path)

dfs([[0,1,1,0],[0,0,0,1],[0,0,0,0],[0,0,1,0]])    
