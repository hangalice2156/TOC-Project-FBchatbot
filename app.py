from bottle import route, run, request, abort, static_file
from fsm import TocMachine
import os

PORT = os.environ['PORT']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']

machine = TocMachine(
    states=[
        'user',
        'manual',
            'showFSM',
            'help',
            'credits',
            'about',
            'playgame',
                'encounterA',
                'encounterB',
                    'encounterBA',
                        'encounterBAA',
                        'encounterBAB',
                    'encounterBB',
                        'encounterBBA',
                        'encounterBBB',
                'encounterC',
                    'encounterCA',
                    'encounterCB',
                    'encounterCC',
    ],
    transitions=[
        #initailize, enter manual state when user type something
        {
            'trigger': 'wakeup',
            'source': 'user',
            'dest': 'manual'
        },
        #manual advance
        {
            'trigger': 'advance',
            'source': 'manual',
            'dest': 'help',
            'conditions': 'is_going_to_help'
        },
        {
            'trigger': 'advance',
            'source': 'manual',
            'dest': 'credits',
            'conditions': 'is_going_to_credits'
        },
        {
            'trigger': 'advance',
            'source': 'manual',
            'dest': 'showFSM',
            'conditions': 'is_going_to_showFSM'
        },
        {
            'trigger': 'advance',
            'source': 'manual',
            'dest': 'about',
            'conditions': 'is_going_to_about'
        },
        {
            'trigger': 'advance',
            'source': 'manual',
            'dest': 'playgame',
            'conditions': 'is_going_to_playgame'
        },
        ##play game event
        {
            'trigger': 'advance',
            'source': 'playgame',
            'dest': 'encounterA',
            'conditions': 'is_optionA'
        },
        {
            'trigger': 'advance',
            'source': 'playgame',
            'dest': 'encounterB',
            'conditions': 'is_optionB'
        },
        {
            'trigger': 'advance',
            'source': 'playgame',
            'dest': 'encounterC',
            'conditions': 'is_optionC'
        },
        ###options for B
        {
            'trigger': 'advance',
            'source': 'encounterB',
            'dest': 'encounterBA',
            'conditions': 'is_optionBA'
        },
        {
            'trigger': 'advance',
            'source': 'encounterB',
            'dest': 'encounterBB',
            'conditions': 'is_optionBB'
        },
        ###options for C
        {
            'trigger': 'advance',
            'source': 'encounterC',
            'dest': 'encounterCA',
            'conditions': 'is_optionCA'
        },
        {
            'trigger': 'advance',
            'source': 'encounterC',
            'dest': 'encounterCB',
            'conditions': 'is_optionCB'
        },
        {
            'trigger': 'advance',
            'source': 'encounterC',
            'dest': 'encounterCC',
            'conditions': 'is_optionCC'
        },
        ###options for C
        {
            'trigger': 'advance',
            'source': 'encounterC',
            'dest': 'encounterCA',
            'conditions': 'is_optionCA'
        },
        ###options for BA
        {
            'trigger': 'advance',
            'source': 'encounterBA',
            'dest': 'encounterBAA',
            'conditions': 'is_optionBAA'
        },
        {
            'trigger': 'advance',
            'source': 'encounterBA',
            'dest': 'encounterBAB',
            'conditions': 'is_optionBAB'
        },
        
        ###options for BB
        {
            'trigger': 'advance',
            'source': 'encounterBB',
            'dest': 'encounterBBA',
            'conditions': 'is_optionBBA'
        },
        {
            'trigger': 'advance',
            'source': 'encounterBB',
            'dest': 'encounterBBB',
            'conditions': 'is_optionBBB'
        },
        
        #go back to manual
        {
            'trigger': 'advance',
            'source': [
                'user',
                    'help',
                    'credits',
                    'showFSM',
                    'about',
                    'encounterA',
                        'encounterCA',
                        'encounterCB',
                        'encounterCC',
                            'encounterBAA',
                            'encounterBAB',
                            'encounterBBA',
                            'encounterBBB',
            ],
            'dest': 'manual',
            'conditions': 'return_to_manual'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if event.get("message") and event['message'].get("text"):
            if machine.state == 'user':
                machine.wakeup(event)
            else:
                machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
