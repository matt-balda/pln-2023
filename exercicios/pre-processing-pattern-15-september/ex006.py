import re
import nltk
from unidecode import unidecode
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import RSLPStemmer
nltk.download('rslp')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

inputt = "Joãozinho e Maria, dois irmãos aventureiros, decidiram explorar a floresta misteriosa próxima à sua casa. A floresta era densa, com árvores altas e folhagem espessa. Enquanto caminhavam, João e Maria encontraram pegadas estranhas no chão e decidiram segui-las. As pegadas os levaram a uma clareira onde descobriram uma casa feita inteiramente de doces! Ficaram fascinados e não resistiram à tentação de experimentar os doces. Mas, assim que começaram a comer, uma bruxa má e enrugada apareceu. A bruxa riu de forma maligna e os assustou. Joãozinho e Maria, apavorados, deixaram os doces e fugiram da casa. A bruxa tentou segui-los, mas eles eram ágeis e conseguiram escapar. Finalmente, após uma longa e cansativa jornada, João e Maria voltaram em segurança para sua casa, onde prometeram nunca mais se aventurar naquela floresta perigosa.".lower() 

inputNoAccent = unidecode(inputt) 

searchRegex = re.compile(r'\b(João|Joãozinho|Maria)\b', re.IGNORECASE) # regex para selecionar João, Joãozinho e Maria

changedInput = searchRegex.sub(lambda match: match.group().upper(), inputt) # modifique o texto

print(changedInput)

tokenizeRegex = re.findall(r'\b\w+\b', inputNoAccent) 

stopwords = stopwords.words('portuguese')

lemmatizer = WordNetLemmatizer()

stemmer = RSLPStemmer()

filteredTokens = []

for word in tokenizeRegex:
    if word not in stopwords:
        filteredTokens.append(word)

lemmatizedWords = [lemmatizer.lemmatize(word, pos='v') for word in filteredTokens]

stemmedWords = [stemmer.stem(word) for word in filteredTokens]

# for original, lemmatized in zip(filteredTokens, lemmatizedWords):
#     print(f"Original: {original}, Lemmatized: {lemmatized}")
    
# for original, stemmed in zip(filteredTokens, stemmedWords):
#     print(f"Original: {original}, Stemmed: {stemmed}")