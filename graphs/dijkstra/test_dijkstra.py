from graph.graph import Graph, adjacency_dict


def main():
    print("--- Testing Dijkstra ---\n")

    G = Graph(["A", "B", "C"],
              edges=[("B", "A"), ("B", "C"), ("A", "C")],
              is_directed=False)

    expected_adj_dict = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["B", "A"]
    }

    assert (
        adjacency_dict(G) == expected_adj_dict
    ), "Test failed for adjacency_dict"



if __name__ == "__main__":
    main()

