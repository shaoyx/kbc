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
           log -----> deep_transe_fb_margin1_lr001
            lr -----> 0.001
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

   //	Deepwalk parameters
   	Default paramters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.03627837686851416
   Hits@1(filter)      : 0.07772003182610757
   Hits@1(filter)_1-1  : 0.23877068557919623
   Hits@1(filter)_1-n  : 0.08369668246445498
   Hits@1(filter)_n-1  : 0.051093623423214905
   Hits@1(filter)_n-n  : 0.09000428806788688
   Hits@10             : 0.29450153205464613
   Hits@10(filter)     : 0.4126390276108412
   Hits@10(filter)_1-1 : 0.42671394799054374
   Hits@10(filter)_1-n : 0.5822748815165877
   Hits@10(filter)_n-1 : 0.3554565443814373
   Hits@10(filter)_n-n : 0.43778916247263533
   Hits@10_1-1         : 0.42671394799054374
   Hits@10_1-n         : 0.5590521327014218
   Hits@10_n-1         : 0.34127994445087373
   Hits@10_n-n         : 0.29774989279830283
   Hits@1_1-1          : 0.23877068557919623
   Hits@1_1-n          : 0.08161137440758294
   Hits@1_n-1          : 0.049820622613123484
   Hits@1_n-n          : 0.03613261414159651
   Hits@3              : 0.13805420595554502
   Hits@3(filter)      : 0.22372230028271065
   Hits@3(filter)_1-1  : 0.3309692671394799
   Hits@3(filter)_1-n  : 0.3776303317535545
   Hits@3(filter)_n-1  : 0.2305288739729198
   Hits@3(filter)_n-n  : 0.22999842018551536
   Hits@3_1-1          : 0.32505910165484636
   Hits@3_1-n          : 0.3638862559241706
   Hits@3_n-1          : 0.2221386413609536
   Hits@3_n-n          : 0.12439910627637726
   MRR                 : 0.12214087791114143
   MRR(filter)         : 0.18859480210304141
   MRR(filter)_1-1     : 0.3080977302668133
   MRR(filter)_1-n     : 0.2662837460581834
   MRR(filter)_n-1     : 0.16255604217763184
   MRR(filter)_n-n     : 0.20178123879398316
   MRR_1-1             : 0.30657557273717645
   MRR_1-n             : 0.25412002115147764
   MRR_n-1             : 0.15513055335887563
   MRR_n-n             : 0.12046159455406383
   ````

   ​