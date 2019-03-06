
import re 
import numpy as np
import nltk
from sklearn.datasets import load_files
from nltk.corpus import stopwords
import pickle
from sklearn.externals import joblib
nltk.download('stopwords')

reviews=load_files("DocumentClassification/datasets/")
X,y=reviews.data,reviews.target
corpus=[]
for i in range(len(X)):
    review=re.sub(r'\W',' ',str(X[i]))
    review=review.lower()
    review=re.sub(r'\s+[a-zA-Z]\s+',' ',review)
    review=re.sub(r'^[a-zA-Z]\s+',' ',review)
    review=re.sub(r'\s+',' ',review)
    corpus.append(review)
"""    
from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer(max_features=3000,min_df=3,max_df=0.7,stop_words=stopwords.words('english'))
X=vectorizer.fit_transform(corpus).toarray()

from sklearn.feature_extraction.text import TfidfTransformer
transformer=TfidfTransformer()
X=transformer.fit_transform(X).toarray()
# splitting into test and train
"""
   
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(max_features=3000,min_df=3,max_df=0.7,stop_words=stopwords.words('english'))
X=vectorizer.fit_transform(corpus).toarray()



from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection  import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=0)

 

model = SVC(C = 10000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)



from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)


# accuracy
print("accuracy", metrics.accuracy_score(y_test, y_pred))

"""
joblib.dump(model,'classifier_model_joblib1')

joblib.dump(vectorizer,'vectorizer_joblib1')

#vjb=joblib.load('/home/maldanna/vectorizer_joblib1')

vjb=joblib.load('vectorizer_joblib1')
cmp=joblib.load('classifier_model_joblib1')


sample=[" As per the landing page of the Women's Day Sale on Flipkart, the Honor 9N will be available at Rs. 9,999, down from the launch price of Rs. 11,999. The Nokia 6.1 Plus will also receive a price cut and will go on sale at Rs. 13,999, down from Rs. 15,499. Similarly, the Vivo V9 Pro will be available during the sale at Rs. 13,990. This is Rs. 2,000 discounted from the launch price of Rs. 15,990. To see the individual listed offers, you need visit Flipkart.com on your mobile browser, or through the Flipkart app. The company was initially showing the offers on the Flipkart desktop website as well, but it later removed the links to respective offers."]

sample1=vjb.transform(sample).toarray()


print(cmp.predict(sample1))

"""
import pickle
#home/maldanna/Desktop/project/vectorizer.pickle
with open('model_pickle','wb') as file2:
    pickle.dump(model,file2)
with open('vectorizer_pickle','wb') as file1:
    pickle.dump(vectorizer,file1)


with open('/home/maldanna/Desktop/project/vectorizer_pickle','rb') as f:
    vet=pickle.load(f)

with open('/home/maldanna/Desktop/project/model_pickle','rb') as k:
    clf=pickle.load(k)

sample=["   Director Sukumar has raised curtains to many speculations other day as his film with Allu Arjun got announced, dumping his project with Mahesh. Though the Superstar has later given confirmation that the project is not happening due to creative differences, there is huge pressure on this director now.    Apparently, the Rangasthalam man has to prove two things now. The first one is that he is right with his creative differences over the story he narrated to Mahesh. He has to prove that Mahesh missed out a good story, which would have become another milestone in his career."]
sample1=vet.transform(sample).toarray()

print(clf.predict(sample1))


      """
import pickle
#home/maldanna/Desktop/project/vectorizer.pickle
with open('/home/maldanna/Desktop/project/vectorizer.pickle','rb') as f:
    vet=pickle.load(f)
with open('/home/maldanna/Desktop/project/classifier.pickle','rb') as k:
    clf=pickle.load(k)
sample=[]
sample1=vet.transform(sample).toarray()
print(clf.predict(sample1))

"""
