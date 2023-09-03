import pandas as pd
import openai
import subprocess
import os
os.environ['OPENAI_API_KEY'] ="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"

df = pd.read_csv("health_stat_promt_completion.csv")


prepared_data = df.loc[:,['prompt','completion']]
prepared_data.rename(columns={'prompt':'prompt', 'completion':'completion'}, inplace=True)
prepared_data.to_csv('prepared_data_health_plan_v10.csv',index=False)


## prepared_data.csv --> prepared_data_prepared.json
subprocess.run('openai tools fine_tunes.prepare_data -f prepared_data_health_plan_v10.csv --quiet'.split())#--file prepared_data_v1.csv --quiet'.split())

## Start fine-tuning
#subprocess.run('openai api fine_tunes.create -t prepared_data_health_plan_v10_prepared_train.jsonl -m davinci --suffix "healthplanv10")'.split()) #-m davinci --suffix "SFObjectReqFieldv5"')#.split())
