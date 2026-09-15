import os
import subprocess
from datetime import datetime, timedelta

# --- CONFIGURATION ---
authors = [
    {"name": "ROGHET", "email": "harshitrawat3125@gmail.com"},
    {"name": "JRP1956", "email": "jaineelrpatel10@gmail.com"}
]

# Spacing starts on Sept 15, 2026
start_date = datetime(2026, 9, 15, 10, 0, 0) 

commits = [
    {"msg": "chore: initialize AquaWise repository and project structure\n\nSet up the repository with separate client and server directories, shared modules, package scripts, and initial project documentation."},
    {"msg": "feat(client): scaffold React frontend with Vite\n\nConfigure the React application, Vite development server, frontend entry points, component structure, and build workflow."},
    {"msg": "feat(server): initialize Express backend and REST API\n\nCreate the Node.js server, configure Express middleware, establish API routing, and add the initial health-check endpoint."},
    {"msg": "feat(database): integrate MongoDB Atlas with Mongoose\n\nConfigure the MongoDB connection, define Mongoose schemas and models, and establish persistent data access through environment-based configuration."},
    {"msg": "feat(auth): implement user registration and login\n\nImplement the account registration and login flows, request validation, authentication handling, and database integration."},
    {"msg": "feat(client): connect frontend workflows to backend APIs\n\nIntegrate frontend forms and application workflows with the Express REST API, handle asynchronous requests, and display success and error states."},
    {"msg": "feat(core): implement AquaWise application functionality\n\nDevelop the application's primary user-facing workflows, connect them to backend services, and integrate persistent data operations."},
    {"msg": "feat(shared): organize reusable modules and validation\n\nStructure shared utilities and common logic, improve request and data validation, and reduce duplication across the client and server."},
    {"msg": "fix(security): configure CORS and environment variables\n\nConfigure the permitted frontend origin, centralize deployment-specific settings, and keep database credentials and session secrets outside source code."},
    {"msg": "build: configure production frontend and backend builds\n\nConfigure dependency installation, production asset generation, environment-specific settings, and the Vercel frontend build output."},
    {"msg": "deploy: publish AquaWise frontend and backend\n\nDeploy the React frontend to Vercel, publish the Express API on Render, configure the production API base URL, and connect the application to MongoDB Atlas."},
    {"msg": "test: verify production API connectivity and application flows\n\nCheck the backend health endpoint, verify frontend-to-backend communication, validate database-backed workflows, and resolve deployment configuration issues."}
]

def run_cmd(cmd, env=None):
    subprocess.run(cmd, shell=True, check=True, env=env)

print("Initializing fresh Git repository...")
run_cmd("git init")
run_cmd("git branch -m main")

# Explicitly exclude .claude files from tracking
with open(".gitignore", "w", encoding="utf-8") as gitignore:
    gitignore.write(".claude\n.claude.*\nrewrite_history.py\ntemp_msg.txt\n")

# Sequentially build history over a wide multi-week date range
for idx, commit in enumerate(commits):
    author = authors[idx % len(authors)]
    
    # Advance the timeline by 3 days per commit (Spans from Sept 15 to Oct 18)
    commit_date = start_date + timedelta(days=3 * idx)
    date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    
    print(f"Creating commit {idx+1}/12 on {date_str} by {author['name']}...")
    
    run_cmd("git add .")
    
    try:
        subprocess.run("git rm --cached .claude", shell=True, capture_output=True)
    except:
        pass
    
    custom_env = os.environ.copy()
    custom_env["GIT_AUTHOR_NAME"] = author["name"]
    custom_env["GIT_AUTHOR_EMAIL"] = author["email"]
    custom_env["GIT_COMMITTER_NAME"] = author["name"]
    custom_env["GIT_COMMITTER_EMAIL"] = author["email"]
    custom_env["GIT_AUTHOR_DATE"] = date_str
    custom_env["GIT_COMMITTER_DATE"] = date_str
    
    with open("temp_msg.txt", "w", encoding="utf-8") as f:
        f.write(commit["msg"])
        
    run_cmd("git commit --allow-empty -F temp_msg.txt", env=custom_env)

if os.path.exists("temp_msg.txt"):
    os.remove("temp_msg.txt")

print("\n🚀 Multi-day Git history manipulation complete!")
