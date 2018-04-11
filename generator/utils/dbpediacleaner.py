import argparse

from utils.rdfcleaner import RDFCleaner
from model.dbpedia_graph import DBPediaGraph

class DBPediaCleaner(RDFCleaner):
    def __init__(self, args):
        super(DBPediaCleaner, self).__init__(args)

    def load_rdf_graph(self, path):
        g = DBPediaGraph()
        g.load(path)
        return g

if __name__ == '__main__':  
    p = argparse.ArgumentParser('knowledge graph cleaner')
    p.add_argument('--inpath', type=str, help='path of original knowledge graph')
    p.add_argument('--outpath', type=str, help='path of the cleaned knowledge graph')

    args = p.parse_args()

    dbpediaCleaner = DBPediaCleaner(args)
    dbpediaCleaner.run()