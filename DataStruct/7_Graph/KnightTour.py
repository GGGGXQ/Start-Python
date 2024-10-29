from pythonds.graphs import Graph


def knight_graph(bd_size):
    kt_graph = Graph()
    for row in range(bd_size):
        for col in range(bd_size):
            node_id = pos_to_node_id(row, col, bd_size)
            new_position = gen_legal_moves(row, col, bd_size)
            for e in new_position:
                nid = pos_to_node_id(e[0], e[1], bd_size)
                kt_graph.addEdge(node_id, nid)
    return kt_graph


def pos_to_node_id(row, col, bd_size):
    return row * bd_size + col


def gen_legal_moves(x, y, bd_size):
    new_moves = []
    move_off_sets = [(-1, 2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in move_off_sets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x, bd_size) and legal_coord(new_y, bd_size):
            new_moves.append([new_x, new_y])
    return new_moves


def legal_coord(x, bd_size):
    if 0 <= x < bd_size:
        return True
    else:
        return False


def knight_tour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbr_list = list(order_by_avail(u))
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].getColor() is 'white':
                done = knight_tour(n + 1, path, nbr_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


def order_by_avail(n):
    res_list = []
    for v in n.getConnections():
        if v.getCOlor() is 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() is 'white':
                    c += 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]
