from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "1"
machine = TocMachine(
    states=[
        'user',
        'manual',
        'showFSM',
            'help',
            'credits',
            'about',
            'playgame'
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
        
        #show FSM for each state
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
        
        #go back to manual
        {
            'trigger': 'advance',
            'source': [
                'user',
                    'help',
                    'credits',
                    'showFSM',
                    'about',
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
    run(host="localhost", port=5000, debug=True, reloader=True)
