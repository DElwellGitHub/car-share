import re

email = 'john.smith@gmail'
regex_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
if re.fullmatch(regex_pattern, email):
    print('Good')
else:
    print('Bad')
