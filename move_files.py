import os
import shutil

def move_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Files to move to thinking directory
    thinking_files = [
        'thinking-feature24',
        'thinking-feature25'
    ]
    
    # Files to move to prompts directory
    prompt_files = [
        'v0-system-prompt',
        'v0-system-prompt(updated)',
        'v0-system-prompt(updated 22-11-2024)'
    ]
    
    # Move thinking files
    for file in thinking_files:
        src = os.path.join(base_dir, file)
        dst = os.path.join(base_dir, 'thinking', file)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"Moved {file} to thinking directory")
    
    # Move prompt files
    for file in prompt_files:
        src = os.path.join(base_dir, file)
        dst = os.path.join(base_dir, 'prompts', file)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"Moved {file} to prompts directory")

if __name__ == "__main__":
    move_files()
