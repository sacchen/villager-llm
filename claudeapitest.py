from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

anthropic = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    # api_key=""
)

completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} You are a 16th century bard. \n How does a court case get to the Supreme Court?{AI_PROMPT}",
)
print(completion.completion)
