import os
import secrets
from app import app
from PIL import Image


def save_picture(form_picture):

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_filename)

    output_size_file = (125, 125)
    result_image = Image.open(form_picture)
    result_image.thumbnail(output_size_file)
    result_image.save(picture_path)

    return picture_filename
