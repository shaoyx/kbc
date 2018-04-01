#Train nodes and edges in RDF-KG

## DATA PROCESS

我们需要将RDF格式的源数据，处理成为一个个三元组的edgelist，三元组中只包含数字，相当于对于节点与边进行编号，其中每个元素都代表一个节点或者一条边。

三元的edgelist的元素分别为（主语，宾语，谓词）:（obj, subj, pred）

这部分代码在RDF2edgelist.py中，运行时输入：

```python
python3 RDF2edgelist.py
```

程序输出一个处理后的数据集合osp_triplet.edgelist，和一个json文件word2id.json，保存单词和节点对应的id。

## Trainning

得到的osp_triplet.edgelist可以当做deepwalk的输入

在deepwalk中，做了如下几个工作

1、将edgelist文件转换成Graph类中的定义

2、利用random walk，取节点为初始，然后边-节点-边-节点...这样的方式walk，形成语料。

3、利用word2vec训练，得到词向量，作为节点与边的向量。

输入命令：

```
python3 deepwalk_rdf/deepwalk/__main__.py --format edgelist --input ../datasrc/osp_triplet.edgelist --output ../datasrc/osp.repre > trainrep.res
```

最后的结果保存在osp.repre中

## 使用

结合之前的word2id.json，和osp.repre使用

