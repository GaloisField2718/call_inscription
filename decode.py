from PIL import Image
import base64
import io
import os

def create_collection_folder(collection_name, trait_types):
    try:
        os.mkdir(collection_name)
    except FileExistsError:
        pass

    try:
        os.mkdir(f'{collection_name}/traits')
    except FileExistsError:
        pass
    
    try:
        for trait_type in trait_types:
            os.mkdir(f'{collection_name}/traits/{trait_type}')
    except FileExistsError:
        pass



def generate_trait_picture(collection_name,trait_type,name,data):
    name = name.replace(' ', '')

    # Decode base64 string to image data
    image_data = base64.b64decode(data)

    # Open image from bytes
    img = Image.open(io.BytesIO(image_data))

    # Save image as PNG
    img.save(f'{collection_name}/traits/{trait_type}/{name}.png')


trait_types = [
    "sex",
    "face",
    "hair",
    "ears",
    "cheeks",
    "neck",
    "emotion",
    "beard",
    "lips",
    "teeth",
    "mouth",
    "eyes",
    "nose"
  ]

create_collection_folder('gbrc721bitpunks',trait_types)


name = "Big Beard"
data = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABXSURBVEhL7c3LCQAgDAPQDuRsjuWaav0hpRUVveVBLpJGAgAA2BW8i1Za5Y42qCVXjz+yhgbx/uYDK9yvZ/vUISvcr2dnyqE2KNO61/rAl3FpfDZlgSgBffmb8cxMAMwAAAAASUVORK5CYII="

generate_trait_picture('gbrc721bitpunks','beard',name, data)




