from protein import Protein
class Disease:
    def __init__(self,id = None, chinese_name = None,english_name= None,proteins=None):
        self.id = id
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.proteins = proteins
        self.parse_proteins()
    
    def __repr__(self):
        return f"Disease(id = {self.id}, English_Name={self.english_name})"
    
    def parse_proteins(self):
        proteins = []
        for protein in self.proteins:
            proteins.append(Protein(protein_name=protein.get("geneSymbol",""),uniprot=protein.get("uniprotId","")))
        self.proteins=proteins