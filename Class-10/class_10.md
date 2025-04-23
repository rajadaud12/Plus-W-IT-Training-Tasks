## PLUS W - IT Training
*Date: March 29, 2025*

---

## Class 10: How to Test Any Application to Maintain Quality in Japan

### Acknowledgement
- Supported by **AOTS** and **OEC**
- **Ministry of Economy, Trade and Industry**
- **Overseas Employment Corporation**

---

## 1. Recap of Last Week
- Control and loop statements
- Linear algebra in NumPy
- Data inspection
- Importance of Requirement Analysis
- Case studies on requirement analysis
- Linear/Multi-Linear Regression, SVM, Cost Function

---

## 2. Today’s Focus
- Importance of Requirement Analysis
- Case studies on requirement analysis
- Steps of the testing process
- Types of testing (unit, integration, etc.)
- Test-Driven Development (TDD): Red-Green-Refactor
- Quiz and Q&A

---

## 3. Software Development Life Cycle (SDLC)
A structured process for software development:
1. **Requirement Analysis**: Gather requirements, define scope
2. **Planning**: Timeline, cost, risks
3. **Design**: Architecture, UI/UX, database
4. **Development**: Code with best practices
5. **Testing**: Unit, integration, system tests
6. **Deployment**: Release to production
7. **Maintenance**: Monitor and update

---

## 4. Software Testing
Evaluates software to ensure quality:
- Identifies defects, improves performance/security
- Manual or automated
- Uses Requirement Traceability Matrix (RTM)
- **Task 1**: SDLC Maze Adventure  
  [Link](https://codepen.io/Mise-Academy/full/zxYWKxp)

---

## 5. Testing Process
1. **Requirement Analysis**: Understand needs (e.g., secure login)
2. **Test Planning**: Define scope/types (e.g., e-commerce testing)
3. **Test Case Development**: Positive/negative cases (e.g., "Add to Cart")
4. **Test Environment Setup**: Mimic real conditions
5. **Test Execution**: Run and verify results
6. **Defect Reporting**: Log bugs (e.g., in JIRA)
7. **Test Closure**: Summarize findings

---

## 6. Types of Testing
- **Unit Testing**: Individual components (e.g., smoke, regression)
- **Integration Testing**: Module compatibility (e.g., performance)
- **System Testing**: Full system (e.g., security)
- **Acceptance Testing**: Meets business needs

---

## 7. Test-Driven Development (TDD)
Write tests before code:
- **Red**: Failing test (e.g., `assert add(2, 3) == 5`)
- **Green**: Minimal code (e.g., `return a + b`)
- **Refactor**: Optimize (e.g., add validation)

### Case Example: Email Validation
- **Red**: Test valid/invalid emails
- **Green**: Simple check (e.g., `@` presence)
- **Refactor**: Use regex (`/^[^\s@]+@[^\s@]+\.[^\s@]+$/`)

---

## 8. Benefits of TDD
- Ensures correctness early
- Reduces debugging time
- Encourages modular code
- Improves collaboration

---

## 9. Interactive Task
- **Task 2**: Software Testing & TDD Game  
  [Link](https://codepen.io/Mise-Academy/full/yyLRLwR)

---
