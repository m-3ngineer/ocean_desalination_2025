import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np

# below you guys can add/remove/edit our major tasks and responsibilities labelled as resource
tasks = [
    {"name": "Project Initiation", "start_week": 1, "duration_weeks": 1, "resource": "All Members", "color": "skyblue", "progress": 0},
    {"name": "Research Phase", "start_week": 2, "duration_weeks": 2, "resource": "All Members", "color": "limegreen", "progress": 0},
    {"name": "System Selection & Analysis", "start_week": 4, "duration_weeks": 2, "resource": "All Members", "color": "gold", "progress": 0},
    {"name": "Design Development", "start_week": 6, "duration_weeks": 2, "resource": "All Members", "color": "orange", "progress": 0},
    {"name": "Preliminary Design", "start_week": 8, "duration_weeks": 2, "resource": "All Members", "color": "red", "progress": 0},
    {"name": "Final Design", "start_week": 9, "duration_weeks": 2, "resource": "All Members", "color": "purple", "progress": 0},
    {"name": "Final Report", "start_week": 10, "duration_weeks": 2, "resource": "All Members", "color": "blue", "progress": 0},
    {"name": "Project Presentation", "start_week": 11.5, "duration_weeks": 1.5, "resource": "All Members", "color": "cyan", "progress": 0}
]

# these milestones/deadlines dont need to be changed
milestones = [
    {"name": "Project Bid Proposal Deadline", "week": 2, "color": "skyblue"},
    {"name": "Project Timeline Deadline", "week": 3, "color": "limegreen"},
    {"name": "Responsibilities Deadline", "week": 4, "color": "gold"},
    {"name": "Preliminary Design Deadline", "week": 9, "color": "red"},
    {"name": "Interim Report Deadline", "week": 6, "color": "orange"},
    {"name": "Final Report Submission Deadline", "week": 12, "color": "blue"},
]

# this basically determines the plot size in pixels
fig, ax = plt.subplots(figsize=(12, 8))
yticks = []
ytick_labels = []

# basic plotting code - ive added a progress syntax for our interim timeline halfway into the semester
for i, task in enumerate(tasks):
    start = task["start_week"]
    duration = task["duration_weeks"]
    progress = task["progress"] / 100 
    yticks.append(i + 1)
    ytick_labels.append(task["name"])

    
    ax.barh(i + 1, duration, left=start, color=task["color"], edgecolor='black', alpha=0.7)

      # once we decide on our responsibilities, this syntax can be used to adjust the names within the rectangle thingies
    text_position = start + duration / 2  #centering
    if text_position + 0.2 > start + duration:  #too far right ---> adjust to left
        text_position = start + duration - 0.2  # move left within the bar

    # format for our names
    ax.text(text_position, i + 1, f"{task['resource']}", va='center', ha='center', fontsize=10, color="black")

# this line plots those little colored dots marking our deadlines (see legend for this lower right corner)
for milestone in milestones:
        ax.scatter(milestone["week"], len(tasks) + 1, color=milestone["color"], zorder=5)

# if you guys need to edit the axis range foor some reason
ax.set_yticks(yticks)
ax.set_yticklabels(ytick_labels, fontsize=10)
ax.set_xticks(range(1, 13)) 
ax.set_xticklabels([f"W{i}" for i in range(1, 13)], rotation=0, fontsize=9)
ax.set_xlabel("Timeline (Weeks)", fontsize=12, fontweight='bold')
ax.set_ylabel("Tasks", fontsize=12, fontweight='bold')
ax.set_title("Gantt Chart: Ocean Water Desalination Project 2025", fontsize=14)

# lower right legend for those little colored dots - you can edit the format of the entire legend over here
milestone_legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=milestone["color"], markersize=10, label=milestone["name"]) for milestone in milestones]
ax.legend(handles=milestone_legend_elements, loc='lower right', fontsize=9, title="Milestones")

# ignore this shit - background shading and grid interval stuff
ax.grid(axis='x', linestyle='--', alpha=0.5)
for i in range(len(tasks)):
    if i % 2 == 0:
        ax.axhspan(i + 0.5, i + 1.5, color='lightgray', alpha=0.2)

plt.suptitle("3A&K ENGINEERING CONSULTANTS", fontsize=18, fontweight='bold', y=0.95)

fig.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.2)

plt.show()
