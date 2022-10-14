#!/usr/bin/python3
"""import modules"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """ base class for instance """

    def __init__(self, *args, **kwargs):
        """intialisation of id abd the instance with datetime
        args:
            args: set for arguments
            kwargs: sts for the named arguments
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return tring with some information about thhe object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute with date"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary containing keys and values dict of instance"""

        dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                dict[key] = value.isoformat()
            else:
                dict[key] = value
        return dict
