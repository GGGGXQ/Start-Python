from csp import CSP, Constraint


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns):
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment):
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True


if __name__ == "__main__":
    test_columns = [1, 2, 3, 4, 5, 6, 7, 8]
    rows = {}
    for column in test_columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp = CSP(test_columns, rows)
    csp.add_constraint(QueensConstraint(test_columns))
    solution = csp.back_tracking_search()
    if solution is None:
        print("No solution found")
    else:
        print(solution)
