from collections import defaultdict

def solution(info, edges):
    answer = 0
    current_node = 0
    dicts = defaultdict(list)
    
    for lists in edges:
        dicts[str(lists[0])].append(str(lists[1]))
    
    visited = [0, for _ in range(len(info))]
    visited[0] += 1
    sheep = 1
    wolf = 0
    current_node = 0
    while sheep > wolf:
        node_list = dicts[str(current_node)]
        for i in range(len(node_list)):
            if visited[node_list[i]] != 0:
                continue
            current_node = node_list[i]
            if info[str(current_node)]  
            
            
    return answer