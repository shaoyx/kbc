### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
   // 	TransE Setting
   	batch -----> 128
     cp_ratio -----> 0.5
          dim -----> 64
          ent -----> ../dat/wordnet-mlj12/train.entlist
        epoch -----> 300
     filtered -----> False
     gradclip -----> 5
     graphall -----> None
       l2_reg -----> 0.0001
          log -----> /Users/CaiYaohui/Documents/Lab/KBEcodes/
           lr -----> 0.01
       margin -----> 2.0
       method -----> transe
       metric -----> mrr
         mode -----> pairwise
        nbest -----> None
     negative -----> 10
          opt -----> sgd
          rel -----> ../dat/wordnet-mlj12/train.rellist
    save_step -----> 100
        train -----> ../dat/wordnet-mlj12/wordnet-mlj12-train.txt
        valid -----> None

   // 	Deepwalk Setting
   	
   	Default parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.0166
   Hits@1(filter)      : 0.0256
   Hits@10             : 0.722
   Hits@10(filter)     : 0.8594
   Hits@10(filter)_head_1-1: 0.8333333333333334
   Hits@10(filter)_head_1-n: 0.9262998485613326
   Hits@10(filter)_head_n-1: 0.8126691932864104
   Hits@10(filter)_head_n-n: 0.8610619469026549
   Hits@10(filter)_tail_1-1: 0.8571428571428571
   Hits@10(filter)_tail_1-n: 0.779404341241797
   Hits@10(filter)_tail_n-1: 0.9193286410395235
   Hits@10(filter)_tail_n-n: 0.8601769911504424
   Hits@3              : 0.3807
   Hits@3(filter)      : 0.5117
   MRR                 : 0.24641589115499382
   MRR(filter)         : 0.30840964992250486
   ````

   ​

