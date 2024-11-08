from ingredient import Ingredient

class Herb:
    def __init__(self, hvm_id, name, ingredients):
        self.hvm_id = hvm_id
        self.name = name
        self.ingredients = ingredients  # Store the full ingredients data

    def __repr__(self):
        return f"Herb(hvm_id={self.hvm_id}, name={self.name})"

    def parse_ingredients(self):
        """Convert raw ingredient data to a list of Ingredient objects."""
        ingredient_list = []
        for item in self.ingredients:
            ingredient = Ingredient(
                hvc_id=item.get('Hvc id', None),
                name=item.get('Name', None),
                smiles=item.get('SMILES', None),
                cas_id=item.get('CAS id', None),
                pubchem_id=item.get('PubChem id', None),
                drugbank_id=item.get('DrugBank id', None),
                stich_id=item.get('STICH id', None),
                herb_id=item.get('Herb id', None)
            )
            ingredient_list.append(ingredient)
        self.ingredients = ingredient_list
    
    def get_uniprot(self):
        uniprot_list = []
        for ingredient in self.ingredients:
            for protein in ingredient.proteins:
                uniprot_list.append(protein.uniprot)
        return uniprot_list