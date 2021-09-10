graph_list = {1: set([2,3,4]),
              2: set([1,5]),
              3: set([1,6,7]),
              4: set([1,8]),
              5: set([2, 9]),
              6: set([3, 10]),
              7: set([3]),
              8: set([4]),
              9: set([5]),
              10: set([6])}
root_node = 1

def DFS(graph, root):
    visit = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            temp = list(graph[n] - set(visit))
            temp.sort(reverse=True)
            stack += temp
            
    return visit

print(DFS(graph_list, root_node))