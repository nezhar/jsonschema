import json
import time

import yaml

import jsonschema

# https://raw.githubusercontent.com/tfranzel/drf-spectacular/master/tests/test_basic.yml
with open('tests/test_basic.yml') as fh:
    data = yaml.load(fh.read(), Loader=yaml.SafeLoader)

# https://raw.githubusercontent.com/tfranzel/drf-spectacular/master/drf_spectacular/validation/openapi3_schema.json
# which comes from:
# https://github.com/OAI/OpenAPI-Specification/blob/6d17b631fff35186c495b9e7d340222e19d60a71/schemas/v3.0/schema.json
with open('tests/openapi3_schema.json') as fh:
    openapi3_schema_spec = json.load(fh)

t_acc = 0

for i in range(500):
    t0 = time.time()
    jsonschema.validate(instance=data, schema=openapi3_schema_spec)
    t1 = time.time()
    t_acc += t1 - t0

print(f'{t_acc} sec')
