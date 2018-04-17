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
     graphall -----> ../dat/FB15k/whole.txt
       l2_reg -----> 0.0001
          log -----> ne_transe_fb15k
           lr -----> 0.01
       margin -----> 1.0
       method -----> transe_set
       metric -----> mrr
         mode -----> pairwise
        nbest -----> None
     negative -----> 10
          opt -----> sgd
          rel -----> ../dat/FB15k/train.rellist
    save_step -----> 10
        train -----> ../dat/FB15k/freebase_mtr100_mte100-train.txt
        valid -----> None
        
   //	NE parameters

   改过的
   --format edgelist
   --number-walks 30
   --input xxxxxx
   --output xxxxxx
   --walk-length 50
   --window-size 7

   没动的
   --excludlist default
   --matfile-variable-name default='network',
   --max-memory-data-size default=1000000000, type=int
   --representation-size', default=64, type=int,
   --seed', default=0, type=int,
   --undirected', default=True, type=bool,
   --vertex-freq-degree, default=False
   --workers', default=1, type=int
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.038165935907636575
   Hits@1(filter)      : 0.1251544751231569
   Hits@10             : 0.4391664268422745
   Hits@10(filter)     : 0.6386551776675526
   Hits@10(filter)_head_1-1: 0.6997635933806147
   Hits@10(filter)_head_1-n: 0.8518689966439069
   Hits@10(filter)_head_n-1: 0.33061611374407585
   Hits@10(filter)_head_n-n: 0.6752352795143199
   Hits@10(filter)_tail_1-1: 0.6973995271867612
   Hits@10(filter)_tail_1-n: 0.29498900590209465
   Hits@10(filter)_tail_n-1: 0.8327962085308057
   Hits@10(filter)_tail_n-n: 0.6387867024757949
   Hits@3              : 0.21710314706031725
   Hits@3(filter)      : 0.4190211779045555
   MRR                 : 0.16953203351983018
   MRR(filter)         : 0.30760457349241055
   ````

   ​