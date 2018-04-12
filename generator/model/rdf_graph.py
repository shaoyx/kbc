from utils.voca import Vocab

class Node(object):
    def __init__(self, nid):
        self.node_id = nid
        self.in_edges = []
        self.out_edges = []

    def degree(self):
        return self.in_degree() + self.out_degree()

    def in_degree(self):
        return len(self.in_edges)

    def out_degree(self):
        return len(self.out_edges)

class RdfGraph(object):
    def __init__(self):
        self.node_size = 0
        self.edge_size = 0
        self.is_directed = False

        self.node_list = []

        self.ent_vocab = None
        self.rel_vocab = None

    def add_edge(self, src, label, dst):
        dst_id = self.ent_vocab[dst]
        rel_id = self.rel_vocab[label]
        src_id = self.ent_vocab[src]

        self.node_list[src_id].out_edges.append( (dst_id, rel_id) ) # outgoing edge
        self.node_list[dst_id].in_edges.append( (src_id, rel_id) ) # incoming edge
        
        self.edge_size += 1


    def get_degree_dist(self):
        return [node.in_degree() for node in self.node_list]

    def extract_edges(self, degree_threshold, relation_threshold):
        print("Threshold: ent={}, rel={}".format(degree_threshold, relation_threshold))
        edge_list = []
        for node in self.node_list:
            if node.degree() >= degree_threshold:
                for (dst, rel) in node.out_edges:
                    if self.node_list[dst].degree() >= degree_threshold and self.rel_vocab.get_frequency(rel):
                        edge_list.append((self.ent_vocab.id2word[node.node_id], self.rel_vocab.id2word[rel], self.ent_vocab.id2word[dst]))
        return edge_list

    def get_size(self):
        return {"node_size":self.node_size, "edge_size":self.edge_size}

    def load_dict(self, ent_dict_path, rel_dict_path):
        self.ent_vocab = Vocab.load(ent_dict_path)
        self.rel_vocab = Vocab.load(rel_dict_path)
        self.node_size = len(self.ent_vocab)
        self.node_list = [Node(i) for i in range(self.node_size)]

    def is_iri(self, str):
        raise NotImplementedError

    def load(self, graph_path):
        raise NotImplementedError