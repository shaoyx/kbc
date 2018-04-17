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
      graphall -----> ../dat/FB15k/freebase_mtr100_mte100-test.txt
        l2_reg -----> 0.0001
           log -----> deep_transe_fb_valid_lr01
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
         valid -----> ../dat/FB15k/freebase_mtr100_mte100-valid.txt

   //	Deepwalk parameters
   	Default parameters

   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.03627837686851416
   Hits@1(filter)      : 0.07772003182610757
   Hits@10             : 0.29450153205464613
   Hits@10(filter)     : 0.4126390276108412
   Hits@10(filter)_head_1-1: 0.42671394799054374
   Hits@10(filter)_head_1-n: 0.6385834972804073
   Hits@10(filter)_head_n-1: 0.11848341232227488
   Hits@10(filter)_head_n-n: 0.43778916247263533
   Hits@10(filter)_tail_1-1: 0.44562647754137114
   Hits@10(filter)_tail_1-n: 0.14894109478069667
   Hits@10(filter)_tail_n-1: 0.5520379146919431
   Hits@10(filter)_tail_n-n: 0.41237671804825204
   Hits@3              : 0.13805420595554502
   Hits@3(filter)      : 0.22372230028271065
   MRR                 : 0.12214087791114143
   MRR(filter)         : 0.18859480210304141
   ````

   ​