#!/usr/bin/python3
"""import modules"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """ base class for instance """

    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

    def __str__(self):
        """return tring with some information about thhe object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute with date"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ return a dictionary containing al keys and values of dict of the instance"""
        dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                dict[key] = value.isoformat()
            else:
                dict[key] = value
        return dict
