### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
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

   ````reStructuredText
   Hits@1              : 0.0482
   Hits@1(filter)      : 0.0857
   Hits@10             : 0.7046
   Hits@10(filter)     : 0.8529
   Hits@10(filter)_head_1-1: 0.8333333333333334
   Hits@10(filter)_head_1-n: 0.8571428571428571
   Hits@10(filter)_head_n-1: 0.8657282079047104
   Hits@10(filter)_head_n-n: 0.8132743362831858
   Hits@10(filter)_tail_1-1: 0.9047619047619048
   Hits@10(filter)_tail_1-n: 0.8632004038364463
   Hits@10(filter)_tail_n-1: 0.8624796968056307
   Hits@10(filter)_tail_n-n: 0.8292035398230089
   Hits@3              : 0.3017
   Hits@3(filter)      : 0.4559
   MRR                 : 0.23765815392234632
   MRR(filter)         : 0.32556975553752243
   ````

   ​

