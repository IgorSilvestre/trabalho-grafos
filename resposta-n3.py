from igraph import *

g = Graph(directed=False)

g.add_vertices(10)
g.vs['name'] = ['Sao Paulo','Florianopolis','Curitiba','Santos','Salvador','Blumenau','Porto Alegre','Canoas','Santa Cruz','Uberlandia']
g.vs[0]['edges'] = [1,3,5]
g.vs[1]['edges'] = [0,8,2]
g.vs[2]['edges'] = [3,1]
g.vs[3]['edges'] = [4,2,0]
g.vs[4]['edges'] = [5,3]
g.vs[5]['edges'] = [7,4,0]
g.vs[6]['edges'] = [8,7,]
g.vs[7]['edges'] = [6,5]
g.vs[8]['edges'] = [1,6,9]
g.vs[9]['edges'] = [8]

g.add_edges([(0,1),(1,8),(8,6),(6,7),(7,5),(5,4),(4,3),(3,2),(2,1),(9,8),(3,0),(5,0)])
g.es['weight']=[7,9,6,3,9,18,3,2,5,2,3,8]


def one_vertex_search (graph, begin_vertex, end_vertex):
    result = []
    result_weight = []
    for begin_adj in graph.get_adjlist()[begin_vertex]:
        for end_adj in graph.get_adjlist()[end_vertex]:
            if begin_adj == end_adj:
                begin_adj_id = g.get_eid(begin_vertex, begin_adj)
                end_adj_id = g.get_eid(end_vertex, end_adj)
                result_weight.append(g.es[begin_adj_id]['weight'])
                result_weight.append(g.es[end_adj_id]['weight'])
                result.append([begin_vertex, begin_adj, end_vertex])
    
    if len(result) > 1:
        first_path = result_weight[0] + result_weight[1]
        second_path = result_weight[2] + result_weight[3]
        result_weight = [first_path, second_path]
        if first_path > second_path:
            return result[1]
        else:
            return result[0]

    return result

def dfs (graph, begin_vertex, end_vertex):
    for begin_adj in graph.get_adjlist()[begin_vertex]:
        if begin_adj == end_vertex:
            return begin_vertex, end_vertex

    single_step_search = one_vertex_search(graph, begin_vertex, end_vertex)
    if single_step_search:
        return single_step_search

    for begin_adj in graph.get_adjlist()[begin_vertex]:
        double_step_search = one_vertex_search(graph, begin_adj, end_vertex)
        if double_step_search:
            return begin_vertex, double_step_search

    for begin_adj in graph.get_adjlist()[begin_vertex]:
        for end_adj in graph.get_adjlist()[end_vertex]:
            triple_step_search = one_vertex_search(graph, begin_adj, end_adj)
            if triple_step_search:
                return begin_vertex, triple_step_search, end_vertex

    return 'Error'

#Trocar os numero do segundo e terceiro argumento com os vértices que deseja usar
# Lembrar que no gráfico os vertices começam por 1 e no código começam por 0
print(str(dfs(g, 2, 7))) 

print('\n\n-------------------------\n')
# print(g.vs[0]['name'])

# se quiser ver a lista de arestas
# print(g.get_adjlist())

# se quiser ver a matrix
# print('\nMatriz:\n' + str(g.get_adjacency())) 