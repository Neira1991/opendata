import json
import matplotlib.pyplot as plt
from makegraph.generate_graph import GenerateGraph
import networkx as nx


def run():
    # Opening JSON file
    f = open('data/matches/2068/structured_data.json', 'r')
    p = open('data/matches/2068/match_data.json', 'r')
    data = json.load(f)
    data_players = json.load(p)
    f.close()
    p.close()
    match_iterator = GenerateGraph(data, data_players['players'])
    graph_match = None;
    for element in match_iterator:
        graph_match = element.graph

    enlarge = [(u, v) for (u, v, d) in graph_match.edges(data=True) if d["weight"] > 2]
    small = [(u, v) for (u, v, d) in graph_match.edges(data=True) if d["weight"] <= 1]

    node_pos = nx.circular_layout(graph_match)
    nx.draw_networkx_edges(graph_match, node_pos, edgelist=enlarge)
    nx.draw_networkx_edges(graph_match, node_pos, edgelist=small, alpha=0.5, edge_color="b", style="dashed")
    nx.draw_networkx_labels(graph_match, node_pos, font_size=20, font_family="sans-serif")
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run()
