#!/usr/bin/env python
# coding: utf-8

# # Import Data and required Libraries

# In[95]:


get_ipython().system('pip install pandas')


# In[96]:


get_ipython().system('pip install numpy')


# In[97]:


get_ipython().system('pip install matplotlib')


# In[98]:


get_ipython().system('pip install boto3')


# In[ ]:


get_ipython().system('pip install scikit-learn')


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import boto3
#from google.colab import files


# In[2]:


get_ipython().system('pip install s3fs')


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# In[4]:


get_ipython().system('pip install --force-reinstall --no-deps fsspec==2023.6.0')


# # Retrieve Data From S3 

# In[5]:


#bucket='tshfyptest/read'
data_key = r"C:\Users\ASUS\Desktop\is483_project\TSH_Application\backend\ML\WA_Fn-UseC_-HR-Employee-Attrition.csv"
# data_key = 'WA_Fn-UseC_-HR-Employee-Attrition.csv'
#data_location = 's3://{}/{}'.format(bucket, data_key)

df_original = pd.read_csv(data_key)


# In[6]:


df_original.info()


# # Data Cleaning

# In[7]:


# Drop the unnecessary columns (no variability, not helpful, meaningless, highly correlating variables)
df_dropped = df_original.drop(columns = ["Department","EmployeeCount", "Over18", "StandardHours", "EmployeeNumber",'DailyRate', 'HourlyRate','JobRole','Age','BusinessTravel','DistanceFromHome','EnvironmentSatisfaction','JobInvolvement','JobLevel','JobSatisfaction','MaritalStatus','MonthlyIncome','MonthlyRate','OverTime','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','StockOptionLevel','TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','Gender'])

df_dropped.head()


# According to Dataset, Education: 
# 
# 1 'Below College'
# 2 'College'
# 3 'Bachelor'
# 4 'Master'
# 5 'Doctor'

# In[8]:


# Create an array of all categorical datatypes
cat_cols = ['Attrition','EducationField']
cat_cols


# In[9]:


df_noncat = df_dropped.drop(columns=cat_cols)
df_noncat.columns


# In[10]:


df_cat = df_dropped.loc[:,cat_cols]
df_cat.columns


# **Trying to reduce dimensions for encoded categorical variables**

# Mapping education field to 2 columns, stem and non-stem education
# 
# - Life Sciences = STEM
# - Medical = STEM
# - Marketing = non-STEM
# - Technical Degree = STEM
# - Other = non-STEM
# - Human Resources = non-STEM

# In[11]:


df_cat['EducationField'].value_counts()


# In[12]:


cleanup_edu = {"EducationField": {"Life Sciences": "stem", 
                                  "Medical": "stem",
                                  "Marketing": "non-stem",
                                  "Technical Degree": "stem",
                                  "Other": "non-stem",
                                  "Human Resources": "non-stem"}}


# In[13]:


df_cat.replace(cleanup_edu, inplace=True)

df_cat.head()


# In[14]:


df_cat = pd.get_dummies(df_cat, columns=["EducationField"])

df_cat.head()


# In[15]:


df_cat.describe()


# In[16]:


# Drop this encoded column for independance assumption to hold
df_cat.drop(columns='EducationField_non-stem',inplace=True)


# One-hot the remaining categorical variables as they have low unique values
# 
# Target variable attrition is mapped
# 
# Yes = 1
# No = 0

# In[17]:


df_cat = pd.get_dummies(df_cat, columns=["Attrition"])


# In[18]:


df_cat.drop(columns = ["Attrition_Yes"], inplace=True)

df_cat.head()


# In[19]:


pd.set_option('display.max_columns', None)


# In[20]:


df_cat.describe(include = "all")


# #Drop the following encoded column for independance assumption to hold
# df_cat.drop(columns=['Gender_Male'],inplace=True)
# 
# df_cat.head()

# Now standardize the numeric variables

# In[21]:


df_noncat.head()


# In[22]:


from sklearn.preprocessing import StandardScaler
import sklearn


# In[23]:


# scales data as z = (x - u) / s

