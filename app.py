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
    completed_record = []
    url_list = []
    for row in df.itertuples():
        url_list.append(row.URL)
        try:
            star, rating = crawler(row.URL.strip())
        except:
            print(f'{row.Product} *******has failed*******')
            continue # https://stackoverflow.com/questions/1843659/how-to-get-back-to-the-for-loop-after-exception-handling
        rows_to_insert = [{
            'URL': row.URL,
            "Company": row.Company,
            "Product": row.Product,
            "totalReview": rating,
            "Score": star,
            "Date": time.strftime("%Y-%m-%d %H:%M:%S")
            }]        
        table_id = f'studied-beanbag-362003.crawl_data.crawl_data'
        errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
        if errors == []:
            print(f"New row have been added.")
        else:
            print(f"Encountered errors while inserting row: {errors}")

        completed_record.append(row.Company)
        print(f'{row.Company} completed: scraping & updating was successful at {time.strftime("%Y-%m-%d %H:%M:%S")}' )
    return completed_record

if __name__ == '__main__':
    app.run(debug=False)