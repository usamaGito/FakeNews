#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:
os.chdir("E:/Project")



#!pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html


# In[3]:


import pandas as pd


# In[4]:


os.chdir("liar_plus_dataset/")


# In[5]:


os.getcwd()


# In[6]:


columns = ['id_json', 'label', 'statement', 'subject', 
 'speaker', 'speaker_job', 'state', 'party', 
 'barely_true_counts', 'false_counts', 'half_true_counts',
 'mostly_true_counts', 'pants_on_fire_counts', 'context', 'justification']


# In[7]:


train_data = pd.read_csv("train2.tsv", sep='\t', header=None, index_col=0, names=columns)
val_data = pd.read_csv('val2.tsv', sep='\t', header=None, index_col=0, names=columns)
test_data = pd.read_csv('test2.tsv', sep='\t', header=None, index_col=0, names=columns)


# In[8]:


train_data.set_index('id_json',inplace=True)
val_data.set_index('id_json',inplace=True)
test_data.set_index('id_json',inplace=True)


# In[9]:


train_data.head()


# In[10]:


val_data.head()


# In[11]:


test_data.head()


# In[12]:


print(train_data.shape, val_data.shape, test_data.shape)


# In[13]:


data_na = pd.DataFrame(train_data.isnull().sum(), columns=['NAinTrain']).join(
    pd.DataFrame(val_data.isnull().sum(), columns=['NAinVal']).join(
        pd.DataFrame(test_data.isnull().sum(), columns=['NAinTest'])))


# In[14]:


print(data_na)


# In[15]:


# Dropping records where label in NA in Train 
train_data.dropna(subset=['label'],inplace=True)
# Viewing updated NA Dataframe 
data_na_1 = pd.DataFrame(train_data.isnull().sum(), columns=['NAinTrain']).join(
    pd.DataFrame(val_data.isnull().sum(), columns=['NAinVal']).join(
        pd.DataFrame(test_data.isnull().sum(), columns=['NAinTest'])))
print(data_na_1)


# In[16]:


# Dropping Records where the all the count flags are NA in train data 
train_data.dropna(subset=['barely_true_counts'],inplace=True)
# Viewing Updated NA Dataframe 
data_na_2 = pd.DataFrame(train_data.isnull().sum(), columns=['NAinTrain']).join(
    pd.DataFrame(val_data.isnull().sum(), columns=['NAinVal']).join(
        pd.DataFrame(test_data.isnull().sum(), columns=['NAinTest'])))
print(data_na_2)


# In[17]:


# Replacing all NA with "" (Empty space) speaker_job
train_data.speaker_job.fillna("", inplace=True)
val_data.speaker_job.fillna("", inplace=True)
test_data.speaker_job.fillna("", inplace=True)


# In[18]:


# Replacing all NA with "" (Empty space) state
train_data.state.fillna("", inplace=True)
val_data.state.fillna("", inplace=True)
test_data.state.fillna("", inplace=True)


# In[19]:


# Replacing all NA with "" (Empty space) Context
train_data.context.fillna("", inplace=True)
val_data.context.fillna("", inplace=True)
test_data.context.fillna("", inplace=True)


# In[20]:


# Replacing all NA with "" (Empty space) Justification
train_data.justification.fillna("", inplace=True)
val_data.justification.fillna("", inplace=True)
test_data.justification.fillna("", inplace=True)


# In[21]:


# Viewing Updated NA Dataframe 
data_na_3 = pd.DataFrame(train_data.isnull().sum(), columns=['NAinTrain']).join(
    pd.DataFrame(val_data.isnull().sum(), columns=['NAinVal']).join(
        pd.DataFrame(test_data.isnull().sum(), columns=['NAinTest'])))
print(data_na_3)


# In[22]:


