#!/usr/bin/env python
# coding: utf-8

# ## Spotify Data Extraction for Visualization

# In[1]:


# Import Libraries
import os
import numpy as np
import pandas as pd
import dotenv
import tekore as tk
import time
from datetime import datetime, timedelta


# In[3]:


# import authentification file
import authentification


# In[4]:


#import user token
from authentification import spotify


# In[5]:


def recent_listens(numofsongs):
    '''
    function to list most recently played songs
    numofsongs: number of songs to list, limit=50
    '''
    print('Your {} most recently played songs!'.format(numofsongs))
    for i in spotify.playback_recently_played(limit=numofsongs).items:
        print('{}, {}'.format(i.track.name,i.track.artists[0].name))
    


# In[6]:


recent_listens(3)


# In[7]:


def top_tracks(time_period='medium_term',limit=10,offset=0):
    ''' 
    Parameters
    time_period (str) – Over what time frame are the affinities computed. Valid-values: short_term (1 month) , medium_term (6 months), long_term (years)

    limit (int) – the number of items to return (1..50)

    offset (int) – the index of the first item to return
    '''
    if time_period=='medium_term':
        period='6 months'
    elif time_period=='short_term':
        period='month'
    elif time_period=='long_term':
        period='few years'
    print('Your top {} tracks over the past {} are:'.format(limit,period))
    for i in spotify.current_user_top_tracks(time_range=time_period,limit=limit).items:
        print('{}, {}'.format(i.name,i.artists[0].name))


# In[8]:


top_tracks('long_term',limit=10)


# In[9]:


def top_artists(time_period='medium_term',limit=10,offset=0):
    ''' 
    Parameters
    time_period (str) – Over what time frame are the affinities computed. Valid-values: short_term (1 month) , medium_term (6 months), long_term (years)

    limit (int) – the number of items to return (1..50)

    offset (int) – the index of the first item to return
    '''
    if time_period=='medium_term':
        period='6 months'
    elif time_period=='short_term':
        period='month'
    elif time_period=='long_term':
        period='few years'
    print('Your top {} tracks over the past {} are:'.format(limit,period))
    for i in spotify.current_user_top_artists(time_range=time_period,limit=limit).items:
        print('{}'.format(i.name))


# In[10]:


top_artists()


# In[15]:


def top_genres(top=True,limit=10):
    '''
    Top genres assosiated with the artists of the last saved 1000 songs in a spotify users library. Tracks are not associated with genres but artists are. This function takes the artists' genres (primary and featured) and returns the top most genres or bottom most.
    Options:
        top: if true returns top genres, if false returns bottom
        limit: number of genres to return
    
    '''
    ids=[]
    for i in range(int(1000/50)):
        for j in spotify.saved_tracks(limit=50,offset=i*50).items:
            for h in j.track.artists:
                try:
                    ids.append(spotify.artist(h.id).genres)
                except:
                    pass
    genres=[]
    for j in ids:
        for h in j:
            genres.append(h)
    if top==True:
        return pd.Series(genres).value_counts(ascending=False)[0:limit]
    else:
        return pd.Series(genres).value_counts(ascending=True)[0:limit]


# In[16]:


top_genres(top=False)

