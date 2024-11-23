import os

def create_project_structure():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directories = ['thinking', 'prompts', 'generated', 'templates']
    
    for dir_name in directories:
        dir_path = os.path.join(base_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

if __name__ == "__main__":
    create_project_structure()
