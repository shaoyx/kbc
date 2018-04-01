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
          log -----> transe_fb_lr001
           lr -----> 0.001
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

   //	Deepwalk parameters
   	Default parameters
   ````

2. ##### Results

   ````reStructuredText
   Hits@1              : 0.02552013678454741
   Hits@1(filter)      : 0.03962181104095072
   Hits@1(filter)_1-1  : 0.23167848699763594
   Hits@1(filter)_1-n  : 0.06872037914691943
   Hits@1(filter)_n-1  : 0.041951163059831036
   Hits@1(filter)_n-n  : 0.04089462637387438
   Hits@10             : 0.2616089113101183
   Hits@10(filter)     : 0.32978957525689423
   Hits@10(filter)_1-1 : 0.34988179669030733
   Hits@10(filter)_1-n : 0.5590521327014218
   Hits@10(filter)_n-1 : 0.34127994445087373
   Hits@10(filter)_n-n : 0.3500191834615992
   Hits@10_1-1         : 0.3475177304964539
   Hits@10_1-n         : 0.5503317535545024
   Hits@10_n-1         : 0.33595648651776416
   Hits@10_n-n         : 0.26019544562052854
   Hits@1_1-1          : 0.23167848699763594
   Hits@1_1-n          : 0.06796208530805688
   Hits@1_n-1          : 0.04148825367434325
   Hits@1_n-n          : 0.02241079690356361
   Hits@3              : 0.13245077957034754
   Hits@3(filter)      : 0.18510775168864588
   Hits@3(filter)_1-1  : 0.26713947990543735
   Hits@3(filter)_1-n  : 0.4374407582938389
   Hits@3(filter)_n-1  : 0.2670408517532693
   Hits@3(filter)_n-n  : 0.17867701821300414
   Hits@3_1-1          : 0.2647754137115839
   Hits@3_1-n          : 0.4300473933649289
   Hits@3_n-1          : 0.2625274852447633
   Hits@3_n-n          : 0.10453858132659279
   MRR                 : 0.10729550263417335
   MRR(filter)         : 0.14258216453443256
   MRR(filter)_1-1     : 0.2708889462260519
   MRR(filter)_1-n     : 0.2704056490390268
   MRR(filter)_n-1     : 0.16507230629335323
   MRR(filter)_n-n     : 0.1456195336887546
   MRR_1-1             : 0.2698177493525293
   MRR_1-n             : 0.26320030573044356
   MRR_n-1             : 0.16067371979262696
   MRR_n-n             : 0.09945942506460241
   ````

   ​