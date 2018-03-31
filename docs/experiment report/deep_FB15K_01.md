### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
   //	TransE parameters
        batch -----> 128
     cp_ratio -----> 0.5
          dim -----> 64
          ent -----> ../dat/FB15k/train.entlist
        epoch -----> 300
     filtered -----> False
     gradclip -----> 5
     graphall -----> None
       l2_reg -----> 0.0001
          log -----> deep_transe_fb_margin1_lr01
           lr -----> 0.01
       margin -----> 1.0
       method -----> transe_set
       metric -----> mrr
         mode -----> pairwise
        nbest -----> None
     negative -----> 10
          opt -----> sgd
          rel -----> ../dat/FB15k/train.rellist
    save_step -----> 100
        train -----> ../dat/FB15k/freebase_mtr100_mte100-train.txt
        valid -----> None

   //	deepwalk parameters
   	Default parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.03705710077703103
   Hits@1(filter)      : 0.0
   Hits@10             : 0.3727632848605915
   Hits@10(filter)     : 0.0
   Hits@3              : 0.17662643259805996
   Hits@3(filter)      : 0.0
   MRR                 : 0.14675161164906228
   MRR(filter)         : 0.0
   ````

   ​

