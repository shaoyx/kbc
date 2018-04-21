lr_arrs=(0.01 0.001 0.0001 0.1)
opt_arrs=("sgd" "adagrad")
method=line
rel_list="../dat/wordnet-mlj12/train.rellist"
ent_list="../dat/wordnet-mlj12/train.entlist"
train="../dat/wordnet-mlj12/wordnet-mlj12-train.txt"
epoch=200
margin=1

for lr in ${lr_arrs[@]}; do
    for opt in ${opt_arrs[@]}; do
        cmd="python train.py --mode pairwise --ent ${ent_list} --rel ${rel_list} --train ${train_data} --method ${method} --epoch ${epoch} --margin ${margin} --opt ${opt} --lr ${lr}"
        echo $cmd
    done
done
