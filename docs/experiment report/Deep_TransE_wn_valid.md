### Experiment Report

1. ##### Parameter Setting

   ````reStructuredText
   //	TransE parameters
         batch -----> 128
      cp_ratio -----> 0.5
           dim -----> 64
           ent -----> ../dat/wordnet-mlj12/train.entlist
         epoch -----> 300
      filtered -----> True
      gradclip -----> 5
      graphall -----> ../dat/wordnet-mlj12/whole.txt
        l2_reg -----> 0.0001
           log -----> deep_transe_wn_valid_filall
            lr -----> 0.01
        margin -----> 2.0
        method -----> transe_set
        metric -----> mrr
          mode -----> pairwise
         nbest -----> None
      negative -----> 10
           opt -----> sgd
           rel -----> ../dat/wordnet-mlj12/train.rellist
     save_step -----> 10
         train -----> ../dat/wordnet-mlj12/wordnet-mlj12-train.txt
         valid -----> ../dat/wordnet-mlj12/wordnet-mlj12-valid.txt

   //	Deepwalk parameters
   	Default Parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.0509
   Hits@1(filter)      : 0.0913
   Hits@1(filter)_1-1  : 0.0
   Hits@1(filter)_1-n  : 0.1204656199242014
   Hits@1(filter)_n-1  : 0.11231701161029783
   Hits@1(filter)_n-n  : 0.0
   Hits@10             : 0.7077
   Hits@10(filter)     : 0.8567
   Hits@10(filter)_1-1 : 0.8333333333333334
   Hits@10(filter)_1-n : 0.8957769355711965
   Hits@10(filter)_n-1 : 0.8351842503785967
   Hits@10(filter)_n-n : 0.8168141592920354
   Hits@10_1-1         : 0.8333333333333334
   Hits@10_1-n         : 0.7184623714131023
   Hits@10_n-1         : 0.6698637051993942
   Hits@10_n-n         : 0.7530973451327434
   Hits@1_1-1          : 0.0
   Hits@1_1-n          : 0.0660530590146183
   Hits@1_n-1          : 0.061585058051489144
   Hits@1_n-n          : 0.0
   Hits@3              : 0.2988
   Hits@3(filter)      : 0.4616
   Hits@3(filter)_1-1  : 0.2857142857142857
   Hits@3(filter)_1-n  : 0.5181375203031944
   Hits@3(filter)_n-1  : 0.48308934881373045
   Hits@3(filter)_n-n  : 0.32212389380530976
   Hits@3_1-1          : 0.23809523809523808
   Hits@3_1-n          : 0.33919870059556034
   Hits@3_n-1          : 0.31625441696113077
   Hits@3_n-n          : 0.2150442477876106
   MRR                 : 0.23986445582743832
   MRR(filter)         : 0.3308910027037436
   MRR(filter)_1-1     : 0.22129455641360385
   MRR(filter)_1-n     : 0.3681610343111583
   MRR(filter)_n-1     : 0.3432576629847096
   MRR(filter)_n-n     : 0.23578907982527544
   MRR_1-1             : 0.20810233508062626
   MRR_1-n             : 0.2623602438951332
   MRR_n-1             : 0.2446135136165122
   MRR_n-n             : 0.1950608819793653
   ````

   ​