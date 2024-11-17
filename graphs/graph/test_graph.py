from graph import Graph, adjacency_dict, adjacency_matrix


def test_adjacency_dict():
    G = Graph(["A", "B", "C"], edges=[("B", "A"), ("B", "C"), ("A", "C")],
              is_directed=False)

    expected_adj_dict = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["B", "A"]
    }

    assert (
        adjacency_dict(G) == expected_adj_dict
    ), "Test failed for adjacency_dict"


def test_adjacency_matrix():
    G = Graph(nodes=range(3), edges=[(1, 0), (1, 2), (0, 2)],
              is_directed=False)

    expected_adj_matrix = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    result_matrix = adjacency_matrix(G)

    assert (
        result_matrix == expected_adj_matrix
    ), "Test failed for adjacency_matrix"


if __name__ == "__main__":
    test_adjacency_dict()
    test_adjacency_matrix()
    print("All quite for now!")

