import mygene


class Ingredient:
    def __init__(self, hvc_id, name, smiles, cas_id, pubchem_id, drugbank_id, stich_id, herb_id, proteins=None):
        self.hvc_id = hvc_id
        self.name = name
        self.smiles = smiles
        self.cas_id = cas_id
        self.pubchem_id = pubchem_id
        self.drugbank_id = drugbank_id
        self.stich_id = stich_id
        self.herb_id = herb_id
        self.proteins = proteins

    def __repr__(self):
        return f"Ingredient(name={self.name}, hvc_id={self.hvc_id})"

    def parse_uniprot(self):
        mg = mygene.MyGeneInfo()
        for protein in self.proteins:
            ensembl_id = protein.ensembl_id
            gene_info = mg.query(ensembl_id, scopes='ensembl', fields='uniprot')
            gene_info = gene_info.get("hits",[])
            if len(gene_info) > 0:
                gene_info = gene_info[0].get("uniprot",{})
                if len(gene_info) > 0:
                    protein.uniprot = gene_info.get('Swiss-Prot',"")
                else:
                    protein.uniprot = ""
            else:
                protein.uniprot = ""