# create a StandardScaler object
scaler_num = StandardScaler()

# fit the wines by calling the fit() function 
noncat_scaled_np = scaler_num.fit_transform(df_noncat)

df_scaled_noncat = pd.DataFrame(noncat_scaled_np, columns= df_noncat.columns)


# In[24]:


df_scaled_noncat.head()


# Now all categorical variables are encoded
# 
# All numeric variables are standardized
# 
# 
# Combine the categorical variables with the non-categorical variables into 1 dataframe

# In[25]:


combined_df = pd.concat([df_cat, df_scaled_noncat], axis=1)


# In[26]:


combined_df.head()


# Renaming Attrition_No to Hired_Yes to further fit the context of the project. Taking liberty to assume that if not fired = hired.

# In[27]:


combined_df = combined_df.rename(columns={'Attrition_No': 'Hired_Yes'})


# In[28]:


combined_df.head()


# Continue your models/algorithms and tuning as needed...

# # Train Model and Calculate Probability

# In[29]:


#Split into input and target dataframes. axis=0=> row, axis=1=>column. 

input_df = combined_df.drop(['Hired_Yes'], axis=1)
target = combined_df['Hired_Yes']

print(input_df.shape,target.shape)


# In[30]:


#distribution of class
target.value_counts()


# In[31]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#Split feature and label sets to train and data sets - 80-20, random_state is desirable for reproducibility, stratify - same proportion as input data
#The stratify means split the data based on target column
#The random_state is to ensure that everyone will have the same answer due to the same random state.
X_train, X_test, y_train, y_test = train_test_split(input_df, target, test_size = 0.2, random_state = 11, stratify = target)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[32]:


#Normalize using MinMaxScaler to constrain values to between 0 and 1.
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range = (0,1))

scaler.fit(X_train)
#only fit the train model
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[33]:


#Create a logistic regression classifier, default c=1

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

#look at the value under the positive class - macro avg is insensitive to imbalanced data, micro result will be affected if there is imbalance data - infleunce by majority
#print(classification_report(y_test, y_pred))

print('Testing accuracy %s' % accuracy_score(y_test, y_pred))


# In[34]:


from sklearn.model_selection import cross_val_predict, cross_val_score 
from sklearn.metrics import accuracy_score, classification_report 
from sklearn.metrics import confusion_matrix 
  

#print_score(logreg, X_train, y_train, X_test, y_test, train = True)          
#print_score(logreg, X_train, y_train, X_test, y_test, train = False)


# In[35]:


#get the sorting indices in descending order (before SMOTE)
sorted_index = np.argsort(-(abs(logreg.coef_)))
print(sorted_index[0][:5])
print('-------------------')
#get the feature_names
feature_names = input_df.columns

#get the names of the important features
print(feature_names[sorted_index[0][:5]])


# In[36]:


logreg.coef_[0][sorted_index[0][:5]]


# In[39]:


get_ipython().system('pip install -U imbalanced-learn')


# In[40]:


#Handling imbalance data - Rerunning above with resampled data - using oversampling. Synthetically generate more data
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state = 11)
X_train_sm, y_train_sm = sm.fit_resample(X_train, y_train)

print(X_train_sm.shape, X_train.shape)
print(y_train.value_counts())
print(y_train_sm.value_counts())


# In[41]:


logreg_sm = LogisticRegression()

clf=logreg_sm.fit(X_train_sm, y_train_sm)
y_pred = clf.predict(X_test)
#look at the value under the positive class - macro avg is insensitive to imbalanced data, micro result will be affected if there is imbalance data - infleunce by majority
#print_score(clf, X_train_sm, y_train_sm, X_test, y_test, train = False)


# In[42]:


print(np.std(X_train_sm, 0)*logreg_sm.coef_)


# In[43]:


print(input_df)


# In[44]:


#get the sorting indices in descending order (After SMOTE)
sorted_index1 = np.argsort(-abs(logreg_sm.coef_))
print(sorted_index1)
print('-------------------')
#get the feature_names
feature_names = input_df.columns
print(feature_names)
print('-------------------')
#get the names of the important features
print(feature_names[sorted_index1[0][:5]])


