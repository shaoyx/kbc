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
          log -----> ne_transe_fb15k
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
   //	At 30 epoch
   Hits@1              : 0.07875268744392341
   Hits@1(filter)      : 0.17694807942983867
   Hits@1(filter)_1-1  : 0.2718676122931442
   Hits@1(filter)_1-n  : 0.28881516587677725
   Hits@1(filter)_n-1  : 0.1763106121976623
   Hits@1(filter)_n-n  : 0.18820104267755985
   Hits@10             : 0.423879737942476
   Hits@10(filter)     : 0.5899172182627686
   Hits@10(filter)_1-1 : 0.682033096926714
   Hits@10(filter)_1-n : 0.8345023696682464
   Hits@10(filter)_n-1 : 0.5094317787293138
   Hits@10(filter)_n-n : 0.6119072874585298
   Hits@10_1-1         : 0.6784869976359338
   Hits@10_1-n         : 0.7566824644549763
   Hits@10_n-1         : 0.46192570304362923
   Hits@10_n-n         : 0.4218330361777517
   Hits@1_1-1          : 0.26832151300236406
   Hits@1_1-n          : 0.25620853080568723
   Hits@1_n-1          : 0.1564055086216873
   Hits@1_n-n          : 0.0646144124218556
   Hits@3              : 0.22379847979550033
   Hits@3(filter)      : 0.39075857865957914
   Hits@3(filter)_1-1  : 0.5141843971631206
   Hits@3(filter)_1-n  : 0.6075829383886255
   Hits@3(filter)_n-1  : 0.37090614512209236
   Hits@3(filter)_n-n  : 0.40093434742377393
   Hits@3_1-1          : 0.5011820330969267
   Hits@3_1-n          : 0.5474881516587677
   Hits@3_n-1          : 0.33422057632218494
   Hits@3_n-n          : 0.19912433139994132
   MRR                 : 0.19068913577833244
   MRR(filter)         : 0.31924899225736086
   MRR(filter)_1-1     : 0.42193678549436353
   MRR(filter)_1-n     : 0.4855526155163931
   MRR(filter)_n-1     : 0.2964113004107131
   MRR(filter)_n-n     : 0.33232742103789226
   MRR_1-1             : 0.41511451968311885
   MRR_1-n             : 0.4357821918775729
   MRR_n-1             : 0.26602836039280137
   MRR_n-n             : 0.17712334316580527

   //	At 300 epoch
   Hits@1              : 0.038165935907636575
   Hits@1(filter)      : 0.1251544751231569
   Hits@1(filter)_1-1  : 0.23522458628841608
   Hits@1(filter)_1-n  : 0.0595260663507109
   Hits@1(filter)_n-1  : 0.036338386760791576
   Hits@1(filter)_n-n  : 0.15371594935566138
   Hits@10             : 0.4391664268422745
   Hits@10(filter)     : 0.6386551776675526
   Hits@10(filter)_1-1 : 0.6997635933806147
   Hits@10(filter)_1-n : 0.8630331753554502
   Hits@10(filter)_n-1 : 0.5268487443582919
   Hits@10(filter)_n-n : 0.6752352795143199
   Hits@10_1-1         : 0.693853427895981
   Hits@10_1-n         : 0.7829383886255924
   Hits@10_n-1         : 0.477953940516144
   Hits@10_n-n         : 0.43704439278701845
   Hits@1_1-1          : 0.23522458628841608
   Hits@1_1-n          : 0.05090047393364929
   Hits@1_n-1          : 0.031072792500867957
   Hits@1_n-n          : 0.03850233586855944
   Hits@3              : 0.21710314706031725
   Hits@3(filter)      : 0.4190211779045555
   Hits@3(filter)_1-1  : 0.508274231678487
   Hits@3(filter)_1-n  : 0.6162085308056872
   Hits@3(filter)_n-1  : 0.376171739382016
   Hits@3(filter)_n-n  : 0.4422803493646889
   Hits@3_1-1          : 0.49527186761229314
   Hits@3_1-n          : 0.5537440758293839
   Hits@3_n-1          : 0.3380395787524592
   Hits@3_n-n          : 0.1854702204969645
   MRR                 : 0.16953203351983018
   MRR(filter)         : 0.30760457349241055
   MRR(filter)_1-1     : 0.4033891175825738
   MRR(filter)_1-n     : 0.3709874119908522
   MRR(filter)_n-1     : 0.226473625535441
   MRR(filter)_n-n     : 0.336382269401782
   MRR_1-1             : 0.39812589248508534
   MRR_1-n             : 0.33202560013713056
   MRR_n-1             : 0.20268892960575913
   MRR_n-n             : 0.16197328570180833

   //	At 800 epoch
   Hits@1              : 0.03909701884173283                            
   Hits@1(filter)      : 0.12664420781771088                            
   Hits@1(filter)_1-1  : 0.23404255319148937                            
   Hits@1(filter)_1-n  : 0.057251184834123225                           
   Hits@1(filter)_n-1  : 0.0349496586043282                             
   Hits@1(filter)_n-n  : 0.15475411315985466                            
   Hits@10             : 0.4393611078194038                             
   Hits@10(filter)     : 0.6425995835519968                             
   Hits@10(filter)_1-1 : 0.6914893617021277                             
   Hits@10(filter)_1-n : 0.8700473933649289                             
   Hits@10(filter)_n-1 : 0.531130656174054                              
   Hits@10(filter)_n-n : 0.6832923333859938                             
   Hits@10_1-1         : 0.6855791962174941                             
   Hits@10_1-n         : 0.7871090047393365                             
   Hits@10_n-1         : 0.4804999421363268                             
   Hits@10_n-n         : 0.43607393531788124                            
   Hits@1_1-1          : 0.23404255319148937                            
   Hits@1_1-n          : 0.050616113744075826                           
   Hits@1_n-1          : 0.030899201481310035                           
   Hits@1_n-n          : 0.04062380103365005                            
   Hits@3              : 0.21911767195408915                            
   Hits@3(filter)      : 0.42638519747422593                            
   Hits@3(filter)_1-1  : 0.508274231678487                              
   Hits@3(filter)_1-n  : 0.6262559241706162                             
   Hits@3(filter)_n-1  : 0.3823052887397292                             
   Hits@3(filter)_n-n  : 0.4516238236024284                             
   Hits@3_1-1          : 0.49527186761229314                            
   Hits@3_1-n          : 0.5674881516587678                             
   Hits@3_n-1          : 0.3464298113644254                             
   Hits@3_n-n          : 0.18723058520842267                            
   MRR                 : 0.1710375697357211                             
   MRR(filter)         : 0.31153044672268404                            
   MRR(filter)_1-1     : 0.40189344824266265                            
   MRR(filter)_1-n     : 0.37423058664949066                            
   MRR(filter)_n-1     : 0.22845345961995864                            
   MRR(filter)_n-n     : 0.3407783314220303                             
   MRR_1-1             : 0.396129439676129                              
   MRR_1-n             : 0.33611714262296283                            
   MRR_n-1             : 0.205186659800501                              
   MRR_n-n             : 0.1638063653402902 

   //	At 1000 epoch
   Hits@1              : 0.039943457872729425                                   
   Hits@1(filter)      : 0.12782922246110612                                    
   Hits@1(filter)_1-1  : 0.23404255319148937                                    
   Hits@1(filter)_1-n  : 0.04843601895734597                                    
   Hits@1(filter)_n-1  : 0.029568336998032636                                   
   Hits@1(filter)_n-n  : 0.15534090139700737                                    
   Hits@10             : 0.43964043269963266                                    
   Hits@10(filter)     : 0.6462900577271419                                     
   Hits@10(filter)_1-1 : 0.693853427895981                                      
   Hits@10(filter)_1-n : 0.8734597156398104                                     
   Hits@10(filter)_n-1 : 0.533213748408749                                      
   Hits@10(filter)_n-n : 0.6860231555665892                                     
   Hits@10_1-1         : 0.6855791962174941                                     
   Hits@10_1-n         : 0.78739336492891                                       
   Hits@10_n-1         : 0.48067353315588474                                    
   Hits@10_n-n         : 0.4370218240086664                                     
   Hits@1_1-1          : 0.23404255319148937                                    
   Hits@1_1-n          : 0.04464454976303318                                    
   Hits@1_n-1          : 0.02725379007059368                                    
   Hits@1_n-n          : 0.04053352592024194                                    
   Hits@3              : 0.2199979685463256
   Hits@3(filter)      : 0.42997409896565153
   Hits@3(filter)_1-1  : 0.5070921985815603
   Hits@3(filter)_1-n  : 0.628436018957346
   Hits@3(filter)_n-1  : 0.3836361532230066
   Hits@3(filter)_n-n  : 0.45564106614908934
   Hits@3_1-1          : 0.4940898345153664
   Hits@3_1-n          : 0.5681516587677725
   Hits@3_n-1          : 0.34683485707672723
   Hits@3_n-n          : 0.189126362589993
   MRR                 : 0.17181853941119515
   MRR(filter)         : 0.3131381998977318
   MRR(filter)_1-1     : 0.4013220315171271
   MRR(filter)_1-n     : 0.36977119001674447
   MRR(filter)_n-1     : 0.22573116853817002
   MRR(filter)_n-n     : 0.3419266577307421
   MRR_1-1             : 0.3958798094605903
   MRR_1-n             : 0.3330300506971575
   MRR_n-1             : 0.20330210825454326
   MRR_n-n             : 0.16402674179451987

   ````

   ​