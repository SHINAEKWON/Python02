from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


def main():
    """
    Main entry of the program that
    extracts France life expectancy data.
    """

    try:
        matplotlib.use("Agg")
        read_data = load("life_expectancy_years.csv")
        if read_data is None:
            return
        france = read_data[read_data["country"] == "France"]
        if france.empty:
            raise ValueError("Unable to find the country name in the file")

        years = read_data.columns[1:].astype(int)
        life_expectancy = france.values[0][1:].astype(float)

        sns.lineplot(x=years, y=life_expectancy)
        plt.title("France Life expectancy Projections")
        plt.xlabel("Years")
        plt.ylabel("Life expectancy")
        plt.xticks(range(min(years), max(years) + 1, 40))
        plt.savefig("france_life_expectancy.png")

    except ValueError as msg:
        print("Value error:", msg)

    except Exception as e:
        print("Unhandled message:", e)

    return


if __name__ == "__main__":
    main()
