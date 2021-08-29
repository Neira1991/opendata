import networkx as nx


class GenerateGraph:
    def __init__(self, data_match, data_players):
        self.data_players = data_players
        self.my_iter = iter(data_match)
        graph = nx.Graph()
        graph.edges.data("weight", default=0)
        self.graph = graph
        self.possession_group = None
        self.trackable_object = None
        return None

    def __iter__(self):
        return self

    def __next__(self):
        try:
            possession_group = next(self.my_iter)['possession']['group']
            trackable_object = next(self.my_iter)['possession']['trackable_object']

            if possession_group is None or possession_group == "away team":
                self.possession_group = None
                self.trackable_object = None
                return self
            player_with_possession = list(
                filter(lambda track_item: track_item['trackable_object'] == trackable_object, self.data_players))

            if len(player_with_possession):
                if player_with_possession[0]['team_id'] == 145:
                    if trackable_object is not None and self.trackable_object is None:
                        self.trackable_object = trackable_object
                        return self
                    elif trackable_object is not None and self.trackable_object is not None:
                        if trackable_object != self.trackable_object:
                            has_edge = self.graph.has_edge(self.trackable_object, trackable_object)
                            if not has_edge:
                                self.graph.add_edge(self.trackable_object, trackable_object, weight=1)
                            else:
                                self.graph[self.trackable_object][trackable_object]["weight"] += 1;
                            self.trackable_object = trackable_object
                        else:
                            self.trackable_object = trackable_object
                        return self
                return self
            return self

        except StopIteration:
            raise StopIteration
