from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# Model parameters
PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
}

# watsonx credentials
# Note: Normally we'd need an API key, but in Skill's Network Cloud IDE will automatically handle that for you.

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


# Model IDs
LLAMA3_MODEL_ID = "meta-llama/llama-3-2-11b-vision-instruct"
GRANITE_MODEL_ID = "ibm/granite-3-8b-instruct"
MIXTRAL_MODEL_ID = "mistralai/mistral-large"