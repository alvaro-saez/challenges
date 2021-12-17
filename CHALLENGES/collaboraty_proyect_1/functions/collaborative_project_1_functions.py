import pandas as pd
import requests
import bs4
import numpy as np
import re
import lxml

def html_get(url):
    r = requests.get(url)
    if r.status_code < 300:
        print('request was successful')
        return r.content
    elif r.status_code >= 400 and r.status_code < 500:
        print('request failed because the resource either does not exist or is forbidden')
    else:
        print('request failed because the response server encountered an error')

#url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
#output_html_get = html_get(url)
#output_html_get

def html_parsing(output_html_get, parser, html_element, css_element, css_element_value, position):
    soup = bs4.BeautifulSoup(output_html_get, parser).find_all(html_element,{css_element:css_element_value})[position]
    return soup

#parser = "html.parser"
#response = output_html_get
#html_element = "table"
#css_element = "class"
#css_element_value = "wikitable sortable"
#position = 0
#output_html_parsing = html_parsing(response, parser, html_element, css_element, css_element_value, position)

def name_columns(output_html_parsing):
    name_columns_html_find = output_html_parsing.find_all("tbody")[0].find_all("th")[0:7]
    name_columns_list = [re.sub("\[a\]|\d|\[|\]","",i.text.strip()) for i in name_columns_html_find]
    return name_columns_list

#output_name_columns = name_columns(output_html_parsing)
#output_name_columns

def raws_value(output_html_parsing):
    raws_value = output_html_parsing.find_all("tbody")[0].find_all("tr")[1:]
    raws_value_list = [i.text.replace("\n\n",",").strip() for i in raws_value]
    raws_value_list_array = [i.split(",")[:7] for i in raws_value_list]
    return raws_value_list_array

#output_raw_values = raws_value(output_html_parsing)
#output_raw_values

def data_frame_table(output_raw_values,output_name_columns):
    df_table = pd.DataFrame(output_raw_values,columns=output_name_columns)
    return df_table

#df_table_final = data_frame_table(output_raw_values)
#df_table_final

def table_to_csv(df_table_final):
    csv_table_exported = df_table_final.to_csv("data/df_wiki_table_alvaro_cll1.csv", sep=",", index=False)
    print("csv created sucessfully")
    return csv_table_exported

#table_to_csv(df_table_final)
