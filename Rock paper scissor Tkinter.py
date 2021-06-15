class RockPaperScissor:
    def __init__(self,name,options):
        self.name=name
        self.options=options
        

def check_win(human_score,computer_score,current_round):
    global hu
    global co
    global cr
    current_round+=1
    if human_turn==computer_turn:
        result="It's a tie"
    elif human_turn=="rock" and computer_turn=="paper":
        result="You lose"
        computer_score+=1
    elif human_turn=="paper" and computer_turn=="scissor":
        result="You lose"
        computer_score+=1
    elif human_turn=="scissor" and computer_turn=="rock":
        result="You lose"
        computer_score+=1
    elif human_turn=="rock" and computer_turn=="scissor":
        result="You win!"
        human_score+=1
    elif human_turn=="paper" and computer_turn=="rock":
        result="You win"
        human_score+=1
    elif human_turn=="scissor" and computer_turn=="paper":
        result="You win"
        human_score+=1
    
    text_box.insert('insert',"Round "+str(current_round)+'\n')
    text_box.insert('insert',"Player choose: "+human_turn+'\n')
    text_box.insert('insert',"Computer choose: "+computer_turn+'\n')
    text_box.insert('insert',result+'\n')        
    text_box.insert('insert',"Player score: "+str(human_score)+'\n')
    text_box.insert('insert',"Computer score: "+str(computer_score)+'\n'+'\n')
    
    if int(current_round)>=int(rounds):
        text_box.delete('1.0',END)
        text_box.insert('insert',"Game Over "+'\n')
        if int(human_score)>int(computer_score):
            text_box.insert('insert',"You win!"+'\n')
        elif int(human_score)<int(computer_score):
            text_box.insert('insert',"You lose!"+'\n')
        else:
            text_box.insert('insert',"It's a draw"+'\n')
        
        text_box.insert('insert',"Final score:"+'\n')
        text_box.insert('insert',"Player score: "+str(human_score)+'\n')
        text_box.insert('insert',"Computer score: "+str(computer_score)+'\n'+'\n')
        
        
    hu=human_score
    co=computer_score
    cr=current_round


class Computer(RockPaperScissor):
    def make_random_choice(self,options):
        global computer_turn
        computer_turn=random.choice(options)

class Human(RockPaperScissor):
    def make_choice(self,options):
        global human_turn
        human_turn=options

    
def rock():
    opponent.make_random_choice(choices)
    human_turn=choices[0]
    player.make_choice(human_turn)
    h=hu
    c=co
    r=cr
    check_win(h,c,r)

def paper():
    opponent.make_random_choice(choices)
    human_turn=choices[1]
    player.make_choice(human_turn)
    h=hu
    c=co
    r=cr
    check_win(h,c,r)

def scissor():
    opponent.make_random_choice(choices)
    human_turn=choices[2]
    player.make_choice(human_turn)
    h=hu
    c=co
    r=cr
    check_win(h,c,r)

def main():
    global text_box
    
    root.title("Rock Paper Scissor Game")
    root.resizable(False,False)
    
    rock_button=Button(root,text="Rock",bg="#33FFCC",command=rock)
    rock_button.grid(row=1,column=0,padx=10,pady=10)
    
    paper_button=Button(root,text="Paper",bg="#FF99FF",command=paper)
    paper_button.grid(row=1,column=1,padx=10,pady=10)
    
    scissor_button=Button(root,text="Scissor",bg="#66FF66",command=scissor)
    scissor_button.grid(row=1,column=2,padx=10,pady=10)
    text_box=Text(root,bg="#FFFF66",width=50,height=20)
    text_box.grid(row=2,column=0,columnspan=3)
    
    quit_button=Button(root,text="Exit",command=quit)
    quit_button.grid(row=3,column=1)
    
    restart_button=Button(root,text="Restart",command=re_start)
    restart_button.grid(row=3,column=2)
    
def re_start():
    root.destroy()
    start()
def start():
    global h,hu,c,co,r,cr,rounds,choices,root,opponent,player
    root=Tk()
    choices=["rock","paper","scissor"]
    h=0
    c=0
    hu=0
    co=0
    r=0
    cr=0
    rounds=input("How many rounds do you want to play?: ")
    print('\n'*100000)
    opponent=Computer("Computer",choices)
    player=Human("Player",choices)
    main()
    mainloop()
    
if __name__=='__main__':
    from tkinter import *
    import random
    start()
    
