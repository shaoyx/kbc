from utils.voca import Vocab

class Edge(object):
    def __init__(self, dst, label, direction):
        self.dst = dst
        self.label = label
        self.direction = direction

class Node(object):
    def __init__(self, nid, label):
        self.node_id = nid
        self.label = label
        self.in_edges = []
        self.out_edges = []

    def degree(self):
        return self.in_degree() + self.out_degree()

    def in_degree(self):
        return len(self.in_edges)

    def out_degree(self):
        return len(self.out_edges)

    def add_edge(self, dst, label, direction=0):
        if direction == 0 or direction == -1: #out going or undirected
            self.out_edges.append(Edge(dst, label, direction))
        elif direction == 1:
            self.in_edges.append(Edge(dst, label, direction))
        else:
            print("Direction {} is not correct!".format(direction))

class RdfGraph(object):
    def __init__(self):
        self.node_size = 0
        self.edge_size = 0
        self.is_directed = False

        self.node_list = []

        self.iri_vocab = Vocab()
        self.rel_vocab = Vocab()
        # self.literal_vocab = Vocab()

    def _get_or_create_iri_id(self, iri):
        if self.iri_vocab.exist(iri) == False:
            self.iri_vocab.add(iri)
        return self.iri_vocab[iri]

    def _get_or_create_rel_id(self, rel):
        if self.rel_vocab.exist(rel) == False:
            self.rel_vocab.add(rel)
        return self.rel_vocab[rel]

    # def _get_or_create_literal_id(self, literal):
    #     if self.literal_vocab.exist(literal) == False:
    #         self.literal_vocab.add(literal)
    #     return self.literal_vocab[literal]

    def add_edge(self, src, label, dst):
        if self.is_iri(dst):
            dst_id = self._get_or_create_iri_id(dst)
            rel_id = self._get_or_create_rel_id(label)
            src_id = self._get_or_create_iri_id(src)
            if dst_id == self.node_size:
                self.node_size += 1
                self.node_list.append(Node(dst_id, dst))

            if src_id == self.node_size:
                self.node_size += 1
                self.node_list.append(Node(src_id, src))

            self.node_list[src_id].add_edge(dst_id, label, -1)# outgoing edge
            self.node_list[dst_id].add_edge(src_id, label, 1) # incoming edge
            self.edge_size += 1

        else:
            # skip literal
            # dst_id = self._get_or_create_literal_id(dst)
            return
            # Do nothing

    def get_degree_dist(self):
        return [node.in_degree() for node in self.node_list]

    def extract_edges(self, degree_threshold, relation_threshold):
        print("Threshold: ent={}, rel={}".format(degree_threshold, relation_threshold))
        edge_list = []
        for node in self.node_list:
            if node.degree() >= degree_threshold:
                for edge in node.out_edges:
                    dst = edge.dst
                    rel = edge.label
                    if self.node_list[dst].degree() >= degree_threshold and self.rel_vocab.get_frequency(rel):
                        edge_list.append((self.iri_vocab.id2word[node.node_id], rel, self.iri_vocab.id2word[dst]))
        return edge_list

    def get_size(self):
        return {"node_size":self.node_size, "edge_size":self.edge_size}

    def is_iri(self, str):
        raise NotImplementedError
    
    def load(cls, graph_path):
        raise NotImplementedError