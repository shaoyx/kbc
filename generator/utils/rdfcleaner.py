import argparse
import random

import time
import logging

class RDFCleaner(object):
    def __init__(self, args):
        self.entity_freq_threshold = args.ent_th
        self.relation_freq_threshold = args.rel_th

        self.rdfpath = args.graph
        self.ent_dict_path = args.ent_dict
        self.rel_dict_path = args.rel_dict
        self.outpath = args.outpath

        self.valid_size = args.valid_size
        self.test_size = args.test_size

        self.train_triples = []
        self.test_triples = []
        self.valid_triples = []

    def _finalize(self):
        with open(self.outpath+".train", "w") as otrain, \
             open(self.outpath+".test", "w") as otest, \
             open(self.outpath+".valid", "w") as ovalid:
            for e in self.train_triples:
                otrain.write(e[0]+"\t"+e[1]+"\t"+e[2]+"\n")
            for e in self.test_triples:
                otest.write(e[0]+"\t"+e[1]+"\t"+e[2]+"\n")
            for e in self.valid_triples:
                ovalid.write(e[0]+"\t"+e[1]+"\t"+e[2]+"\n")

    def run(self):
        start = time.time()
        logger = logging.getLogger()
        logger.info("Beging Loading graphs ... ")
        g = self.load_rdf_graph(self.ent_dict_path, self.rel_dict_path, self.rdfpath)
        logger.info("Graph size{}, cost: {}".format(g.get_size(), time.time() - start))
        start = time.time()
        logger.info("Extracting triples ... ")
        triples = self.extract_triples(g)
        logger.info("Extracting cost: {}".format(time.time() - start))
        start = time.time()
        logger.info("Spliting test/train/valid sets ... ")
        self.split_datasets(triples)
        logger.info("Spliting cost: {}".format(time.time() - start))
        self._finalize()

    def load_rdf_graph(self, path):
        raise NotImplementedError

    def generate_rdf_dict(self):
        raise NotImplementedError

    def extract_triples(self, rdfgraph):
        degree_dist = rdfgraph.get_degree_dist()
        deg_sort = sorted(degree_dist)
        deg_threashold = max(10, deg_sort[int(len(deg_sort) * self.entity_freq_threshold)])
        return rdfgraph.extract_edges(deg_threashold, self.relation_freq_threshold)

    def split_datasets(self, triples):
        rands = random.sample(range(len(triples)), self.valid_size + self.test_size)

        valid_set = set([rands[x] for x in range(self.valid_size)])
        test_set = set([rands[x] for x in range(self.valid_size, self.valid_size+self.test_size)])

        for idx in range(0, len(triples)):
            if idx in valid_set:
                self.valid_triples.append(triples[idx])
            elif idx in test_set:
                self.test_triples.append(triples[idx])
            else:
                self.train_triples.append(triples[idx])
