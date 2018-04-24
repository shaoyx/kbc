lr_arrs=(0.5 0.1 0.01 0.001)
opt_arrs=("sgd" "adagrad" "dsgd")
method=line
epoch=1000
margin=1

#rel_list="../dat/wordnet-mlj12/train.rellist"
#ent_list="../dat/wordnet-mlj12/train.entlist"
#train_data="../dat/wordnet-mlj12/wordnet-mlj12-train.txt"
#test_data="../dat/wordnet-mlj12/wordnet-mlj12-test.txt"
#whole_data="../dat/wordnet-mlj12/whole.txt"
#dataset="wordnet"

rel_list="../dat/FB15k/train.rellist"
ent_list="../dat/FB15k/train.entlist"
train_data="../dat/FB15k/freebase_mtr100_mte100-train.txt"
test_data="../dat/FB15k/freebase_mtr100_mte100-test.txt"
whole_data="../dat/FB15k/whole.txt"
dataset="FB15k"

for lr in ${lr_arrs[@]}; do
    for opt in ${opt_arrs[@]}; do
        log_path="../log/linemodel_${dataset}_${lr}_${opt}"
        cmd_train="python train.py --mode pairwise --ent ${ent_list} --rel ${rel_list} --train ${train_data} --method ${method} --epoch ${epoch} --margin ${margin} --opt ${opt} --lr ${lr} --log ${log_path}"
        echo ${cmd_train}
        mkdir -p ${log_path}
        ${cmd_train}
        cmd_test="python test.py --method line --ent ${ent_list} --rel ${rel_list} --data ${test_data} --filtered --graphall ${whole_data} --model ${log_path}/LineModel.epoch${epoch}"
        echo ${cmd_test}
        ${cmd_test}
    done
done
