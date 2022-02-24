##
## EPITECH PROJECT, 2022
## googleClashCode
## File description:
## main
##

from pprint import pprint
import sys
from typing import Tuple

contributors  = []
projects = []

nb_contributors = 0
nb_projects = 0
cmds = []

def calcScore(time, score, bb, day):
    t = bb - day

    if (t < 0):
        return (t + score - time)
    t -= time
    if (t < 0):
        return (score + t)
    return score

def getBestProject(projects):
    bestScore = 0
    bestTime = 999999
    idxToSave = 0
    day = 0
    for val, project in enumerate(projects):
        tmp = calcScore(project['time'], project['score'], project['best_before'], day)
        print(tmp)
        if bestScore < tmp and bestTime < project['time']:
            bestScore = tmp
            bestTime = project['time']
            idxToSave = val
    return projects[idxToSave]

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
            tskill["skill"] = t
            skills[t].append(tskill)
    for i in range(nb_project):
        project = parceProject(cmds.pop(0))
        for i in range(project["nb_skills"]):
            project["skills"].append(parceSkill(cmds.pop(0)))
        projects.append(project)

def checkIfcan(project):
    for skill in project["skills"]:
        name = skill["name"]
        lvl = skill["lvl"]
        skill = skills.get(name)
        if skill == None:
            return False
        for t in skill:
            if t["lvl"] >= lvl:
                return True
    return False

def removeCan():
    i = 0
    imp_project = []
    for project in projects:
        if  checkIfcan(project):
            i += 1
        else:
            imp_project.append(projects.pop(i))
    return imp_project
jobOccupi = []

def givePeople(project, date: int):
    t = []
    t.append(date + project["time"])
    for skill in project["skills"]:
        name = skill["name"]
        lvl = skill["lvl"]
        skill = skills.get(name)
        if skill == None:
            return False
        i = 0
        for people in skill:
            if people["lvl"] >= lvl:
                skill.pop(i)
                t.append(people)
                break
            i += 1
    return t

def pushIn(projectIn : list, date: int):
    i = 0
    for p in projectIn:
        if date >= p[0]:
            projectIn.pop(i)
            for people in p[1:]:
                skills[people["skill"]].append(people)
        else:
            i += 1

removeProject = removeCan()
day = 0
while (len(project) > 0):
    project = getBestProject(projects)
    jobOccupi.append(givePeople(project, day))
    print(jobOccupi)
    pushIn(jobOccupi, 8)
    for r in removeProject:
        projects.push(r)
    removeProject = removeCan()
    day += 1