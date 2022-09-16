from queue import Queue
def solution(map):
    x, y, h, w = 0, 0, len(map), len(map[0])
    paths_len = []
    for i in range(h):
        for j in range(w):
            if map[i][j]:
                seen = {(0, 0)}
                queue = Queue()
                queue.put([(0, 0)])
                map[i][j] = 0
                while not queue.empty():
                    path = queue.get()
                    (x, y) = path[-1]
                    if (x, y) == (w-1, h-1):
                        break
                    for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        if 0 <= x2 < w and 0 <= y2 < h and map[y2][x2] != 1 and (x2, y2) not in seen:
                            queue.put(path + [(x2, y2)])
                            seen.add((x2, y2))
                paths_len.append(len(path) if path[-1] == (w-1, h-1) else w*h)
                map[i][j] = 1
    return min(paths_len)
# The below test is probably one of the most important ones
print(solution( [
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
]))
# Google first two tests
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))