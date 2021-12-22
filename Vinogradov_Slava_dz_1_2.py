import re

# RE_IP = re.compile(r'^\d+[.]\d+[.]\d+[.]\d+')
# RE_DATE = re.compile(r'\d{2}[/]\w+[/]\d{4}[:]\d+[:]\d+[:]\d+[ ][+]\d{4}')
# RE_RESPONSE = re.compile(r'\"[A-Z]+[ ]')
# RE_RESOURCE = re.compile(r'/[a-z]+[/]\w+[ ]')
# RE_CODE = re.compile(r'\"[ ]\d{3}')
# RE_SIZE = re.compile(r'[ ]\d+[ ]\"')


COMP_ALL = re.compile(r'^\d+[.]\d+[.]\d+[.]\d+|\d{2}[/]\w+[/]\d{4}[:]\d+[:]\d+[:]\d+[ ][+]\d{4}|'
                      r'\"[A-Z]+[ ]|/[a-z]+[/]\w+[ ]|\"[ ]\d{3}|[ ]\d+[ ]\"')
result = []

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    pars_text = f.readlines()

for text in pars_text:
    result.append(re.findall(COMP_ALL, text))

print(result[0])
