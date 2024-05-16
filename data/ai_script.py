import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from tqdm import tqdm

# Directory containing the CLI help files
input_dir = "cli_help_files"
output_dir = "AI_formatted_cli_help_files"
os.makedirs(output_dir, exist_ok=True)

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


def format_help_with_gpt2(help_text):
    # Prepare the input prompt for GPT-2
    input_prompt = f"Transform the following CLI help output into a tutorial-like document with examples for each option. Use a readable format:\n\n{help_text}\n\nFormatted:"

    # Tokenize the input prompt
    inputs = tokenizer.encode(input_prompt, return_tensors="pt")

    # Generate the formatted text
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=2048,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode the generated text
    formatted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return formatted_text


def process_help_files():
    for filename in tqdm(os.listdir(input_dir)):
        if filename.endswith("_help.txt"):
            command = filename.replace("_help.txt", "")
            with open(os.path.join(input_dir, filename), "r") as file:
                help_text = file.read()

            formatted_help = format_help_with_gpt2(help_text)
            if formatted_help:
                output_filename = f"{command}_formatted_help.txt"
                with open(os.path.join(output_dir, output_filename), "w") as file:
                    file.write(formatted_help)


if __name__ == "__main__":
    process_help_files()
    print(
        f"Formatted CLI help files have been generated in the directory: {output_dir}"
    )
