## AIlabTools - 7CEIXoSvhUYN4tLOiSxrGeKuTeWs8VKAV2NZUFAHIayc25dkg6nDkQYRBdnWaf3J

import enum
import pydantic

from langchain.chat_models import ChatOpenAI
from kor import create_extraction_chain, Object, Text, Number
from typing import List
from kor import from_pydantic
from pydantic import BaseModel, Field
from typing import Optional

## frequency_penalty, presense_penalty and top_g are optional parameters. kors example top_g was set to 1.0.
llm = ChatOpenAI(
    openai_api_key="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",
    model_name="gpt-3.5-turbo",
)
