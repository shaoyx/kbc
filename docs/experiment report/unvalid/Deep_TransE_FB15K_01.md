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
   Hits@1(filter)      : 0.08032706404157708
   Hits@1(filter)_1-1  : 0.23522458628841608
   Hits@1(filter)_1-n  : 0.07516587677725119
   Hits@1(filter)_n-1  : 0.04588589283647726
   Hits@1(filter)_n-n  : 0.09341217359904308
   Hits@10             : 0.3727632848605915
   Hits@10(filter)     : 0.516175449882345
   Hits@10(filter)_1-1 : 0.5721040189125296
   Hits@10(filter)_1-n : 0.7292890995260664
   Hits@10(filter)_n-1 : 0.4452031014928828
   Hits@10(filter)_n-n : 0.5488275519646122
   Hits@10_1-1         : 0.5697399527186762
   Hits@10_1-n         : 0.6906161137440758
   Hits@10_n-1         : 0.4215947228330054
   Hits@10_n-n         : 0.3732875939425399
   Hits@1_1-1          : 0.23522458628841608
   Hits@1_1-n          : 0.07270142180094787
   Hits@1_n-1          : 0.044381437333641936
   Hits@1_n-n          : 0.03595206391478029
   Hits@3              : 0.17662643259805996
   Hits@3(filter)      : 0.3022887711398148
   Hits@3(filter)_1-1  : 0.3912529550827423
   Hits@3(filter)_1-n  : 0.5123222748815166
   Hits@3(filter)_n-1  : 0.3127531535701886
   Hits@3(filter)_n-n  : 0.3111106095827033
   Hits@3_1-1          : 0.3829787234042553
   Hits@3_1-n          : 0.4860663507109005
   Hits@3_n-1          : 0.2967249160976739
   Hits@3_n-n          : 0.1495181565821842
   MRR                 : 0.14675161164906228
   MRR(filter)         : 0.22982540388098477
   MRR(filter)_1-1     : 0.34626890036165736
   MRR(filter)_1-n     : 0.3277264902129145
   MRR(filter)_n-1     : 0.20006448742889982
   MRR(filter)_n-n     : 0.24484946784677708
   MRR_1-1             : 0.3429670108485889
   MRR_1-n             : 0.30866398604756057
   MRR_n-1             : 0.18842755773647518
   MRR_n-n             : 0.1400621787466835
   ````

   ​

