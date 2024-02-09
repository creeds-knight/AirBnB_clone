#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel


all_objs = storage.all()
print("####### reloading")
storage.reload()


print("printing storage********",all_objs)
print("len of storage before ********",len(all_objs))
pep = BaseModel()
storage.new(pep)
print("len after but before saveing",len(all_objs))
print("++++++++ saving")
storage.save()
print("len after saving",len(all_objs))


print("####### reload")

