# Intro to Modern App dev - Lecture **1**

## Lecture summary:

1. Intro to the subject
2. HTML
3. CSS
4. Git

## Using Git

Git is a version control system. GitHub is a platform built on top of git to store and manage code remotely.

### How to use Git - the basic setup

1. Ideally, you should set up git at the start of your project. 
2. It's fine if you do it midway; but be mindful of sensitive information (API KEYS, SECRETS, etc)
3. To initialize a git repository, run `git init` from the terminal / cmd. Make sure you do so from the root directory of your project
4. After changes are made, use `git status`. This shows all the newly created files, modifications and untracked changes.
5. Create a **.gitignore** file in the root. List all sensitive / unnecessary files (.env, logs, \_\_pycache\_\_, etc.). This prevents from tracking and commiting this information. **VERY IMPORTANT STEP!**
6. To save the changes, there is a 2 step process. First run, `git add <file_path>`. This sets up the specified file/module in the staging environment. To stage all the changes, run `git add .`
7. Next step is to commit the staged changes. Run `git commit -m "<commit_message>"`. Please use meaningful commit messages. These will help a lot in the future of a complex project.
8. To see all commits, use `git log`. This shows all the commits that have been made so far, along with the author, timestamp, commit ID. To see a smaller summary use `git log --oneline`


This is all you need to get started with git. We will cover connecting with remote GitHub repos later as we work through our projects. More advanced concepts like branches, pull requests, merge conflicts.

## HTML - The Web Skeleton

Nothing much here. We covered some basic HTML tags and concepts.

* HTML as a markup language
* `<head>`, `<link>`,`<meta>` tags as the basic setup
* Design tags such as
> * div
> * h1-h6 - heading tags
> * p - paragraph
> * img
> * a - anchor / link tags
> * table, td, th, tr - table tags
> * ol - ordered lists \ ul - unordered lists \ li - list item
> * form
* `<style>` `<script>` tags
* Attributes - Id, class

## CSS - The Design

CSS / Cascading Style Sheets

* Inline, style, external CSS
* CSS selectors

More CSS later. The torture never ends :)






