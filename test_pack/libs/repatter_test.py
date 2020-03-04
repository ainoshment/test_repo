import re

pattern = r"ca"
text = "caabsacasca"
text2 = "wwwwwwwww"
repatter = re.compile(pattern)
matchOB = repatter.match(text)
print(matchOB)