# src > repository > systemprompt.js

# system prompt (instruction given to ai)
# the ai's hidden instruction that guide it's behaviour and response..
# the higher the quality of system prompt  , better the output..

# model id - if model id is outdated then the program will not work

# tokens are used to set the limit of request..by which the ai will stop accepting the user request 

#  chunks of stream - a chunk is a small piece of data at that comes from a stream... instead of loading all data at once , a stream sends data in small parts(chunks)..
# chunk is a small piece of data transferred through a stream.
# it carries a smaal portion of data from one place to another through a stream.
# it is used to filter the data and remove the unwanted data...


# Src > Controller > groqController-js

# Controller Folder:- Handle incoming requests from the user

# User Request (Input message submitted by the user to the AI model)
# Get Prompt (The controller extracts the user's message from the request body)
# Validate Prompt (Check whether the prompt exists and is valid)
# Call Service (After validation, the controller sends the prompt to the service)
# Return Service (service returns the AI answer)

# Src > Controller > groqController.js

# In the start ,where we import all prompts
#import {bankingPrompt, hospitalityPrompt, insurancePrompt, realEstatePrompt, retailPrompt 

# const userPrompt = req.body.prompt;

# await response. save); (used to store response in database)

# 1.	User Request
#          |
# 2.	Get User Prompt(const userPrompt = req. body•prompt;)
#	       |  
# 3.	Validate User Prompt
#          |	
# 4.	Call Service
#	       |
# 5.	Return Response

# Src > Controller > groqController.js

# User prompt(the services recieved from the cantroller)
# system prompt(the service add a system prompt to guide ai response)
# model selection(the services select the appropriate ai model to use)
# api call(the services call the OpenAI api with the combined prompt and model)
# stream processing(it deleviers the ai response in real time gradually insted waiting for the entire response to complete)
# chunks(the are the small piece of the data recieved from the stream)
# console.log(it is used when we have to debug )
# build final response(select the wanted data from chunks and remove unwanted data)
# return reponse(it return response to the user)


# services - contains the application's bussiness logic.
#  1.  Recive Valid prompt(user prompt)
#      |
#  2.  Get system Prompt
#      |
#  3.  Select Model id
#      |
#  4.  Call OpenAI API(ask openAI for response)
#      |
#  5.  Process Stream and Chunks 
#      |
#  6.  Build final response
#      |
#  7.  Return result

