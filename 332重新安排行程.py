import copy


class Solution:
    def findItinerary(self, tickets):
        d = {}
        p_index = 0
        for each in tickets:
            for p in each:
                if p not in d.keys():
                    d[p] = p_index
                    p_index = p_index + 1
        ptp = [[0 for _ in range(p_index)] for _ in range(p_index)]
        one_nums = 0
        for each in tickets:
            ptp[d[each[0]]][d[each[1]]] = 1
            one_nums = one_nums + 1
        result = []
        for each in ptp:
            print(each)
        def find_way(start_index, one_nums, way, ptp):
            if one_nums == 0:
                result.append(copy.deepcopy(way))
                return
            for i in range(len(ptp[start_index])):
                if ptp[start_index][i] == 1:
                    for key in d.keys():
                        if d[key] == i:
                            way.append(key)
                            break
                    one_nums = one_nums - 1
                    ptp[start_index][i] = 0
                    tmp_index = start_index
                    start_index = i
                    find_way(start_index, one_nums, way, ptp)
                    start_index = tmp_index
                    ptp[start_index][i] = 1
                    one_nums = one_nums + 1
                    way.pop()

        find_way(d['JFK'], one_nums, ['JFK'], ptp)
        return min(result)


if __name__ == '__main__':
    s = Solution()
    # s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
    s.findItinerary(
        [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"],
         ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]])
