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
           log -----> transe_fb_valid_lr001
            lr -----> 0.001
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
   	Default parateters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.02552013678454741
   Hits@1(filter)      : 0.03962181104095072
   Hits@10             : 0.2616089113101183
   Hits@10(filter)     : 0.32978957525689423
   Hits@10(filter)_head_1-1: 0.34988179669030733
   Hits@10(filter)_head_1-n: 0.6493461404929985
   Hits@10(filter)_head_n-1: 0.05440758293838863
   Hits@10(filter)_head_n-n: 0.3500191834615992
   Hits@10(filter)_tail_1-1: 0.3605200945626478
   Hits@10(filter)_tail_1-n: 0.049878486286309455
   Hits@10(filter)_tail_n-1: 0.5347867298578199
   Hits@10(filter)_tail_n-n: 0.309237400979485
   Hits@3              : 0.13245077957034754
   Hits@3(filter)      : 0.18510775168864588
   MRR                 : 0.10729550263201858
   MRR(filter)         : 0.1425821645481579
   ````

   ​