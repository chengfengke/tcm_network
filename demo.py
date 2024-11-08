import mygene

# 初始化mygene对象
mg = mygene.MyGeneInfo()

# 假设您有一个Ensembl ID
ensembl_id = 'ENSP00000206765'

# 使用query函数查询基因信息
gene_info = mg.query(ensembl_id, scopes='ensembl', fields='uniprot')

# 打印查询结果
print(gene_info)