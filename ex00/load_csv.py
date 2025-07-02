import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    This function will read
    a csv file received with input
    """

    try:
        read_data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {read_data.shape}")
        return read_data

    except Exception as e:
        print("Unhandled message:", e)
        return None
