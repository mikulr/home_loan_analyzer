# Machine Learning Loan Analysis 



For this project I analyzed four years of historical consumer loan information to create a machine learning model to predict loan approval based on a combination of nine factors. The original dataset was ~57M records, after cleaning and narrowing the scope of our modeling I had a data set of +14M records.  In order to effectivly utilize resources/time I randomly sampled 500,000 from the main dataset in order to create a supervised learning model in Scikit Learn. After model choosing and refining, the best four models were tested againt the entire ~14M record dataset (minus the 500,000 used for initial train/testing.) After choosing the model, it was deployed with a flask server hosted on Heroku.  From the bootstrap based webpage, I collect user data, send it to the flask server, run it through the model and return a prediction of success or failure for loan approval.  On the results page you will also find visualizations of the loan applicants information by state.

Originally a group project, I have forked the original repository and revised/updated all work. (As a group project, I was initially responsible for ETL work, model creation as well as creating simple overviews by state.)

Initial CSV files downloaded from the [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/data-research/hmda/historic-data/?geo=nationwide&records=all-records&field_descriptions=labels)

- [2017](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2017_nationwide_all-records_codes.zip)
- [2016](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2016_nationwide_all-records_codes.zip)
- [2015](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2015_nationwide_all-records_codes.zip)
- [2014](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2014_nationwide_all-records_codes.zip)