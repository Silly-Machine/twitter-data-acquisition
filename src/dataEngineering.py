from datetime import datetime
import pandas as pd
import glob
import json
import os


def load_dataframes(path_class="data/raw/"):
    return pd.concat(map(pd.read_csv, glob.glob(f'{path_class}*.csv')))


def to_pandas(raw_json):
    teweets_list = []
    for status in raw_json:
        json_dump = json.dumps(status._json)
        json_data = json.loads(json_dump)
        teweets_list.append(json_data)

    return pd.DataFrame(teweets_list)


def batch_to_csv(api_cnx, queries=[""], path="data/raw/", batch=10, loop=False):

    if loop == True:
        cycle = 0
        while loop == True:
            cycle += 1
            counter = 0
            for query in queries:
                counter += 1

                temp_json = api_cnx.get_tweets(query=query, count=batch)
                temp_df = to_pandas(temp_json)

                search_key = 'notheme' if query == '' else query
                file_name = '_'.join(search_key.split(' '))
                date_time = datetime.now().strftime("%m%d%Y%H%M%S")
                batch_size = len(temp_df)

                print(
                    f" loop :{loop} - {datetime.now().strftime('%m-%d-%Y %H:%M:%S')} - [{cycle}/{counter}/{len(queries)}]..... batch size: {batch_size}..... key: {search_key} ")

                temp_df.to_csv(
                    f'{path}/raw_tweets_{file_name}_s{batch_size}_dt{date_time}.csv', index=False)
    else:
        counter = 0
        for query in queries:
            counter += 1

            temp_json = api_cnx.get_tweets(query=query, count=batch)
            temp_df = to_pandas(temp_json)

            search_key = 'notheme' if query == '' else query
            file_name = '_'.join(search_key.split(" "))
            date_time = datetime.now().strftime("%m%d%Y%H%M%S")
            batch_size = len(temp_df)

            print(
                f" loop :{loop} - {datetime.now().strftime('%m-%d-%Y %H:%M:%S')} - [{counter}/{len(queries)}]..... batch size: {batch_size}..... key: {search_key} ")

            temp_df.to_csv(
                f'{path}/raw_tweets_{file_name}_s{batch_size}_dt{date_time}.csv', index=False)


def load_expressions(path='data/ref/', key_name="expressions"):
    word_list = []

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if filename.endswith('.json'):
            with open(file_path) as file:
                data = json.load(file)

                if key_name in data:
                    word_list.extend(data[key_name])

    return word_list
