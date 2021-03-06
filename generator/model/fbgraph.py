from model.rdf_graph import RdfGraph

# import logging
# import time

class FBGraph(RdfGraph):
    def __init__(self):
        super(FBGraph, self).__init__()

    def is_iri(self, label):
        return label.strip().startswith('"') == False

    def load(self, path):
        # prog = 0
        # start = time.time()
        # logger = logging.getLogger()
        with open(path) as fd:
            for line in fd:
                # add an edge into graph
                if line.startswith("#"):
                    continue
                recs = line.strip().split("\t")
                # prog += 1
                sub = recs[0]
                rel = recs[1]
                obj = recs[2]

                if self.is_iri(sub) and self.is_iri(obj):
                    self.add_edge(sub, rel, obj)
                # if prog % 10000 == 0:
                #     logger.info('progress: {}, cost: {}'.format(prog, time.time()-start))
                #     start = time.time()
            

    