class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        # y = [k,b] y = kx+b
        x1,x2,y1,y2 = None,None,None,None
        if start1[0] == end1[0]:
            x1 = start1[0]
        elif start1[1] == end1[1]:
            y1 = [0,start1[0]]
        else:
            y1 = [(start1[1]-end1[1])/(start1[0]-end1[0]), start1[1] - ((end1[1]-start1[1])/(end1[0]-start1[0]))*start1[0]]
        if start2[0]==end2[0]:
            x2 = start2[0]
        elif start2[1] == end2[1]:
            y2 = [0,start2[0]]
        else:
            y2 = [(start2[1]-end2[1])/(start2[0]-end2[0]), start2[1] - ((end2[1]-start2[1])/(end2[0]-start2[0]))*start2[0]]
        print(y1,y2,x1,x2)
        if x1 == None and x2 == None:
            # 平行
            if y1[0] == y2[0]:
                if y1[1] != y2[1]:
                    return []
                else:
                    if end1[0] < start2[0]:
                        return []
                    else:
                        return [start2[0],start2[1]]
            jdx = (y2[1] - y1[1])/(y1[0]-y2[0])
            if jdx>=min(start1[0],end1[0]) and jdx <= max((start1[0],end1[0])):
                jdy = jdx * y1[0] + y1[1]
                return [jdx,jdy]
            else:
                return []
        if x1 == None and x2 != None:
            jdx = x2
            jdy = jdx*y1[0] + y1[1]
            if jdy >= min(start2[1],end2[1]) and jdy <= max(start2[1],end2[1]):
                return [jdx,jdy]
        if x1 != None and x2 == None:
            jdx = x1
            jdy = jdx*y2[0] + y2[1]
            if jdy >= min(start1[1],end1[1]) and jdy <= max(start1[1],end1[1]):
                return [jdx,jdy]
        if x1 != None and x2 != None:
            if x1 != x2:
                return []
            else:
                if end1[1] < start2[1]:
                    return []
                else:
                    return [x1,int(sorted([start1[1],end1[1],start2[1],end2[1]])[1])]