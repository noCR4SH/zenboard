#!/usr/bin/python3
from components import call_module
from components import handler_module

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Handler()
    unassigned_raw = unassigned_call.unassigned_queue
    (unassigned_handle.tickets, unassigned_handle.ticket_count,
    unassigned_handle.platinum_count, unassigned_handle.premium_count) = (unassigned_raw, unassigned_raw,
                                                                        unassigned_raw, unassigned_raw)
    unassigned_view = unassigned_handle.get_view('Unassigned')
    return unassigned_handle.ticket_count, unassigned_handle.platinum_count, unassigned_handle.premium_count, unassigned_view

def team_taken():
    call = call_module.ZendeskCall()
    handle = handler_module.Handler()
    raw = call.team_taken
    (handle.tickets, handle.ticket_count) = (raw, raw)
    lista = handle.tickets_per_agent()
    return lista

def team_solved():
    call = call_module.ZendeskCall()
    handle = handler_module.Handler()
    raw = call.team_solved
    (handle.tickets, handle.ticket_count) = (raw, raw)
    ludzie = handle.tickets_per_agent()
    return ludzie

def not_answered_india():
    not_answered_call = call_module.ZendeskCall()
    not_answered_handle = handler_module.Handler()
    not_answered_raw = not_answered_call.not_answered_india
    (not_answered_handle.tickets, not_answered_handle.view_ticket_count) = (not_answered_raw, not_answered_raw)
    not_answered_view_india = not_answered_handle.get_view('NotAnsweredIndia')
    return not_answered_view_india

def not_answered_mtv():
    not_answered_call = call_module.ZendeskCall()
    not_answered_handle = handler_module.Handler()
    not_answered_raw = not_answered_call.not_answered_mtv
    (not_answered_handle.tickets, not_answered_handle.view_ticket_count) = (not_answered_raw, not_answered_raw)
    not_answered_view_mtv = not_answered_handle.get_view('NotAnsweredMTV')
    return not_answered_view_mtv

def not_answered():
    not_answered_call = call_module.ZendeskCall()
    not_answered_handle = handler_module.Handler()
    not_answered_raw = not_answered_call.not_answered
    (not_answered_handle.tickets, not_answered_handle.view_ticket_count) = (not_answered_raw, not_answered_raw)
    not_answered_view = not_answered_handle.get_view('NotAnswered')
    return not_answered_view
# def jira():
#     call = call_module.JiraCall()
#     return call.view_jira_details
#==========================================================================================#
# Variables

(un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()

# Premium and platinum together

ludzie_taken = team_taken()
ludzie_solved = team_solved()
print(ludzie_taken)
print(ludzie_solved)

print(not_answered())
print(not_answered_india())
print(not_answered_mtv)

# case = jira()
# print(case)


#List of unassigned queue

#==========================================================================================#
