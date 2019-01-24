

class HausdorffMetricMatrix:
    D = []

    def __init__(self,Dist):

        for dist_row in range(len(Dist)):
            D_row = []
            for dist_col in range(len(dist_row)):
                D_row.append(self.HD(dist_row, dist_col, Dist))
            self.D.append(D_row)

    def HD(self, x, y, Dist):
        min_over_x = self.get_min_over_x(x,y,Dist)
        median_over_y = self.get_median_over_y(min_over_x,y,Dist)

        min_over_y = self.get_min_over_y(x,y,Dist)
        median_over_x = self.get_median_over_x(min_over_y,y,Dist)

        return max(median_over_y, median_over_x)

    def min_over_x(self, x, y, Dist):
        values = [Dist(i, y) for x in Dist]

