from graph.graph import Graph, adjacency_dict
inf = float('inf')


def update_dist(node_list, node, dist, prev):
    for i in range(len(node_list)):
        if node_list[i][0] == node and dist < node_list[i][1]:
            node_list[i] = (node, dist, None if prev is None else prev[0])


def pop_smallest(node_list):
    small_value = inf
    small = None
    index = None

    for i in range(len(node_list)):
        if node_list[i][1] < small_value:
            small_value = node_list[i][1]
            index = i

    if (index is None):
        small = node_list.pop(0)
    else:
        small = node_list.pop(index)

    return small


def get_prev(table, node):
    for n in table:
        if n[0] == node:
            return n[2]

    return None


def get_path(table, node):
    if node is None:
        return []

    prev = get_prev(table, node)

    return get_path(table, prev) + [node[0]]


def dijkstra(adj_dict, origin):

    unvisited = [(node, inf) for node in adj_dict]
    visited = []

    update_dist(unvisited, origin, 0, None)
    p = pop_smallest(unvisited)
    visited.append(p)

    while unvisited:
        adj = adj_dict[p[0]]

        # Update the adjacents distancies
        for node in adj:
            n, d = node
            acumulada = p[1] + d

            update_dist(unvisited, n, acumulada, p)

        # Find the unvisited node with the smallest distance from the origin
        p = pop_smallest(unvisited)
        visited.append(p)


    return visited



def main():
    print("\n--- Dijkstra ---\n")

    nodes = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B", 6),
        ("A", "D", 1),
        ("D", "B", 2),
        ("D", "E", 1),
        ("B", "C", 5),
        ("E", "C", 5),
    ]

    G = Graph(nodes, edges, is_directed=False)

    graph = adjacency_dict(G)

    result = dijkstra(graph, "A")
    print(result)

    print("Path: " + str(get_path(result, 'A')))
    print("Path: " + str(get_path(result, 'B')))
    print("Path: " + str(get_path(result, 'C')))
    print("Path: " + str(get_path(result, 'D')))
    print("Path: " + str(get_path(result, 'E')))


if __name__ == "__main__":
    main()




