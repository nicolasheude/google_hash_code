##
## EPITECH PROJECT, 2022
## googleClashCode
## File description:
## main
##

from pprint import pp, pprint
import sys
contributors  = []
projects = []

nb_contributors = 0
nb_projects = 0
cmds = []

def parceSkill(skill: str):
    t = skill.split(" ")
    return {"name": t[0], "lvl": int(t[1])}

def parceProject(project: str):
    t = project.split(" ")
    return {"name": t[0], "time": int(t[1]), "score": int(t[2]), "best_before": int(t[3]), "nb_skills": int(t[4]), "skills": []}

def parceContributor(contributer: str):
    t = contributer.split(" ")
    return {"name": t[0], "nb_skills": int(t[1]), "skills": []}

if len(sys.argv) != 2:
    print("need 1 file")
    sys.exit(-1)

with open(sys.argv[1]) as f:
    for line in f:
        cmds.append(line[0:-1])
    t = cmds[0].split(" ")
    nb_contributors = int(t[0])
    nb_project = int(t[1])
    cmds.pop(0)
    for i in range(nb_contributors):
        contributor = parceContributor(cmds.pop(0))
        for i in range(contributor["nb_skills"]):
            contributor["skills"].append(parceSkill(cmds.pop(0)))
        contributors.append(contributor)
    for i in range(nb_project):
        project = parceProject(cmds.pop(0))
        for i in range(project["nb_skills"]):
            project["skills"].append(parceSkill(cmds.pop(0)))
        projects.append(project)