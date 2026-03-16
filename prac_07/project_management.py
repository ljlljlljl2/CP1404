"""
Project Management Program
Estimate: 60 minutes
Actual:   85 minutes
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Run project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = input(f"{MENU}\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_date = datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
            filter_projects_by_date(projects, filter_date)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        choice = input(f"{MENU}\n>>> ").upper()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ")
    if save_choice.lower() in ("yes", "y"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename, "r") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    """Display projects starting on or after given date."""
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=lambda project: project.start_date)
    for project in filtered_projects:
        print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update completion percentage and/or priority of a selected project."""
    for i, project in enumerate(projects):
        print(i, project)

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


main()