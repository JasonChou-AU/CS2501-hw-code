import numpy as np
import Matrix_transformer as mt

def print_test(name, original, converted):
    print(f"--- Testing: {name} ---")
    print("Original:\n", original)
    print("Converted:\n", converted)
    print("Success:", np.array_equal(original, converted))
    print()


adj_test = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
])


inc_mat = mt.adj_to_inc(adj_test)
adj_back = mt.inc_to_adj(inc_mat)
print_test("Adj <-> Inc", adj_test, adj_back)

el, pl = mt.adj_to_forward_star(adj_test)
adj_back_fs = mt.forward_star_to_adj(el, pl, n=4)
print(f"--- Testing: Adj -> Forward Star ---")
print(f"EL (Edges List): {el}")
print(f"PL (Point List): {pl}")
print("Success:", np.array_equal(adj_test, adj_back_fs))
print()

edge_list = mt.inc_to_edge_list(inc_mat)
inc_back = mt.edge_list_to_inc(edge_list, n=4)
print_test("Inc <-> Edge List", inc_mat, inc_back)