# In[45]:


#print_score(logreg_sm, X_train_sm, y_train_sm, X_test, y_test, train = False)


# # Predicting Unseen Data (Codes placed into Markdown)
# 

# # For extraction of email
# 
# bucket='tshfyptest/read'
# data_key = 'CV_5_email.csv'
# data_location = 's3://{}/{}'.format(bucket, data_key)
# 
# df_with_email = pd.read_csv(data_location)
# df_unseen = df_with_email.drop(columns=["emails"])
# df_unseen

# df_with_email

# email = df_with_email.iat[0,5]
# print(email)

# cat_cols = ['EducationField']

# 
# df_noncat = df_unseen.drop(columns = ["Gender","EducationField"])
# df_cat = df_unseen.loc[:,cat_cols]

# cleanup_edu = {"EducationField": {"Life Sciences": "stem", 
#                                   "Medical": "stem",
#                                   "Marketing": "non-stem",
#                                   "Technical Degree": "stem",
#                                   "Other": "non-stem",
#                                   "Engineering":"stem",
#                                   "Microbiology":"stem",
#                                   "Public Management": "non-stem",
#                                   "Human Resources": "non-stem"}}

# df_cat.replace(cleanup_edu, inplace=True)
# df_cat = pd.get_dummies(df_cat, columns=["EducationField"])
# print(df_cat)
# #df_cat.drop(columns='EducationField_stem',inplace=True)
# 

# df_cat = pd.get_dummies(df_cat, columns=["Gender"])
# 
# #Drop the following encoded column for independance assupmtion to hold
# 
# df_cat.head()

# from sklearn.preprocessing import StandardScaler
# import sklearn

# df_noncat

# #fit the wines by calling the fit() function 
# noncat_scaled_np = scaler_num.transform(df_noncat)
# noncat_scaled_np
# df_scaled_noncat = pd.DataFrame(noncat_scaled_np, columns= df_noncat.columns)

# #df_cat.insert(1, "EducationField_stem", [0])
# #df_cat.insert(2, "Gender_Female", [0])
# #df_cat.drop(columns="Gender_Male",inplace=True)
# df_cat.drop(columns="EducationField_non-stem",inplace=True)
# 

# df_cat.head()

# input_df.head()

# combined_df = pd.concat([df_cat, df_scaled_noncat], axis=1)
# combined_df

# unseen_df = combined_df.copy()

# unseen_df

# coeff_arr = logreg.coef_
# unseen_np = unseen_df.to_numpy()
# 
# sum_of_attributes = np.multiply(coeff_arr, unseen_np).sum()
# z = -(sum_of_attributes + logreg.intercept_)
# 
# print(z)

# z = -logreg.decision_function(unseen_df)
# print(z)

# import math
# 
# probability = 1 / (1 + math.exp(-z))
# print('Probability of this unseen record joining the company is: ')
# print("{:.5f}".format(probability))

# data = {
#     'Probability': [probability]
# }
# 
# df = pd.DataFrame(data)
# 
# df.to_csv('probability.csv', index=False)

# df.to_csv('s3://tshfyptest/read/probability.csv', index=False)

# new_df = pd.read_csv('s3://tshfyptest/read/probability.csv')

# new_df

# # Feature Importance

# In[46]:


# Get feature importances
feature_importances = np.abs(logreg.coef_[0])  # Absolute values for better visualization


# In[47]:


# Create a DataFrame to display feature importances
feature_importance_df = pd.DataFrame({'Feature': input_df.columns, 'Importance': feature_importances})
feature_importance_df.sort_values(by='Importance', ascending=False, inplace=True)


# In[48]:


# Plot feature importances
#plt.figure(figsize=(10, 6))
#plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
#plt.xlabel('Importance')
#plt.ylabel('Feature')
#plt.title('Feature Importance for Logistic Regression')
#plt.show()


# In[49]:


feature_importance_df.head(10)


# TotalWorkingYearsProbability = (feature_importances[3]/sum(feature_importances)) * probability
# TotalWorkingYearsProbability