# Handling the State column anamolies 
train_data.loc[train_data.state.isin(['None', 'Unknown']), 'state'] = ''
train_data.loc[train_data.state.isin(['Tennesse']), 'state'] = 'Tennessee'
train_data.loc[train_data.state.isin(['PA - Pennsylvania']), 'state'] = 'Pennsylvania'
train_data.loc[train_data.state.isin(['Rhode island']), 'state'] = 'Rhode Island'
train_data.loc[train_data.state.isin(['Tex']), 'state'] = 'Texas'
train_data.loc[train_data.state.isin(['Virgiia','Virgina', 'Virginia director, Coalition to Stop Gun Violence']), 'state'] = 'Virginia'
train_data.loc[train_data.state.isin(['Washington D.C.','Washington DC','Washington state', 'Washington, D.C.',]), 'state'] = 'Washington'

val_data.loc[val_data.state.isin(['None', 'Unknown']), 'state'] = ''
val_data.loc[val_data.state.isin(['Tennesse']), 'state'] = 'Tennessee'
val_data.loc[val_data.state.isin(['PA - Pennsylvania']), 'state'] = 'Pennsylvania'
val_data.loc[val_data.state.isin(['Rhode island']), 'state'] = 'Rhode Island'
val_data.loc[val_data.state.isin(['Tex']), 'state'] = 'Texas'
val_data.loc[val_data.state.isin(['Virgiia','Virgina', 'Virginia director, Coalition to Stop Gun Violence']), 'state'] = 'Virginia'
val_data.loc[val_data.state.isin(['Washington D.C.','Washington DC','Washington state', 'Washington, D.C.',]), 'state'] = 'Washington'


val_data.loc[val_data.state.isin(['None', 'Unknown']), 'state'] = ''
val_data.loc[val_data.state.isin(['Tennesse']), 'state'] = 'Tennessee'
val_data.loc[val_data.state.isin(['PA - Pennsylvania']), 'state'] = 'Pennsylvania'
val_data.loc[val_data.state.isin(['Rhode island']), 'state'] = 'Rhode Island'
val_data.loc[val_data.state.isin(['Tex']), 'state'] = 'Texas'
val_data.loc[val_data.state.isin(['Virgiia','Virgina', 'Virginia director, Coalition to Stop Gun Violence']), 'state'] = 'Virginia'
val_data.loc[val_data.state.isin(['Washington D.C.','Washington DC','Washington state', 'Washington, D.C.',]), 'state'] = 'Washington'


# In[23]:


train_data['Text'] = train_data['statement'].map(str) + train_data['justification'].map(str)
val_data['Text']   = val_data['statement'].map(str) + val_data['justification'].map(str)
test_data['Text']  = test_data['statement'].map(str) + test_data['justification'].map(str)


# In[24]:


train_data = train_data.drop(labels=['statement','justification'],axis=1)
val_data   = val_data.drop(labels=['statement','justification'],axis=1)
test_data  = test_data.drop(labels=['statement','justification'],axis=1)


# In[25]:


val_data['Text']


# In[26]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


# In[27]:


Y_train = le.fit_transform(train_data['label'])
Y_val   = le.fit_transform(val_data['label'])
Y_test  = le.fit_transform(test_data['label'])
#le.inverse_transform(Y_train)


# In[28]:


#Test
#le.inverse_transform(Y_train)
#le.inverse_transform(Y_val)
#le.inverse_transform(Y_test)


# In[29]:


X_train = train_data.drop(labels=['label'],axis=1)
X_val   = val_data.drop(labels=['label'],axis=1)
X_test  = test_data.drop(labels=['label'],axis=1)


# In[30]:


print(" X Train Data ")
print(X_train.head())
print(" X Val Data ")
print(X_val.head())
print(" X Test Data ")
print(X_test.head())


# In[31]:


print(" X Train Columns")
print(X_train.columns)
print(" X Val Columns ")
print(X_val.columns)
print(" X Test Columns ")
print(X_test.columns)


# In[32]:


CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have",
}
# The code for expanding contraction words
def expand_contractions(text, contraction_mapping =  CONTRACTION_MAP):
    """expand shortened words to the actual form.
       e.g. don't to do not
    
       arguments:
            input_text: "text" of type "String".
         
       return:
            value: Text with expanded form of shorthened words.
        
       Example: 
       Input : ain't, aren't, can't, cause, can't've
       Output :  is not, are not, cannot, because, cannot have 
    
     """
    # Tokenizing text into tokens.
    list_Of_tokens = text.split(' ')

    # Checking for whether the given token matches with the Key & replacing word with key's value.
    
    # Check whether Word is in lidt_Of_tokens or not.
    for Word in list_Of_tokens: 
        # Check whether found word is in dictionary "Contraction Map" or not as a key. 
         if Word in CONTRACTION_MAP: 
                # If Word is present in both dictionary & list_Of_tokens, replace that word with the key value.
                list_Of_tokens = [item.replace(Word, CONTRACTION_MAP[Word]) for item in list_Of_tokens]
                
    # Converting list of tokens to String.
    String_Of_tokens = ' '.join(str(e) for e in list_Of_tokens) 
    return String_Of_tokens


# In[33]:


#Punctuation deleting
#Lowercase + strip
#Numbers replacement with "NUM" token
#Extra whitespaces removing
txt_features = ['context', 'subject', 'speaker_job', 'Text']

for feature in txt_features:
    X_train[feature] = X_train[feature].str.replace(r'[^\w\s]+', ' ')
    X_train[feature] = X_train[feature].apply(lambda x: x.lower().strip())
    X_train[feature] = X_train[feature].str.replace('\w*\d+\w*','NUM')
    X_train[feature] = X_train[feature].str.replace('\s{2,}',' ')
    


for feature in txt_features:
    X_val[feature] = X_val[feature].str.replace(r'[^\w\s]+', ' ')
    X_val[feature] = X_val[feature].apply(lambda x: x.lower().strip())
    X_val[feature] = X_val[feature].str.replace('\w*\d+\w*','NUM')
    X_val[feature] = X_val[feature].str.replace('\s{2,}',' ')
    


for feature in txt_features:
    X_test[feature] = X_test[feature].str.replace(r'[^\w\s]+', ' ')
    X_test[feature] = X_test[feature].apply(lambda x: x.lower().strip())
    X_test[feature] = X_test[feature].str.replace('\w*\d+\w*','NUM')
    X_test[feature] = X_test[feature].str.replace('\s{2,}',' ')


# In[34]:


print(X_train['subject'].value_counts().nunique())
print(X_train['speaker'].value_counts().nunique())
print(X_train['speaker_job'].value_counts().nunique())
print(X_train['state'].value_counts().nunique())
print(X_train['party'].value_counts().nunique())
print(X_train['context'].value_counts().nunique())


# In[35]:


# Label Encoding subject,speaker,speaker job, state and party
le_subj    = LabelEncoder()
le_spkr    = LabelEncoder()
le_spkr_jb = LabelEncoder()
le_state   = LabelEncoder()
le_prty    = LabelEncoder()
le_ctxt    = LabelEncoder()

X_train['subject'] = le_subj.fit_transform(X_train['subject'])
X_train['speaker']   = le_spkr.fit_transform(X_train['speaker'])
X_train['speaker_job']   = le_spkr_jb.fit_transform(X_train['speaker_job'])
X_train['state']   = le_state.fit_transform(X_train['state'])
X_train['party']   = le_prty.fit_transform(X_train['party'])
X_train['context']   = le_ctxt.fit_transform(X_train['context'])

X_val['subject'] = le_subj.fit_transform(X_val['subject'])
X_val['speaker']   = le_spkr.fit_transform(X_val['speaker'])
X_val['speaker_job']   = le_spkr_jb.fit_transform(X_val['speaker_job'])
X_val['state']   = le_state.fit_transform(X_val['state'])
X_val['party']   = le_prty.fit_transform(X_val['party'])
X_val['context']   = le_ctxt.fit_transform(X_val['context'])

