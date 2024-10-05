def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    
    def DFS(ticket_list, route):   # 남은 ticket_list와 현재까지 경로를 담은 route를 받는다.
        if not ticket_list:
            return route
        e = route[-1]
        
        next_list = []   # 다음 방문 후보들 index 저장
        for i in range(len(ticket_list)):
            if ticket_list[i][0] == e:
                next_list.append(i)
        
        for i in next_list:   # next_list가 비어있으면 for문이 돌지 않고 => return None
            res = DFS(ticket_list[:i] + ticket_list[i+1:], route + [ticket_list[i][1]])
            if res:   # None이 아니란 얘기는 ticket을 다 소진하고, route를 return했다는 의미
                return res
            else:   # res가 None이라는 것은 그 경우는 끝까지 ticket을 소진하지 못하는 경우의 수이므로,
                pass   # 아무것도 하지 않는다.(백트래킹)
    return DFS(tickets, ["ICN"])   # route는 "ICN" 부터 시작