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

    def generator_rdf_dict(self):
        start = time()
        prog = 0

        node_iri_dict = {}
        edge_iri_dict = {}

        with open(self.graph) as fd:
            for line in fd.readlines():
                if line.startswith("#"):
                    continue
                recs = line.strip().split(" ")

                sub = recs[0]
                rel = recs[1]
                obj = recs[2]

                if sub not in self.node_iri_dict:
                    node_iri_dict[sub] = 1
                else:
                    node_iri_dict[sub] += 1
                
                if rel not in self.edge_iri_dict:
                    edge_iri_dict[rel] = 1
                else:
                    edge_iri_dict[rel] += 1
                
                if self.is_iri(obj) and obj not in node_iri_dict:
                    node_iri_dict[obj] = 1
                else:
                    node_iri_dict[obj] += 1

                if prog % 10000 == 0:
                    logger.info('progress: {}, cost: {}'.format(prog, time()-start))
                    start = time()
        
        with open(self.outpath+".entlist", "w") as fent, open(out_path+".rellist", "w") as frel:
            for k,v in node_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                fent.write("{}\t{}".format(k,v))

            for k,v in edge_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                frel.write("{}\t{}".format(k,v))

if __name__ == '__main__':  
    p = argparse.ArgumentParser('knowledge graph cleaner')
    p.add_argument('--inpath', type=str, help='path of original knowledge graph')
    p.add_argument('--outpath', type=str, help='path of the cleaned knowledge graph')

    args = p.parse_args()

    dbpediaCleaner = DBPediaCleaner(args)
    dbpediaCleaner.run()