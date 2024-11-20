import os

# Define the desired project structure
project_structure = {
    "data": {
        "raw": [],
        "processed": []
    },
    "docs": [
        "architecture-diagram.png",
        "README.md"
    ],
    "src": {
        "agents": [
            "agent.py",
            "rl_agent.py",
            "nlp_agent.py"
        ],
        "environment": [
            "environment.py",
            "custom_env.py"
        ],
        "models": [
            "gan.py",
            "transformer.py",
            "policy.py"
        ],
        "utils": [
            "config.py",
            "logger.py",
            "visualization.py"
        ]
    },
    "tests": [
        "test_agents.py",
        "test_env.py",
        "test_models.py"
    ],
    "root_files": [
        ".gitignore",
        "requirements.txt",
        "Dockerfile",
        "docker-compose.yml",
        "LICENSE",
        "README.md"
    ]
}

def create_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):  # It's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)  # Recursively create subdirectories
        elif isinstance(value, list):  # List of files
            os.makedirs(path, exist_ok=True)
            for file in value:
                file_path = os.path.join(path, file)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        f.write("")  # Create an empty file
        else:  # Unsupported type
            raise ValueError(f"Unsupported structure value: {value}")

def create_root_files(base_path, files):
    for file in files:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")  # Create an empty file

if __name__ == "__main__":
    base_directory = os.getcwd()  # Set base directory to the current working directory
    for directory, content in project_structure.items():
        if directory == "root_files":
            create_root_files(base_directory, content)
        else:
            create_structure(base_directory, {directory: content})

    print("Project structure is now complete!")
