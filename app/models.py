import pandas as pd
from pandas import DataFrame
from fastapi import UploadFile
import io

class DataProcessing():

    @staticmethod
    def read_csv(file: UploadFile):
        df = pd.read_csv(io.BytesIO(file.file.read()))
        return df

    @staticmethod
    def add_columns_risk_level_by_range_km(df: DataFrame):
        df["risk_level"] = pd.cut(df["range_km"],bins=[0,20,100,300,float("inf")],labels=["low", "medium", "high","extreme"],include_lowest= True)
        df["risk_level"] =  df["risk_level"].astype(str)
        return df

    @staticmethod
    def handling_missing_values(df: DataFrame):
        df['manufacturer'] = df['manufacturer'].replace("","Unknown")
        return df
    
    @staticmethod
    def main_function(file):
        df = DataProcessing.read_csv(file)
        adding_column = DataProcessing.add_columns_risk_level_by_range_km(df)
        df = DataProcessing.handling_missing_values(adding_column)
        return df
