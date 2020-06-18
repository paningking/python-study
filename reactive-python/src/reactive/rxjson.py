import requests
import rx
import json
from rx import operators as ops
import random

content = requests.get('https://jsonplaceholder.typicode.com/users')
y = json.loads(content.text)
source = rx.from_(y)
 
def filternames(x):
    if (x["name"].startswith("C")):
        return x["name"]
    else:
        return ""


def filterById(x):
    if (x["name"].startswith("C")):
        return x
    else:
        return ""

# case1 = source.pipe(
#     ops.filter(lambda c: filternames(c)),
#     ops.map(lambda a: a["name"])
# )

# case1.subscribe(
#     on_next=lambda i: print("Got - {0}".format(i)),
#     on_error=lambda e: print("Error : {0}".format(e)),
#     on_completed=lambda: print("Job Done!"),
# )

case2 = source.pipe(
    ops.filter(lambda c: filternames(c)),
    ops.flat_map(lambda a: a["id"])
)

case2.subscribe(
    on_next=lambda i: print("Got - {0}".format(i)),
    on_error=lambda e: print("Error : {0}".format(e)),
    on_completed=lambda: print("Job Done!"),
)
