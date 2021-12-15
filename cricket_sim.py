import random

Pak={
       
       'Muhammad Rizwan':{'runs':0,'balls_faced':0,'play_status':True},
       'Babar Azam':{'runs':0,'balls_faced':0,'play_status':True},
       'Fakhar Zaman':{'runs':0,'balls_faced':0,'play_status':True},
       'Muhammad Hafeez':{'runs':0,'balls_faced':0,'play_status':True},
       'Shoaib Malik':{'runs':0,'balls_faced':0,'play_status':True},
       'Asif Ali':{'runs':0,'balls_faced':0,'play_status':True},
       'Shadab Khan':{'runs':0,'balls_faced':0,'play_status':True},
       'Imad Wasim':{'runs':0,'balls_faced':0,'play_status':True},
       'Hassan Ali':{'runs':0,'balls_faced':0,'play_status':True},
       'Shaheen Afridi':{'runs':0,'balls_faced':0,'play_status':True},
       'Total':{'runs':0,'balls_faced':0,'play_status':False}
       
       
}



Ind={
       
       'KL Rahul':{'runs':0,'balls_faced':0,'play_status':True},
       'Rohit Sharma':{'runs':0,'balls_faced':0,'play_status':True},
       'Virat Kohli':{'runs':0,'balls_faced':0,'play_status':True},
       'Suryakumar Yadav':{'runs':0,'balls_faced':0,'play_status':True},
       'Rishabh Pant':{'runs':0,'balls_faced':0,'play_status':True},
       'Ravindra Jadeja':{'runs':0,'balls_faced':0,'play_status':True},
       'Hardik Pandya':{'runs':0,'balls_faced':0,'play_status':True},
       'Bhuvneshwar Kumar':{'runs':0,'balls_faced':0,'play_status':True},
       'Muhammad Shami':{'runs':0,'balls_faced':0,'play_status':True},
       'Jasprit Bumrah':{'runs':0,'balls_faced':0,'play_status':True},
       'Total':{'runs':0,'balls_faced':0,'play_status':False}
       
    
}



ball_outcomes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,4,4,4,6,6,"wide","no_ball","out"]

teams=["Pakistan","India"]
Choice=["Batting","Bowling"]

target=0


def faced_ball(team,n):
    ball=random.choice(ball_outcomes)
    
    if ball==0:
        team[n]['runs']=team[n]['runs']+0
        team['Total']['runs']=team['Total']['runs']+0
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1        
    elif ball==1:
        team[n]['runs']=team[n]['runs']+1
        team['Total']['runs']=team['Total']['runs']+1
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1
    elif ball==2:
        team[n]['runs']=team[n]['runs']+2
        team['Total']['runs']=team['Total']['runs']+2
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1
    elif ball==3:
        team[n]['runs']=team[n]['runs']+3
        team['Total']['runs']=team['Total']['runs']+3
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1
    elif ball==4:
        team[n]['runs']=team[n]['runs']+4
        team['Total']['runs']=team['Total']['runs']+4
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1
    elif ball==6:
        team[n]['runs']=team[n]['runs']+6
        team['Total']['runs']=team['Total']['runs']+6
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1
    elif ball=="wide":
        team[n]['runs']=team[n]['runs']+1
        team['Total']['runs']=team['Total']['runs']+1
        team[n]['balls_faced']=team[n]['balls_faced']+0
        team['Total']['balls_faced']=team['Total']['balls_faced']+0
    elif ball=="no_ball":
        team[n]['runs']=team[n]['runs']+1
        team['Total']['runs']=team['Total']['runs']+1
        team[n]['balls_faced']=team[n]['balls_faced']+0
        team['Total']['balls_faced']=team['Total']['balls_faced']+0
    elif ball=="out":
        team[n]['runs']=team[n]['runs']+0
        team['Total']['runs']=team['Total']['runs']+0
        team[n]['balls_faced']=team[n]['balls_faced']+1
        team['Total']['balls_faced']=team['Total']['balls_faced']+1
        team[n]['play_status']=False
    
        

def inning(team):
    for i in team:
        while team[i]['play_status']==True and team['Total']['balls_faced']<120:
            faced_ball(team,i)
            if team['Total']['balls_faced']>=120:
                break
    return team['Total']['runs']



def inning2(team,Target):
    for i in team:
        while team[i]['play_status']==True and team['Total']['balls_faced']<120 and team['Total']['runs'] <= Target+1:
            faced_ball(team,i)
            if team['Total']['balls_faced']>=120 or team['Total']['runs'] >= Target+1:
                break
    return team['Total']['runs']



def toss(Pak,Ind):
    toss_w=random.choice(teams)
    decision=random.choice(Choice)
    
    global target
    
    if toss_w=="Pakistan":
        if decision=="Batting":
            print("Pakistan Won the Toss and Chose to Bat\n\n")
            target = inning(Pak)
            print("\n\n",Pak)
            print("\n\nThe Target is",target+1)
            inning2(Ind,target)
            print("\n\n",Ind)
        else:
            print("Pakistan Won the Toss and Chose to Bowl\n\n")
            target = inning(Ind)
            print(Ind)
            print("\n\nThe Target is",target+1)
            inning2(Pak,target)
            print("\n\n",Pak)
    elif toss_w=="India":
        if decision=="Batting":
            print("India Won the Toss and Chose to Bat\n\n")
            target = inning(Ind)
            print("\n\n",Ind)
            print("\n\nThe Target is",target+1)
            inning2(Pak,target)
            print("\n\n",Pak)
        else:
            print("India Won the Toss and Chose to Bowl\n\n")
            target = inning(Pak)
            print("\n\n",Pak)
            print("\n\nThe Target is",target+1)
            inning2(Ind,target)
            print("\n\n",Ind)
 
            
            
toss(Pak,Ind)



if Pak['Total']['runs']>Ind['Total']['runs']:
    print("\n\nPakistan WON")
elif Pak['Total']['runs']==Ind['Total']['runs']:
    print("\n\nDRAW")
else:
    print("\n\nIndia WON")