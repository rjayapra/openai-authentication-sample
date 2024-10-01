from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    api_version="2024-02-15-preview",
    azure_endpoint="https://learnopenai-rj.openai.azure.com/",
    azure_ad_token_provider=token_provider
)

response = client.chat.completions.create(
    model="chat", #"gpt-35-turbo-0125", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)
print(response.choices[0].message.content)

# get user input
user_input = input("Enter your message: ")
response = client.chat.completions.create(
    model="chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"},
        {"role": "system", "content": response.choices[0].message.content}, 
        {"role": "user", "content": user_input}
    ]
)

print(response.choices[0].message.content)