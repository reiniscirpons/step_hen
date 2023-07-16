from typing import Set, Dict
from tempfile import NamedTemporaryFile
from step_hen.wordgraph import WordGraph
from graphviz import Digraph


def word_graph_to_dot(
    wg: WordGraph,
    highlight_states: Set[int],
    colors: Dict[int, str],
) -> Digraph:
    f = NamedTemporaryFile(delete=False)
    g = Digraph(
        "G",
        filename=f.name,
        node_attr={"shape": "point", "label": "", "margin": "0"},
        engine="neato",
    )
    f.close()

    for node in wg.nodes:
        if node in highlight_states:
            g.node(str(node), shape="circle", width="0.1")
        else:
            g.node(str(node))

    for node in wg.nodes:
        for letter in range(len(wg.presn.alphabet)):
            child = wg.path(node, letter)
            if letter not in colors or child is None:
                continue
            g.edge(str(node), str(child), color=colors[letter])

    return g
