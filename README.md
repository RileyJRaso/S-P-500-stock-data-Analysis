# S-P-500-stock-data-Analysis

a python script for getting data from kaggle and display to user in a readable way through the use of tables and graphs. 

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
