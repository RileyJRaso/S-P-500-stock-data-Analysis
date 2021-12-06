#!/bin/bash

printf "\n\n----------------- installing libraries -----------------\n\n"

pip install kaggle

printf "\n\n----------------- Setting up environment -----------------\n\n"

#setting up global variables
input="SignInInfo.txt"
while IFS= read -r line
do

  if [[ "${line:0:1}" == "U" ]]
  then
    echo "Username is ${line:2} "
    export KAGGLE_USERNAME="${line:2}"
  fi
  if [[ "${line:0:1}" == "K" ]]
  then
    echo "Key is ${line:2} "
    export KAGGLE_KEY="${line:2}"
  fi
done < "$input"


printf "\n\n---------------- Getting Data from kaggle ----------------\n\n"

kaggle datasets download -d camnugent/sandp500/all_stocks_5yr.csv
mk dir ./Data
unzip -d ./Data sandp500.zip

printf "\n\n---------------- Cleaning up directory ----------------\n\n"

echo "Removing sandp500.zip..."
rm ./sandp500.zip
