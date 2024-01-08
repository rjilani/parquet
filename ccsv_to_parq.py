import pandas as pd
import timeit

if __name__ == '__main__':
    start = timeit.default_timer()
    df = pd.read_csv("C:\\Users\\rjilani\\Documents\\Projects\\jupyter_projects\\spark_examples\\complaints.csv")
    # pd.options.display.max_columns = None
    # print(df.columns)
    print(df.head())
    print(df.count())

    count_row = df.shape[0]  # Gives number of rows
    count_col = df.shape[1]  # Gives number of columns

    print(count_row)
    print(count_col)

    df.rename(columns={'Date received': 'Datereceived', 'Sub-product': 'Subproduct', 'Sub-issue' : 'Subissue',
                       'Consumer complaint narrative' : 'Consumercomplnarrative', 'Company public response' : 'Companypublicresponse',
                       'ZIP code':'ZIP',
                       'Consumer consent provided?' : 'ConsumerConsentprovided',
                       'Submitted via': 'Submittedvia', 'Date sent to company': 'Datesenttocompany',
                       'Company response to consumer': 'Companyresponsetoconsumer',
                       'Timely response?' : 'Timelyresponse', 'Consumer disputed?' : 'Consumerdisputed',
                       'Complaint ID' : 'ComplaintID'}, inplace=True)
    print(df.columns)
    df.to_parquet('complaints.parquet', engine="fastparquet")

    print("The time taken :",
          timeit.default_timer() - start)

