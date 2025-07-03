from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd


def abbreviated_num_converter(original: pd.DataFrame) -> pd.DataFrame | None:
    """
    This converts B, K, M respectively to numbers.
    It takes and returns DataFrame
    """
    duplicated = original
    for i in range(len(duplicated)):
        for j in range(1, len(duplicated.columns)):
            val = duplicated.iat[i, j]
            val = val.strip()
            if val.endswith("M"):
                duplicated.iat[i, j] = float(val[:-1]) * 1_000_000
            elif val.endswith("k"):
                duplicated.iat[i, j] = float(val[:-1]) * 1_000
            elif val.endswith("B"):
                duplicated.iat[i, j] = float(val[:-1]) * 1_000_000_000
    return duplicated


def compare_two_population(first: str, second: str) -> None:
    """
    Takes two country names and extracts their datas
    to make comparative graphs.
    Output is saved to a file name compare.png
    """
    try:
        matplotlib.use("Agg")

        read_data = load("population_total.csv")
        converted_data = abbreviated_num_converter(read_data)
        if converted_data is None:
            print("No data has been read")
            return

        first_input = converted_data[converted_data["country"] == first]
        if first_input.empty:
            raise ValueError("Unable to find the data for", first)
        second_input = converted_data[converted_data["country"] == second]
        if second_input.empty:
            raise ValueError("Unable to find the data for", second)

        start_year = converted_data.columns.get_loc("1800")
        end_year = converted_data.columns.get_loc("2050") + 1
        years = converted_data.columns[start_year:end_year].astype(int)
        first_population = first_input.values[
            0, start_year:end_year
        ].astype(float)
        second_population = second_input.values[
            0, start_year:end_year
        ].astype(float)

        sns.lineplot(x=years, y=first_population, label=first)
        sns.lineplot(x=years, y=second_population, label=second)
        plt.title("Population Projections")
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.yticks(range(int(0), int(max(first_population)) + 1, 20_000_000))
        plt.xticks(range(1800, 2051, 40))
        yticks = plt.yticks()[0]
        y_label = [f"{int(y / 1_000_000)}M" for y in yticks]
        plt.yticks(yticks, y_label)
        plt.legend(loc="lower right")
        plt.savefig("compare.png")

    except ValueError as msg:
        print("Value error:", msg)

    except Exception as e:
        print("Unhandled error:", e)


def main():
    """
    Main entry of the program that extracts
    population data of France and another country.
    """
    compare_two_population("France", "South Korea")


if __name__ == "__main__":
    main()
