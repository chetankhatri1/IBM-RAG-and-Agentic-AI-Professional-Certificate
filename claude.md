# Project Context for Claude Code

## Project Overview
**Project Name:** [Your Project Name]
**Type:** [Web App / API / CLI Tool / Library / etc.]
**Tech Stack:** [e.g., React, Node.js, TypeScript, Python, etc.]
**Purpose:** [Brief description of what this project does]

## Architecture & Structure
```
project-root/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration files
└── scripts/       # Build/deployment scripts
```

## Key Technologies & Dependencies
- **Frontend:** [Framework/libraries used]
- **Backend:** [Framework/libraries used]
- **Database:** [Database type and ORM if applicable]
- **Testing:** [Testing frameworks]
- **Build Tools:** [Webpack, Vite, etc.]
- **Package Manager:** [npm, yarn, pnpm]

## Development Guidelines

### Code Style & Standards
- Use [ESLint/Prettier/Black/etc.] for formatting
- Follow [specific naming conventions]
- Write tests for all new features
- Use TypeScript strict mode (if applicable)
- Comment complex business logic

### Git Workflow
- Use conventional commits (feat:, fix:, docs:, etc.)
- Create feature branches from `main`
- Require PR reviews before merging
- Run tests before committing

### Testing Strategy
- Unit tests for core business logic
- Integration tests for API endpoints
- E2E tests for critical user flows
- Maintain >80% code coverage

## Current Development Focus
**Active Features:**
- [Feature 1 being worked on]
- [Feature 2 being worked on]

**Known Issues:**
- [Issue 1 that needs attention]
- [Issue 2 that needs attention]

**Next Priorities:**
- [Upcoming feature/refactor]
- [Performance improvements needed]

## Environment Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## Key Files & Their Purpose
- `src/main.js` - Application entry point
- `src/components/` - Reusable UI components
- `src/utils/` - Helper functions and utilities
- `config/database.js` - Database configuration
- `tests/` - All test files organized by feature

## API Information
**Base URL:** [Development/Production URLs]
**Authentication:** [JWT/OAuth/API Keys/etc.]
**Key Endpoints:**
- `GET /api/users` - Fetch user list
- `POST /api/auth/login` - User authentication
- [Add other important endpoints]

## Database Schema
**Key Models:**
- **Users:** id, email, username, created_at
- **Posts:** id, title, content, user_id, created_at
- [Add other important models]

## Common Commands & Scripts
```bash
# Development
npm run dev          # Start dev server
npm run test:watch   # Run tests in watch mode
npm run lint         # Check code style

# Database
npm run db:migrate   # Run database migrations
npm run db:seed      # Seed database with test data

# Deployment
npm run build        # Build for production
npm run deploy       # Deploy to staging/production
```

## External Services & APIs
- **Payment:** [Stripe/PayPal integration details]
- **Email:** [SendGrid/Mailgun setup]
- **Storage:** [AWS S3/Cloudinary configuration]
- **Analytics:** [Google Analytics/Mixpanel setup]

## Helpful Context for Claude
- **Code Review Focus:** Look for performance issues, security vulnerabilities, and maintainability
- **Preferred Patterns:** [Specific design patterns or architectural preferences]
- **Avoid:** [Anti-patterns or things to avoid in this codebase]
- **Documentation Style:** [How you prefer code to be documented]

## Project-Specific Notes
- [Any unique aspects of this project]
- [Special business rules or constraints]
- [Performance requirements or considerations]
- [Security considerations specific to this project]

---
*Last updated: [Date]*
*This file helps Claude understand your project context for better assistance with coding tasks.*