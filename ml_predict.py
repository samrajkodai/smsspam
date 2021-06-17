import pickle
cv=pickle.load(open('cv-transform.pkl','rb'))
clas=pickle.load(open('predict.pkl','rb'))

def prdict(data):
  data=[data]
  x=cv.transform(data).toarray()
  s=clas.predict(x)
  if s==0:
    return 'not spam'
  else:
    return "spam "
