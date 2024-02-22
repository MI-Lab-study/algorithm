def solution(maps):
    from collections import deque

    def bfs(graph, start):
        queue = deque()
        queue.append(start)
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            current_h, current_w = queue.popleft()

            for m in move:
                future_h, future_w = current_h+m[0], current_w+m[1]

                if 0 <= future_h <= height-1 and 0 <= future_w <= width-1:
                    if graph[future_h][future_w] == 1:
                        graph[future_h][future_w] = graph[current_h][current_w]+1
                        queue.append((future_h, future_w))
                    elif graph[future_h][future_w] == 0:
                        continue

        r = graph[height-1][width-1]

        return r if not r == 1 else -1
    
    
    start = (0,0)
    height = len(maps) 
    width = len(maps[0])
    
    answer = bfs(maps, start)
    
    return answer