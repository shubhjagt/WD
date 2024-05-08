# Dataset: SMSSpamCollection 
# Location: https://mitu.co.in/dataset #Download Dataset 
import pandas as pd 
df = pd.read_csv('D:SMSSpamCollection', sep = '\t', #Set your dataset location 
 names=['label','text']) 
df 
df.shape 
# input 
x = df['text'] 
# output 
y = df['label'] 
import seaborn as sns 
sns.countplot(x = y); 
y.value_counts() 
# 1. Remove the punctuation symbols 
# 2. Remove the stopwords 
# 3. Remove the stems 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
sent = 'Hello friends! How are you. Welcome to Nashik.' 
tokens = word_tokenize(sent) 
clean1 = [x.lower() for x in tokens if x.isalpha() or x.isdigit()] 
swords = stopwords.words('english') 
clean2 = [x for x in clean1 if x not in swords] 
ps = PorterStemmer() 
clean3 = [ps.stem(x) for x in clean2] 
def clean_text(sent): 
 tokens = word_tokenize(sent) 
 clean1 = [x.lower() for x in tokens if x.isalpha() or x.isdigit()] 
 clean2 = [x for x in clean1 if x not in swords] 
 clean3 = [ps.stem(x) for x in clean2] 
 return clean3 
clean_text(sent) 
x.apply(lambda a: clean_text(a)) 
from sklearn.feature_extraction.text import TfidfVectorizer 
tfidf = TfidfVectorizer(analyzer=clean_text) 
x_vect = tfidf.fit_transform(x) 
x_vect 
pd.DataFrame(x_vect) 
tfidf.get_feature_names_out() 
len(tfidf.get_feature_names_out()) 
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split( 
 x_vect, y, random_state=0, stratify=y)
x_train.shape 
x_test.shape 
from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(random_state=0) 
clf.fit(x_train, y_train) 
RandomForestClassifier(random_state=0) 
y_pred = clf.predict(x_test) 
from sklearn.metrics import classification_report, accuracy_score 
accuracy_score(y_test, y_pred) 
print(classification_report(y_test, y_pred)) 
# Download a sample.csv file for prediction 
# Location: https://mitu.co.in 
new = pd.read_csv('sample.csv', sep='\t', 
 names = ['text']) 
new = tfidf.transform(new['text']) 
new.shape 
clf.predict(new)