#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd

#open csv with pandas
df = pd.read_csv('/Users/edwardkohn/Desktop/Homeworks/Python/election_data.csv')
df.head()


# In[34]:


# Total Votes Casted
total_votes_casted = df.County.count()



# In[42]:


#List of candidates
list_of_candidates = df['Candidate'].unique()



# In[36]:


#used to get the number of votes per candidate
khan_votes = df.loc[df.Candidate == 'Khan', 'Candidate'].count()
correy_votes = df.loc[df.Candidate == 'Correy', 'Candidate'].count()
li_votes = df.loc[df.Candidate == 'Li', 'Candidate'].count()
tooley_votes =df.loc[df.Candidate == "O'Tooley", "Candidate"].count()

#divided the votes for each candidate by the total votes to get percentages
khan_percentage = round((khan_votes/total_votes_casted) * 100,2)
correy_percentage = round((correy_votes/total_votes_casted) * 100,2)
li_percentage = round((li_votes/total_votes_casted) * 100,2)
tooley_percentage = round((tooley_votes/total_votes_casted) * 100,2)


# In[40]:


print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes_casted}')
print(f'Khan: {khan_percentage}% ({khan_votes })')
print(f'Correy: {correy_percentage}% ({correy_votes})')
print(f'Li: {li_percentage}% ({li_votes})')
print("O'Tooley: " + str(tooley_percentage) +"%"+"("+ str(tooley_votes)+")")
print('----------------------------')
print('Winner: Khan')
print('----------------------------')


# In[43]:


n1 = 'Election Results'
n2 = '---------------------------'
n3 = f'Total Votes: {total_votes_casted}'
n4 = f'Khan: {khan_percentage}% ({khan_votes })'
n5 = f'Correy: {correy_percentage}% ({correy_votes})'
n6 = f'Li: {li_percentage}% ({li_votes})'
n7 = "O'Tooley: " + str(tooley_percentage) +"%"+"("+ str(tooley_votes)+")"
n8 = '----------------------------'
n9 = 'Winner: Khan'
n10 ='----------------------------'


pyp = {'str': [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]}
      
output = pd.DataFrame(pyp)

output.to_csv('Py_poll.txt',header=False,index=False)

