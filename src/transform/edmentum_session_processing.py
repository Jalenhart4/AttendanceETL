import pandas as pd


def transform_student_sessions(df, session_threshold):
    """Transforms student session data by filtering valid sessions,
       formatting dates, and removing weekends."""

    # Convert to datetime and calculate session duration
    df["LoginDateTime"] = pd.to_datetime(df["LoginDateTime"], format="%m/%d/%Y %I:%M:%S %p")
    df["LogOutDateTime"] = pd.to_datetime(df["LogOutDateTime"], format="%m/%d/%Y %I:%M:%S %p")

    df["SessionDuration"] = (df["LogOutDateTime"] - df["LoginDateTime"]).dt.total_seconds() / 60
    df["SessionDate"] = df["LoginDateTime"].dt.date  # Extract date only

    # Remove weekends (Saturday = 5, Sunday = 6)
    df = df[df["LoginDateTime"].dt.weekday < 5]

    # Filter by session duration
    df = df[df["SessionDuration"] > session_threshold]

    # Drop duplicates to keep only one session per student per day
    df = df.drop_duplicates(subset=["LearnerLastName", "LearnerFirstName", "SessionDate"])

    return df[["LearnerLastName", "LearnerFirstName", "SessionDate"]]  # Return cleaned DataFrame
