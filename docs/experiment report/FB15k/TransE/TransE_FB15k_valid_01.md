### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
   //	TransE parameters
         batch -----> 128
      cp_ratio -----> 0.5
           dim -----> 64
           ent -----> ../dat/FB15k/train.entlist
         epoch -----> 300
      filtered -----> True
      gradclip -----> 5
      graphall -----> ../dat/FB15k/freebase_mtr100_mte100-test.txt
        l2_reg -----> 0.0001
           log -----> transe_fb_valid_lr01
            lr -----> 0.01
        margin -----> 1.0
        method -----> transe
        metric -----> mrr
          mode -----> pairwise
         nbest -----> None
      negative -----> 10
           opt -----> sgd
           rel -----> ../dat/FB15k/train.rellist
     save_step -----> 10
         train -----> ../dat/FB15k/freebase_mtr100_mte100-train.txt
         valid -----> ../dat/FB15k/freebase_mtr100_mte100-valid.txt
   //	Deepwalk parameters
   	Default parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.0423134871595199
   Hits@1(filter)      : 0.06658089417819235
   Hits@10             : 0.32724179377359447
   Hits@10(filter)     : 0.43179394288229417
   Hits@10(filter)_head_1-1: 0.5035460992907801
   Hits@10(filter)_head_1-n: 0.7272306446013193
   Hits@10(filter)_head_n-1: 0.11355450236966824
   Hits@10(filter)_head_n-n: 0.45977115258751045
   Hits@10(filter)_tail_1-1: 0.524822695035461
   Hits@10(filter)_tail_1-n: 0.11422289086911237
   Hits@10(filter)_tail_n-1: 0.6496682464454976
   Hits@10(filter)_tail_n-n: 0.41693561127536166
   Hits@3              : 0.15882581977620153
   Hits@3(filter)      : 0.2391782769887085
   MRR                 : 0.1361710796222476
   MRR(filter)         : 0.19010919877750462
   ````

   ​