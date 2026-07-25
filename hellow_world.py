print("Hello World")
from datetime import datetime
print("Hello Again ",datetime.now())
print(str(datetime.now()))
print("Hello Again")
print("hellow Again")
for func in list(dir(datetime)):
    if not func.startswith('__'):
        print(f'{func}',f'{help(func)}')