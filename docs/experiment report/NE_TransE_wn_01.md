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
          log -----> ne_transe_wn
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
   Hits@1              : 0.1377                                          
   Hits@1(filter)      : 0.2153                                          
   Hits@1(filter)_1-1  : 0.0                                             
   Hits@1(filter)_1-n  : 0.3002165674066053                              
   Hits@1(filter)_n-1  : 0.27990913679959617                             
   Hits@1(filter)_n-n  : 0.0008849557522123894                           
   Hits@10             : 0.756                                           
   Hits@10(filter)     : 0.9062                                          
   Hits@10(filter)_1-1 : 0.9523809523809523                              
   Hits@10(filter)_1-n : 0.9396318354087709                              
   Hits@10(filter)_n-1 : 0.8760726905603231                              
   Hits@10(filter)_n-n : 0.8920353982300885                              
   Hits@10_1-1         : 0.9523809523809523                              
   Hits@10_1-n         : 0.7620465619924202                              
   Hits@10_n-1         : 0.7104997476022211                              
   Hits@10_n-n         : 0.8460176991150442                              
   Hits@1_1-1          : 0.0                                             
   Hits@1_1-n          : 0.1940985381700054                              
   Hits@1_n-1          : 0.18096920747097425                             
   Hits@1_n-n          : 0.0                                             
   Hits@3              : 0.4652                                          
   Hits@3(filter)      : 0.6451                                          
   Hits@3(filter)_1-1  : 0.47619047619047616                             
   Hits@3(filter)_1-n  : 0.7114239306984299                              
   Hits@3(filter)_n-1  : 0.663301362948006                               
   Hits@3(filter)_n-n  : 0.5212389380530974                              
   Hits@3_1-1          : 0.47619047619047616                             
   Hits@3_1-n          : 0.5203031943692474                              
   Hits@3_n-1          : 0.4851085310449268                              
   Hits@3_n-n          : 0.3769911504424779                              
   MRR                 : 0.34160314091138505                             
   MRR(filter)         : 0.45786996809799346                             
   MRR(filter)_1-1     : 0.3271387101592001                              
   MRR(filter)_1-n     : 0.5275796348448106                              
   MRR(filter)_n-1     : 0.49189277413345006                             
   MRR(filter)_n-n     : 0.3054500648446208                              
   MRR_1-1             : 0.30870377208140487                             
   MRR_1-n             : 0.38940753184370275                             
   MRR_n-1             : 0.3630669920824427                              
   MRR_n-n             : 0.2542228899257717                              
   ````

   ​