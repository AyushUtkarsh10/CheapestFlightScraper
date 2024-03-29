import pandas as pd
import os
from base_logger import logger
# from options import XPATH_KEYS
KEYS = ['outbound', 'inbound', 'codes', 'price', 'company', 'info', 'duration', 'stops']

class ReadResult():
    def __init__(self, filename) -> None:
        self.filename = filename
        self.df = pd.read_csv(filename, header=None)      
        # Check if number of columns in the file is greater than the length of the header KEYS
        if len(self.df.columns) > len(KEYS):
            new_header = KEYS + [f"return_{col}" for col in KEYS[2:]]
            self.df.columns = new_header
        else:
            self.df.columns = KEYS[:len(self.df.columns)] 
        
    def sort_by_price(self, col_name='price'):
        def extract_price(s):
            try:
                if isinstance(s, str):
                    return int(float((s.split(' ')[0]).replace('.','')))
                elif pd.isna(s):
                    return 0
                else:
                    return int(s)
            except:
                return 0
        self.df[col_name] = self.df[col_name].fillna('0 €')
        self.df[col_name] = self.df[col_name].apply(extract_price)
        sorted_df = self.df[self.df[col_name] != 0].sort_values(col_name)
        logger.info(f'Flights sorted by price:\n{sorted_df.head()}')
        return sorted_df
        
    def sort_by_duration(self, col_name='duration'):
        pass
                
                




        
