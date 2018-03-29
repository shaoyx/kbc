#Train nodes and edges in RDF-KG

## DATA PROCESS

我们需要将RDF格式的源数据，处理成为一个个三元组的edgelist，三元组中只包含数字，相当于对于节点与边进行编号，其中每个元素都代表一个节点或者一条边。

三元的edgelist的元素分别为（主语，宾语，谓词）:（obj, subj, pred）

这部分代码在RDF2edgelist.py中，运行时输入：

```python
~$ python3 RDF2edgelist.py
```

程序输出一个处理后的数据集合osp_triplet.edgelist，和一个json文件word2id.json，保存单词和节点对应的id。