X_test['subject'] = le_subj.fit_transform(X_test['subject'])
X_test['speaker']   = le_spkr.fit_transform(X_test['speaker'])
X_test['speaker_job']   = le_spkr_jb.fit_transform(X_test['speaker_job'])
X_test['state']   = le_state.fit_transform(X_test['state'])
X_test['party']   = le_prty.fit_transform(X_test['party'])
X_test['context']   = le_ctxt.fit_transform(X_test['context'])


# In[36]:


print(" ----------------------- X Train Data ---------------------------- ")
print(X_train.head())
print(" ----------------------- X Val Data   ------------------------------")
print(X_val.head())
print(" ----------------------- X Test Data  ------------------------------")
print(X_test.head())


# In[37]:


X_train_idx = X_train.index
X_val_idx   = X_val.index
X_test_idx  = X_test.index


# In[38]:


X_test_idx


# In[39]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import  LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.metrics import confusion_matrix, f1_score, classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn import svm
from sklearn import metrics

#from gensim.models.word2vec import Word2Vec


# In[40]:


# Count Vectorizer Implementation 
# create a count vectorizer objec
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}',stop_words='english')
count_vect.fit(X_train['Text'])
# transform the training, testing and validation data using count vectorizer object
X_train_count =  count_vect.transform(X_train['Text'])
X_val_count   =  count_vect.transform(X_val['Text'])
X_test_count  =  count_vect.transform(X_test['Text'])


# In[41]:


# TF IDF Implementation 
#
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)
tfidf_vect.fit(X_train['Text'])
X_train_tfidf =  tfidf_vect.transform(X_train['Text'])
X_val_tfidf   =  tfidf_vect.transform(X_val['Text'])
X_test_tfidf  =  tfidf_vect.transform(X_test['Text'])


# In[42]:


X_train_af = X_train[['subject', 'speaker', 'speaker_job', 'state', 'party',
       'barely_true_counts', 'false_counts', 'half_true_counts',
       'mostly_true_counts', 'pants_on_fire_counts', 'context']]


# In[43]:


X_val_af = X_val[['subject', 'speaker', 'speaker_job', 'state', 'party',
       'barely_true_counts', 'false_counts', 'half_true_counts',
       'mostly_true_counts', 'pants_on_fire_counts', 'context']]


# In[44]:


X_test_af = X_test[['subject', 'speaker', 'speaker_job', 'state', 'party',
       'barely_true_counts', 'false_counts', 'half_true_counts',
       'mostly_true_counts', 'pants_on_fire_counts', 'context']]


# In[45]:


# Modelling
#naive bayes classifier
naive_bayes_classifier_count = MultinomialNB()
naive_bayes_classifier_count.fit(X_train_count, Y_train)


# In[46]:


# Predictions 
#predicted y
y_pred_val_count = naive_bayes_classifier_count.predict(X_val_count)
y_pred_test_count = naive_bayes_classifier_count.predict(X_test_count)


# In[47]:


# Validation Metrics 
print(metrics.classification_report(Y_val, y_pred_val_count))
# Test Metrics 
print(metrics.classification_report(Y_test, y_pred_test_count))


# In[48]:


# Naive Bayes with tfidf

naive_bayes_classifier_tfidf = MultinomialNB()
naive_bayes_classifier_tfidf.fit(X_train_tfidf, Y_train)

y_pred_val_tfidf = naive_bayes_classifier_tfidf.predict(X_val_tfidf)
y_pred_test_tfidf = naive_bayes_classifier_tfidf.predict(X_test_tfidf)


# In[49]:


# Validation Metrics 
print(metrics.classification_report(Y_val, y_pred_val_tfidf))
# Test Metrics 
print(metrics.classification_report(Y_test, y_pred_test_tfidf))


# In[50]:


