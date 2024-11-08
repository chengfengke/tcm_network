import requests
import urllib.parse
import re
from formula import Formula
from herb import Herb
from ingredient import Ingredient
from protein import Protein
from disease import Disease
import json

def get_tcmid(herb_name):
    encoded_name = urllib.parse.quote(herb_name)
    url = f"http://117.72.73.151:80/api/formula/keyword/{encoded_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get("data", {}).get("formulas", [])
        
        ask_list = []
        if len(data) > 1:
            for item in data:
                ask_list.append(item.get("Name", ""))
            formula_choice = input(f"共有{len(ask_list)}个结果,分别是：{ask_list}，请选择你要对哪个方剂进行分析：")
            data = data[ask_list.index(formula_choice)]
        elif len(data) == 0:
            print("没有数据，再见！")
            return None
        else:
            data = data[0]

        hvp_id = data.get("Hvp id", "")
        name = data.get("Name", "")
        return Formula(hvp_id=hvp_id, name=name, herbs=[])  # Return an empty Formula for now

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def get_herbs(formula):
    if not formula.hvp_id:
        print("无有效tcmid，无法获取成分数据")
        return

    # API endpoint to get ingredients data using hvp_id
    url = f"http://117.72.73.151:80/api/tcm/formula/{formula.hvp_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        ingredients_data = response.json().get("data", {}).get("ingredients", [])

        # Populate formula with Herb instances
        for item in ingredients_data:
            hvm_id = item.get("Hvm id", "")
            name = item.get("Chinese Name", "")
            herb_ingredients = get_chemical_ingredients(hvm_id)
            herb = Herb(hvm_id=hvm_id, name=name, ingredients=herb_ingredients)
            herb.parse_ingredients()
            formula.herbs.append(herb)

        
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
    return formula.herbs

def get_chemical_ingredients(hvm_id):
    url = f"http://117.72.73.151:80/api/chemical/tcm/{hvm_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        chemical_data = response.json().get("data", {}).get("chemicals", [])
        return chemical_data  # Return full ingredients data for the herb

    except requests.RequestException as e:
        print(f"Error fetching chemical ingredients from API: {e}")
        return []
    
def get_protein_targets(hvc_id):
    """Fetch protein targets for a given chemical compound using its hvc_id."""
    url = f"http://117.72.73.151:80/api/protein/chemical/{hvc_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        proteins_data = response.json().get("data", [])
        proteins_data = proteins_data.get("proteins",[])
        
        protein_targets = []
        for item in proteins_data:
            protein = Protein(
                ensembl_id=item.get("Ensembl id"),
                protein_name=item.get("Protein Name"),
                gene_name=item.get("Gene Name"),
                combined_score=item.get("Combined Score")
            )
            protein_targets.append(protein)
        
        return protein_targets

    except requests.RequestException as e:
        print(f"Error fetching protein targets: {e}")
        return []
    
def get_disease_targets(disease_key):
    """Fetch protein targets for a given chemical compound using its hvc_id."""
    url = "http://117.72.73.151:80/api/disease/target/all"
    # 定义请求的 payload
    payload = {
    "keyword": disease_key
    }

    # 将 payload 转换为 JSON 字符串
    payload_json = json.dumps(payload)

    # 定义 headers
    headers = {
    'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, data=payload_json, headers=headers)
        print(response)
        response.raise_for_status()
        disease_list = response.json().get("data", [])
        disease_name_list = []
        if len(disease_list)>0:
            for item in disease_list:
                disease_name_list.append(item.get("chineseName",""))
            disease_choice = input(f"共有{len(disease_list)}个结果，分别是：{disease_list}，请选择你要对哪个疾病进行分析：")
            disease_choice = disease_list[disease_name_list.index(disease_choice)]
        else:
            print("没有任何相关疾病")
        return Disease(id=disease_choice.get("id",""),chinese_name=disease_choice.get("chineseName",""),english_name=disease_choice.get("englishName",""),proteins=disease_choice.get("targetVOList",[]))

    except requests.RequestException as e:
        print(f"Error fetching disease targets: {e}")
        return []

formula_name = input("Enter the name of the herb: ")
disease_name = input("Enter the name of the disease: ")
# diseasea = get_disease_targets(disease_name)
formula = get_tcmid(formula_name)  # Get the Formula with hvp_id and name
print("他的tcm id为："+formula.hvp_id)
herbs = None
herbs_uniprot_list = []
disease_uniprot_list = []
if formula:
    herbs = get_herbs(formula)
for herb in herbs:
    for ingredient in herb.ingredients:
        ingredient.proteins = get_protein_targets(ingredient.hvc_id)
        print(len(herbs))
        print(len(herb.ingredients))
        print(len(ingredient.proteins))
        print("1")
        ingredient.parse_uniprot()
    herbs_uniprot_list.extend(herb.get_uniprot())
# for protein in diseasea.proteins:
#     disease_uniprot_list.append(protein.uniprot)

print(herbs_uniprot_list)
print(disease_uniprot_list)
