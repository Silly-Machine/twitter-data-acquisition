import pandas as pd
import json

def to_pandas(raw_json):
    teweets_list = []
    for status in raw_json:
        json_dump = json.dumps(status._json)
        json_data = json.loads(json_dump)
        teweets_list.append(json_data)
        
    return pd.DataFrame(teweets_list)
