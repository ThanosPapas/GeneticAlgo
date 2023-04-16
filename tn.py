import networkx as nx
import matplotlib.pyplot as plt
from tn2 import Genetic_Algo

nodes = [i for i in range(1,17)]
edges = [(1,2),(1,3),(1,4),(1,13),(1,15),(1,16),(2,3),(2,5),(2,8),(2,9),(2,16),(3,4),(3,5),(3,6),(4,6),(4,13),(5,6),(5,7),(5,9),(5,10),(6,7),(6,11),
         (6,13),(7,10),(7,11),(8,9),(8,14),(9,10),(9,12),(9,14),(10,11),(10,12),(11,12),(11,13),(12,13),(12,14),(12,15),(13,15),(14,15),(15,16)]

tst = Genetic_Algo(nodes,edges)
cnt=0
tst.initialization()
for i in range(40):
    tst.parent_selection()
    tst.reproduction()



color_map = tst.parents[0].color_map
print(color_map)

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=500, node_color=color_map)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()

