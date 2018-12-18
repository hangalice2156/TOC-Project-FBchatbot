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
        send_text_message(sender_id, "Welcom to EVE online mini game o7")
        send_text_message(sender_id, "Note: this is unofficial fan page\nCreated for school project with python")
        send_text_message(sender_id, "Type one of the following message to continue:\n- help\n- credits\n- show fsm\n- about\n- play")
        self.advance(event)
        
    ##help
    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def on_enter_help(self, event):
        print("I'm entering help")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "This game is pretty easy,\njust follow the instructions and type something like a,b,c and you can complete the game!")
        send_text_message(sender_id, "type: back\nto return to manual")
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
        send_text_message(sender_id, "Made by Chuki\nSpecial thanks to CCP games to make wonderful game EVE online o7")
        send_text_message(sender_id, "type: back\nto return to manual")
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
        send_text_message(sender_id, "type: back\nto return to manual")
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
        send_text_message(sender_id, "EVE online is an MMOPRG that you can fly various ships across the universe and build your own empire\nhowever I may not put business promotion here")
        send_text_message(sender_id, "type: back\nto return to manual")
        self.advance(event)
        
    def on_exit_about(self, event):
        print('Leaving about')
        
        
    ##play game
    def is_going_to_playgame(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'play'
        return False
