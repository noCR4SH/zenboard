from components import call_module
from components import handler_module

from random import random
from time import sleep
from threading import Thread, Event

from flask import Flask, render_template, url_for, copy_current_request_context
from flask_socketio import SocketIO, emit

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Handler()
    unassigned_raw = unassigned_call.unassigned_queue
    (unassigned_handle.tickets, unassigned_handle.view_ticket_count, \
    unassigned_handle.platinum_ticket_count, unassigned_handle.premium_ticket_count, \
    unassigned_handle.divide_ticket_count) = (unassigned_raw, unassigned_raw, \
                                         unassigned_raw, unassigned_raw, unassigned_raw)
    transfer_tickets, unassigned_tickets = unassigned_handle.divide_ticket_count
    unassigned_view = unassigned_handle.get_view('Unassigned')
    return unassigned_handle.platinum_ticket_count, unassigned_handle.premium_ticket_count, unassigned_view, unassigned_tickets, transfer_tickets

def not_answered():
    not_answered_call = call_module.ZendeskCall()
    not_answered_handle = handler_module.Handler()
    not_answered_raw = not_answered_call.not_answered
    (not_answered_handle.tickets, not_answered_handle.view_ticket_count) = (not_answered_raw, not_answered_raw)
    not_answered_view = not_answered_handle.get_view('NotAnswered')
    return not_answered_view

def team_taken():
    call = call_module.ZendeskCall()
    handle = handler_module.Handler()
    raw = call.team_taken
    (handle.tickets, handle.view_ticket_count) = (raw, raw)
    lista = handle.tickets_per_agent()
    return lista

def team_solved():
    call = call_module.ZendeskCall()
    handle = handler_module.Handler()
    raw = call.team_solved
    (handle.tickets, handle.view_ticket_count) = (raw, raw)
    ludzie = handle.tickets_per_agent()
    return ludzie

#============================================================================================================

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnhfakjdgh12345JHSDG'
app.config['DEBUG'] = True

socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

class RequesterThread(Thread):
    def __init__(self):
        self.delay = 5
        super(RequesterThread, self).__init__()

    def post_stats(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            (un_platinum, un_premium, unassigned_list, un_Tickets, trans_Tickets) = unassigned()
            taken_list = team_taken()
            solved_tickets = team_solved()
            (not_answered_view) = not_answered()

            socketio.emit('newstatus', {'un_ticket_count': un_Tickets, 
                                        'un_premium_count': un_premium, 
                                        'un_platinum_count': un_platinum, 
                                        'un_list': unassigned_list, 
                                        'trans_count': trans_Tickets, 
                                        'taken_list': taken_list, 
                                        'solved_list': solved_tickets, 
                                        'not_answered_list': not_answered_view}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.post_stats()

@app.route('/')
def poland_team():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RequesterThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)