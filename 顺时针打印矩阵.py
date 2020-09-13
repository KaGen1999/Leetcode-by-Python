# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []

        def get_circle(s1, s2, s3, s4):
            for i in range(s2, s4 + 1):
                if len(result) == len(matrix) * len(matrix[0]):
                    return result
                result.append(matrix[s1][i])

            for i in range(s1 + 1, s3 + 1):
                if len(result) == len(matrix) * len(matrix[0]):
                    return result
                result.append(matrix[i][s4])
            for i in range(s4 - 1, s1 - 1, -1):
                if len(result) == len(matrix) * len(matrix[0]):
                    return result
                result.append(matrix[s3][i])
            for i in range(s3 - 1, s2 - 0, -1):
                if len(result) == len(matrix) * len(matrix[0]):
                    return result
                result.append(matrix[i][s2])

        s1, s2 = 0, 0
        s3, s4 = len(matrix) - 1, len(matrix[0]) - 1
        if s3 == 0:
            return matrix[0]
        if s3 == -1:
            return []
        if s4 == 0:
            result = [i[0] for i in matrix]
            return result
        while s1 + s2 <= s3 + s4:
            get_circle(s1, s2, s3, s4)
            if len(result) == len(matrix) * len(matrix[0]):
                return result
            s1 = s1 + 1
            s2 = s2 + 1
            s3 = s3 - 1
            s4 = s4 - 1
        return result
