# Data Science Job Salary Prediction

This repository contains a personal data science project that aims to predict data science job salaries using data scraped from Glassdoor. The project involves various stages, including data collection, data cleaning, exploratory data analysis (EDA), and ultimately building a predictive model.

## Project Overview

The goal of this project is to create a machine learning model that can accurately predict salaries for data science jobs based on features such as job title, location, company size, and more. By leveraging data collected from Glassdoor, we aim to provide valuable insights to both job seekers and employers in the data science field.

## Files

The repository currently includes the following files:

1. `data-collection.py`: This Python script is responsible for scraping job-related data from Glassdoor. The data collected is stored in `glassdoor_jobs.csv`.

2. `datacleaning.py`: This Python script focuses on cleaning and preprocessing the scraped data from `glassdoor_jobs.csv`. The cleaned data is saved as `salary_data_cleaned.csv`.

3. `eda.ipynb`: This Jupyter Notebook contains the Exploratory Data Analysis (EDA) phase of the project. It explores the data, visualizes distributions, and identifies patterns or correlations that could be helpful in building the prediction model.

4. `glassdoor_scraper.py`: This Python script contains the necessary functions to scrape data from Glassdoor's website. It is used in `data-collection.py`.

5. `salary_data_cleaned.csv`: This CSV file contains the cleaned data after going through the data cleaning process.



### resources

https://github.com/arapfaik/scraping-glassdoor-selenium
