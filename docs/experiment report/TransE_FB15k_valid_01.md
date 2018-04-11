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
           log -----> transe_fb_valid_lr01
            lr -----> 0.01
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
   	Default parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.0423134871595199
   Hits@1(filter)      : 0.06658089417819235
   Hits@1(filter)_1-1  : 0.23286052009456265
   Hits@1(filter)_1-n  : 0.12890995260663507
   Hits@1(filter)_n-1  : 0.07869459553292443
   Hits@1(filter)_n-n  : 0.07181385271615247
   Hits@10             : 0.32724179377359447
   Hits@10(filter)     : 0.43179394288229417
   Hits@10(filter)_1-1 : 0.5035460992907801
   Hits@10(filter)_1-n : 0.6524170616113744
   Hits@10(filter)_n-1 : 0.398275662539058
   Hits@10(filter)_n-n : 0.45977115258751045
   Hits@10_1-1         : 0.5035460992907801
   Hits@10_1-n         : 0.6346919431279621
   Hits@10_n-1         : 0.38745515565328087
   Hits@10_n-n         : 0.3263896725270261
   Hits@1_1-1          : 0.23167848699763594
   Hits@1_1-n          : 0.1261611374407583
   Hits@1_n-1          : 0.07701654901053119
   Hits@1_n-n          : 0.03692252138391749
   Hits@3              : 0.15882581977620153
   Hits@3(filter)      : 0.2391782769887085
   Hits@3(filter)_1-1  : 0.37825059101654845
   Hits@3(filter)_1-n  : 0.4772511848341232
   Hits@3(filter)_n-1  : 0.2913435944913783
   Hits@3(filter)_n-n  : 0.24128280936152927
   Hits@3_1-1          : 0.3747044917257683
   Hits@3_1-n          : 0.4638862559241706
   Hits@3_n-1          : 0.283184816572156
   Hits@3_n-n          : 0.13299781082849985
   MRR                 : 0.1361710796222476
   MRR(filter)         : 0.19010919877750462
   MRR(filter)_1-1     : 0.331101962436289
   MRR(filter)_1-n     : 0.3295970990840453
   MRR(filter)_n-1     : 0.20120642259788657
   MRR(filter)_n-n     : 0.1989556182457537
   MRR_1-1             : 0.32814107394796005
   MRR_1-n             : 0.31854918142267047
   MRR_n-1             : 0.1944620914251343
   MRR_n-n             : 0.12784839055885563
   ````

   ​