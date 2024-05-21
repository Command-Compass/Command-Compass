import os
import subprocess

# Define the command to run before executing commands from files
INITIAL_COMMAND = "ollama run phi3"

# Define the folder containing command files
COMMANDS_FOLDER = "test"
# Define the folder to save command outputs
OUTPUT_FOLDER = "test_output"


def run_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output = result.stdout
        error = result.stderr
    except subprocess.CalledProcessError as e:
        output = e.stdout
        error = e.stderr

    return output, error


def main():
    # Ensure the output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Execute the initial command
    print("Executing initial command:", INITIAL_COMMAND)
    initial_output, initial_error = run_command(INITIAL_COMMAND)
    if initial_output:
        print("Initial command output:\n", initial_output)
    if initial_error:
        print("Initial command error:\n", initial_error)

    # Iterate over files in the commands folder
    for filename in os.listdir(COMMANDS_FOLDER):
        if filename.endswith(".txt"):
            # Read commands from the file
            file_path = os.path.join(COMMANDS_FOLDER, filename)
            with open(file_path, "r") as file:
                commands = file.readlines()

            # Execute commands and save outputs to a new file
            output_file = os.path.join(
                OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}_output.txt"
            )
            with open(output_file, "w") as output:
                for command in commands:
                    command = command.strip()
                    if command:
                        output.write(f"Command: {command}\n")
                        command_output, command_error = run_command(command)
                        if command_output:
                            output.write(f"Output:\n{command_output}\n")
                        if command_error:
                            output.write(f"Error:\n{command_error}\n")
                        output.write("\n")
            print(f"Output saved to {output_file}")


if __name__ == "__main__":
    main()
