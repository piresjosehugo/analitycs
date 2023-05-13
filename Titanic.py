#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from pandas import Series, DataFrame


# In[6]:


titanic_df = pd.read_csv('train.csv')


# In[7]:


titanic_df.head()


# In[8]:


titanic_df.info()


# In[9]:


#1.) Who were the passengers on the Titanic? (Ages, Gender,Class,...etc)
#2.) What deck were the passengers on and how does that relate to their class?
#3.)Where did the passengers come from?
#4.)Who was alone and who was with family?
#5.)What factors helped someone survive the sinking?

#So let's stark with the first question: Who were the passenges on the titanic?


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


sns.catplot(x='Sex', kind='count', data=titanic_df)


# In[23]:


# create a categorical plot of Sex and Pclass
sns.catplot(x='Sex', data=titanic_df, hue='Pclass', kind='count')


# In[24]:


sns.catplot(x='Pclass', data=titanic_df, hue='Sex', kind='count')


# In[27]:


def male_female_child(passenger):
    age,sex = passenger
    
    if age < 16:
       return 'child'
    else:
        return sex


# In[28]:


titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)


# In[29]:


titanic_df[0:10]


# In[30]:


sns.catplot(x='Pclass', data=titanic_df, hue='person', kind='count')


# In[32]:


titanic_df['Age'].hist(bins=70)


# In[33]:


titanic_df['Age'].mean()


# In[34]:


titanic_df['person'].value_counts()


# In[36]:


fig = sns.FacetGrid(titanic_df,hue='Sex',aspect=4)
fig.map(sns.kdeplot,'Age',fill=True)

oldest = titanic_df['Age'].max()

fig.set(xlim=(0,oldest))

fig.add_legend()


# In[37]:


fig = sns.FacetGrid(titanic_df,hue='person',aspect=4)
fig.map(sns.kdeplot,'Age',fill=True)

oldest = titanic_df['Age'].max()

fig.set(xlim=(0,oldest))

fig.add_legend()


# In[38]:


fig = sns.FacetGrid(titanic_df,hue='Pclass',aspect=4)
fig.map(sns.kdeplot,'Age',fill=True)

oldest = titanic_df['Age'].max()

fig.set(xlim=(0,oldest))

fig.add_legend()


# In[39]:


#2.) What deck were the passengers on and how does that relate to their class?


# In[40]:


deck = titanic_df['Cabin'].dropna()


# In[41]:


deck.head()


# In[59]:


levels = []

for level in deck:
    levels.append(level[0])
cabin_df = DataFrame(levels)    


cabin_df.columns = ['Cabin']


sns.catplot(x='Cabin', data=cabin_df, kind='count', palette="Set2")


# In[62]:


cabin_df = cabin_df[cabin_df.Cabin != 'T']

sns.catplot(x='Cabin', data=cabin_df, kind='count', palette="Dark2")


# In[63]:


titanic_df.head()


# In[74]:


#3.)Where did the passengers come from?

sns.catplot(x='embarked', data=titanic_df, hue='pclass', kind='count')


# In[75]:


#4.)Who was alone and who was with family?
titanic_df.head()


# In[79]:


titanic_df['Alone'] = titanic_df.sibsp + titanic_df.parch


# In[80]:


titanic_df['Alone'].loc[titanic_df['Alone'] >0] = 'With Family'

titanic_df['Alone'].loc[titanic_df['Alone'] ==0] = 'Alone'


# In[81]:


titanic_df.head()


# In[82]:


sns.catplot(x='Alone', data=titanic_df, kind='count', palette="Blues")


# In[83]:


#5.)What factors helped someone survive the sinking?

titanic_df['Survivor'] = titanic_df.survived.map({0:'no',1:'yes'})

sns.catplot(x='Survivor', data=titanic_df, kind='count', palette="Set1")


# In[105]:


# Create a pointplot to compare pclass and survived

sns.pointplot(x='pclass', y='survived', data=titanic_df)


# In[113]:


import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Define a function to map age and sex to person
def get_person(passenger):
    age, sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex

# Create a person column in the DataFrame
titanic_df['person'] = titanic_df[['age', 'sex']].apply(get_person, axis=1)

# Create a pointplot to compare pclass and survived, with hue by person
sns.pointplot(x='pclass', y='survived', hue='person', data=titanic_df)


# In[115]:


sns.lmplot(x='age', y='survived', data=titanic_df)


# In[116]:


sns.lmplot(x='age', y='survived',hue='pclass', data=titanic_df,palette='winter')


# In[117]:


generations = [10,20,40,60,80]

sns.lmplot(x='age',y='survived',hue='pclass',data=titanic_df,palette='winter',x_bins=generations)


# In[119]:


sns.lmplot(x='age', y='survived',hue='sex', data=titanic_df,palette='winter',x_bins=generations)


# In[125]:


sns.barplot(x='deck', y='survived', data=titanic_df)


# In[128]:


# Create a new column 'family_member' indicating whether a passenger had a family member on board
titanic_df['family_member'] = (titanic_df['sibsp'] + titanic_df['parch'] > 0).astype(int)

# Calculate the survival rate for passengers with and without family members
survival_rate_by_family_member = titanic_df.groupby('family_member')['survived'].mean()

# Visualize the results
sns.barplot(x='family_member', y='survived', data=titanic_df)


# In[ ]:




