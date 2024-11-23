# GhostCode - Automated Code Generation System

GhostCode is an advanced code generation system that uses sophisticated thinking processes and system prompts to automatically generate high-quality, accessible, and modern React components.

## Project Structure

```
.
├── thinking/           # Thinking process definitions
├── prompts/           # System prompts
├── generated/         # Generated code output
├── templates/         # Code templates
├── ghost_code_generator.py  # Main generator script
├── config.json        # Configuration file
└── README.md         # Documentation
```

## Features

- Automated code generation based on thinking processes
- Modern React component generation with TypeScript
- Built-in support for:
  - Next.js
  - Tailwind CSS
  - shadcn/ui components
  - Accessibility features
  - Dark mode
  - Responsive design
- Comprehensive system prompts
- Template-based generation
- Configurable output

## Usage

1. Configure your requirements in `config.json`
2. Run the generator:
   ```bash
   python ghost_code_generator.py
   ```
3. Find your generated code in the `generated/` directory

## Thinking Processes

The system includes multiple thinking processes:
- Feature24: UI Component generation
- Feature25: Enhanced component generation

## System Prompts

Multiple system prompts are available:
- Base system prompt
- Updated system prompt (recommended)
- Latest system prompt (22-11-2024)

## Configuration

Edit `config.json` to customize:
- Default language and framework
- Component features
- Output directory
- Logging settings

## Requirements

- Python 3.8+
- TypeScript/Next.js environment for generated code
- Node.js 18+
