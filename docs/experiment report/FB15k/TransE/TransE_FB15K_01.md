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
           log -----> transe_fb
            lr -----> 0.01
        margin -----> 1.0
        method -----> transe
        metric -----> mrr
          mode -----> pairwise
         nbest -----> None
      negative -----> 10
           opt -----> sgd
           rel -----> ../dat/FB15k/train.rellist
     save_step -----> 100
         train -----> ../dat/FB15k/freebase_mtr100_mte100-train.txt
         valid -----> None

   //	deepwalk setting
   	Defalut parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.03628684125882413
   Hits@1(filter)      : 0.05976705997866974
   Hits@10             : 0.3281390191464509
   Hits@10(filter)     : 0.4328181341098001
   Hits@10(filter)_head_1-1: 0.49763593380614657
   Hits@10(filter)_head_1-n: 0.727809281333179
   Hits@10(filter)_head_n-1: 0.11545023696682465
   Hits@10(filter)_head_n-n: 0.4620957367577693
   Hits@10(filter)_tail_1-1: 0.5271867612293144
   Hits@10(filter)_tail_1-n: 0.11121397986344173
   Hits@10(filter)_tail_n-1: 0.6532701421800948
   Hits@10(filter)_tail_n-n: 0.41722900539393803
   Hits@3              : 0.15753076805877672
   Hits@3(filter)      : 0.23968614040730646
   MRR                 : 0.132482158346453
   MRR(filter)         : 0.18634544956164378

   ````
