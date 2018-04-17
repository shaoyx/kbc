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
         log -----> deep_transe_fb_valid_lr001
          lr -----> 0.001
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
   	Default paramters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.04352389497384503
   Hits@1(filter)      : 0.07727141913967937
   Hits@10             : 0.34322256267881024
   Hits@10(filter)     : 0.4623080699497215
   Hits@10(filter)_head_1-1: 0.5106382978723404
   Hits@10(filter)_head_1-n: 0.7572040273116537
   Hits@10(filter)_head_n-1: 0.12928909952606635
   Hits@10(filter)_head_n-n: 0.49177368029068586
   Hits@10(filter)_tail_1-1: 0.5189125295508275
   Hits@10(filter)_tail_1-n: 0.15634764494850134
   Hits@10(filter)_tail_n-1: 0.6873933649289099
   Hits@10(filter)_tail_n-n: 0.44584621634430927
   Hits@3              : 0.16085727345059336
   Hits@3(filter)      : 0.2556245873609724
   MRR                 : 0.1409513615859344
   MRR(filter)         : 0.20556997754569253
   ````

   ​