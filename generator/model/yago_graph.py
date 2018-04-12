from model.rdf_graph import RdfGraph

import time
import logging

class YagoGraph(RdfGraph):
    def __init__(self):
        super(YagoGraph, self).__init__()

    def is_iri(self, label):
        return label.strip().startswith('"') == False

    def load(self, path):
        start = time.time()
        prog = 0
        logger = logging.getLogger()
        with open(path) as fd:
            for line in fd:
                # add an edge into graph
                if len(line.strip()) == 0 or line.strip().startswith("#") or line.strip().startswith("@"):
                    continue
                recs = line.split("\t")
                
                prog += 1
                sub = recs[0]
                rel = recs[1]
                obj = recs[2].strip('. \n')

                if self.is_iri(sub) and self.is_iri(obj):
                    self.add_edge(sub, rel, obj)

                if prog % 10000 == 0:
                    logger.info('progress: {}, cost: {}'.format(prog, time.time()-start))
                    start = time.time()