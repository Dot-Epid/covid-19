import requests

def getreq():
    data = requests.get("https://api.rootnet.in/covid19-in/stats/latest")
    data = data.json()
    return data
def getsummary():
    data=getreq()
    cases=data['data']
    summary=cases['summary']
    return summary
def statelist():
    statelist=[]
    data=getreq();
    cases=data['data']
    regional=cases['regional']
    for state in regional:
        loc=state['loc']
        statelist.append(loc) 
    return statelist

def confirmcases():
    confirmcaseslist=[]
    data=getreq();
    cases=data['data']
    regional=cases['regional']
    for state in regional:
        confirmedCasesIndian=state['confirmedCasesIndian']
        confirmedCasesForeign=state['confirmedCasesForeign']
        confirmcases=confirmedCasesForeign+confirmedCasesIndian
        confirmcaseslist.append(confirmcases)
    return confirmcaseslist

def deathcases():
    deathcaseslist=[]
    data=getreq();
    cases=data['data']
    regional=cases['regional']
    for state in regional:
        deaths=state['deaths']
        deathcaseslist.append(deaths)
    return deathcaseslist

def dischargedcases():
    dischargedcaseslist=[]
    data=getreq();
    cases=data['data']
    regional=cases['regional']
    for state in regional:
        discharged=state['discharged']
        dischargedcaseslist.append(discharged)
    return dischargedcaseslist