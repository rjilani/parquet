import pandas as pd
import timeit

if __name__ == '__main__':
    start = timeit.default_timer()
    df = pd.read_csv("C:\\Users\\rjilani\\Documents\\Projects\\jupyter_projects\\spark_examples\\complaints.csv")
    pd.options.display.max_columns = None
    # print(df.columns)
    # print(df.head())

    # print(df.info(verbose = True, show_counts = True))

    df.rename(columns={'Date received': 'Datereceived', 'Sub-product': 'Subproduct', 'Sub-issue' : 'Subissue',
                       'Consumer complaint narrative' : 'Consumercomplnarrative', 'Company public response' : 'Companypublicresponse',
                       'ZIP code':'ZIP',
                       'Consumer consent provided?' : 'ConsumerConsentprovided',
                       'Submitted via': 'Submittedvia', 'Date sent to company': 'Datesenttocompany',
                       'Company response to consumer': 'Companyresponsetoconsumer',
                       'Timely response?' : 'Timelyresponse', 'Consumer disputed?' : 'Consumerdisputed',
                       'Complaint ID' : 'ComplaintID'}, inplace=True)

    # print(df.loc[[0, 1], ['Datereceived', 'Subproduct']])
    rows = df.sample(n=10)
    rows.to_csv("sample1.csv", encoding='utf-8', index=False)
    # print(rows[['Datereceived', 'Datereceived']])
    # print(rows.iloc[[0,1], [0,4]])
    print(rows.iloc[[0, 1], 0:2])

    print("The time taken :",
          timeit.default_timer() - start)
