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
   Hits@1              : 0.030319446090298116
   Hits@1(filter)      : 0.05070169795669618 
   Hits@1(filter)_1-1  : 0.23286052009456265 
   Hits@1(filter)_1-n  : 0.0757345971563981  
   Hits@1(filter)_n-1  : 0.046233074875593104
   Hits@1(filter)_n-n  : 0.05709900923063035 
   Hits@10             : 0.2515870731831186  
   Hits@10(filter)     : 0.33578236359635016 
   Hits@10(filter)_1-1 : 0.3333333333333333  
   Hits@10(filter)_1-n : 0.5251184834123223  
   Hits@10(filter)_n-1 : 0.3205647494502951  
   Hits@10(filter)_n-n : 0.3590918323591144  
   Hits@10_1-1         : 0.3321513002364066  
   Hits@10_1-n         : 0.5150710900473934  
   Hits@10_n-1         : 0.31443120009258185 
   Hits@10_n-n         : 0.2529057302128236  
   Hits@1_1-1          : 0.23286052009456265 
   Hits@1_1-n          : 0.07412322274881517 
   Hits@1_n-1          : 0.04524939243143155 
   Hits@1_n-n          : 0.0285720733936672  
   Hits@3              : 0.11111205159892333 
   Hits@3(filter)      : 0.16352355639823263 
   Hits@3(filter)_1-1  : 0.24940898345153664 
   Hits@3(filter)_1-n  : 0.32454976303317534 
   Hits@3(filter)_n-1  : 0.19812521698877444 
   Hits@3(filter)_n-n  : 0.1668058407998375  
   Hits@3_1-1          : 0.2458628841607565  
   Hits@3_1-n          : 0.31677725118483413 
   Hits@3_n-1          : 0.19338039578752458 
   Hits@3_n-n          : 0.09451804373829245 
   MRR                 : 0.10310774369854225 
   MRR(filter)         : 0.14343091583628084 
   MRR(filter)_1-1     : 0.26505294515373606 
   MRR(filter)_1-n     : 0.23470267111344742 
   MRR(filter)_n-1     : 0.14327700383328723                                                                             
   MRR(filter)_n-n     : 0.15245115881445295                                                                             
   MRR_1-1             : 0.26410516461080646                                                                             
   MRR_1-n             : 0.22774574747054668                                                                             
   MRR_n-1             : 0.1390300680369324                                                                              
   MRR_n-n             : 0.09965314540767414                                                                             
   ````

   ​