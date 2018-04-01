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
   Hits@1(filter)_1-1  : 0.0
   Hits@1(filter)_1-n  : 0.11938278289117488
   Hits@1(filter)_n-1  : 0.11130742049469965
   Hits@1(filter)_n-n  : 0.0
   Hits@10             : 0.7046
   Hits@10(filter)     : 0.8529
   Hits@10(filter)_1-1 : 0.8333333333333334
   Hits@10(filter)_1-n : 0.892528424472117
   Hits@10(filter)_n-1 : 0.8321554770318021
   Hits@10(filter)_n-n : 0.8132743362831858
   Hits@10_1-1         : 0.8333333333333334
   Hits@10_1-n         : 0.7171088251218192
   Hits@10_n-1         : 0.6686017163048965
   Hits@10_n-n         : 0.7530973451327434
   Hits@1_1-1          : 0.0
   Hits@1_1-n          : 0.0676773145641581
   Hits@1_n-1          : 0.06309944472488642
   Hits@1_n-n          : 0.0
   Hits@3              : 0.3017
   Hits@3(filter)      : 0.4559
   Hits@3(filter)_1-1  : 0.3333333333333333
   Hits@3(filter)_1-n  : 0.5075798592311858
   Hits@3(filter)_n-1  : 0.47324583543664817
   Hits@3(filter)_n-n  : 0.3345132743362832
   Hits@3_1-1          : 0.2857142857142857
   Hits@3_1-n          : 0.34028153762858687
   Hits@3_n-1          : 0.31726400807672894
   Hits@3_n-n          : 0.23185840707964603
   MRR                 : 0.23765815392234632
   MRR(filter)         : 0.32556975553752243
   MRR(filter)_1-1     : 0.2363423822070437
   MRR(filter)_1-n     : 0.3649080508731099
   MRR(filter)_n-1     : 0.3402247198196035
   MRR(filter)_n-n     : 0.23741562550046966
   MRR_1-1             : 0.22214170193493482
   MRR_1-n             : 0.2614639961475775
   MRR_n-1             : 0.24377789040109837
   MRR_n-n             : 0.19802840893401796
   ````

   ​

