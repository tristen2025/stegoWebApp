
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import render_template
from flask import request,jsonify
 
# Flask constructor takes the name of
# current module (__name__) as argument.


from joblib import dump, load
clf= load('predictiontree2.joblib')
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')

def hello_world():
    return render_template("index.html")
@app.route('/cytoscape.min.js')

def getJS():
    return render_template("cytoscape.min.js")    

#@app.route('/lehmer')

#def getLehmer():
#    return render_template("lehmer.html")     
@app.route('/checkString', methods=['GET', 'POST'])
def parse_request():
    resDict = request.json # data is empty
    # need posted data here    
    el=resDict['string']
    print(el)
    tempList=[]
    for word in el.split(' '):
        if word=='.': continue
        word=word.lower()
        #print('is the current word ',word,' ',len(word))
        if len(word)==0: continue
        l= len(word)
        
        w=string.ascii_lowercase.index(word[0])

        tempList.append(w)
        tempList.append(l)
        if len(tempList)==500:
            break
    tempList += [0] * (500 - len(tempList))    
    while len(tempList)<500:
        tempList.append(0)
    #print(vectorizer.transform([el]).toarray())
    #pre=vectorizer.transform([el]).toarray()
    print(clf.predict([tempList]))
    #return clf.predict([tempList])
    return jsonify({"result":clf.predict([tempList])[0]})
 
# main driver function
#if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.


from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump, load
import random
import string
import sys
import re
'''
lines=[]
#with open(sys.argv[1]) as f:
#    lines = f.readlines()
original=[]
with open(sys.argv[1]) as f:
    original = f.readlines()
with open(sys.argv[2]) as f:
    stego = f.readlines()
print(original)
print(stego)
#vectorizer = CountVectorizer(min_df=0, lowercase=False)
#vectorizer.fit(lines)
train=[]
labels=[]
#trainorig=vectorizer.transform(original).toarray()
print("train orig is ")
#print(trainorig)
regex = re.compile('[^a-zA-Z ]')
original = [regex.sub('',w) for w in original]
for el in original:
    if random.randint(0,5)>4: continue
    tempList=[]
    #if len(el)==0: continue
    for word in el.split(' '):
        word=word.lower()
        print('is the current word ',word,' ',len(word))
        if len(word)==0: continue
        l= len(word)
        w=string.ascii_lowercase.index(word[0])
        tempList.append(w)
        tempList.append(l)
    tempList += [0] * (500 - len(tempList))    
    train.append(tempList)
    labels.append("orig")
#trainstego=vectorizer.transform(stego).toarray()
#print("train orig is ")
#print(trainstego)
stego = [regex.sub('',w) for w in stego]
for el in stego:
    if random.randint(0,5)>3: continue
    tempList=[]
    for word in el.split(' '):
        word=word.lower()
        print('is the current word ',word,' ',len(word))
        if len(word)==0: continue
        l= len(word)
        l= len(word)
        w=string.ascii_lowercase.index(word[0])
        tempList.append(w)
        tempList.append(l)
    tempList += [0] * (500 - len(tempList))  
    train.append(tempList)  
    labels.append("stego")
#train=[]
#train=original+stego
#train=vectorizer.transform(train).toarray()
#train.append(trainorig)
#trainorig.append(trainstego)
import numpy
#train=numpy.concatenate(trainorig,trainstego)
print(train)
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train, labels)
for el in original+stego:
    tempList=[]
    for word in el.split(' '):
        word=word.lower()
        #print('is the current word ',word,' ',len(word))
        if len(word)==0: continue
        l= len(word)
        
        w=string.ascii_lowercase.index(word[0])

        tempList.append(w)
        tempList.append(l)
    tempList += [0] * (500 - len(tempList))    
    #print(vectorizer.transform([el]).toarray())
    #pre=vectorizer.transform([el]).toarray()
    print(clf.predict([tempList]))

for el in sys.stdin:
    tempList=[]
    for word in el.split(' '):
        word=word.lower()
        #print('is the current word ',word,' ',len(word))
        if len(word)==0: continue
        l= len(word)
        
        w=string.ascii_lowercase.index(word[0])

        tempList.append(w)
        tempList.append(l)
    tempList += [0] * (500 - len(tempList))    
    #print(vectorizer.transform([el]).toarray())
    #pre=vectorizer.transform([el]).toarray()
    print(clf.predict([tempList]))
   
from joblib import dump, load
dump(clf, 'predictiontree1.joblib')
'''
app.run()