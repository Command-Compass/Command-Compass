import os
import csv

# Directory containing the help text files
input_dir = "cli_help_files"
output_dir = "formatted_cli_help_csv"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)


def format_help_file_to_csv(cmd, input_file, output_file):
    with open(input_file, "r") as infile:
        lines = infile.readlines()

        usage_section = []
        options_section = []
        examples_section = []
        additional_info_section = []

        current_section = None

        for line in lines:
            if line.startswith("Usage:"):
                current_section = usage_section
                usage_section.append(line.strip().replace("Usage: ", ""))
            elif line.strip().startswith("POSIX options:") or line.strip().startswith(
                "Short options:"
            ):
                current_section = options_section
                options_section.append(line.strip())
            elif line.strip().startswith("Examples:"):
                current_section = examples_section
                examples_section.append(line.strip().replace("Examples:", ""))
            elif line.strip().startswith("To report bugs"):
                current_section = additional_info_section
                additional_info_section.append(line.strip())
            elif current_section is not None:
                current_section.append(line.strip())

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the usage section
        if usage_section:
            writer.writerow(["Section", "Content"])
            writer.writerow(["Usage"])
            for line in usage_section:
                writer.writerow(["", line])
            writer.writerow([])  # Blank row for separation

        # Write the options section
        if options_section:
            writer.writerow(["Options"])
            for line in options_section:
                if line.startswith("-") or line.startswith("--"):
                    parts = line.split()
                    option = parts[0]
                    description = " ".join(parts[1:])
                    writer.writerow(["", f"{option}: {description}"])
                else:
                    writer.writerow(["", line])
            writer.writerow([])  # Blank row for separation

        # Write the examples section
        if examples_section:
            writer.writerow(["Examples"])
            for line in examples_section:
                writer.writerow(["", line])
            writer.writerow([])  # Blank row for separation

        # Write the additional information section
        if additional_info_section:
            writer.writerow(["Additional Information"])
            for line in additional_info_section:
                writer.writerow(["", line])


def main():
    for filename in os.listdir(input_dir):
        if filename.endswith("_help.txt"):
            cmd = filename.replace("_help.txt", "")
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f"{cmd}_formatted_help.csv")
            format_help_file_to_csv(cmd, input_file, output_file)
            print(f"Formatted help for {cmd} saved to {output_file}")


if __name__ == "__main__":
    main()