# NumCompaniesWorkedProbability = (feature_importances[2]/sum(feature_importances)) * probability
# NumCompaniesWorkedProbability

# EducationFieldProbability = (feature_importances[0]/sum(feature_importances)) * probability
# EducationFieldProbability

# EducationProbability = (feature_importances[1]/sum(feature_importances)) * probability
# EducationProbability

# # Saving to DB (Codes placed into Markdown)

# In[50]:


get_ipython().system('pip install psycopg2-binary')


# In[51]:


get_ipython().system('pip install snowflake-connector-python')


# In[52]:


get_ipython().system('pip install mysql-connector-python')


# In[53]:


get_ipython().system('pip install ipython-sql')


# In[54]:


get_ipython().system('pip install pymysql')


# In[55]:


get_ipython().run_line_magic('reload_ext', 'sql')


# In[56]:


get_ipython().run_line_magic('sql', 'mysql+pymysql://admin:fypproject@database-fypsg.cj6uwc2aysh9.ap-southeast-1.rds.amazonaws.com:3306/tsh_db')


# %%sql
# show tables

# %%sql    
# drop table if exists Probability;
# CREATE TABLE Probability (
#     ID VARCHAR(50),
#     Email VARCHAR(50),
#     Probability DECIMAL(17,16)
# );

# %%sql
# show tables

# %%sql
# insert into Probability values("3", "testemail",probability);

# %%sql 
# select * from Probability;

# In[57]:


get_ipython().system('pip install configparser')


# In[58]:


#Enter the values for you database connection
database = "tsh_db"                # e.g. "pidata"
hostname = "database-fypsg.cj6uwc2aysh9.ap-southeast-1.rds.amazonaws.com"         # e.g.: "mydbinstance.xyz.us-east-1.rds.amazonaws.com"
port = 3306                        # e.g. 3306 
uid = "admin"                   # e.g. "user1"
pwd = "fypproject"                     # e.g. "Password123"


# In[59]:


import mysql.connector


# In[60]:


conn = mysql.connector.connect( host=hostname, user=uid, passwd=pwd, db=database )
cur = conn.cursor()


# cur.execute("CREATE TABLE Probability (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), probability DECIMAL(17,16))")

# %%sql
# drop table Probability

# %%sql
# show tables

# In[61]:


from sqlalchemy import create_engine


# data = {
#     'email': [email],
#     'Overall_Probability': [probability],
#     'TotalWorkingYears': [TotalWorkingYearsProbability],
#     'NumCompaniesWorked': [NumCompaniesWorkedProbability],
#     'EducationField': [EducationFieldProbability],
#     'EducationLevel': [EducationProbability]
# }
# 
# df = pd.DataFrame(data)

# df

# In[62]:


engine = create_engine("mysql+pymysql://admin:fypproject@database-fypsg.cj6uwc2aysh9.ap-southeast-1.rds.amazonaws.com:3306/tsh_db")


# df.to_sql('Probability', con=engine, if_exists='append', index=False)

# %%sql
# show tables
# 

# %%sql 
# select * from Probability

# # Parameters Testing

# # DB Test

# In[63]:


get_ipython().run_cell_magic('sql', '', 'show tables\n')


# In[64]:


get_ipython().run_cell_magic('sql', '', 'select * from ML_Fields\n')


# In[65]:


db_connect = engine.connect()


# In[66]:


df_from_db = pd.read_sql('SELECT * FROM ML_Fields order by timestamp_column_name desc', con=engine)


# In[67]:


#Cleaning

df_from_db['EducationField_stem'] = df_from_db['Education_field'].astype(str)
df_from_db['Education'] = df_from_db['Education_level'].astype(str)
df_from_db['NumCompaniesWorked'] = df_from_db['Num_companies_worked'].astype(float)
df_from_db['TotalWorkingYears'] = df_from_db['Total_working_years'].astype(float)
df_from_db['Email'] = df_from_db['Email'].astype(str)


# In[68]:


df_from_db.info()


# In[69]:

df_from_db = df_from_db.drop(columns = ["timestamp_column_name","Total_working_years","Num_companies_worked","Education_level","Education_field"])


