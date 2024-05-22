Explanation:

The `su` command is used in Unix and Linux operating systems to switch the user context from one user to another. By default, it changes the current working directory and sets the effective user ID (UID) and group ID (GID) of the process running the command to that of the specified target user. It also starts a new login shell or executes commands as if they were entered in an interactive shell. Here's a breakdown of its usage, options, and functionality:

Usage: `su [options] [-] [<user> [<argument>...]]`

- `-`: This option is used to invoke the behavior of `su -l`, which makes the shell a login shell. A login shell usually executes some initialization scripts like `.bashrc` or `.profile`.

- `<user>`: The target user whose UID and GID will be changed, as well as for whom the commands are executed (if any). If this option is not given, the default user assumed by `su` is root.

Arguments (`<argument>`): Additional arguments can be passed to various options or functions when using `su`.

Options:
- `-m`: Do not reset environment variables when switching users with su. This option overrides the behavior of `-p`, which is used for preserving environment variables by default.
- `-p`: Preserve environmental variables during user switch operations. If this option is omitted, standard behavior is applied (which typically means resetting environment variables).
- `--preserve-environment`: Equivalent to using `-p` and will preserve environment variables when switching users.
- `-w`: A whitelist for environment variables that should not be reset during user switch operations. This can be specified as `<list>`.
- `--whitelist-environment <list>`: List of specific environment variables that are allowed to remain unchanged upon user switch.
- `-g`, `--group`: Specify the primary group ID (GID) for the target user. By default, `su` uses the GID corresponding to the specified or assumed user's login name.
- `-G`, `--supp-group`: Specify a supplemental group for the target user. If this option is not given and no group is already associated with the user, `su` will set one of them as the primary (or "effective") group ID to be used during command executions in that context.
- `-l`, `--login`: Indicates that a login shell should be launched after switching users. This option typically ensures that the correct initialization files are sourced, allowing user-specific customizations and configurations to take effect properly.
- `-c`, `--command <command>`: Execute a single command without launching an interactive login shell. This option is useful for running commands as another user or executing non-interactive scripts. If multiple arguments (commands) are provided, they will be passed sequentially after the initial `su` call.
- `--session-command <command>`: Similar to `-c`, but it passes a single command to an interactive login shell session without creating a new one. It is also used for executing non-interactive scripts in the context of another user's environment.
- `-f, --fast`: For Csh and TCsh shells, this option enables a fast startup by not loading many initialization files like `.cshrc`, which might otherwise affect performance when launching interactive shells. It is typically used for automated or scripted execution scenarios where extensive user customizations are unnecessary.
- `-s, --shell <shell>`: Specify the target shell to be executed after changing users with `su`. The specified shell must be included in `/etc/shells`, which lists the available login shells on the system. This option allows using non-standard or customized shells that aren't typically found in `/bin` directories, as long as they are allowed by `/etc/shells`.
- `-P, --pty`: Enable a pseudo-terminal (PTY) for executing commands under `su`. When enabled, the new session will mimic an interactive terminal environment. This option is useful when running shell programs that require standard input and output streams or expect them to be PTYs.
- `-h, --help`: Displays usage information and a list of options available with the command in question.
- `-V, --version`: Shows version information for `su`.

For more detailed explanations about each option and additional usage examples, you can refer to the manual page by executing `man su` or `su --help` on your system.

Examples:

1. Changing the user ID and group ID for root to a regular user:
```bash
su alice -
```
Explanation: This command changes the effective user ID and group ID to that of 'alice', assuming 'alice' is not provided, it defaults to root with no additional arguments.

2. Preserving environment variables while changing user/group:
```bash
su -m alice
```
Explanation: This command changes the effective user to 'alice' but preserves all existing environment variables due to using '-m'.

3. Specifying primary and supplemental groups for a given user:
```bash
su -g wheel -G sudo alice
```
Explanation: This changes the effective user ID and group ID of 'alice' to that of 'wheel' (primary group) with a supplemental group of 'sudo'.

4. Making the shell login-capable as root without changing environment variables:
```bash
su -l
```
Explanation: This command makes the current shell run as a login shell for the default user, typically root if not specified, and it doesn't alter any environment variables due to using '-'.

5. Passing a single command with '--command':
```bash
su --command echo "Hello, World!"
```
Explanation: This executes the given command ('echo Hello, World!') in the context of the root user without creating a new session or changing environment variables.

6. Running an unconventional shell with '-s' and ensuring it is allowed on system:
```bash
su -s rbash
```
Explanation: This attempts to run 'rbash', assuming '/etc/shells' allows this custom shell, for the current user (default root if not specified).