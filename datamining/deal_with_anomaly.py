"""
Deal with dtypes, datetime transformation
, and bool, etc.
"""
import pandas as pd

FILE_PATH = "dtype_sample.csv"
DESTINATION_FILE_PATH = "n_dtype_sample.csv"

DTYPES = {
    "DepartmentID": str,
    "Remote": bool,
    # "OnBoard": bool,  # It will raise Exception
    "Intern": bool,
}

# @task
def e_read_dtype_sample_df() -> pd.DataFrame:
    return pd.read_csv(
        FILE_PATH,
        dtype=DTYPES,
    )

# @task
def t_datetime_normalization(df: pd.DataFrame) -> pd.DataFrame:
    df["CreatedDatetime"] = pd.to_datetime(
        df["CreatedDatetime"],
        errors="coerce",
    )
    df["CreatedDatetimeTZ"] = pd.to_datetime(
        df["CreatedDatetimeTZ"],
        errors="coerce",
    )

    return df

# @task
def t_onboard_to_bool(df: pd.DataFrame) -> pd.DataFrame:
    df["OnBoard"] = df["OnBoard"].apply(
        lambda x: True if x.upper() == "V" else False
    )

    return df

# @task
def l_df_to_csc(df: pd.DataFrame):
    df.to_csv(
        DESTINATION_FILE_PATH,
        index=False,
    )

# @dag
def main():
    df = e_read_dtype_sample_df()
    df = t_datetime_normalization(df)
    df = t_onboard_to_bool(df)
    l_df_to_csc(df)


if __name__ == "__main__":
    main()