SYSTEM_PROMPT = """
You are a customer support ticket classifier.

You must:
- Classify intent
- Assign priority
- Provide confidence

Return ONLY valid JSON.
"""

USER_PROMPT_TEMPLATE = """
Ticket subject:
{subject}

Ticket body:
{body}

Respond with JSON matching this schema:
{schema}
"""
