#%%
from scrape_repo import *
from scrape_user import *
from utils import *
#import datapane as dp 
import pandas as pd 
from tqdm import tqdm 
#from folium import plugins
#import geopandas
#from geopy.geocoders import Nominatim
#import folium

keyword_list = ["HTML",
                "CSS",
                "javascript",
                "Python",
                "Cyber security"]
filename='GithubProfileDataScrap_'+'_'.join(keyword_list)
all_users=pd.DataFrame()
stop_pages = [10,20,30,40,50,60,70,80,90,100]
start_pages = [1,11,21,31,41,51,61,71,81,91]

for keyword in keyword_list:
    try:
        for i in range(len(stop_pages)):
            contributors = get_top_contributors(keyword, start_page=start_pages[i], stop_page=stop_pages[i], max_n_top_contributors=1000)
            # Remove duplicates
            contributors = contributors[~contributors.duplicated()]
            users = get_top_users(keyword, start_page=start_pages[i], stop_page=stop_pages[i])
            all_users = pd.concat([all_users,contributors, users])
            all_users.to_csv(keyword+'_'+start_pages[i]+'_'+stop_pages[i]+'.csv')
            print(i,keyword)
    except:
        continue

# Remove duplicated users
all_users = all_users[~all_users.duplicated()]

all_users['real_url'] = all_users.login.apply(lambda login: 'https://github.com/' + login)

all_users.to_csv(filename+'.csv')

# %%
