import requests
from io import BytesIO
from PIL import Image
import base64
from pathlib import Path

def load_image_from_url(image_url:str)->tuple[Image.Image, str] | None:
    try:
        res = requests.get(image_url, timeout=10)
        if res.status_code == 200:
            image = Image.open(BytesIO(res.content))
            return image, image.format.lower()
        else:
            print(f"Error loading image from URL: {res.status_code}")
            return None
    except Exception as e:
        print(f"Error loading image from URL: {e}")
        return None


def encode_the_image_b64(image:Image.Image|str)->str:
    """
    Encodes the image to base64
    args:
        image: Image object or image url like path
    returns:
        base64 encoded image
    """
    
    try:
        if isinstance(image, str):
            if not Path.exists(image):
                raise FileNotFoundError(f"Image not found at {image}")
            image = load_image_from_url(image)
            if image is None:
                raise ValueError(f"Error loading image from URL {image}")
        elif isinstance(image, Image.Image):
            buffered = BytesIO()
            image.save(buffered, format=image.format)
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return img_str
        else:
            raise TypeError(f"Invalid image type: {type(image)}")
    except Exception as e:
        raise e