from scipy.spatial import ConvexHull

points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]

hull = ConvexHull(points).simplices

print(hull)