### Experiment Report

1. ##### Parameter Setting

   ````C++
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

   ````
   Hits@1              : 0.0166
   Hits@1(filter)      : 0.0
   Hits@10             : 0.722
   Hits@10(filter)     : 0.0
   Hits@3              : 0.3807
   Hits@3(filter)      : 0.0
   MRR                 : 0.24641589115499382
   MRR(filter)         : 0.0
   ````

   ​