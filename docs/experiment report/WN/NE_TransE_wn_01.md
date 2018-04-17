### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
   //	TransE parameters
        batch -----> 128
     cp_ratio -----> 0.5
          dim -----> 64
          ent -----> ../dat/wordnet-mlj12/train.entlist
        epoch -----> 300
     filtered -----> True
     gradclip -----> 5
     graphall -----> ../dat/wordnet-mlj12/whole.txt
       l2_reg -----> 0.0001
          log -----> ne_transe_wn
           lr -----> 0.01
       margin -----> 2.0
       method -----> transe_set
       metric -----> mrr
         mode -----> pairwise
        nbest -----> None
     negative -----> 10
          opt -----> sgd
          rel -----> ../dat/wordnet-mlj12/train.rellist
    save_step -----> 10
        train -----> ../dat/wordnet-mlj12/wordnet-mlj12-train.txt
        valid -----> None
        
   //	Deepwalk parameters

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
   Hits@1              : 0.1377
   Hits@1(filter)      : 0.2153
   Hits@10             : 0.756
   Hits@10(filter)     : 0.9062
   Hits@10(filter)_head_1-1: 0.9523809523809523
   Hits@10(filter)_head_1-n: 0.9459868753154972
   Hits@10(filter)_head_n-1: 0.8646453708716838
   Hits@10(filter)_head_n-n: 0.8920353982300885
   Hits@10(filter)_tail_1-1: 0.9523809523809523
   Hits@10(filter)_tail_1-n: 0.9442338927991337
   Hits@10(filter)_tail_n-1: 0.8662291771832408
   Hits@10(filter)_tail_n-n: 0.9230088495575222
   Hits@3              : 0.4652
   Hits@3(filter)      : 0.6451
   MRR                 : 0.34160314091138505
   MRR(filter)         : 0.45786996809799346
   ````

   ​