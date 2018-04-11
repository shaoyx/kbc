import argparse

class DBPediaCleaner(object):
    def __init__(self, args):
        self.inpath = args.inpath
        self.outpath = args.outpath
        self.outfd = open(args.outpath, 'w')
        
        self.node_iri_dict = {}
        self.node_literal_dict = {}
        self.edge_iri_dict = {}

        self.node_size = 0
        self.edge_size = 0
        self.attribute_size = 0
        self.edge_iri = 0
        self.node_iri = 0
        self.node_literal = 0

    def _finalize(self):
        self.outfd.close()

    def process_single_line(self, line):
        if line.startswith("#") == False:
            recs = line.split("> ")
            sub = recs[0]+">"
            pre = recs[1]+">" # TODO: has problem here!!!! Copy or reference???
            obj = recs[2]
            is_attribute = obj.startswith('"')
            if is_attribute == False:
                obj = obj + ">"

            if sub not in self.node_iri_dict:
                self.node_iri_dict[sub] = self.node_iri
                self.node_iri = self.node_iri + 1
            if pre not in self.edge_iri_dict:
                self.edge_iri_dict[pre] = self.edge_iri
                self.edge_iri = self.edge_iri + 1
            if is_attribute and obj not in self.node_literal_dict:
                self.node_literal_dict[obj] = self.node_literal
                self.node_literal = self.node_literal + 1
            if is_attribute == False and obj not in self.node_iri_dict:
                self.node_iri_dict[obj] = self.node_iri
                self.node_iri = self.node_iri + 1

            if is_attribute:
                self.attribute_size = self.attribute_size + 1
                self.outfd.write(str(self.node_iri_dict[sub])+"\t"+str(self.edge_iri_dict[pre])+"\t"+str(self.node_literal_dict[obj])+"\tATTR\n")
            else:
                self.edge_size = self.edge_size + 1
                self.outfd.write(str(self.node_iri_dict[sub])+"\t"+str(self.edge_iri_dict[pre])+"\t"+str(self.node_iri_dict[obj])+"\tEDGE\n")

    def run(self):
        with open(self.inpath) as f:
            for line in f.readlines():
                self.process_single_line(line)
        self.node_size = self.node_iri
        self.save_dicts()
        self._finalize()

    def save_dicts(self):
        with open(self.outpath+"_dict", 'w') as fw:
            fw.write("#Node"+
                "\t"+"Edge"+
                "\t"+"Node_iri"+
                "\t"+"Node_literal"+
                "\t"+"Edge_iri"+
                "\n")
            fw.write(str(self.node_size)+
                "\t"+str(self.edge_size)+
                "\t"+str(self.node_iri)+
                "\t"+str(self.node_literal)+
                "\t"+str(self.edge_iri)+
                "\n")
            fw.write(str("#Node\n"))
            for k,v in self.node_iri_dict.items():
                fw.write(k+"\t"+str(v)+"\tIRI\n")

            fw.write(str("#LITERAL\n"))
            for k,v in self.node_literal_dict.items():
                fw.write(k+"\t"+str(v)+"\tLITERAL\n")
            
            fw.write(str("#Edge\n"))
            for k,v in self.edge_iri_dict.items():
                fw.write(k+"\t"+str(v)+"\tIRI"+"\n")

if __name__ == '__main__':	
    p = argparse.ArgumentParser('knowledge graph cleaner')
    p.add_argument('--inpath', type=str, help='path of original knowledge graph')
    p.add_argument('--outpath', type=str, help='path of the cleaned knowledge graph')

    args = p.parse_args()

    dbpediaCleaner = DBPediaCleaner(args)
    dbpediaCleaner.run()