import sys
import io

from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7688", auth=("neo4j", "123456"))

# kg_path_train = "../KBEcodes/dat/wordnet-mlj12/wordnet-mlj12-train.txt"
# kg_path_train = "../KBEcodes/dat/wordnet-mlj12/test"
# kg_path_train = "../KBEcodes/dat/FB15k/freebase_mtr100_mte100-train.txt"

def add_relation(tx, head, rel, tail):
    tx.run("MERGE (h:Word {name: $head})"
           "MERGE (t:Word {name: $tail})"
           "MERGE (h)-[:Type {name: $rel}]->(t)",
           head=head, rel=rel, tail=tail)

def query_relation(tx, head, tail):
  tx.run("MATCH (h:Word {name: $head}) -[:Type]- (t:Word {name: $tail})",
          head=head, tail=tail)

def import_graph(path):
  with driver.session() as session:
    with open(path, "r") as kg_data:
      cnt = 0;
      for line in kg_data:
        head, rel, tail = line.strip().split('\t')
        cnt = cnt + 1
        if cnt % 10000 == 0:
          print(cnt)
        session.write_transaction(add_relation, head, rel, tail)

def query_graph(path, out_path):
  with driver.session() as session:
    with open(path, "r") as kg_data, open(out_path, "w") as fout:
      cnt = 0
      for line in kg_data:
        head, rel, tail = line.strip().split('\t')
        cnt = cnt + 1
        if cnt % 10000 == 0:
          print(cnt)
        with session.begin_transaction() as tx:
          l = []
          for record in tx.run("MATCH (h:Word {name: $head}) -[r:Type]- (t:Word {name: $tail}) RETURN r.name",
                                head=head, tail=tail):
              l.append(record["r.name"])
          print('{} {} {} {}: {}'.format(head, rel, tail, len(l), l), file=fout)

if __name__ == '__main__':
  in_path = sys.argv[1]
  out_path = sys.argv[2]
  query_graph(in_path, out_path)

