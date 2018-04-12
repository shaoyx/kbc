import argparse

from utils.rdfcleaner import RDFCleaner
from model.dbpedia_graph import DBPediaGraph

import time
import logging

class DBPediaCleaner(RDFCleaner):
    def __init__(self, args):
        super(DBPediaCleaner, self).__init__(args)

    def is_iri(self, label):
        return label.strip().startswith('"') == False

    def load_rdf_graph(self, ent_dict_path, rel_dict_path, path):
        g = DBPediaGraph()
        logger = logging.getLogger()
        g.load_dict(ent_dict_path, rel_dict_path)
        logger.info("Finish loading dict")
        g.load(path)
        return g

    def generate_rdf_dict(self):
        start = time.time()
        prog = 0
        logger = logging.getLogger()

        node_iri_dict = {}
        edge_iri_dict = {}

        with open(self.rdfpath) as fd:
            for line in fd.readlines():
                if line.startswith("#"):
                    continue
                recs = line.strip().split(" ")

                sub = recs[0]
                rel = recs[1]
                obj = recs[2]

                if self.is_iri(obj) == False:
                    continue

                if sub not in node_iri_dict:
                    node_iri_dict[sub] = 1
                else:
                    node_iri_dict[sub] += 1
                
                if rel not in edge_iri_dict:
                    edge_iri_dict[rel] = 1
                else:
                    edge_iri_dict[rel] += 1
                
                if obj not in node_iri_dict:
                    node_iri_dict[obj] = 1
                else:
                    node_iri_dict[obj] += 1

                prog += 1
                if prog % 10000 == 0:
                    logger.info('progress: {}, cost: {}'.format(prog, time.time()-start))
                    start = time.time()
        
        with open(self.outpath+".entlist", "w") as fent, open(self.outpath+".rellist", "w") as frel:
            for k,v in node_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                fent.write("{}\t{}\n".format(k,v))

            for k,v in edge_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                frel.write("{}\t{}\n".format(k,v))

if __name__ == '__main__':  
    p = argparse.ArgumentParser('knowledge graph cleaner')
    p.add_argument('--inpath', type=str, help='path of original knowledge graph')
    p.add_argument('--outpath', type=str, help='path of the cleaned knowledge graph')

    args = p.parse_args()

    dbpediaCleaner = DBPediaCleaner(args)
    dbpediaCleaner.run()
