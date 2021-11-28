{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "97213025",
   "metadata": {},
   "source": [
    "# Pandas Input/output\n",
    "\n",
    "Can read: `.csv`, `.json`, `.xlsx`, `.parquet`, `.db`, `.hdf`, ...\n",
    "\n",
    "\n",
    "https://pandas.pydata.org/pandas-docs/stable/reference/io.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37b7567a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97c8ba03",
   "metadata": {},
   "source": [
    "### Our Data\n",
    "\n",
    "- `attacks.csv` from Kaggle\n",
    "- `github_pulls.json` from GitHub API\n",
    "- `2021_Accidentalidad.xlsx` from Datos Abiertos Ayuntamiento de Madrid\n",
    "- `test.parquet` from Kaggle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02d1ad7b",
   "metadata": {},
   "source": [
    "__.CSV Files__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c307aea0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Raw \"Comma\"-Separated Values file (a.k.a.: CSV file)\n",
    "\n",
    "with open('./datasets/attacks.csv') as f:\n",
    "    lines = f.readlines()\n",
    "lines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86aca4e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import .CSV \n",
    "# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#\n",
    "\n",
    "df_csv = pd.read_csv('./datasets/attacks.csv')\n",
    "df_csv.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "282b3f4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's explore the dataset\n",
    "\n",
    "print(df_csv.shape)\n",
    "print(df_csv.info())\n",
    "#df_csv_short = df_csv[['Date', 'Type', 'Country', 'Injury']]\n",
    "#df_csv_short = df_csv_short.dropna(subset=['Country'])\n",
    "#print(df_csv_short.shape)\n",
    "#print(df_csv_short.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d4f0abe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a new .csv file\n",
    "\n",
    "df_csv_short.to_csv('./datasets/shark_attacks_short.csv', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24d165b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_csv_s = pd.read_csv('./datasets/shark_attacks_short.csv')\n",
    "\n",
    "df_csv_s.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0d65d5b",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12be646d",
   "metadata": {},
   "source": [
    "__.JSON Files__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bf608ab",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Raw JavaScript Object Notation file (a.k.a.: JSON file)\n",
    "\n",
    "import json\n",
    "\n",
    "with open('./datasets/github_pulls.json', encoding=\"utf8\") as f:\n",
    "    json_file = json.load(f)\n",
    "\n",
    "json_file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1cd98df2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import .JSON \n",
    "# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.json.read_json.html#pandas.io.json.read_json\n",
    "\n",
    "df_json = pd.read_json('./datasets/github_pulls.json')\n",
    "df_json.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f345c90e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's explore the dataset\n",
    "\n",
    "print(df_json.shape)\n",
    "print(df_json.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8a49524",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dict flatten\n",
    "\n",
    "df_json_new = list(df_json['_links'])\n",
    "df_json_new = pd.DataFrame(df_json_new)\n",
    "df_json_new.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb08ab58",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a new .JSON file\n",
    "\n",
    "df_json_new.to_json('./datasets/github_pulls_new.json')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b0862fe",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae360767",
   "metadata": {},
   "source": [
    "__.XLSX Files__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c2b3877",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Additional libraries for Excel files\n",
    "\n",
    "#!conda install -y xlrd\n",
    "#!conda install -y openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5222d79a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import .XLSX \n",
    "# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html\n",
    "\n",
    "df_excel = pd.read_excel('./datasets/2021_Accidentalidad.xlsx', sheet_name='Accidentes_2021')\n",
    "df_excel.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6888056f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's explore the dataset\n",
    "\n",
    "print(df_excel.shape)\n",
    "print(df_excel.info())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "630bc08e",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04949dad",
   "metadata": {},
   "source": [
    "__.PARQUET Files__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ac5ee75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Additional library for Parquet files\n",
    "\n",
    "#!conda install -c conda-forge pyarrow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2a51ac5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import .PARQUET (column-oriented data storage format with schema)\n",
    "# https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html\n",
    "\n",
    "df_parquet = pd.read_parquet('./datasets/test.parquet')\n",
    "df_parquet.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5abead1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's explore the dataset (https://www.kaggle.com/dschettler8845/recsys-2020-ecommerce-dataset)\n",
    "\n",
    "print(df_parquet.shape)\n",
    "print(df_parquet.info())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a40a4fdc",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0e0e834",
   "metadata": {},
   "source": [
    "__SQL Files...in the next episode...__"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:.conda-ironhack]",
   "language": "python",
   "name": "conda-env-.conda-ironhack-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}