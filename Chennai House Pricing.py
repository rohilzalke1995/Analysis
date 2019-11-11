
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


os.chdir('C:\\Users\\rohil\\Desktop\\Machine Learning\\Data')


# In[4]:


df = pd.read_csv('chennai_house_price_prediction.csv')


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


df.describe(include = 'all')


# In[9]:


df.columns


# In[10]:


df.isnull().sum()


# In[11]:


df['N_BEDROOM'].unique()


# In[12]:


df['N_BEDROOM'] = df['N_BEDROOM'].fillna(df['N_BEDROOM'].mode()[0])


# In[13]:


df['N_BEDROOM'].unique()


# In[14]:


df['N_BEDROOM'].value_counts().plot(kind = 'bar')


# In[15]:


df['N_BATHROOM'].value_counts().plot(kind = 'bar')


# In[16]:


df['N_BATHROOM'].mode()


# In[17]:


df['N_BEDROOM'].unique()


# In[18]:


df['N_BATHROOM'].isnull().sum()


# In[19]:


df.loc[df['N_BATHROOM'].isnull()==True]


# In[20]:


for i in range(0, len(df)):
    if pd.isnull(df['N_BATHROOM'][i]) == True:
        if (df['N_BEDROOM'][i]==1.0):
            df['N_BATHROOM'][i]=1.0
        else:
            df['N_BATHROOM'][i]=2.0


# In[21]:


df['N_BATHROOM'].isnull().sum()


# In[22]:


df['N_BATHROOM'].unique()


# In[23]:


df.isnull().sum()


# In[24]:


def fill_na(x):
    return (x['QS_ROOMS'] + x['QS_BATHROOM'] + x['QS_ROOMS'])/3

df['QS_OVERALL'] = df.apply(lambda x: fill_na(x) if pd.isnull(x['QS_OVERALL']) else x['QS_OVERALL'], axis = 1)


# In[25]:


df.isnull().sum()


# In[26]:


df.head()


# In[27]:


df.columns


# In[28]:


t = ['PRT_ID', 'AREA', 'INT_SQFT', 'DIST_MAINROAD', 'N_BEDROOM',
       'N_BATHROOM', 'N_ROOM', 'SALE_COND', 'PARK_FACIL', 'BUILDTYPE',
       'UTILITY_AVAIL', 'STREET', 'MZZONE', 'QS_ROOMS', 'QS_BATHROOM',
       'QS_BEDROOM', 'QS_OVERALL', 'COMMIS', 'SALES_PRICE']
for i in t:
    print("******************Unique values of " + i )
    print("*****************plot of " + i)
   


# In[29]:


a = ['AREA', 'N_BEDROOM', 'N_BATHROOM', 'N_ROOM', 'SALE_COND', 'PARK_FACIL', 'UTILITY_AVAIL', 'STREET', 'MZZONE']
for i in a:
    print("**********************Value counts of "+ i)
    print(df[i].value_counts()/len(df[i])*100)


# In[30]:


a = ['AREA', 'N_BEDROOM', 'N_BATHROOM', 'N_ROOM', 'SALE_COND', 'PARK_FACIL', 'UTILITY_AVAIL', 'STREET', 'MZZONE']
for i in a:
    print("***************plot of " + i + "****************")
    df[i].value_counts().plot(kind = 'bar')
    plt.show()


# In[31]:


df['PARK_FACIL'] = df['PARK_FACIL'].replace('Noo','No')
df['PARK_FACIL'].unique()


# In[32]:


df['UTILITY_AVAIL'] = df['UTILITY_AVAIL'].replace({'All Pub':'AllPub'})
df['UTILITY_AVAIL'].unique()


# In[33]:


df['STREET'] = df['STREET'].replace({'Pavd':'Paved', 'NoAccess':'No Access'})


# In[34]:


df['STREET'].unique()


# In[35]:


df['SALE_COND'] = df['SALE_COND'].replace({'Ab Normal':'AbNormal','AB Normal':'AbNormal', 'Partial1':'partial', 
                                           'PartiaL1':'partial', 'Adj Land':'AdjLand', 'Partial':'partial'})
df['SALE_COND'] = df['SALE_COND'].replace('PartiaL1', 'Partial')
df['SALE_COND'] = df['SALE_COND'].replace('Partial1', 'Partial')


# In[36]:


df['SALE_COND'].unique()


# In[37]:


df['AREA'].unique()
df['AREA'] = df['AREA'].replace({'TNagar':'T Nagar', 'Chrompt':'Chrompet', 'Chrmpet':'Chrompet', 'Karapakam':'Karapakkam',
                                'Chormpet':'Chrompet', 'Ana Nagar':'Anna Nagar', 'Adyr':'Adyar', 'Velchery':'Velachery',
                                'Ann Nagar':'Anna Nagar', 'KKNagar':'KK Nagar'})


# In[38]:


df['SALE_COND'].value_counts().plot(kind = 'bar')


# In[39]:


df.columns


# In[40]:


#plt.scatter(x = 'INT_SQFT', y = 'SALES_PRICE', data = df)
df.plot.scatter('INT_SQFT', 'SALES_PRICE')


# In[41]:


df['BUILDTYPE'] = df['BUILDTYPE'].replace('Other', 'Others')
df['BUILDTYPE'] = df['BUILDTYPE'].replace('Comercial', 'Commercial')


# In[42]:


fig, ax = plt.subplots()
color = {'Commercial':'blue', 'House':'green', 'Others':'red'}
ax.scatter(df['INT_SQFT'],df['SALES_PRICE'],  c = df['BUILDTYPE'].apply(lambda x:color[x]))


# In[43]:


df['BUILDTYPE'].unique()


# In[77]:


plt.hist('SALES_PRICE', data = df, bins = 50)
plt.show()


# In[48]:


ax = plt.figure().add_subplot(111)
bx = ax.boxplot([df['QS_ROOMS'], df['QS_BATHROOM'], df['QS_BEDROOM'], df['QS_OVERALL']])


# In[49]:


df.columns


# In[57]:


df.pivot_table(values = 'SALES_PRICE', index = 'N_BEDROOM', columns = 'N_BATHROOM', aggfunc = 'median')


# In[59]:


df.pivot_table(values = 'SALES_PRICE', index = 'UTILITY_AVAIL', columns = 'N_BATHROOM', aggfunc = 'median')


# In[61]:


df.groupby('BUILDTYPE').SALES_PRICE.median()


# In[62]:


df.groupby('STREET').SALES_PRICE.median()


# In[70]:


df_new = df.loc[(df['BUILDTYPE']=='Commercial') & (df['AREA'] == 'Anna Nagar')]


# In[73]:


df_new['SALES_PRICE'].plot.hist(bins = 50)


# In[76]:


df.groupby(['BUILDTYPE', 'PARK_FACIL']).SALES_PRICE.median()
df.groupby(['BUILDTYPE', 'PARK_FACIL']).SALES_PRICE.median().plot(kind = 'bar')


# In[79]:


df.groupby('AREA').SALES_PRICE.median()


# In[81]:


df.groupby(['AREA', 'UTILITY_AVAIL']).SALES_PRICE.median().plot(kind = 'bar')


# In[92]:


df.pivot_table(values = 'SALES_PRICE', index = 'AREA', aggfunc = 'median') #columns = 'SALE_COND')


# In[83]:


plt.scatter(x = 'DIST_MAINROAD', y = 'SALES_PRICE', data = df)

