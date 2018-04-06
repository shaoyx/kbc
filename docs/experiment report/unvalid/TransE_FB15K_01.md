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
   Hits@1(filter)_1-1  : 0.23286052009456265
   Hits@1(filter)_1-n  : 0.10293838862559242
   Hits@1(filter)_n-1  : 0.0628399490799676
   Hits@1(filter)_n-n  : 0.06811257306641992
   Hits@10             : 0.3281390191464509
   Hits@10(filter)     : 0.4328181341098001
   Hits@10(filter)_1-1 : 0.49763593380614657
   Hits@10(filter)_1-n : 0.6538388625592417
   Hits@10(filter)_n-1 : 0.3991436176368476
   Hits@10(filter)_n-n : 0.4620957367577693
   Hits@10_1-1         : 0.49645390070921985
   Hits@10_1-n         : 0.6364928909952606
   Hits@10_n-1         : 0.3885545654438144
   Hits@10_n-n         : 0.3294138888261978
   Hits@1_1-1          : 0.23167848699763594
   Hits@1_1-n          : 0.10132701421800948
   Hits@1_n-1          : 0.06185626663580604
   Hits@1_n-n          : 0.03459793721365863
   Hits@3              : 0.15753076805877672
   Hits@3(filter)      : 0.23968614040730646
   Hits@3(filter)_1-1  : 0.3806146572104019
   Hits@3(filter)_1-n  : 0.47601895734597155
   Hits@3(filter)_n-1  : 0.29059136673996067
   Hits@3(filter)_n-n  : 0.2413053781398813
   Hits@3_1-1          : 0.37706855791962174
   Hits@3_1-n          : 0.4622748815165877
   Hits@3_n-1          : 0.28220113412799447
   Hits@3_n-n          : 0.13053781398812883
   MRR                 : 0.132482158346453
   MRR(filter)         : 0.18634544956164378
   MRR(filter)_1-1     : 0.33222127049136735
   MRR(filter)_1-n     : 0.3146553948674337
   MRR(filter)_n-1     : 0.1920850836622745
   MRR(filter)_n-n     : 0.19702200412879836
   MRR_1-1             : 0.32905715255400125
   MRR_1-n             : 0.30360596662407935
   MRR_n-1             : 0.1853398303370003
   MRR_n-n             : 0.12619296809020364
   ````
