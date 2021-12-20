# S-P-500-stock-data-Analysis

a python script for getting data from kaggle and display to user in a readable way through the use of tables and graphs. the bash script sets up all the libraries used by the python script, downloads the data from kaggle (if needed, will check for data folder if already downloaded), and if the -r flag is given will remove the data after the analysis is done.

the python script will ask the user for the stock symbol, the date they want to start looking at data for, and the date they want to stop the collection on. it will than read in data from a csv file, and go through the data analysis process of: cleaning the data, manipulating the data, and finally showing the data in a graph to the user

the data set used can be found here: https://www.kaggle.com/camnugent/sandp500

the anaysis tried to answer the following question:
- how did stock X do from this date, to this date? this anaysis is important is it allows the user to define how long of a timeline they want to look at a stock for, this is beneficial as longer timelines might give the user a better understanding of the trend of the company, is this company gaining value? lossing value? gaining exponentially? or slowing it's growth? and shorter timelines is valueable for high frequency traders and technical analysis to try and prodict if the stock will gain or loss value in the next few days/hours. 

# Installation

in order to get the scripts run: git clone https://github.com/RileyJRaso/S-P-500-stock-data-Analysis.git

important: all other libraries are installed with start up script, make sure you run the script in order to run the python code

git clone 

# Steps to run script

## Setting up environement

in order for the script to work we need to set up our kaggle access (in order for the script to download the files needed). first we need to go to the kaggle site and set up an account, once that is down we need to set up a API key which will save a file on our machine with a key.

once this is done we create a **SignInInfo.txt** file in the same folder that our script is in. the **SignInInfo.txt** file will contain two line, one starting with U: followed by your username, and the second line starting with K: followed by the key provided by kaggle. see example below for file look:

```text

U:{Unsername of kaggle account no space}
K:{Key provided by kaggle pasted from file, no space}

```

example:

```text

U:FakeName
K:346FakeKey342

```

## Running the script

once this file is made run the script by running the attached bash script (in the folder with the script):

```bash
./StartUpScript.sh

```

if you want to remove the data files from your computer after the analysis run the script with the r flag like below:

```bash
./StartUpScript.sh -r

```

this flag will tell the script to rm all the csv files that are downloaded from kaggle

# Future plans

- add more user input validation so the script doesn't break when someone enters something wrong
- try and do some more exploratory data analysis to see what stocks tend to rise/fall together
- try and do some more exploratory data analysis to see what stocks perform opposite to each other for hedging
