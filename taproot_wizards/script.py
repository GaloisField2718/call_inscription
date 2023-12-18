#############################################
###             IMPORT                  ####
###########################################

# Manage data and commands
import json
import sys
import os

# Manage images
import requests
from PIL import Image
from io import BytesIO

#############################################
###     FUNCTIONS  GETTER               ####
###########################################

def get_ids_inscriptions(inscriptions_file) -> list[str]:
    """
        Get inscriptions ids from inscriptions.json collection description in 
        -> https://github.com/ordinals-wallet/ordinals-collections/tree/de39bdc496424b690cf8e03a64e37b9f5e01f81d/collections.
        @param: inscriptions_file.json
    """
    # Load JSON data from the file
    with open(inscriptions_file, 'r') as file:
        inscriptions = json.load(file)
    
    ids = []
    nb_inscriptions = len(inscriptions)

    for index in range(nb_inscriptions):
        inscription_id = inscriptions[index]["id"]
        ids.append(inscription_id)

    return ids

def get_image_from_id(inscription_id: str) -> Image:
    """
        Request localhost ordinal server from inscription_id to get content of inscription.
        @param : inscription_id
    """
    image_url = f"http://0.0.0.0:80/content/{inscription_id}"
    response = requests.get(image_url)

    if response.status_code == 200:
        image_content = response.content
        
        # Create a PIL Image object from the image content
        image = Image.open(BytesIO(image_content))

        # To visualise one image. Not using with save_all_wizards
        #image.show()

        return image

    else:
        print(f"Failed to download image. Status code: {response.status_code}")



#############################################
###     FUNCTIONS SAVERS IMAGES         ####
###########################################


def save_image(image: Image, name_image: str):
    """
        Save image given in paramter into global variable folder not given in parameter.
        @param : image
    """
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    save_path = os.path.join(save_folder, f'{name_image}.png')

    image.save(save_path)


def save_all_wizards(ids):
    
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for index in range(len(ids)):
        name_wizard = f"wizard_{index}"
        image = get_image_from_id(ids[index])
        save_image(image, name_wizard)


#############################################
###             MAIN                    ####
###########################################


if __name__ == "__main__":

    file_path = './inscriptions.json'
    save_folder = './wizards'

    ids = get_ids_inscriptions(file_path)
    save_all_wizards(ids)

