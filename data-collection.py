# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 2023

@author: Cyril
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "/Users/cyrilkhoneisser/Documents/MyStuff/DS-projects/ds_salary_pred/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)