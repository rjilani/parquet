import pandas as pd
import timeit

if __name__ == '__main__':
    start = timeit.default_timer()
    df = pd.read_csv("C:\\Users\\rjilani\\Documents\\Projects\\jupyter_projects\\Pakistan_Temperature\\Tempreture_1901_2016_Pakistan.csv")
    # pd.options.display.max_columns = None
    print(df.columns)
    # print(df.head())
    # print(df.count())

    count_row = df.shape[0]  # Gives number of rows
    count_col = df.shape[1]  # Gives number of columns

    print(count_row)
    print(count_col)
    #
    df.rename(columns={'Temperature - (Celsius)': 'TempCelcius', ' Year': 'Year_a',
                       'Month': 'Month_a'}, inplace=True)
    print(df.columns)
    df.to_csv('Pak_Temp/Tempreture_1901_2016_Pakistan.csv',index=False)
    # df.to_parquet('Pak_Temp/Tempreture_1901_2016_Pakistan.parquet', engine="fastparquet")



    print("The time taken :",
          timeit.default_timer() - start)
