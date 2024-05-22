Explanation:

The `mkdir` command in GNU core utilities is used to create a directory, or multiple directories if provided with several arguments. The following are the detailed explanations of its options and usage scenarios:

**Mandatory argument - DIRECTORY(ies):** This represents the name of one or more directories that you want to create. These names can be absolute paths (e.g., `/home/user/mydir`) or relative paths (e.g., `mydir`). When creating multiple directories, you provide them as a list separated by spaces.

**Optional options:**

- `-m`, `--mode=MODE`: This option allows you to set the file mode for the created directory using an octal number representing permissions (for example - `mkdir mydir 0755`). It is not equivalent to setting a read/write/execute (`rwx`) permission directly. Instead, it sets specific access rights for owner, group, and others.

- `-p`, `--parents`: This option does not raise an error if the parent directory already exists or cannot be created because of permissions issues. It ensures that all necessary intermediate directories are also created as needed.

- `-v`, `--verbose`: When this is selected, `mkdir` will print a message for each directory it creates, providing feedback on its operations. This can be useful during debugging and monitoring the execution process.

- `-Z`: If enabled with this option, `mkdir` sets the SELinux security context of the newly created directories to the default type using the SELinux policy. You can also specify a custom SELinux or SMACK (Security-Enhanced Linux kernel module) context for each directory by appending `--context=CTX`.

**Help and Version information:** The `-h` or `--help` option displays usage instructions, while the `--version` provides version details of GNU core utilities.

**Additional Information:** 
- This command can be accessed online through the official documentation at <https://www.gnu.org/software/coreutils/> and supports local help access via `info '(coreutils) mkdir invocation'`.
- Translation issues or bugs should be reported to <https://translationproject.org/team/>.
  
**Example usage:** 
To create a directory named `mydir` with the default SELinux context and verbose output, you would use:
```bash
mkdir -vZ mydir
```
To create multiple directories (`dir1`, `dir2`) along with their parents without any error if they already exist or print creation messages, use `-p` option like this: 
```bash
mkdir -p dir1/dir2
```

Examples:

1. Creating a new directory with default permissions and without checking for its existence or parent directories:
   ```bash
   mkdir sample-directory
   ```
   
2. Using the `-v` (verbose) option to create a directory and list each step:
   ```bash
   mkdir -v project-folder
   ```

3. Creating a nested directory with SELinux security context using both short (`-Z`) and long options (`--context=default`):
   ```bash
   mkdir -p deep-directory --verbose --context=default
   ```

4. Specifying the exact file mode for the created directory:
   ```bash
   mkdir -m 0755 new-folder
   ```

5. Creating a parent directory and its subdirectories if they do not exist, while also setting SELinux contexts on all directories (long form):
   ```bash
   mkdir -p /projects/new-project --context=system:object_rce
   ```

6. Displaying help or version information of `mkdir`:
   ```bash
   mkdir --help
   mkdir --version
   ```