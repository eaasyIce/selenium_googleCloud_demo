from google.cloud import bigquery
from flask import Flask
import time
from crawler import crawler

app = Flask(__name__)

@app.route('/')
def main():
    print('starts')
    
    # Retrieve source data
    client = bigquery.Client()
    sql = """SELECT * FROM `studied-beanbag-362003.source_urls.source_urls`"""
    df = client.query(sql).to_dataframe()
    url_list = df['URL'].to_list()
    try:   
        results = crawler(url_list)
    except:
        print(f'******* Fail to start the crawler *******')
        return "Fail to start the crawler"
    for row, resultTuple in zip(df.itertuples(), results):
        rows_to_insert = [{
            'URL': row.URL,
            "Company": row.Company,
            "Product": row.Product,
            "totalReview": resultTuple[1],
            "Score": resultTuple[0],
            "Date": time.strftime("%Y-%m-%d %H:%M:%S")
            }]        
        table_id = f'studied-beanbag-362003.crawl_data.crawl_data'
        client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
        if resultTuple[1] == -1 or resultTuple[0] == -1:
            print(f"Unable to crawl {row.Company}, inserting default values")
        print(f'{row.Company} completed: scraping & updating was successful at {time.strftime("%Y-%m-%d %H:%M:%S")}' )
    return "Crawling requests has been completed"

if __name__ == '__main__':
    app.run(debug=False)