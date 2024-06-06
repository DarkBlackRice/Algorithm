# DFS와 BFS_연습필요

import sys
input = sys.stdin.readline

# 탐색함수 만들기 (경험 있음)

# DFS
def dfs(tree,start_node):

    visited_node = [start_node]
    srch_ord = [start_node]
    now = start_node

    while visited_node:
        
        
        dead_end = True
        for n in sorted(tree[now]):
            if n not in srch_ord:
                dead_end = False
                visited_node.append(now)
                srch_ord.append(n)
                now = n
                break
        if dead_end:
            now = visited_node.pop()
        
    return srch_ord


def bfs(tree,start_node):

    visited_node = [start_node]
    srch_ord = [start_node]

    while visited_node:

        now = visited_node.pop(0)
        
        for n in sorted(tree[now]):
            if n not in srch_ord:
                srch_ord.append(n)
                visited_node.append(n)
        
    return srch_ord

    
# 트리만들기 (노베이스)

node, edge, root = map(int,input().split())
input_tree = {}

for i in range(1,node+1):
    input_tree[i] = []

for _ in range(edge):
    n1, n2 = map(int,input().split())
    input_tree[n1].append(n2)
    input_tree[n2].append(n1)

print(*dfs(input_tree,root))
print(*bfs(input_tree,root))


