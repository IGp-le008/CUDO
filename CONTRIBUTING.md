"""Contributing guidelines."""

# Contributing to COLLEXA

We welcome contributions! This document outlines how to contribute.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn
- Report issues responsibly

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit with clear messages
5. Push to your fork
6. Create a Pull Request

## Development Workflow

### Setup Development Environment
```bash
git clone <your-fork-url>
cd VibeCode
docker-compose up -d
```

### Code Standards

**Python (Backend)**
- Use type hints
- Follow PEP 8
- Format with `black`
- Lint with `ruff`

```bash
cd backend
black .
ruff check .
```

**TypeScript (Frontend)**
- Use strict mode
- Format with `prettier`
- Lint with `eslint`

```bash
cd frontend
npm run format
npm run lint
```

### Testing

**Backend**
```bash
cd backend
pytest
pytest --cov=.
```

**Frontend**
```bash
cd frontend
npm test
npm run type-check
```

### Commit Messages

```
feat: Add new feature
fix: Fix a bug
docs: Update documentation
style: Code formatting
refactor: Code refactoring
test: Add tests
chore: Update dependencies
```

Example:
```
feat: Add student results endpoint

- Implemented GET /api/results/my-results
- Added authentication check
- Added database query optimization
```

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Provide clear PR description
6. Link related issues

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Changes Made
- Bullet point 1
- Bullet point 2

## Testing Done
- Manual testing
- Unit tests
- Integration tests

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes
```

## Reporting Bugs

Include:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Environment (OS, Docker version, etc.)
- Logs/error messages
- Screenshots if applicable

## Feature Requests

Include:
- Use case/motivation
- Proposed implementation (optional)
- Examples/mockups
- Related features

## Documentation

- Update README.md for user-facing changes
- Add docstrings to functions
- Update API docs in FastAPI
- Add comments for complex logic

## Performance

- Consider database query efficiency
- Optimize frontend bundle size
- Use caching where appropriate
- Profile before claiming performance improvements

## Security

- Don't commit secrets or credentials
- Report security issues privately
- Use environment variables for sensitive data
- Validate all inputs
- Sanitize outputs

## Questions?

- Open a GitHub Discussion
- Check existing issues
- Review documentation
- Ask in comments

---

Thank you for contributing! 🙏
