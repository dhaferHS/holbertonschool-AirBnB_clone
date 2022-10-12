#!//usr/bin/python3
"""impot modules"""

from models.base_model import BaseModel

"""class file for user"""


class User(BaseModel):
    """class user inherits from basemodel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
