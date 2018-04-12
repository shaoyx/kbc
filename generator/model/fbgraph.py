from model.rdf_graph import RdfGraph

class FBGraph(RdfGraph):
    def __init__(self):
        super(FBGraph, self).__init__()

    def is_iri(self, label):
        return label.strip().startswith('"') == False

    def load(self, path):
        with open(path) as fd:
            for line in fd.readlines():
                # add an edge into graph
                if line.startswith("#"):
                    continue
                recs = line.split("\t")
                self.add_edge(recs[0], recs[1], recs[2])

    def generator_dict(self, path, out_path):
        start = time()
        prog = 0

        node_iri_dict = {}
        edge_iri_dict = {}

        with open(path) as fd:
            for line in fd.readlines():
                if line.startswith("#"):
                    continue
                recs = line.strip().split("\t")

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
        
        with open(out_path+".entlist", "w") as fent, open(out_path+".rellist", "w") as frel:
            for k,v in node_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                fent.write("{}\t{}".format(k,v))

            for k,v in edge_iri_dict.items():
                if len(k.strip()) == 0:
                    continue
                frel.write("{}\t{}".format(k,v))