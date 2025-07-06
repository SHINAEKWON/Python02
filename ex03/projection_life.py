from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib
import pandas as pd


def life_expectancy_to_gdp():
    gdp_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_data = load("life_expectancy_years.csv")
    combined_data = pd.DataFrame({
        "gdp": gdp_data["1900"],
        "life_expectancy": life_data["1900"]
    })
    sns.scatterplot(x=combined_data["gdp"], y=combined_data["life_expectancy"])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    plt.gca().xaxis.set_major_formatter(formatter)
    xticks = [300, 1000, 10000]
    xlabels = ["300", "1k", "10k"]
    plt.xticks(xticks, xlabels)

    plt.savefig("correlation")


def main():
    try:
        matplotlib.use("Agg")
        life_expectancy_to_gdp()
    except Exception as e:
        print("Error:", e)

    return


if __name__ == "__main__":
    main()
