##
## EPITECH PROJECT, 2022
## googleClashCode
## File description:
## main
##

from os import kill
from pprint import pp, pprint
from re import L
import sys
from tkinter.messagebox import NO
from unicodedata import name

from sklearn import pipeline
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

skills = {}

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
            tskill = parceSkill(cmds.pop(0))
            t = tskill["name"]
            if skills.get(t) == None:
                skills[t] = []
            tskill["name"] = contributor["name"]
            skills[t].append(tskill)
    for i in range(nb_project):
        project = parceProject(cmds.pop(0))
        for i in range(project["nb_skills"]):
            project["skills"].append(parceSkill(cmds.pop(0)))
        projects.append(project)

i = 0
imp_project = []
for project in projects:
    for skill in project["skills"]:
        name = skill["name"]
        lvl = skill["lvl"]
        skill = skills.get(name)
        if skill == None:
            imp_project.append(projects.pop(i))
            i -= 1
            break
        b = 0
        for t in skill:
            if t["lvl"] >= lvl:
                b = 1
                break
        if b == 0:
            imp_project.append(projects.pop(i))
            i -= 1
            break
    i += 1

print(i)
# pprint(projects)