# Merging additional features with vectors
X_train_af_count   =  X_train_af.merge(pd.DataFrame(X_train_count.toarray(),index=X_train_idx),left_index=True, right_index=True
)

X_val_af_count    =  X_val_af.merge(pd.DataFrame(X_val_count.toarray(),index=X_val_idx),left_index=True, right_index=True
)

X_test_af_count   =  X_test_af.merge(pd.DataFrame(X_test_count.toarray(),index=X_test_idx),left_index=True, right_index=True
)

X_train_af_tfidf  =  X_train_af.merge(pd.DataFrame(X_train_tfidf.toarray(),index=X_train_idx),left_index=True, right_index=True
)

X_val_af_tfidf    =  X_val_af.merge(pd.DataFrame(X_val_tfidf.toarray(),index=X_val_idx),left_index=True, right_index=True
)

X_test_af_tfidf   =  X_test_af.merge(pd.DataFrame(X_test_tfidf.toarray(),index=X_test_idx),left_index=True, right_index=True
)


# In[51]:


X_val_af_tfidf


# In[ ]:


# Naive Bayes with count vector with additional features

naive_bayes_classifier_count_af = MultinomialNB()
naive_bayes_classifier_count_af.fit(X_train_af_count, Y_train)

y_pred_val_count_af    = naive_bayes_classifier_count_af.predict(X_val_af_count)
y_pred_test_count_af   = naive_bayes_classifier_count_af.predict(X_test_af_count)


# In[ ]:


# Validation Metrics 
print(metrics.classification_report(Y_val, y_pred_val_count_af))
# Test Metrics 
print(metrics.classification_report(Y_test, y_pred_test_count_af))


# In[ ]:


# Naive Bayes with tfidf with additional features 


# In[ ]:


naive_bayes_classifier_tfidf_af = MultinomialNB()
naive_bayes_classifier_tfidf_af.fit(X_train_af_tfidf, Y_train)

y_pred_val_tfidf_af    = naive_bayes_classifier_tfidf_af.predict(X_val_af_tfidf)
y_pred_test_tfidf_af   = naive_bayes_classifier_tfidf_af.predict(X_test_af_tfidf)


# In[ ]:


# Validation Metrics 
print(metrics.classification_report(Y_val, y_pred_val_tfidf_af))
# Test Metrics 
print(metrics.classification_report(Y_test, y_pred_test_tfidf_af))


# In[ ]:





# In[57]:


# Testing pytorch GPU 
import torch

torch.cuda.is_available()


# In[58]:


# Checking GPU 
torch.cuda.get_device_name(0)


# In[59]:


#!pip install TPOT


# In[59]:


from tpot import TPOTClassifier
from sklearn.model_selection import RepeatedStratifiedKFold


# In[60]:


cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)


# In[72]:


tpot = TPOTClassifier(max_time_mins=600, population_size=50, verbosity=2, random_state=42, cv= cv, scoring='accuracy', config_dict ='TPOT NN', warm_start=True)
tpot.fit(X_train_af_count, Y_train)
print(tpot.score(X_test_af_count, Y_test))


# In[75]:


print(tpot.score(X_test_af_count, Y_test))


# In[76]:


print(tpot.score(X_val_af_count, Y_val))


# In[73]:


tpot.export('tpot_exported_pipeline_2_linux_count.py')


# In[61]:


os.getcwd()


# In[ ]:


# Implemenation of TFIDF with TPOT


# In[ ]:


tpot_tfidf = TPOTClassifier(max_time_mins=150, population_size=50, verbosity=3, random_state=42, cv= cv, scoring='accuracy', config_dict ='TPOT NN', warm_start=True, n_jobs=-1)
tpot_tfidf.fit(X_train_af_tfidf, Y_train)
print(tpot_tfidf.score(X_test_af_tfidf, Y_test))


# In[ ]:

tpot.export('tpot_exported_pipeline_linux_tfidf.py')


