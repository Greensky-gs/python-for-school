import networkx as nx
import matplotlib.pyplot as plt

# Liste des noeuds
LN = ['Laurent', 'Pierre', 'Lucie', 'Sophie', 'Martin','Jacques','Berthe','Yvonne']
LA = [
['Laurent','Pierre', "Berthe"],
['Lucie','Pierre'],
['Sophie','Lucie'],
['Sophie','Martin', "Pierre"],
['Jacques','Berthe'],
['Martin','Laurent', "Jacques", "Lucie"],
['Jacques','Martin'],
['Jacques','Laurent', "Laurent"],
['Berthe', 'Yvonne', "Martin"]
]

# Création d'un nouveau graphe
reseau_social=nx.Graph()

def pcc(A,B):
	ch=nx.shortest_path(reseau_social,A,B)
	return len(ch)-1, ch

def pop(nodeName):
    liste = []
    return len(list(filter(lambda x: nodeName in x, reseau_social.edges)));
# Le diametre d'un graphe est le plus long des plus courts chemins
def diam() :
    r=0
    for e in LN :
        for f in LN :
            temp=pcc(e,f)
            if temp[0] > r :
                r=temp[0]
                chemin=temp[1]
    return r, chemin

for x in list(map(lambda x: [ x[0], x[1:] ], LA)):
    name = x[0];
    links = x[1];

    if len(links) == 1:
        reseau_social.add_edges_from([(name, links[0])])
    else:
        reseau_social.add_edges_from(map(lambda x: ( name, x ), links ))

# Affichage des caractéristiques du graphe
print("nombre de noeuds = ",reseau_social.number_of_nodes())
print("nombre de arêtes = ",reseau_social.number_of_edges())
print('diamètre = ',nx.diameter(reseau_social))
print('centre = ', nx.center(reseau_social))
print('rayon = ',nx.radius(reseau_social))

# Couleurs
colorMap = [];
for node in LN:
    if len(node) <= 5:
        colorMap.append('red')
    else:
        colorMap.append('green')

# Dessin du graphe
nx.draw(reseau_social, node_color=colorMap, with_labels=True)
plt.draw()
plt.show()
plt.close()

