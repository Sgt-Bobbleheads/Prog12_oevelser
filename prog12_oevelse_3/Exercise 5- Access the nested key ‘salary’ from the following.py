import json


sample_json = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data=json.loads(sample_json)
print(data["company"]["employee"]["payble"]["salary"])
print(data.get("company").get("employee").get("payble").get("salary"))
