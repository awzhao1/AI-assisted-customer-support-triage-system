import json
from openai import OpenAI

from app.ai.schemas import AIDecision
from app.ai.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
import os

SECRET_KEY = os.getenv('OPENAI_SECRET')
client = OpenAI(api_key=SECRET_KEY)


def run_ai_decision(subject: str, body: str) -> AIDecision:
    schema = AIDecision.model_json_schema()

    prompt = USER_PROMPT_TEMPLATE.format(
        subject=subject,
        body=body,
        schema=json.dumps(schema),
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    parsed = json.loads(content)
    return AIDecision(**parsed)
