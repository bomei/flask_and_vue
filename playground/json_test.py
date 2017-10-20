d=dict()
d['你好']='hello'
import json
res = json.dumps(d)
print(res)
dd=json.loads(res)
print(dd)