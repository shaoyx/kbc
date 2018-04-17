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
   Hits@10             : 0.7244
   Hits@10(filter)     : 0.8569
   Hits@10(filter)_head_1-1: 0.8571428571428571
   Hits@10(filter)_head_1-n: 0.9262998485613326
   Hits@10(filter)_head_n-1: 0.8045479155387114
   Hits@10(filter)_head_n-n: 0.8530973451327434
   Hits@10(filter)_tail_1-1: 0.9047619047619048
   Hits@10(filter)_tail_1-n: 0.7839475012619889
   Hits@10(filter)_tail_n-1: 0.9112073632918246
   Hits@10(filter)_tail_n-n: 0.8619469026548673
   Hits@3              : 0.3815
   Hits@3(filter)      : 0.5113
   MRR                 : 0.24689814388200013
   MRR(filter)         : 0.3073818158199418
   ````

   ​