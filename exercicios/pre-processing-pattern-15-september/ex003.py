import re
import nltk
from unidecode import unidecode
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

inputt = "Joãozinho e Maria, dois irmãos aventureiros, decidiram explorar a floresta misteriosa próxima à sua casa. A floresta era densa, com árvores altas e folhagem espessa. Enquanto caminhavam, João e Maria encontraram pegadas estranhas no chão e decidiram segui-las. As pegadas os levaram a uma clareira onde descobriram uma casa feita inteiramente de doces! Ficaram fascinados e não resistiram à tentação de experimentar os doces. Mas, assim que começaram a comer, uma bruxa má e enrugada apareceu. A bruxa riu de forma maligna e os assustou. Joãozinho e Maria, apavorados, deixaram os doces e fugiram da casa. A bruxa tentou segui-los, mas eles eram ágeis e conseguiram escapar. Finalmente, após uma longa e cansativa jornada, João e Maria voltaram em segurança para sua casa, onde prometeram nunca mais se aventurar naquela floresta perigosa.".lower() ## colocar em minúsculo

inputNoAccent = unidecode(inputt) # remoção dos acentos com unidecode

tokenizeRegex = re.findall(r'\b\w+\b', inputNoAccent) 

stopwords = stopwords.words('portuguese')

filteredTokens = []

for word in tokenizeRegex:
    if word not in stopwords:
        filteredTokens.append(word)

print(filteredTokens)