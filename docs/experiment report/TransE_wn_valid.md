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
          log -----> transe_wn_valid_whore
           lr -----> 0.01
       margin -----> 2.0
       method -----> transe
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
   Hits@1              : 0.0167
   Hits@1(filter)      : 0.0243
   Hits@1(filter)_1-1  : 0.0
   Hits@1(filter)_1-n  : 0.033567948023822416
   Hits@1(filter)_n-1  : 0.031297324583543666
   Hits@1(filter)_n-n  : 0.0
   Hits@10             : 0.7244
   Hits@10(filter)     : 0.8569
   Hits@10(filter)_1-1 : 0.8571428571428571
   Hits@10(filter)_1-n : 0.8990254466702762
   Hits@10(filter)_n-1 : 0.8382130237253912
   Hits@10(filter)_n-n : 0.8530973451327434
   Hits@10_1-1         : 0.8333333333333334
   Hits@10_1-n         : 0.7371413102328099
   Hits@10_n-1         : 0.6872791519434629
   Hits@10_n-n         : 0.8097345132743363
   Hits@1_1-1          : 0.0
   Hits@1_1-n          : 0.023822414726583648
   Hits@1_n-1          : 0.02221100454316002
   Hits@1_n-n          : 0.0
   Hits@3              : 0.3815
   Hits@3(filter)      : 0.5113
   Hits@3(filter)_1-1  : 0.38095238095238093
   Hits@3(filter)_1-n  : 0.5644288034650785
   Hits@3(filter)_n-1  : 0.5262493690055527
   Hits@3(filter)_n-n  : 0.452212389380531
   Hits@3_1-1          : 0.2857142857142857
   Hits@3_1-n          : 0.43936112615051437
   Hits@3_n-1          : 0.40964159515396265
   Hits@3_n-n          : 0.31150442477876106
   MRR                 : 0.24689814388200013
   MRR(filter)         : 0.3073818158199418
   MRR(filter)_1-1     : 0.23304831304412144
   MRR(filter)_1-n     : 0.33705656916905596
   MRR(filter)_n-1     : 0.31425718488402177
   MRR(filter)_n-n     : 0.27163064402993686
   MRR_1-1             : 0.21970809333744204
   MRR_1-n             : 0.2717273621101841
   MRR_n-1             : 0.25334701555654227
   MRR_n-n             : 0.2259012323774881
   ````

   ​