from google.cloud import bigquery
from flask import Flask
import time
from site_gartner.scrap_gartner import scrap_gartner
from site_tr.scrap_tr import scrap_tr
from site_g2.scrap_g2 import scrap_g2

app = Flask(__name__)
@app.route('/')

def main():
    print('starts')
    client = bigquery.Client()
    # for site in ['gartner', 'tr']:
    for site in ['g2']:
        if site == 'gartner':
            sql = """SELECT * FROM `my-first-dash-app.source_data.source_gartner`"""
            scrap_function = scrap_gartner
            scrap_table_name = 'scrap_gartner'
        elif site == 'tr':
            sql = """SELECT * FROM `my-first-dash-app.source_data.source_tr`"""
            scrap_function = scrap_tr
            scrap_table_name = 'scrap_tr'
        else: 
            sql = """SELECT * FROM `my-first-dash-app.source_data.source_g2`"""
            scrap_function = scrap_g2
            scrap_table_name = 'scrap_g2'

        # Retrieve source data
        df = client.query(sql).to_dataframe()

        print(f"Source data has been downloaded. Starting to scrap *******{site}*******")

        for row in df.itertuples():
            try:
                totalReview, score = scrap_function(row.url.strip())
            except:
                print(f'{site}:{row.product_name}_{row.catagory} *******failed*******')
                continue # https://stackoverflow.com/questions/1843659/how-to-get-back-to-the-for-loop-after-exception-handling
            rows_to_insert = [{
            # 'url': row.url,
            "productName": row.product_name,
            "catagory": row.catagory,
            "is_genesys": row.is_genesys,
            "totalReview": totalReview,
            "score": score,
            "date": time.strftime("%Y-%m-%d %H:%M:%S")
            }]

            # print(f"New row have been added.")
        # write into respective scrap table 
        
            table_id = f'my-first-dash-app.scrap_data.{scrap_table_name}'
            errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
            if errors == []:
                print(f"New row have been added.")
            else:
                print(f"Encountered errors while inserting row: {errors}")

        print(f'Completed: scraping & updating was successful on *******{site}******* at {time.strftime("%Y-%m-%d %H:%M:%S")}' )
    return 'Scraping program has finished!!!'

if __name__ == '__main__':
    app.run()