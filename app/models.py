import pandas as pd
from pandas import DataFrame


class DataProcessing():

    @staticmethod
    def add_columns_risk_level_by_range_km(df):
        df["risk_level"] = pd.cut(df["range_km"],[0,20,100,300,float("inf")],labels=["low", "medium", "high","extreme"],include_lowest=True)
        return df

    @staticmethod
    def handling_missing_values(df):
        df['manufacturer'] = df['manufacturer'].replace("","Unknown")
        return df