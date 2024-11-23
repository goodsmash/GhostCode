import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging
from pathlib import Path
from ai_engine import AIEngine, AIContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ThinkingProcess:
    name: str
    description: str
    steps: List[str]
    output_format: Dict[str, str]

@dataclass
class CodeTemplate:
    name: str
    language: str
    framework: str
    template: str

class GhostCodeGenerator:
    def __init__(self):
        self.ai_engine = AIEngine()
        self.config = self._load_config()
        self.thinking_processes = {}
        self.code_templates = {}
        self.system_prompts = {}
        
    def _load_config(self) -> Dict:
        try:
            with open("config.json", 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            return {}

    def load_thinking_process(self, file_path: str) -> None:
        """Load thinking process from file."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                process_name = os.path.basename(file_path)
                self.thinking_processes[process_name] = self._parse_thinking_process(content)
                logger.info(f"Loaded thinking process: {process_name}")
        except Exception as e:
            logger.error(f"Error loading thinking process {file_path}: {str(e)}")

    def load_system_prompt(self, file_path: str) -> None:
        """Load system prompt from file."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                prompt_name = os.path.basename(file_path)
                self.system_prompts[prompt_name] = content
                logger.info(f"Loaded system prompt: {prompt_name}")
        except Exception as e:
            logger.error(f"Error loading system prompt {file_path}: {str(e)}")

    def _parse_thinking_process(self, content: str) -> ThinkingProcess:
        """Parse thinking process content into structured format."""
        # Add parsing logic based on your thinking process format
        # This is a placeholder implementation
        steps = content.split('\n')
        return ThinkingProcess(
            name="default",
            description="Automated thinking process",
            steps=steps,
            output_format={"type": "text"}
        )

    def generate_component(self, 
                         name: str,
                         requirements: Dict[str, any]) -> str:
        """Generate a component using AI engine"""
        try:
            # Create AI context
            context = AIContext(
                language=requirements.get("language", "typescript"),
                framework=requirements.get("framework", "next.js"),
                patterns=self._get_relevant_patterns(requirements),
                requirements=requirements,
                history=[]
            )
            
            # Generate code using AI engine
            code = self.ai_engine.generate_code(context)
            
            # Get suggestions for improvements
            suggestions = self.ai_engine.suggest_improvements(code)
            
            # Log suggestions
            if suggestions:
                logger.info("Suggestions for improvement:")
                for suggestion in suggestions:
                    logger.info(f"- {suggestion}")
            
            return code
            
        except Exception as e:
            logger.error(f"Error generating component: {str(e)}")
            return None

    def _get_relevant_patterns(self, requirements: Dict[str, any]) -> List[str]:
        """Get relevant patterns based on requirements"""
        patterns = []
        
        # Add patterns based on component type
        if requirements.get("type") == "form":
            patterns.extend([
                "react.hooks.useState",
                "react.hooks.useEffect",
                "typescript.types.interface"
            ])
        
        # Add patterns based on features
        features = requirements.get("features", [])
        if "responsive" in features:
            patterns.extend([
                "tailwind.layout.grid",
                "tailwind.layout.flex"
            ])
        
        if "dark-mode" in features:
            patterns.append("tailwind.components.card")
        
        return patterns

    def save_generated_code(self, code: str, output_path: str) -> None:
        """Save generated code to file"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w') as f:
                f.write(code)
            logger.info(f"Saved generated code to: {output_path}")
        except Exception as e:
            logger.error(f"Error saving generated code: {str(e)}")

def main():
    # Initialize the generator
    generator = GhostCodeGenerator()

    # Get base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load thinking processes from thinking directory
    thinking_dir = os.path.join(base_dir, "thinking")
    for file in os.listdir(thinking_dir):
        generator.load_thinking_process(os.path.join(thinking_dir, file))

    # Load system prompts from prompts directory
    prompts_dir = os.path.join(base_dir, "prompts")
    for file in os.listdir(prompts_dir):
        generator.load_system_prompt(os.path.join(prompts_dir, file))

    # Example requirements for a form component
    requirements = {
        "language": "typescript",
        "framework": "next.js",
        "type": "form",
        "features": [
            "responsive",
            "accessible",
            "dark-mode",
            "validation"
        ],
        "fields": [
            {
                "name": "email",
                "type": "email",
                "required": True,
                "validation": "email"
            },
            {
                "name": "password",
                "type": "password",
                "required": True,
                "validation": "min:8"
            }
        ]
    }

    # Generate the component
    generated_code = generator.generate_component(
        name="LoginForm",
        requirements=requirements
    )

    # Save generated code
    if generated_code:
        output_path = os.path.join(base_dir, "generated", "login-form.tsx")
        generator.save_generated_code(generated_code, output_path)

if __name__ == "__main__":
    main()
