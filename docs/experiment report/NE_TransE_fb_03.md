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
         log -----> ne_transe_fb15k_ada
          lr -----> 0.01
      margin -----> 1.0
      method -----> transe_set
      metric -----> mrr
        mode -----> pairwise
       nbest -----> None
    negative -----> 10
         opt -----> adagrad
         rel -----> ../dat/FB15k/train.rellist
   save_step -----> 10
       train -----> ../dat/FB15k/freebase_mtr100_mte100-train.txt
       valid -----> None
   	
   //	NE parameters

   改过的
   --format edgelist
   --number-walks 30
   --input xxxxxx
   --output xxxxxx
   --walk-length 50
   --window-size 7

   没动的
   --excludlist default
   --matfile-variable-name default='network',
   --max-memory-data-size default=1000000000, type=int
   --representation-size', default=64, type=int,
   --seed', default=0, type=int,
   --undirected', default=True, type=bool,
   --vertex-freq-degree, default=False
   --workers', default=1, type=int
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.04875488818540401
   Hits@1(filter)      : 0.1542042626669601
   Hits@1(filter)_1-1  : 0.25295508274231676
   Hits@1(filter)_1-n  : 0.05848341232227488
   Hits@1(filter)_n-1  : 0.035701886355745865
   Hits@1(filter)_n-n  : 0.19630323410593783
   Hits@10             : 0.4295762726210831
   Hits@10(filter)     : 0.6177819911631766
   Hits@10(filter)_1-1 : 0.6997635933806147
   Hits@10(filter)_1-n : 0.7781990521327015
   Hits@10(filter)_n-1 : 0.4750607568568453
   Hits@10(filter)_n-n : 0.6560066803583922
   Hits@10_1-1         : 0.6926713947990544
   Hits@10_1-n         : 0.7069194312796209
   Hits@10_n-1         : 0.43154727462099296
   Hits@10_n-n         : 0.4399783339727821
   Hits@1_1-1          : 0.25177304964539005
   Hits@1_1-n          : 0.04995260663507109
   Hits@1_n-1          : 0.030494155769008217
   Hits@1_n-n          : 0.055880295199620844
   Hits@3              : 0.20953598212320768
   Hits@3(filter)      : 0.40357366558886765
   Hits@3(filter)_1-1  : 0.524822695035461
   Hits@3(filter)_1-n  : 0.4874881516587678
   Hits@3(filter)_n-1  : 0.2975928711954635
   Hits@3(filter)_n-n  : 0.43706696156537045
   Hits@3_1-1          : 0.5141843971631206
   Hits@3_1-n          : 0.42625592417061614
   Hits@3_n-1          : 0.2602129383173244
   Hits@3_n-n          : 0.20038818298765487
   MRR                 : 0.17196917839511214
   MRR(filter)         : 0.3159713349915401
   MRR(filter)_1-1     : 0.4182749250048862
   MRR(filter)_1-n     : 0.32151805753939106
   MRR(filter)_n-1     : 0.1962744767411513
   MRR(filter)_n-n     : 0.3546308869397644
   MRR_1-1             : 0.4119163551272371
   MRR_1-n             : 0.2844519736944564
   MRR_n-1             : 0.17364705025324118
   MRR_n-n             : 0.17570449287507206
   ````

   ​