# In[70]:


df_from_db.info()


# In[71]:


email = df_from_db.iat[0,0]
print(email)


# In[72]:


# Create an array of all categorical datatypes
cat_cols_db = ['EducationField_stem','Email']
cat_cols_db


# In[73]:


df_noncat_db = df_from_db.drop(columns=cat_cols_db)
df_noncat_db.columns


# In[74]:


df_cat_db = df_from_db.loc[:,cat_cols_db]
df_cat_db.columns


# In[75]:
df_cat_db_new = df_cat_db.copy()


stem_list = ["Science","Systems", "Business", "Engineering", "Engineer","Machining"]


for i in df_cat_db['EducationField_stem']:
    string = i
    # using lambda functions to check if string contains any element from list
    contains_word = lambda s, l: any(map(lambda x: x in s, l))
    # printing the result
    if contains_word(string, stem_list):
        df_cat_db_new['EducationField_stem'].replace(i, True, inplace=True)
    else:
        df_cat_db_new['EducationField_stem'].replace(i, False, inplace=True)


# 1 'Below College' 2 'College' 3 'Bachelor' 4 'Master' 5 'Doctor'
df_noncat_db_new = df_noncat_db.copy()
# In[76]:


Bachelor = "Bachelor"
College = "College"
Master = "Master"
Doctor = "Doctor"

for i in df_noncat_db['Education']:
    if College in i:
        df_noncat_db_new['Education'].replace(i, 2, inplace=True)
    elif Bachelor in i:
        df_noncat_db_new['Education'].replace(i, 3, inplace=True)
    elif Master in i:
        df_noncat_db_new['Education'].replace(i, 4, inplace=True)
    elif Doctor in i:
        df_noncat_db_new['Education'].replace(i, 5, inplace=True)
    else:
        df_noncat_db_new['Education'].replace(i, 1, inplace=True)
    


# In[77]:


df_noncat_db


# In[78]:


# fit the wines by calling the fit() function 
noncat_scaled_np_db = scaler_num.transform(df_noncat_db_new)
noncat_scaled_np_db
df_scaled_noncat_db = pd.DataFrame(noncat_scaled_np_db, columns= df_noncat_db.columns)


# In[79]:


df_scaled_noncat_db


# In[80]:


combined_df_db = pd.concat([df_cat_db_new, df_scaled_noncat_db], axis=1)


# In[81]:


unseen_df_db = combined_df_db.drop(columns = ['Email'])


# In[82]:


z = -logreg.decision_function(unseen_df_db.iloc[0:1])
print(z)


# In[83]:


import math
probability = 1 / (1 + math.exp(-z))
print('Probability of this unseen record joining the company is: ')
print("{:.5f}".format(probability))


# In[84]:


TotalWorkingYearsProbability = (feature_importances[3]/sum(feature_importances)) * probability
TotalWorkingYearsProbability


# In[85]:


NumCompaniesWorkedProbability = (feature_importances[2]/sum(feature_importances)) * probability
NumCompaniesWorkedProbability


# In[86]:


EducationFieldProbability = (feature_importances[0]/sum(feature_importances)) * probability
EducationFieldProbability


# In[87]:


EducationProbability = (feature_importances[1]/sum(feature_importances)) * probability
EducationProbability


# In[88]:


get_ipython().run_cell_magic('sql', '', 'show tables\n')


# In[89]:


data = {
    'Email': [email],
    'Overall_probability': [probability],
    'Total_working_years': [TotalWorkingYearsProbability],
    'Num_companies_worked': [NumCompaniesWorkedProbability],
    'Education_field': [EducationFieldProbability],
    'Education_level': [EducationProbability]
}

df = pd.DataFrame(data)


# In[90]:


df


# In[91]:


df.to_sql('Probability', con=engine, if_exists='append', index=False)


# In[92]:


get_ipython().run_cell_magic('sql', '', 'select * from Probability\n')


# In[93]:


get_ipython().run_cell_magic('sql', '', 'select * from ML_Fields\n')


# In[ ]:




