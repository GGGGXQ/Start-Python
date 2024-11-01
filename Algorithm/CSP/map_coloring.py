from csp import Constraint, CSP


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1, place2):
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2

    def satisfied(self, assignment):
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
    variables = ["Western Australia", "Northern Territory", "South Australia", "Queens land", "New South Wales",
                 "Victoria", "Tasmania"]
    domains = {}
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
    csp = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queens land", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("Queens land", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queens land", "South Australia"))
    csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))
    csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))

    solution = csp.back_tracking_search()
    if solution is None:
        print("No solution found.")
    else:
        print(solution)
