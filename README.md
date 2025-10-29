# Activity 08: Dictionaries and Git Workflow

## Overview
**Time:** 30 minutes  
**Team Size:** 2-3 students  
**Topic:** Python Dictionaries + Git Branching and Pull Requests

## Learning Objectives
By the end of this activity, you will be able to:
- Create and manipulate Python dictionaries effectively
- Use git branching for collaborative development
- Create and review pull requests on GitHub
- Practice team-based software development workflow

## Setup Instructions

### Step 1: Team Formation and Repository Setup
1. **Form teams** of 2-3 students
2. **Designate one person** as the "Repository Owner"
3. **Repository Owner:** Fork this repository to your GitHub account
4. **Repository Owner:** Add team members as collaborators:
   - Go to Settings → Collaborators → Add people
   - Add your teammates using their GitHub usernames
5. **All team members:** Clone the forked repository locally

### Step 2: Git Workflow Overview
Each team member will work on a **different Python file** using **separate branches**:
- **Person 1:** `student-database` branch → `student_database.py`
- **Person 2:** `inventory-manager` branch → `inventory_manager.py`
- **Person 3:** `grade-calculator` branch → `grade_calculator.py`

*(If you have 2 people, skip the grade calculator file)*

## Tasks

### Task Distribution
**Choose who works on which file:**

#### File 1: Student Database (`student_database.py`)
- **Difficulty:** Beginner
- **Focus:** Basic dictionary operations (create, access, modify)
- **Estimated Time:** 8-10 minutes

#### File 2: Inventory Manager (`inventory_manager.py`)
- **Difficulty:** Intermediate  
- **Focus:** Dictionary methods (keys, values, items, pop)
- **Estimated Time:** 10-12 minutes

#### File 3: Grade Calculator (`grade_calculator.py`)
- **Difficulty:** Advanced
- **Focus:** Nested dictionaries and complex operations
- **Estimated Time:** 12-15 minutes

### Git Workflow Steps

#### Phase 1: Create Branches and Start Work (5 minutes)
1. **Each person** creates their own branch:
   ```bash
   git checkout -b your-branch-name
   # Examples: student-database, inventory-manager, grade-calculator
   ```

2. **Each person** works on their assigned Python file
3. **Complete the TODO comments** in your file
4. **Test your code** to make sure it runs without errors

#### Phase 2: Commit and Push (5 minutes)
1. **Add and commit** your changes:
   ```bash
   git add your_file.py
   git commit -m "Complete [file name] implementation"
   git push origin your-branch-name
   ```

#### Phase 3: Create Pull Requests (10 minutes)
1. **Each person** creates a pull request on GitHub:
   - Go to the forked repository on GitHub
   - Click "Compare & pull request"
   - **Title:** "Complete [File Name] - [Your Name]"
   - **Description:** Briefly describe what you implemented

2. **Team Code Review:**
   - **Each person reviews** the other team members' pull requests
   - **Add comments** if you find any issues or have suggestions
   - **Approve** the pull request if the code looks good

#### Phase 4: Merge and Celebrate (5 minutes)
1. **Repository Owner** merges all approved pull requests
2. **All team members** pull the latest changes:
   ```bash
   git checkout main
   git pull origin main
   ```

## Submission
**Repository Owner** submits the GitHub repository URL with all merged pull requests.

## Grading Criteria
- [ ] All team members successfully created branches
- [ ] All assigned Python files are completed correctly
- [ ] All pull requests were created with proper titles/descriptions
- [ ] Code review comments were provided between team members
- [ ] All pull requests were successfully merged
- [ ] Final repository contains all three working Python files

## Tips for Success
1. **Communicate with your team** about progress
2. **Ask for help** if you get stuck on the Python code
3. **Be constructive** in your code reviews
4. **Test your code** before creating pull requests
5. **Don't worry about perfect code** - focus on completing the tasks

## Git Commands Quick Reference
```bash
# Create and switch to new branch
git checkout -b branch-name

# Check current branch
git branch

# Add changes
git add filename.py

# Commit changes
git commit -m "Descriptive message"

# Push branch to GitHub
git push origin branch-name

# Switch back to main
git checkout main

# Pull latest changes
git pull origin main
```

Good luck and have fun collaborating! 🚀