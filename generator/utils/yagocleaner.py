from utils.rdfcleaner import RDFCleaner
from model.yago_graph import YagoGraph

class YagoCleaner(RDFCleaner):
    def __init__(self, args):
        super(YagoCleaner, self).__init__(args)

    def load_rdf_graph(self, path):
        g = YagoGraph()
        g.load(path)
        return g
