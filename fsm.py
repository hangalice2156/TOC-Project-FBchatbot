from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_img_message


class TocMachine(GraphMachine):
    #initial
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    #state conditions and events
    ##manual
    def return_to_manual(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'back'
        return False
    
    def on_enter_manual(self, event):
        print("I'm entering manual")

        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/clans/3952729/e33979288a09394314f7a24d8f63e6a9c3d6ebc7.jpg")
        response = send_text_message(sender_id, "Welcom to EVE online mini game o7")
        response = send_text_message(sender_id, "Note: this is unofficial fan page\nCreated for school project with python")
        response = send_text_message(sender_id, "Type one of the following message to continue:\n- demo\n- help\n- credits\n- show fsm\n- about\n- play")
        self.advance(event)
        
    ##demo
    def is_going_to_demo(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'demo'
        return False

    def on_enter_help(self, event):
        print("deemo")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "This is an additional state for deemo, hope its going fine")
        response = send_text_message(sender_id, "type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_help(self, event):
        print('Deemo!')

    ##help
    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def on_enter_help(self, event):
        print("I'm entering help")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "This game is pretty easy,\njust follow the instructions and type something like a,b,c and you can complete the game!")
        response = send_text_message(sender_id, "type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_help(self, event):
        print('Leaving help')

    ##credits
    def is_going_to_credits(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'credits'
        return False
    
    def on_enter_credits(self, event):
        print("I'm entering credits")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "Made by Chuki\nSpecial thanks to CCP games to make wonderful game EVE online o7")
        response = send_text_message(sender_id, "type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_credits(self, event):
        print('Leaving credits')

    ##show FSM
    def is_going_to_showFSM(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'show fsm'
        return False
    
    def on_enter_showFSM(self, event):
        print("I'm entering showFSM")

        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://raw.githubusercontent.com/hangalice2156/TOC-Project-FBchatbot/master/fsm.png")
        response = send_text_message(sender_id, "type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_showFSM(self, event):
        print('Leaving showFSM')
        
    ##about
    def is_going_to_about(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'about'
        return False
    
    def on_enter_about(self, event):
        print("I'm entering about")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "EVE online is an MMOPRG that you can fly various ships across the universe and build your own empire\nhowever I may not put business promotion here")
        response = send_text_message(sender_id, "type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_about(self, event):
        print('Leaving about')
        
        
    ##play game
    def is_going_to_playgame(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'play'
        return False
    
    def on_enter_playgame(self, event):
        print("I'm entering playgame")

        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://s1.1zoom.me/big3/909/341226-Zhenya.jpg")
        response = send_text_message(sender_id, "On the rim of New Eden, out side of the deadspace. Your fleet encountered Burners!\nYou are now fleet commander, we need your order!\noptions: \na. Engage!\nb. Active defence moduls\nc. Retreat!")
        self.advance(event)
        
    def on_exit_playgame(self, event):
        print('Leaving playgame')
        
    ##encounterA
    def is_optionA(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a'
        return False
    
    def on_enter_encounterA(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://evenews24.com/wp-content/uploads/2013/05/dead_owned_wreck.jpg")
        response = send_text_message(sender_id, "You ordered your fleet to engage target, but they are not prepared.\nYour fleet has been destoryed.")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterA(self, event):
        print('Leaving A')
        
    ##encounterB
    def is_optionB(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'b'
        return False
    
    def on_enter_encounterB(self, event):
        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "You ordered your fleet to active shield and armor hardeners, they are now prepared!")
        response = send_text_message(sender_id, "options:\nba. Fire!\nbb. Retreat!")
        self.advance(event)
        
    def on_exit_encounterB(self, event):
        print('Leaving B')
        
    ##encounterC
    def is_optionC(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'c'
        return False
    
    def on_enter_encounterC(self, event):
        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "You tried to active warp drive to escape from battle field, but the burners used warp scrambler toward your fleet.\nyou cannot retreat.")
        response = send_text_message(sender_id, "options:\nca. Fire!\ncb. Retreat!\ncc. Surrender.")
        self.advance(event)
        
    def on_exit_encounterC(self, event):
        print('Leaving C')
        
    ##encounterBA
    def is_optionBA(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'ba'
        return False
    
    def on_enter_encounterBA(self, event):
        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "Your fleet engaged the burners. The burners suffered huge damege, but the condition is not optimistic")
        response = send_text_message(sender_id, "options:\nbaa. Fire!\nbab. Retreat!")
        self.advance(event)
        
    def on_exit_encounterBA(self, event):
        print('Leaving BA')
        
    ##encounterBB
    def is_optionBB(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'bb'
        return False
    
    def on_enter_encounterBB(self, event):
        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "As you found burners are capable to destory your fleet, you ordered retreat. But they webified and warp scrambled your fleet. You cannot escape!")
        response = send_text_message(sender_id, "options:\nbba. Fire!\nbbb. Retreat!")
        self.advance(event)
        
    def on_exit_encounterBB(self, event):
        print('Leaving BB')
        
    ##encounterCA
    def is_optionCA(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'ca'
        return False
    
    def on_enter_encounterCA(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://evenews24.com/wp-content/uploads/2013/05/dead_owned_wreck.jpg")
        response = send_text_message(sender_id, "As you realize you must fight them, it has been too late.\nYour fleet is destoryed!")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterCA(self, event):
        print('Leaving CA')
        
    ##encounterCB
    def is_optionCB(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'cb'
        return False
    
    def on_enter_encounterCB(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://evenews24.com/wp-content/uploads/2013/05/dead_owned_wreck.jpg")
        response = send_text_message(sender_id, "You know that you cannot escape, but you still ordered retreat. You put your fleet into DEATH!")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterCB(self, event):
        print('Leaving CB')
        
    ##encounterCC
    def is_optionCC(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'cc'
        return False
    
    def on_enter_encounterCC(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://1dfq7235s7hdjun832pbscof-wpengine.netdna-ssl.com/wp-content/uploads/2018/10/project-nova-750x445.jpg")
        response = send_text_message(sender_id, "You tried to surrender to keep your fleet alive, but they did not accpet your surrender. your fleet is destoryed")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterCC(self, event):
        print('Leaving CC')
        
    ##encounterBAA
    def is_optionBAA(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'baa'
        return False
    
    def on_enter_encounterBAA(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Eve_Online_-_Empyrean_Age_screenshot.jpg/800px-Eve_Online_-_Empyrean_Age_screenshot.jpg")
        response = send_text_message(sender_id, "Your fleet keeps fireing at burners. Though we lost some ships but victory claimed!")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterBAA(self, event):
        print('Leaving BAA')
        
    ##encounterBAB
    def is_optionBAB(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'bab'
        return False
    
    def on_enter_encounterBAB(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://www.guinnessworldrecords.com/Images/eve-online-1_tcm25-522237.jpg")
        response = send_text_message(sender_id, "You choose to retreat as you think you cannot hold more damege. Thankfully the burners is dameged so that thay cannot stop you from wrapping.\nYour fleet returned safely.")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterBAB(self, event):
        print('Leaving BAB')
        
    ##encounterBBA
    def is_optionBBA(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'bba'
        return False
    
    def on_enter_encounterBBA(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://www.guinnessworldrecords.com/Images/eve-online-1_tcm25-522237.jpg")
        response = send_text_message(sender_id, "You choose to fight back as you cannot escape. After a fierce battle, only few ships returned safely. The burners are eliminated.")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterBBA(self, event):
        print('Leaving BBA')
        
    ##encounterBBB
    def is_optionBBB(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'bbb'
        return False
    
    def on_enter_encounterBBB(self, event):
        sender_id = event['sender']['id']
        send_img_message(sender_id, "http://evenews24.com/wp-content/uploads/2013/05/dead_owned_wreck.jpg")
        response = send_text_message(sender_id, "You choose to retreat again, but all efforts are invain. your fleet has been destoryed.")
        response = send_text_message(sender_id, "Type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_encounterBBB(self, event):
        print('Leaving BBB')
