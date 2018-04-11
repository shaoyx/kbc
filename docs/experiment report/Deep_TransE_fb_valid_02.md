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
   lr=0.01
   Hits@1              : 0.04352389497384503   
   Hits@1(filter)      : 0.07727141913967937   
   Hits@1(filter)_1-1  : 0.23286052009456265   
   Hits@1(filter)_1-n  : 0.14635071090047394   
   Hits@1(filter)_n-1  : 0.08934151139914362   
   Hits@1(filter)_n-n  : 0.07969035636101018   
   Hits@10             : 0.34322256267881024   
   Hits@10(filter)     : 0.4623080699497215    
   Hits@10(filter)_1-1 : 0.5106382978723404    
   Hits@10(filter)_1-n : 0.6848341232227488    
   Hits@10(filter)_n-1 : 0.418065038768661     
   Hits@10(filter)_n-n : 0.49177368029068586   
   Hits@10_1-1         : 0.5059101654846335    
   Hits@10_1-n         : 0.6598104265402843    
   Hits@10_n-1         : 0.4027890290475639    
   Hits@10_n-n         : 0.34324854995599086   
   Hits@1_1-1          : 0.23286052009456265   
   Hits@1_1-n          : 0.13838862559241707   
   Hits@1_n-1          : 0.08448096285152182   
   Hits@1_n-n          : 0.03383059874968968   
   Hits@3              : 0.16085727345059336   
   Hits@3(filter)      : 0.2556245873609724    
   Hits@3(filter)_1-1  : 0.3321513002364066    
   Hits@3(filter)_1-n  : 0.4776303317535545    
   Hits@3(filter)_n-1  : 0.2915750491841222    
   Hits@3(filter)_n-n  : 0.262181498115507     
   Hits@3_1-1          : 0.32860520094562645   
   Hits@3_1-n          : 0.4622748815165877    
   Hits@3_n-1          : 0.28220113412799447   
   Hits@3_n-n          : 0.13478074431831005   
   MRR                 : 0.1409513615859344    
   MRR(filter)         : 0.20556997754569253   
   MRR(filter)_1-1     : 0.3169618909879271    
   MRR(filter)_1-n     : 0.34584834118466135   
   MRR(filter)_n-1     : 0.21112718432462543   
   MRR(filter)_n-n     : 0.21434666569269975   
   MRR_1-1             : 0.31429894088143934   
   MRR_1-n             : 0.33149891261050873   
   MRR_n-1             : 0.20236740701544179   
   MRR_n-n             : 0.1299408865343736   
   ````

   ​