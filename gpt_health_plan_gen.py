import os
import openai
import pandas as pd

openai.api_key = "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"

df1 = pd.read_csv("health_stat (2).csv")
#print(df2)


df = pd.DataFrame()

for i in df1.index:
    age=df1['age'][i]
    health_status=df1['health_status'][i]
    charges=df1['charges'][i]
    recommended_Plan=df1['recommended_Plan'][i]
    
        
    new_row = {
          'prompt':'Age:'+str(age)+'\nHealth Status:'+str(health_status)+'\nCharges:'+str(charges)+'\n\n###\n\n', 
          'completion':' RecommendedPlan:'+str(recommended_Plan)+' End', 
          }
    new_row = pd.DataFrame([new_row])
    df = pd.concat([df, new_row], axis=0, ignore_index=True)


df.to_csv("health_stat_promt_completion.csv")
