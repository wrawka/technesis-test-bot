import pandas as pd


class XlsParser:
    
    @staticmethod
    def parse_file(file_path: str) -> pd.DataFrame:
        df = pd.read_excel(file_path, sheet_name=None)
        combined_df = pd.concat(df.values(), ignore_index=True)

        return combined_df
