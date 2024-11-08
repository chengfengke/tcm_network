class Protein:
    def __init__(self, ensembl_id=None, protein_name=None, gene_name=None, combined_score=None,uniprot=None):
        self.ensembl_id = ensembl_id
        self.protein_name = protein_name
        self.gene_name = gene_name
        self.combined_score = combined_score
        self.uniprot = uniprot

    def __repr__(self):
        return (f"Protein(ensembl_id={self.ensembl_id}, "
                f"protein_name={self.protein_name}, "
                f"gene_name={self.gene_name}, "
                f"combined_score={self.combined_score}, "
                f"uniprot_id={self.uniprot})")