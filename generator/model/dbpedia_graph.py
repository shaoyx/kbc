from model.rdf_graph import RdfGraph

import logging
import time

class DBPediaGraph(RdfGraph):
    def __init__(self):
        super(DBPediaGraph, self).__init__()

    def is_iri(self, label):
        return label.startswith('"') == False

    def load(self, path):
        prog = 0
        start = time.time()
        logger = logging.getLogger()
        with open(path) as fd:
            for line in fd.readlines():
                # add an edge into graph
                if line.startswith("#"):
                    continue
                recs = line.split(" ")
                prog += 1
                self.add_edge(recs[0], recs[1], recs[2])
                if prog % 10000 == 0:
                    logger.info('progress: {}, cost: {}'.format(prog, time.time()-start))
                    start = time.time()
            

