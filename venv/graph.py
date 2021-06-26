class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict={}
        for start, end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start]= [end]

    def give(self):
        print(self.dict)

    def give_route(self, start, end,route=[]):
        route = route + [start]
        if start == end:
            return [route]
        if start not in self.dict:
            return []
        froutes = []
        for via in self.dict[start]:
            if via not in route:
                new = self.give_route(via, end, route)
                for index in new:
                    froutes.append(index)

        return froutes



