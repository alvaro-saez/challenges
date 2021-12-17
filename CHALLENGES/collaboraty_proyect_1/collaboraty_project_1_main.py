from functions import collaborative_project_1_functions as cp1

import pandas as pd
import requests
import bs4
import numpy as np
import re
#variables

url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
parser = "html.parser"
html_element = "table"
css_element = "class"
css_element_value = "wikitable sortable"
position = 0

if __name__ == '__main__':
    output_html_get = cp1.html_get(url)
    response = output_html_get

    output_html_parsing = cp1.html_parsing(response, parser, html_element, css_element, css_element_value, position)

    output_name_columns = cp1.name_columns(output_html_parsing)

    output_raw_values = cp1.raws_value(output_html_parsing)

    df_table_final = cp1.data_frame_table(output_raw_values,output_name_columns)

    csv_created = cp1.table_to_csv(df_table_final)


