import os
import csv
import time
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from tqdm import tqdm


def read_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def write_text_into_file(file_path, text):
    with open(file_path, "w") as file:
        file.write(text)


llm = ChatOllama(model="phi3")
prompt = ChatPromptTemplate.from_template('{Prompt} "{text}"')

chain = prompt | llm | StrOutputParser()

input_directory = "cli_help_files"
output_directory = "cli_help_files_output"

os.makedirs(output_directory, exist_ok=True)

input_files = [f for f in os.listdir(input_directory) if f.endswith(".txt")]

csv_file_path = "processing_times.csv"
with open(csv_file_path, "w", newline="") as csvfile:
    fieldnames = ["File Name", "Processing Time (s)"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    total_processing_time = 0
    for file_name in tqdm(input_files, desc="Processing files"):
        input_file_path = os.path.join(input_directory, file_name)

        if os.path.isfile(input_file_path):
            text = read_text_from_file(input_file_path)

            start_time = time.time()

            response1 = chain.invoke({"Prompt": "Explain in detail", "text": text})
            response2 = chain.invoke(
                {"Prompt": "Give examples for every argument", "text": text}
            )

            combined_response = (
                f"Explanation:\n\n{response1}\n\nExamples:\n\n{response2}"
            )

            output_file_path = os.path.join(
                output_directory, f"{os.path.splitext(file_name)[0]}.md"
            )

            write_text_into_file(output_file_path, combined_response)

            end_time = time.time()

            processing_time = end_time - start_time
            total_processing_time += processing_time

            writer.writerow(
                {"File Name": file_name, "Processing Time (s)": processing_time}
            )

print(f"Total Processing Time: {total_processing_time} seconds")
