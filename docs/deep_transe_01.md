### Experiment Report

1. ##### Parameter Setting

   ````python
   #	TransE Setting
   	  batch -----> 128
      cp_ratio -----> 0.5
           dim -----> 64
           ent -----> ../dat/wordnet-mlj12/train.entlist
         epoch -----> 300
      filtered -----> False
      gradclip -----> 5
      graphall -----> None
        l2_reg -----> 0.0001
           log -----> deep_transe_wn_sgd_normalized
            lr -----> 0.01
        margin -----> 2.0
        method -----> transe_set
        metric -----> mrr
          mode -----> pairwise
         nbest -----> None
      negative -----> 10
           opt -----> sgd
           rel -----> ../dat/wordnet-mlj12/train.rellist
     save_step -----> 100
         train -----> ../dat/wordnet-mlj12/wordnet-mlj12-train.txt
         valid -----> None

   #	deepwalk setting
   	Default parameters
   ````

2. ##### Results

   ````python
   Hits@1              : 0.0482
   Hits@1(filter)      : 0.0
   Hits@10             : 0.7046
   Hits@10(filter)     : 0.0
   Hits@3              : 0.3017
   Hits@3(filter)      : 0.0
   MRR                 : 0.23765815392234632
   MRR(filter)         : 0.0
   ````

   ​

