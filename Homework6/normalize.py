import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфчцшщъыьэюя"
TRANSLATION = ("a","b","v","g","d","e","e","j","z","i","j","k","l","m","n","o","p","r","s","t","u","f","ch","c","sh","sch","","y","","e", "yu","ya")      


TRANS = {}
for c,l in zip(CYRILLIC_SYMBOLS,TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper
    
def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', "_", t_name)
    return t_name
