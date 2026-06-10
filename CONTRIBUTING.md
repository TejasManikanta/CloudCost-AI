# CloudCost AI - Contributing Guide

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Submit a pull request

## Development Setup

```bash
git clone https://github.com/your-username/CloudCost-AI.git
cd CloudCost-AI

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env with your configuration
```

## Code Standards

### Python

- Follow PEP 8
- Use type hints
- Write docstrings for all functions
- Use 4 spaces for indentation

### JavaScript

- Use ES6+ features
- Follow Airbnb style guide
- Use meaningful variable names
- Add comments for complex logic

### HTML/CSS

- Use semantic HTML
- BEM naming convention for CSS classes
- Mobile-first responsive design

## Commit Messages

Use conventional commits:

```
feat: Add new feature
fix: Fix bug
docs: Update documentation
test: Add tests
refactor: Refactor code
style: Code style changes
chore: Maintenance
```

## Testing

```bash
pytest tests/
pytest --cov=backend tests/
```

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit PR with clear description

## Code Review

All PRs require:
- At least 1 approval
- All tests passing
- No merge conflicts

## Reporting Issues

Include:
- Detailed description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details

## License

MIT License
