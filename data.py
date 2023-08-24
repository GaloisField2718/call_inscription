import requests
import json
import decode
import os

######################################################################################
######              EXTRACT EACH IMAGE FROM gen-brc-721 PROTOCOL        ##############
######################################################################################

def extract_all_images(inscription_id):
    response_table = requests.get(f'https://ordinals.link/content/{inscription_id}')
    table = json.loads(response_table.text)

    collection_name = table["slug"]
    trait_types = table["trait_types"]
    traits = table["traits"]

    decode.create_collection_folder(collection_name,trait_types)

    elements_per_trait = {}
    counter = 0
    arrangements = 1
    data_per_trait = {}
    print("Trait types : ", trait_types)

    for trait_type in trait_types:
        #print(f'For {trait_type} we have : {traits[trait_type]}')
        number_element = len(traits[trait_type])
        counter += number_element
        arrangements *= number_element
        elements_per_trait.update({trait_type : number_element})

#        print(f'For {trait_type} we have : {number_element} traits')

        for trait in traits[trait_type]:
            name = ((traits[trait_type])[trait])["name"]
            data64 = ((traits[trait_type])[trait])["base64"]
            decode.generate_trait_picture(collection_name,trait_type,name,data64)

#            print(f'\n Folder {collection_name}/traits/{trait_type} contains : \n', os.listdir(f'{collection_name}/traits/{trait_type}'))
            
#            data_per_trait.update({trait_type : ["name": name, "data": data64]})
	
	
    print(f"This is the collection {collection_name} with : \n")
    print("Elements per trait : ",elements_per_trait)
    print('total element : ', counter) 
    arrangements = "{:=,}".format(arrangements)
    print('total arrangements : ', arrangements)


import sys

try:
    inscription_id = sys.argv[1]
    extract_all_images(inscription_id)

except IndexError:
    inscription_id = 'c3915284759eaba761f6e5acf64b50e1089fe62448b595f61a40407d71bfb85ei0'
    extract_all_images(inscription_id)


#response_punk= requests.get('https://static.unisat.io/inscription/content/8220176400f4188a51e1a2aaa51020d3b821c6aa697fff8973cc04ed9aebd439i0')

#content = json.loads(response_punk.text)

#traits = content['a']







