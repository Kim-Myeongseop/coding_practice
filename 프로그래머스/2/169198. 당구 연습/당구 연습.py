def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        dist_list = []
        
        if (startY-0) / (startX-0) == (ball[1]-0) / (ball[0]-0):
            if startX < ball[0]:
                d = ((startY-0)**2 + (startX-0)**2) * ((startX-0)+(ball[0]-0) / (startX-0))**2
                dist_list.append(d)
        
        if (startY-0) / (m-startX) == (ball[1]-0) / (m-ball[0]):
            if startX > ball[0]:
                d = ((startY-0)**2 + (m-startX)**2) * ((m-startX)+(m-ball[0]) / (m-startX))**2
                dist_list.append(d)
        
        if (n-startY) / (startX-0) == (n-ball[1]) / (ball[0]-0):
            if startX < ball[0]:
                d = ((n-startY)**2 + (startX-0)**2) * ((startX-0)+(ball[0]-0) / (startX-0))**2
                dist_list.append(d)
        
        if (n-startY) / (m-startX) == (n-ball[1]) / (m-ball[0]):
            if startX > ball[0]:
                d = ((n-startY)**2 + (m-startX)**2) * ((m-startX)+(m-ball[0]) / (m-startX))**2
                dist_list.append(d)
        
        if ball[1] == startY:
            if startX > ball[0]:
                dist_list.append((ball[1]-(startY))**2 + (ball[0]-(2*m - startX))**2)
            else:
                dist_list.append((ball[1]-(startY))**2 + (ball[0]-(-startX))**2)
            dist_list.append((ball[1]-(2*n - startY))**2 + (ball[0]-(startX))**2)
            dist_list.append((ball[1]-(-startY))**2 + (ball[0]-(startX))**2)        
            
        if ball[0] == startX:
            if startY > ball[1]:
                dist_list.append((ball[1]-(2*n - startY))**2 + (ball[0]-(startX))**2)
            else:
                dist_list.append((ball[1]-(-startY))**2 + (ball[0]-(startX))**2)
            dist_list.append((ball[1]-(startY))**2 + (ball[0]-(2*m - startX))**2)
            dist_list.append((ball[1]-(startY))**2 + (ball[0]-(-startX))**2)

        if (ball[1] != startY) and (ball[0] != startX):
            dist_list.append((ball[1]-(startY))**2 + (ball[0]-(-startX))**2)
            dist_list.append((ball[1]-(-startY))**2 + (ball[0]-(startX))**2)
            dist_list.append((ball[1]-(startY))**2 + (ball[0]-(2*m - startX))**2)
            dist_list.append((ball[1]-(2*n - startY))**2 + (ball[0]-(startX))**2)
        
        print(dist_list)
        answer.append(min(dist_list))
    
    return answer