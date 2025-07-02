from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
# Set up credentials for WatsonxLLM
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://eu-gb.ml.cloud.ibm.com"
project_id = "d065193c-9ad1-468b-a895-50a5aed857a0"
api_key = os.environ.get("WATSONX_APIKEY")

credentials = {
    "url": url,
    "api_key": api_key  # Using the api_key variable from environment variables
    # "project_id": project_id  # Also including project_id for completeness
}


params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 100
}

model = ModelInference(
    model_id='meta-llama/llama-3-3-70b-instruct',
    params=params,
    credentials=credentials,
    project_id=project_id
)

# text = """
# Only reply with the answer. What is the capital of Canada?
# """

text = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert assistant who provides concise and accurate answers.<|eot_id|>

<|start_header_id|>user<|end_header_id|>
What is the capital of Canada?<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
"""

print(model.generate(text)['results'][0]['generated_text'])