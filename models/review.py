#!//usr/bin/python3
"""impot modules"""

from models.base_model import BaseModel

"""class file for review"""


class Review(BaseModel):
    """class user inherits from basemodel"""

    place_id = ""
    user_id = ""
    text = ""
