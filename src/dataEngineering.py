from datetime import datetime
import pandas as pd
import glob
import json


def to_pandas(raw_json):
    teweets_list = []
    for status in raw_json:
        json_dump = json.dumps(status._json)
        json_data = json.loads(json_dump)
        teweets_list.append(json_data)

    return pd.DataFrame(teweets_list)


def batch_to_csv(api_cnx, queries=[""], path="data", batch=10):
    counter = 0
    for query in queries:
        counter += 1

        temp_json = api_cnx.get_tweets(query=query, count=batch)
        temp_df = to_pandas(temp_json)

        search_key = 'notheme' if query == '' else query
        date_time = datetime.now().strftime("%m%d%Y%H%M%S")
        batch_size = len(temp_df)

        print(
            f" {datetime.now().strftime('%m-%d-%Y %H:%M:%S')} - [{counter}/{len(queries)}]..... batch size: {batch_size}..... key: {search_key} ")

        temp_df.to_csv(
            f'{path}/raw_tweets_{search_key}_s{batch_size}_dt{date_time}.csv', index=False)


def load_dataframes(path_class="data/raw_tweets"):
    return pd.concat(map(pd.read_csv, glob.glob(f'{path_class}*.csv')))
