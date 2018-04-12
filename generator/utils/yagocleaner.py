from utils.rdfcleaner import RDFCleaner
from model.yago_graph import YagoGraph

import time
import logging

class YagoCleaner(RDFCleaner):
    def __init__(self, args):
        super(YagoCleaner, self).__init__(args)

    def is_iri(self, label):
        return label.strip().startswith('"') == False

    def load_rdf_graph(self, path):
        g = YagoGraph()
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
                if len(line.strip()) == 0 or line.strip().startswith("#") or line.strip().startswith("@"):
                    continue
                recs = line.strip().split("\t")

                sub = recs[0]
                rel = recs[1]
                obj = recs[2]

                if sub not in node_iri_dict:
                    node_iri_dict[sub] = 1
                else:
                    node_iri_dict[sub] += 1
                
                if rel not in edge_iri_dict:
                    edge_iri_dict[rel] = 1
                else:
                    edge_iri_dict[rel] += 1
                
                if self.is_iri(obj) and obj not in node_iri_dict:
                    node_iri_dict[obj] = 1
                else:
                    node_iri_dict[obj] += 1

                if prog % 10000 == 0:
                    logger.info('progress: {}, cost: {}'.format(prog, time()-start))
                    start = time.time()
        
        with open(self.outpath+".entlist", "w") as fent, open(out_path+".rellist", "w") as frel:
            for k,v in node_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                fent.write("{}\t{}".format(k,v))

            for k,v in edge_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                frel.write("{}\t{}".format(k,v))
