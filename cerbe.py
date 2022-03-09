from cerberus import Validator

v = Validator({'name': {'type': 'string'}})
print(v.validate({'name': 'john doe'}))

m = Validator({'id': {'type': 'integer'}})
print(m.validate({'id': 1 }))