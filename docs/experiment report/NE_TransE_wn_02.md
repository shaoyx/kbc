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
          log -----> ne_transe_wn_lr003
           lr -----> 0.003
       margin -----> 2.0
       method -----> transe_set
       metric -----> mrr
         mode -----> pairwise
        nbest -----> None
     negative -----> 10
          opt -----> sgd
          rel -----> ../dat/wordnet-mlj12/train.rellist
    save_step -----> 50
        train -----> ../dat/wordnet-mlj12/wordnet-mlj12-train.txt
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
   Hits@1              : 0.1311
   Hits@1(filter)      : 0.2034
   Hits@1(filter)_1-1  : 0.0
   Hits@1(filter)_1-n  : 0.2820790471034109
   Hits@1(filter)_n-1  : 0.2629984856133266
   Hits@1(filter)_n-n  : 0.0
   Hits@10             : 0.7576
   Hits@10(filter)     : 0.8993
   Hits@10(filter)_1-1 : 0.9285714285714286
   Hits@10(filter)_1-n : 0.9347590687601516
   Hits@10(filter)_n-1 : 0.8715295305401313
   Hits@10(filter)_n-n : 0.9017699115044248
   Hits@10_1-1         : 0.9047619047619048
   Hits@10_1-n         : 0.7655657823497564
   Hits@10_n-1         : 0.7137809187279152
   Hits@10_n-n         : 0.863716814159292
   Hits@1_1-1          : 0.0
   Hits@1_1-n          : 0.18137520303194368
   Hits@1_n-1          : 0.1691065118626956
   Hits@1_n-n          : 0.0
   Hits@3              : 0.4739
   Hits@3(filter)      : 0.6432
   Hits@3(filter)_1-1  : 0.5714285714285714
   Hits@3(filter)_1-n  : 0.7043854899837575
   Hits@3(filter)_n-1  : 0.6567390206966178
   Hits@3(filter)_n-n  : 0.5823008849557522
   Hits@3_1-1          : 0.5476190476190477
   Hits@3_1-n          : 0.5268002165674066
   Hits@3_n-1          : 0.4911660777385159
   Hits@3_n-n          : 0.43716814159292033
   MRR                 : 0.340808387246468
   MRR(filter)         : 0.450055077905498
   MRR(filter)_1-1     : 0.3274787749988748
   MRR(filter)_1-n     : 0.5170976324316336
   MRR(filter)_n-1     : 0.482119801666445
   MRR(filter)_n-n     : 0.3205092534588302
   MRR_1-1             : 0.30987613953909643
   MRR_1-n             : 0.38708866994126995
   MRR_n-1             : 0.360904984039134
   MRR_n-n             : 0.2667943597846051
   ````

   ​

