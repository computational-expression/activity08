# Activity 08: Halloween Dictionary Practice

## Overview
**Team Size:** 2-3 students  
**Topic:** Python Dictionaries + Git Branching & Pull Requests  
**Theme:** Halloween Fun

Welcome to a Halloween-themed coding activity! You will be creating Python programs using dictionaries while practicing collaborative git workflows. 

## Learning Objectives
By the end of this activity, you will be able to:
- Create and manipulate Python dictionaries
- Use git branching for collaborative development
- Create and review pull requests on GitHub
- Practice team-based software development

## Setup Instructions

### Step 1: Form Your Team
1. **Form teams** of 2-3 students
2. **Designate one person** as the "Repository Keeper"
3. **Repository Keeper:** 
   - Click the GitHub Classroom link provided by your instructor
   - Set up your team name (make it Halloween-themed!)
   - Wait for your team members to join
4. **Team Members:** 
   - Click the same GitHub Classroom link
   - **Join your team** (don't create a new one!)
   - Clone the repository locally

### Step 2: Git Workflow
Each team member will work on a **different Python file** using **separate branches**:
- **Person 1:** `haunted-house` branch → `haunted_house.py`
- **Person 2:** `potion-shop` branch → `potion_shop.py`  
- **Person 3:** `monster-school` branch → `monster_school.py`

*(If you have 2 people, skip the monster school)*

## Tasks

### Choose Your Halloween Assignment:

#### File 1: Haunted House Database (`haunted_house.py`)
- **Focus:** Basic dictionary operations (create, access, modify)
- **Theme:** Manage a database of haunted house residents

#### File 2: Potion Shop Inventory (`potion_shop.py`)
- **Focus:** Dictionary operations (create, access, modify, update)
- **Theme:** Keep track of magical potion ingredients

#### File 3: Monster School Grades (`monster_school.py`)
- **Focus:** Dictionary operations (create, access, modify, calculate)
- **Theme:** Calculate grades for monster students

## Git Workflow Steps

### Phase 1: Create Your Branch & Start Working

**Terminal Method:**
```bash
# Create and switch to your branch
git checkout -b your-branch-name
# Examples: haunted-house, potion-shop, monster-school
```

**VS Code Method:**
1. Click the branch name in the bottom-left corner of VS Code
2. Select "Create new branch..."
3. Name your branch (haunted-house, potion-shop, or monster-school)
4. Press Enter to switch to your new branch

### Phase 2: Work on Your Code
1. **Open your assigned Python file**
2. **Complete the TODO comments** (follow the instructions!)
3. **Test your code** to make sure it works properly
4. **Have fun with the Halloween theme!**

### Phase 3: Commit Your Changes

**Terminal Method:**
```bash
# Add your changes
git add your_file.py

# Commit with a descriptive message
git commit -m "Complete [description] for [file name]"

# Push your branch to GitHub
git push origin your-branch-name
```

**VS Code Method:**
1. Click the Source Control icon (looks like a branch)
2. Click the + next to your file to stage it
3. Write a commit message: "Complete [description] for [file name]"
4. Click the checkmark to commit
5. Click "Publish Branch" or "Push" to send to GitHub

### Phase 4: Create Pull Requests
1. **Go to your GitHub repository**
2. **Click "Compare & pull request"** (should appear after pushing)
3. **Create a pull request:**
   - **Title:** "[Your Name]: Complete [File Theme]"
   - **Description:** 
     ```
     ## What did you implement?
     - [Brief description of what you completed]
     
     ## Testing
     - [x] My code runs without errors
     - [x] All functions work as expected
     ```
4. **Add Reviewers**: one team member other than you

### Phase 5: Code Review
1. **Review your team members' pull requests**
2. **Look for:**
   - Does the code work?
   - Are there any bugs?
   - Any suggestions for improvement?

3. **Leave helpful comments:**
   - "Great work on the haunted house database!"
   - "I found a small bug in line 23 - missing a closing bracket"
   - "Love the creative variable names!"

4. **Approve** when ready (click "Approve" in the review)

### Phase 6: Merge & Celebrate
1. **Repository Keeper** merges all approved pull requests
2. **Everyone** pulls the complete code:

**Terminal Method:**
```bash
git checkout main
git pull origin main
```

**VS Code Method:**
1. Switch back to main branch (click branch name → select main)
2. Click Source Control → Pull (or Sync)

## Submission
**Repository Keeper** submits the GitHub repository URL - make sure all pull requests are merged!

## Grading Criteria
- [ ] All team members successfully created branches
- [ ] All assigned Python files are completed with working code
- [ ] Pull requests have clear titles and descriptions
- [ ] Constructive code review comments were shared between team members  
- [ ] All pull requests were successfully merged into the main repository
- [ ] Final repository contains all working Python files

## Git Commands Quick Reference
```bash
# Create and switch to new branch
git checkout -b branch-name

# Check which branch you're on
git branch

# Add your changes
git add filename.py

# Commit your changes
git commit -m "Descriptive commit message"

# Push branch to GitHub
git push origin branch-name

# Return to main branch
git checkout main

# Pull latest changes
git pull origin main
```

## Tips for Success
1. **Communicate with your team** - help each other debug! 
2. **Don't be afraid to ask for help** - everyone needs assistance sometimes
3. **Be encouraging** in your code reviews - spread Halloween cheer!
4. **Test your code** before creating pull requests
5. **Have fun with the theme** - add Halloween-themed variable names and comments!

Happy Halloween Coding!