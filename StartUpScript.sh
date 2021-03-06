#!/bin/bash

printf "\n\n----------------- installing libraries -----------------\n\n"

pip install kaggle
pip install pandas
pip install numpy
pip install matplotlib

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

if [ ! -d "./Data" ]
then
  printf "\nGetting data from kaggle...\n"
  kaggle datasets download -d camnugent/sandp500/all_stocks_5yr.csv
  mkdir ./Data
  unzip -d ./Data sandp500.zip
  printf "\nData folder set up\n"
else
  printf "\nData is already downloaded, skipping step..."
fi


printf "\n\n---------------- Running Script ----------------\n\n"

python analysis_of_stock_data.py

printf "\n\n---------------- Cleaning up directory ----------------\n\n"

if [ -f ./sandp500.zip ]
then
  echo "Removing sandp500.zip..."
  rm ./sandp500.zip
fi

while getopts ":r" opt; do
  case $opt in
    r)
      echo "Removing data files..."
      rm -r ./Data
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

printf "\nCleaning done...\n\n"
