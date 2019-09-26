#!/usr/bin/python3
"""List of view available in zendesk(dict format)."""
main_path = 'https://egnyte.zendesk.com/api/v2/views'
view_unassigned = {
    "id":461492,
    "title":"Unassigned tickets"
    }
view_l2 = {
    "id":32740742,
    "title":"UNASSIGNED - LEVEL II"
    }
view_transfers = {
    "id":360068419072,
    "title":"Case Transfers"
    }
view_pending = {
    "id":558389,
    "title":"My Pending Tickets"
    }
view_poznan = {
    "id":360053215891,
    "title":"Poznan Support Cases"
    }
view_open = {
    "id":461487,
    "title":"My Open tickets"
    }
view_team_taken = {
    'id':360110425272,
    'title':'Team tickets taken last 12h',
    }
view_team_solved = {
    'id':360110564031,
    'title':'Team tickets solved last 12h',
    }
view_not_answered = {
    'id':360110427952,
    'title':'Not answered greater than 48hours'
    }

view_not_answered_mtv = {
    'id': 360112957472,
    'title': 'MTV - Not answered greater than 48hours'
}
# Add new views below in the same configuration.