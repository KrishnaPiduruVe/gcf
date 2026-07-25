print("Hello World")
from datetime import datetime
print("Hello Again ",datetime.now())
print(str(datetime.now()))
for func in list(dir(datetime)):
    if not func.startswith('__'):
        print(func)