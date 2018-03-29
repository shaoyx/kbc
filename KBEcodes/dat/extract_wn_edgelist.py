import_path = "./FB15k/freebase_mtr100_mte100-train.txt"
export_path = "./FB15k/FB15k.edgelist"
with open(import_path, "r") as in_file, open(export_path, "w") as out_file:
	ent = []
	for line in in_file:
		sub, rel, obj = line.strip().split('\t')
		print(sub, obj, file=out_file)
		print(obj, sub, file=out_file)
