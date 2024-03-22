def solution(n, wires):
    answer = n-2
    link_dict = {i+1:[]   for i in range(len(wires)+1)}
    for wire in wires:
        link_dict[wire[0]].append(wire[1])
        link_dict[wire[1]].append(wire[0])
    
    for i in range(len(wires)):
        search_zone = [0   for _ in range(len(wires)+1)]
        a, b = wires[i]
        search_zone[a-1] = 1
        a_tree = [l   for l in link_dict[a]   if l != b]
        for link in a_tree:
            if search_zone[link-1] == 0:
                a_tree.extend(link_dict[link])
                search_zone[link-1] = 1
        
        answer = min(answer, abs(n - 2*sum(search_zone)))
        
    return answer

