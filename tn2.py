from random import randrange, choice, sample
from tn3 import Parent


class Genetic_Algo:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.colors = ['blue','green','red','yellow']
        self.parents = []

    def initialization(self):
        for i in range(100):
            self.colored_nodes = [choice(self.colors) for i in range(len(self.nodes))]
            self.parents.append(Parent(self.colored_nodes))

    def parent_selection(self):
        sum = 0
        ranking_list = []
        tmp_parent_lst1 = []
        for parent in self.parents:
            sum += parent.fitness_function(self.edges)
            ranking_list.append(parent.ranking)

        for j in self.parents:
            if j.ranking == max(ranking_list):
                tmp_parent_lst1.append(j)
                break


        #roullete technique
        total = 0
        while total < 9:
             ball = randrange(1,sum+1)
             cnt = 0
             for i in range(len(ranking_list)):
                 cnt += ranking_list[i]
                 if ball <= cnt:
                    if self.parents[i] not in tmp_parent_lst1:
                        tmp_parent_lst1.append(self.parents[i])
                        total+=1
                        break
                    continue
        self.parents = tmp_parent_lst1

        print(max(ranking_list), min(ranking_list))


    def reproduction(self):
        tmp_parent_lst2 = []
        for i in self.parents:
            for j in self.parents:
                tmp_parent_lst2.append(Parent([i.color_map[m] if randrange(0,2) == 0 else j.color_map[m] for m in range(16)]))
        self.parents = tmp_parent_lst2
        self.mutation()

    def mutation(self):
        tmp_mut_lst = [randrange(0,99) for i in range(10)]
        for i in tmp_mut_lst:
            mutation_num = randrange(0,16)
            new_color = choice(self.colors)
            self.parents[i].color_map[mutation_num] = new_color

