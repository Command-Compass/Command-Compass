import os
import time
import openai
from tqdm import tqdm

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Directory containing the CLI help files
input_dir = "cli_help_files"
output_dir = "AI_formatted_cli_help_files"
os.makedirs(output_dir, exist_ok=True)

# OpenAI API limits
RPM = 3  # Requests per minute
RPD = 200  # Requests per day
TPM = 40000  # Tokens per minute
BATCH_QUEUE_LIMIT = 200000  # Total tokens in the queue

# Initialize counters
requests_count = 0
tokens_count = 0


def format_help_with_openai(command, help_text):
    global requests_count, tokens_count

    # Estimate the number of tokens in the input
    input_tokens = len(help_text.split())
    prompt_tokens = len(
        f"Transform the following CLI help output into a tutorial-like document with examples for each option. Use a readable format:\n\n{help_text}\n\nFormatted:".split()
    )
    total_tokens = input_tokens + prompt_tokens + 2048  # Max tokens for the response

    # Check if adding this request would exceed the limits
    if requests_count >= RPD:
        print(f"Daily request limit reached. Skipping {command}.")
        return ""

    if tokens_count + total_tokens > BATCH_QUEUE_LIMIT:
        print(f"Batch queue limit reached. Skipping {command}.")
        return ""

    # Check if this request would exceed the RPM limit
    if requests_count % RPM == 0 and requests_count != 0:
        print(f"Rate limit reached. Waiting for a minute before processing {command}.")
        time.sleep(60)  # Wait for a minute

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Transform the following CLI help output into a tutorial-like document with examples for each option. Use a readable format:\n\n{help_text}\n\nFormatted:",
            max_tokens=2048,
            temperature=0.7,
            n=1,
            stop=None,
        )
        formatted_text = response.choices[0].text.strip()
        requests_count += 1
        tokens_count += total_tokens
        return formatted_text
    except Exception as e:
        print(f"Error processing command {command}: {e}")
        return ""


def process_help_files():
    for filename in tqdm(os.listdir(input_dir)):
        if filename.endswith("_help.txt"):
            command = filename.replace("_help.txt", "")
            with open(os.path.join(input_dir, filename), "r") as file:
                help_text = file.read()

            formatted_help = format_help_with_openai(command, help_text)
            if formatted_help:
                output_filename = f"{command}_formatted_help.txt"
                with open(os.path.join(output_dir, output_filename), "w") as file:
                    file.write(formatted_help)


if __name__ == "__main__":
    process_help_files()
    print(
        f"Formatted CLI help files have been generated in the directory: {output_dir}"
    )
