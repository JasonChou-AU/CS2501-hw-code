import numpy as np

def adj_to_inc(adj_matrix):
    n = len(adj_matrix)
    edges = [(i, j) for i in range(n) for j in range(n) if adj_matrix[i][j] != 0]
    m = len(edges)
    inc_matrix = np.zeros((n, m), dtype=int)
    for k, (u, v) in enumerate(edges):
        inc_matrix[u][k] = 1  
        inc_matrix[v][k] = -1  
    return inc_matrix

def inc_to_adj(inc_matrix):
    n, m = inc_matrix.shape
    adj_matrix = np.zeros((n, n), dtype=int)
    for k in range(m):
        u = np.where(inc_matrix[:, k] == 1)[0][0]
        v = np.where(inc_matrix[:, k] == -1)[0][0]
        adj_matrix[u][v] = 1
    return adj_matrix

def adj_to_forward_star(adj_matrix):
    n = len(adj_matrix)
    el = []
    pl = [0] * (n + 1)
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0:
                el.append(j)
        pl[i+1] = len(el)
    return el, pl

def forward_star_to_adj(el, pl, n):
    adj_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for idx in range(pl[i], pl[i+1]):
            v = el[idx]
            adj_matrix[i][v] = 1
    return adj_matrix

def inc_to_edge_list(inc_matrix):
    n, m = inc_matrix.shape
    edge_list = []
    for k in range(m):
        u = np.where(inc_matrix[:, k] == 1)[0][0]
        v = np.where(inc_matrix[:, k] == -1)[0][0]
        edge_list.append((u, v))
    return edge_list

def edge_list_to_inc(edge_list, n):
    m = len(edge_list)
    inc_matrix = np.zeros((n, m), dtype=int)
    for k, (u, v) in enumerate(edge_list):
        inc_matrix[u][k] = 1
        inc_matrix[v][k] = -1
    return inc_matrix

