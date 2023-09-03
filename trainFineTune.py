import os
import openai

os.environ['OPENAI_API_KEY'] ="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"
openai.api_key = os.getenv("OPENAI_API_KEY")
######################## Step 1 ################################
# fileCreate = openai.File.create(
#     file=open("dataset3.jsonl", "rb"),
#     purpose='fine-tune'
# )
# print(fileCreate)


################################################################

############################## Step 2 ###########################

#file-M4B5Szq77SOhhdKOpqxdw1gH
#fineTuneJob = openai.FineTuningJob.create(training_file="file-M4B5Szq77SOhhdKOpqxdw1gH", model="davinci-002")
#print(fineTuneJob)

# {
#   "object": "fine_tuning.job",
#   "id": "ftjob-iwvOodBW3oIDHF0hMu69QtII",
#   "model": "davinci-002",
#   "created_at": 1693303702,
#   "finished_at": null,
#   "fine_tuned_model": null,
#   "organization_id": "org-y1CzSQNGTFDekQuVjZ9F0ixT",
#   "result_files": [],
#   "status": "created",
#   "validation_file": null,
#   "training_file": "file-M4B5Szq77SOhhdKOpqxdw1gH",
#   "hyperparameters": {
#     "n_epochs": 3
#   },
#   "trained_tokens": null
# }
#################################################################

############################### Step 3 ##########################
#ftjob-iwvOodBW3oIDHF0hMu69QtII

# jobStatus = openai.FineTuningJob.retrieve("ftjob-iwvOodBW3oIDHF0hMu69QtII")
# print(jobStatus)

# {
#   "object": "fine_tuning.job",
#   "id": "ftjob-iwvOodBW3oIDHF0hMu69QtII",
#   "model": "davinci-002",
#   "created_at": 1693303702,
#   "finished_at": 1693303903,
#   "fine_tuned_model": "ft:davinci-002:personal::7spzBHCf",
#   "organization_id": "org-y1CzSQNGTFDekQuVjZ9F0ixT",
#   "result_files": [
#     "file-XXCA8PG2VlUh90xxSX2oErMd"
#   ],
#   "status": "succeeded",
#   "validation_file": null,
#   "training_file": "file-M4B5Szq77SOhhdKOpqxdw1gH",
#   "hyperparameters": {
#     "n_epochs": 3
#   },
#   "trained_tokens": 3096
# }

#####@@@@@@@@@@@@@@@@@ model = ft:davinci-002:personal::7spzBHCf

#################################################################

############################### Step 4 ##########################

response = openai.Completion.create(
    engine="ft:davinci-002:personal::7spzBHCf",
    prompt= "ok , Create Opportunity and followed by Quote creation\n\n###\n\n",
    temperature=0.9,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n","###"]
)
print(response)

