### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
   // 	TransE Setting
   	batch -----> 128
     cp_ratio -----> 0.5
          dim -----> 64
          ent -----> ../dat/wordnet-mlj12/train.entlist
        epoch -----> 300
     filtered -----> False
     gradclip -----> 5
     graphall -----> None
       l2_reg -----> 0.0001
          log -----> /Users/CaiYaohui/Documents/Lab/KBEcodes/
           lr -----> 0.01
       margin -----> 2.0
       method -----> transe
       metric -----> mrr
         mode -----> pairwise
        nbest -----> None
     negative -----> 10
          opt -----> sgd
          rel -----> ../dat/wordnet-mlj12/train.rellist
    save_step -----> 100
        train -----> ../dat/wordnet-mlj12/wordnet-mlj12-train.txt
        valid -----> None

   // 	Deepwalk Setting
   	
   	Default parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.0166
   Hits@1(filter)      : 0.0256
   Hits@1(filter)_1-1  : 0.0
   Hits@1(filter)_1-n  : 0.03275582024905252
   Hits@1(filter)_n-1  : 0.03054013124684503
   Hits@1(filter)_n-n  : 0.0
   Hits@10             : 0.722
   Hits@10(filter)     : 0.8594
   Hits@10(filter)_1-1 : 0.8333333333333334
   Hits@10(filter)_1-n : 0.9030860855441256
   Hits@10(filter)_n-1 : 0.8419989904088844
   Hits@10(filter)_n-n : 0.8610619469026549
   Hits@10_1-1         : 0.8333333333333334
   Hits@10_1-n         : 0.734163508391987
   Hits@10_n-1         : 0.6845027763755679
   Hits@10_n-n         : 0.8106194690265487
   Hits@1_1-1          : 0.0
   Hits@1_1-n          : 0.022468868435300486
   Hits@1_n-1          : 0.020949015648662292
   Hits@1_n-n          : 0.0
   Hits@3              : 0.3807
   Hits@3(filter)      : 0.5117
   Hits@3(filter)_1-1  : 0.4523809523809524
   Hits@3(filter)_1-n  : 0.5671358960476448
   Hits@3(filter)_n-1  : 0.5287733467945482
   Hits@3(filter)_n-n  : 0.4398230088495575
   Hits@3_1-1          : 0.38095238095238093
   Hits@3_1-n          : 0.4371954520844613
   Hits@3_n-1          : 0.4076224129227663
   Hits@3_n-n          : 0.30442477876106194
   MRR                 : 0.24641589115499382
   MRR(filter)         : 0.30840964992250486
   MRR(filter)_1-1     : 0.2582576938860845
   MRR(filter)_1-n     : 0.3373629517386256
   MRR(filter)_n-1     : 0.3145428429385371
   MRR(filter)_n-n     : 0.27139110742188
   MRR_1-1             : 0.24969876604144234
   MRR_1-n             : 0.27018824740247827
   MRR_n-1             : 0.25191201057666746
   MRR_n-n             : 0.2268918845998761
   ````

   ​

