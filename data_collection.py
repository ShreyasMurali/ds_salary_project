import glassdoor_scraper as gs
import pandas as pd

path = "D:/projects/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',500, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)