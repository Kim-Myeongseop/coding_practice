import sys
sys.setrecursionlimit(10000)

def preorder(answer, linked_list, node):   # root -> left -> right
    answer[0].append(node)
    if linked_list[node][0]:   # 좌측 자식 노드가 있으면
        preorder(answer, linked_list, linked_list[node][0])
    if linked_list[node][1]:   # 우측 자식 노드가 있으면
        preorder(answer, linked_list, linked_list[node][1])

def postorder(answer, linked_list, node):   # left -> right -> root
    if linked_list[node][0]:   # 좌측 자식 노드가 있으면
        postorder(answer, linked_list, linked_list[node][0])
    if linked_list[node][1]:   # 우측 자식 노드가 있으면
        postorder(answer, linked_list, linked_list[node][1])
    answer[1].append(node)

def add_node(new_node, node, nodeinfo, linked_list):
    if nodeinfo[new_node-1][0] < nodeinfo[node-1][0]:   # x값 비교
        if linked_list[node][0]:   # left
            add_node(new_node, linked_list[node][0], nodeinfo, linked_list)
        else:   # linked_list[node][0] == None
            linked_list[node][0] = new_node
            linked_list[new_node] = [None, None]
    else:
        if linked_list[node][1]:
            add_node(new_node, linked_list[node][1], nodeinfo, linked_list)
        else:   # linked_list[node][1] == None
            linked_list[node][1] = new_node
            linked_list[new_node] = [None, None]

def solution(nodeinfo):
    answer = [[], []]
    # y값에 따라 level 별로 나누기(dict)
    level_dict = {}
    for i, node in enumerate(nodeinfo, 1):
        x, y = node
        if level_dict.get(y):
            level_dict[y].append(i)
        else:
            level_dict[y] = [i]
    level_list = sorted(level_dict, reverse=True)   # [6,5,3,2,1]
    
    # linked_list
    linked_list = {}
    for level in level_list:
        level_dict[level].sort(key=lambda x: nodeinfo[x-1][0])
        for new_node in level_dict[level]:
            if not linked_list:   # root node 처리
                root_node = new_node
                linked_list[new_node] = [None, None]
            else:
                add_node(new_node, root_node, nodeinfo, linked_list)
                
    preorder(answer, linked_list, root_node)
    postorder(answer, linked_list, root_node)
    return answer