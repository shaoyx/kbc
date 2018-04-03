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
           log -----> ne_transe_fb_valid_lr01
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
   //	改过的

   --format edgelist
   --number-walks 30
   --input xxxxxx
   --output xxxxxx
   --walk-length 50
   --window-size 7

   //	没改的
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

   Hits@1              : 0.07683973523387111
   Hits@1(filter)      : 0.17770141016742563
   Hits@1(filter)_1-1  : 0.26595744680851063
   Hits@1(filter)_1-n  : 0.27080568720379145
   Hits@1(filter)_n-1  : 0.16531651429232727
   Hits@1(filter)_n-n  : 0.18901351869823285
   Hits@10             : 0.4339354336307156
   Hits@10(filter)     : 0.6072692183981988
   Hits@10(filter)_1-1 : 0.6879432624113475
   Hits@10(filter)_1-n : 0.8605687203791469
   Hits@10(filter)_n-1 : 0.5253442888554566
   Hits@10(filter)_n-n : 0.6294206594597035
   Hits@10_1-1         : 0.6832151300236406
   Hits@10_1-n         : 0.7817061611374407
   Hits@10_n-1         : 0.4772017127647263
   Hits@10_n-n         : 0.4297772461576655
   Hits@1_1-1          : 0.2647754137115839
   Hits@1_1-n          : 0.2418957345971564
   Hits@1_n-1          : 0.14766809397060526
   Hits@1_n-n          : 0.061341939560811576
   Hits@3              : 0.22699801933266747
   Hits@3(filter)      : 0.403226625586159
   Hits@3(filter)_1-1  : 0.524822695035461
   Hits@3(filter)_1-n  : 0.6314691943127962
   Hits@3(filter)_n-1  : 0.38548779076495776
   Hits@3(filter)_n-n  : 0.4123541492699
   Hits@3_1-1          : 0.5130023640661938
   Hits@3_1-n          : 0.5653080568720379
   Hits@3_n-1          : 0.345098946881148
   Hits@3_n-n          : 0.19582928976054526
   MRR                 : 0.1926858252544013
   MRR(filter)         : 0.3259817938748111
   MRR(filter)_1-1     : 0.42386068937329563
   MRR(filter)_1-n     : 0.4865913299460039
   MRR(filter)_n-1     : 0.2970453958413575
   MRR(filter)_n-n     : 0.3386730972766808
   MRR_1-1             : 0.41777412415776044
   MRR_1-n             : 0.43823355797657015
   MRR_n-1             : 0.2675248256366634
   MRR_n-n             : 0.17639342360119056

   //	At 300 epoch

   Hits@1              : 0.045115200352118634                
   Hits@1(filter)      : 0.13603121667146315                 
   Hits@1(filter)_1-1  : 0.23404255319148937                 
   Hits@1(filter)_1-n  : 0.09507109004739336                 
   Hits@1(filter)_n-1  : 0.05803726420553177                 
   Hits@1(filter)_n-n  : 0.15753007289715407                 
   Hits@10             : 0.44426198980887405                 
   Hits@10(filter)     : 0.644030065514381                   
   Hits@10(filter)_1-1 : 0.6997635933806147                  
   Hits@10(filter)_1-n : 0.8813270142180095                  
   Hits@10(filter)_n-1 : 0.5380164332831848                  
   Hits@10(filter)_n-n : 0.680177841973414                   
   Hits@10_1-1         : 0.6950354609929078                  
   Hits@10_1-n         : 0.797345971563981                   
   Hits@10_n-1         : 0.486749218840412                   
   Hits@10_n-n         : 0.4413098918955517                  
   Hits@1_1-1          : 0.23404255319148937                 
   Hits@1_1-n          : 0.08                                
   Hits@1_n-1          : 0.04883694016896192                 
   Hits@1_n-n          : 0.0416393960594913                  
   Hits@3              : 0.221149125628481                   
   Hits@3(filter)      : 0.42359194867193717                 
   Hits@3(filter)_1-1  : 0.5177304964539007                  
   Hits@3(filter)_1-n  : 0.6265402843601896                  
   Hits@3(filter)_n-1  : 0.3824788797592871                  
   Hits@3(filter)_n-n  : 0.4465232796948701                  
   Hits@3_1-1          : 0.5070921985815603                  
   Hits@3_1-n          : 0.5665402843601895                  
   Hits@3_n-1          : 0.34585117463256565                 
   Hits@3_n-n          : 0.18772709833216727                 
   MRR                 : 0.17558472407725836                 
   MRR(filter)         : 0.3159329062373174                  
   MRR(filter)_1-1     : 0.4069485908821896                  
   MRR(filter)_1-n     : 0.3952513102906586                  
   MRR(filter)_n-1     : 0.24128580740460878                 
   MRR(filter)_n-n     : 0.3408050044244767                  
   MRR_1-1             : 0.3995267841895677                  
   MRR_1-n             : 0.35361323386428717                 
   MRR_n-1             : 0.21586735431479157                 
   MRR_n-n             : 0.16512580984088987                 
   ````

   ​