from model.rdf_graph import RdfGraph

class YagoGraph(RdfGraph):
    def __init__(self):
        super(YagoGraph, self).__init__()

    def is_iri(self, label):
        return label.strip().startswith('"') == False

    def load(self, path):
        with open(path) as fd:
            for line in fd.readlines():
                # add an edge into graph
                if len(line.strip()) == 0 or line.strip().startswith("#") or line.strip().startswith("@"):
                    continue
                recs = line.split("\t")
                self.add_edge(recs[0], recs[1], recs[2])