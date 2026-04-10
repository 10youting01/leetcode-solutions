class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        smooth = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum_val = 0
                count = 0
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if 0 <= i+x < m and 0 <= j+y < n:
                            sum_val += img[i+x][j+y]
                            count += 1
                smooth[i][j] = sum_val//count
        return smooth
