def deIn(x, y, z):
    stack = [(0, 0)]
    already = set()
    while stack:
        cx, cy = stack.pop()
        if z in (cx, cy, cx + cy):
            return True
        if (cx, cy) in already:
            continue
        already.add((cx, cy))
        stack.append((x, cy))
        stack.append((cx, y))
        stack.append((0, cy))
        stack.append((cx, 0))
        stack.append((cx - min(cx, y - cy), cy + min(cx, y - cy)))
        stack.append((cx + min(cy, x - cx), cy - min(cy, x - cx)))
    return False


def deIn2(x, y, z):
    stack = [(0, 0)]
    already = set()
    all = []
    result = []

    def bfs(cx, cy, z, result):
        # print(cx,cy)
        if (cx, cy) in already:
            return
        result.append((cx, cy))
        if z in (cx, cy, cx + cy):
            print(result)

        already.add((cx, cy))
        bfs(x, cy, z, result)
        bfs(cx, y, z, result)
        bfs(0, cy, z, result)
        bfs(cx, 0, z, result)
        bfs(cx - min(cx, y - cy), cy + min(cx, y - cy), z, result)
        bfs(cx + min(cy, x - cx), cy - min(cy, x - cx), z, result)
        # stack.append((cx + min(cy, x - cx), cy - min(cy, x - cx)))

    cx, cy = stack.pop()
    bfs(cx, cy, z, result)


deIn2(6, 5, 3)
