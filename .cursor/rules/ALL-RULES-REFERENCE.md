# Cursor IDE Rules Reference Guide - 2026 Best Practices

This reference guide documents all Cursor IDE rule files in the project, detailing their purposes and usage for both React frontend and FastAPI backend development.

## Overview

The Cursor IDE rules establish consistent development practices across the project by defining conventions and standards for various aspects of software development. These rules ensure code quality, reliability, and consistency for both frontend React components and backend FastAPI services.

## Rule File Reference

### 1. React Frontend Development Best Practices
**File**: `react-frontend.mdc`

**Purpose**: Establishes comprehensive React development guidelines with focus on modern patterns, TypeScript integration, performance optimization, and testing practices.

**Key Components**:
- Component structure and file organization with PascalCase naming conventions
- TypeScript usage with proper interfaces and type annotations
- Hook usage best practices with custom hooks and conditional calls
- State management approaches using React built-in state, context, and external libraries
- Performance optimization techniques including memoization, virtualization, and lazy loading
- Accessibility standards with semantic HTML and ARIA attributes
- Error handling with proper error boundaries and user feedback
- Testing practices using React Testing Library with focus on user interactions
- Code documentation following JSDoc conventions
- Environment configuration management best practices

### 2. FastAPI Backend Development Best Practices  
**File**: `fastapi-backend.mdc`

**Purpose**: Defines comprehensive backend development standards for FastAPI applications including code structure, API design, security considerations, testing practices, and performance optimization.

**Key Components**:
- Project structure organization with src/, tests/, docs/ directories
- Type hinting and annotation usage following 2026 best practices
- API design patterns with route organization, response format standards
- Error handling with appropriate HTTP status codes and consistent error objects
- Database integration using SQLAlchemy with proper model definitions and session management
- Security standards including authentication, authorization, and input validation
- Testing practices with pytest, test coverage requirements, and integration testing
- Performance optimization strategies for database queries and caching
- Configuration management with environment variables and Pydantic settings
- API documentation through FastAPI's automatic OpenAPI generation
- Logging and monitoring practices for production reliability

### 3. Production Reliability and Configuration Management
**File**: `production-reliability.mdc`

**Purpose**: Establishes critical standards for production stability, configuration changes, and risk assessment.

**Key Components**:
- Magic number detection and justification requirements for configuration values
- Connection pool management strategies with proper sizing and monitoring
- Security configuration standards including validation of sensitive data
- Risk assessment and change management practices
- Monitoring and observability requirements for critical parameters
- Implementation guidelines with feature flags for risky changes
- Version control and deployment practices

### 4. Testing and Quality Assurance  
**File**: `testing.mdc`

**Purpose**: Defines testing conventions and quality standards for maintaining consistent test coverage and QA practices.

**Key Components**:
- Test organization in dedicated directories with matching component names
- Test writing guidelines with beforeEach/afterEach, proper naming conventions
- Code quality standards including minimum coverage requirements (80%)
- Performance testing practices for API response times and component rendering
- CI/CD integration requirements for automated testing

### 5. Component Development Guidelines
**File**: `components.mdc`

**Purpose**: Establishes consistent patterns for React components, styling, and structure.

**Key Components**:
- React component structure with file naming conventions
- Styling approaches using Tailwind CSS with utility-first methodology
- Best practices for state management, performance optimizations, and accessibility
- Production reliability considerations including parameter validation

### 6. API Routes and Error Handling  
**File**: `api-routes.mdc`

**Purpose**: Establishes consistent structure, response formats, and error management for API routes.

**Key Components**:
- Route organization in src/pages/api/ with kebab-case naming convention
- Route handler patterns with request validation and appropriate error handling
- Response format standards with success flag, data, and error information
- Error handling with HTTP status codes and consistent error object formats

### 7. Database Schema and Query Patterns
**File**: `database.mdc`

**Purpose**: Defines database design and query conventions for consistent schema definition, queries, and data access.

**Key Components**:
- Schema design principles with proper naming conventions and column types
- Query patterns including parameterized queries and transaction usage
- Data access layer using repository pattern with separation of concerns
- Connection pool strategies and configuration standards

### 8. General Code Style and Formatting
**File**: `general.mdc`

**Purpose**: Establishes general code style guidelines enforcing consistent formatting, naming conventions, and code structure.

**Key Components**:
- Code style guidelines with 2-space indentation, semicolons, camelCase
- Naming conventions for variables, functions, classes, and files
- Code structure practices including function size limits and import organization
- Configuration management practices with magic number justification

## Usage Guidelines

1. **File Organization**: All rule files are stored in the `.cursor/rules/` directory
2. **Integration**: Rules are automatically applied by Cursor IDE when working with projects
3. **Updates**: Rule files can be modified directly and will update recommendations immediately
4. **Validation**: These rules help maintain consistency and quality across all developers working on the project

## Benefits

These rule files provide:
- Consistent code style and structure across the team for both frontend and backend
- Improved maintainability through standardization 
- Enhanced production reliability with validation practices and risk assessment
- Better testing coverage through standardized approaches
- Security best practices for configuration management
- Clear conventions for database design, API development, and component structure
- Performance optimization strategies for both React applications and FastAPI services

## Compliance Checklist (2026 Best Practices)

### Frontend Development:
- ✅ Proper TypeScript usage with strict typing
- ✅ Component structure following React best practices
- ✅ Accessibility compliance with semantic HTML
- ✅ Performance optimization techniques implemented
- ✅ Comprehensive testing coverage (80% minimum)
- ✅ Error handling patterns with appropriate user feedback

### Backend Development:
- ✅ API design with clean routes and consistent response formats
- ✅ Database schema following naming conventions and standards
- ✅ Security practices for authentication, authorization, and input validation
- ✅ Error handling with proper status codes and error object structures
- ✅ Configuration management with secure environment variables
- ✅ Testing practices including unit, integration, and performance tests
- ✅ Production-ready documentation and monitoring practices

All rules align with 2026 Cursor IDE best practices for comprehensive software development standards that cover the entire application lifecycle from component design through to production deployment.