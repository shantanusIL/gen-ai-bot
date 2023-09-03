import os
import openai
import subprocess

openai.api_key ="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"
#subprocess.run('openai api fine_tunes.list')

response = openai.Completion.create(
  model="ft:davinci-002:personal::7spzBHCf"#"ft:davinci-002:personal::7spRNiFv",#"curie:ft-personal:sfobjectreqfieldv5-2023-05-18-20-22-49",#"davinci:ft-personal:sfobjectreqfieldv4-2023-05-18-19-51-18"
  #engine="text-davinci-003",
  prompt= "Generate an Quote on top of Account ABC", #""Age:55\nHealth Status:0\nCharges:29000.00\n\n###\n\n",
  #"Age:38\nHealth Status:1\nCharges:7789.6715\n\n###\n\n", #"Age:69\nHealth Status:0\nCharges:44091.0\n\n###\n\n", #"Age:40\nHealth Status:1\nCharges:8059.6791\n\n###\n\n",#"Age:54\nHealth Status:0\nCharges:29637.0\n\n###\n\n",
  #temperature=0,
  #max_tokens=120,
  #top_p=1,
  
  frequency_penalty=0,
  presence_penalty=0,
  stop=["END"]
)
print(response)
resp=response['choices'][0]['text']
end= resp.find('End')
print('...... '+resp[0:end])


