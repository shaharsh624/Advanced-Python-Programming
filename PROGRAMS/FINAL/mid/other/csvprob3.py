import pandas as pd

calculate_average = lambda scores: sum(scores) / len(scores)


def main():
    input_file = "csv1.csv"
    df = pd.read_csv(input_file)
    df["Average"] = df.apply(
        lambda row: calculate_average([row["Maths"], row["Science"], row["English"]]),
        axis=1,
    )
    df.to_csv(input_file, index=False)
    print("Sucess")


if __name__ == "__main__":
    main()
