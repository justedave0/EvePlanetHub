# Cursor IDE Rules for 2026

This directory contains all the rules for Cursor IDE projects following best practices from 2026.

## Rule Structure

Each `.mdc` file in this directory represents a specific rule category, organized by functionality:

- `general.mdc` - General code style and formatting
- `api-routes.mdc` - API route conventions and error handling 
- `components.mdc` - Component development guidelines
- `testing.mdc` - Testing and quality assurance
- `database.mdc` - Database schema and query patterns

## Rule Format

All rule files follow the 2026 standard:
- YAML frontmatter with metadata (name, type, author, version, description)
- Clear markdown structure with code examples
- Consistent formatting and conventions
- Specific guidance for implementation

## Usage

1. Place this `.cursor` directory at the root of your project
2. Cursor IDE will automatically load these rules
3. Rules are applied across all files matching the configured patterns
4. Update rules as needed to fit your specific project requirements

## Maintenance

- Keep rule files focused on single concerns
- Version control changes to track evolution of practices
- Review and update rules periodically based on new best practices