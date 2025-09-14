# Prompts.py
def planner_prompt(user_request: str) -> str:
    PLANNER_PROMPT = f"""You are a planning agent.
Your job is to break down the following user request into high-level engineering tasks.

User request: {user_request}
    """
    return PLANNER_PROMPT
