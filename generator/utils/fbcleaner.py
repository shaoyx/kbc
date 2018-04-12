from utils.rdfcleaner import RDFCleaner
from model.fbgraph import FBGraph

class FBCleaner(RDFCleaner):
    def __init__(self, args):
        super(FBCleaner, self).__init__(args)

    def load_rdf_graph(self, path):
        g = FBGraph()
        g.load(path)
        return g
