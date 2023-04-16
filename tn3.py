class Parent:

    def __init__(self, color_map):
        self.color_map = color_map
        self.ranking = 0

    def fitness_function(self, edge_lst):
        for i in range(1, len(self.color_map)):
            for j in edge_lst:
                if j[0] == i:
                    if self.color_map[i-1] != self.color_map[j[1] - 1]:
                         self.ranking += 10
        return self.ranking


