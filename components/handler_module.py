#!/usr/bin/python3
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from components.files import blueprints as b
import re

class Handler:
    """ This class is processing data about tickets."""
    def __init__(self):
        self._tickets = None
        self._views = None
        self._count = 0
        self._premium = 0
        self._platinum = 0
        self._transfer = 0
        self._unassigned = 0

#======================SETTERS====================GETTERS===================#

    @property
    def tickets(self):
        return self._tickets

    @tickets.setter
    def tickets(self, loaded):
        if 'tickets' in loaded:
            self._tickets = loaded['tickets']
        if 'views' in loaded:
            self._views = loaded['views']

    @property
    def premium_ticket_count(self):
        """Returns premium count of the given view."""
        return self._premium

    @premium_ticket_count.setter
    def premium_ticket_count(self, loaded):
        for i in range(0, self._count):
            if self.support_plan(i) == 'premium':
                self._premium += 1

    @property
    def platinum_ticket_count(self):
        """Returns platinum count of the given view."""
        return self._platinum

    @platinum_ticket_count.setter
    def platinum_ticket_count(self, loaded):
        for i in range(0, self._count):
            if self.support_plan(i) == 'platinum':
                self._platinum += 1

    @property
    def view_ticket_count(self):
        """Returns tickets count of the given view."""
        return self._count

    @view_ticket_count.setter
    def view_ticket_count(self, loaded):
        self._count = loaded['count']
    
    @property
    def divide_ticket_count(self):
        return self._transfer, self._unassigned

    @divide_ticket_count.setter 
    def  divide_ticket_count(self, loaded):
        for i in range(0, self._count):
            if self.group_id(i) == 360002974692:
                self._transfer += 1
            if self.group_id(i) == None:
                self._unassigned += 1

#===========================================================================#
    @property
    def view_in_cmd(self):
        """ This function is viewing the cases in the CMD.
            For testing the code."""
        if self._count is 0:
            print("Queue clear nice!")
        else:
            print("Current number of tickets: {0}".format(self._count))
            for i in range(0,self._count):
                print(self._tickets[i])

    def all_queue_views(self):
        """ This function is preparing a new list of dict that will have
            ID, title and if the ticket is active."""
        _views = []
        for view_number in range(self._count):
            _view = b.view
            _view['id'] = self.view_id(view_number)
            _view['title'] = self.view_title(view_number)
            _view['active'] = self.is_active_view(view_number)
            _views.append(_view)
        return _views

    def get_view(self, view):
        _tickets = []
        for case_number in range(self._count):
            _ticket = []
            if 'Unassigned' == view:
                _ticket.append(self.ticket_id(case_number))
                _ticket.append(self.name_check(self.domain_name(case_number)))
                _ticket.append(self.name_check(self.support_plan(case_number)))
                _ticket.append(self.calculate_delta_time(case_number))
            if 'NotAnswered' == view:
                _ticket.append(self.ticket_id(case_number))
                _ticket.append(self.name_check(self.domain_name(case_number)))
                _ticket.append(self.assignee(case_number))
            _tickets.append(_ticket)
        return _tickets

    def tickets_per_agent(self):
        """ This function is preparing list with numbers of taken/solved cases by agent."""
        (_mosinski, _bremesz, _hgautam,
         _wniekrasz, _jburda) = (0, 0, 0, 0, 0)
        agents_list = [
            _mosinski,     #0
            _bremesz,      #1
            _hgautam,      #2
            _wniekrasz,    #3
            _jburda        #4
            ]
        agents_ids = b.agents_ids
        for case_number in range(self._count):
            for list_id, agent_id in agents_ids.items():
                if agent_id == self.assignee_id(case_number):
                    agents_list[list_id] += 1
        return agents_list

    def calculate_delta_time(self, case_number):
        """"Calculate delta between current time and created time."""
        created_time = datetime.strptime(self.created_at(case_number), '%Y-%m-%dT%H:%M:%SZ').time()
        now = datetime.time(datetime.utcnow().replace(microsecond=0))
        difference_delta = timedelta(hours=now.hour,
                                     minutes=now.minute,
                                     seconds=now.second)\
                         - timedelta(hours=created_time.hour,
                                     minutes=created_time.minute,
                                     seconds=created_time.second)
        return self.date_view(difference_delta.seconds//3600, difference_delta.seconds//60%60)

    def name_check(self, item):
        """Check if ticket contains one or more domain_names/support_plan."""
        if item == None:
            item = '---'
        if ',' in item:
            comma = item.find(',')
            item = item[:comma]
        return item
    
    def assignee(self, case_number):
        """Check who is assignee of the ticket."""
        agents_list = [
            "Mateusz",
            "Bartosz",
            "Harsh",
            "Wojciech",
            "Jakub"
            ]
        agents_ids = b.agents_ids
        for list_id, agent_id in agents_ids.items():
            if agent_id == self.assignee_id(case_number):
                agent = agents_list[list_id]
        return agent
    
    def date_view(self, hours, minutes):
        if hours >= 1:
            alert = '{0}:{1}h'.format(hours, minutes)
        else:
            alert = '{0} mins'.format(minutes)
        return alert

    def created_at(self, case_number):
        return self._tickets[case_number]['created_at']
    
    def assignee_id(self, case_number):
        return self._tickets[case_number]['assignee_id']

    def domain_name(self, case_number):
        return self._tickets[case_number]['custom_fields'][5]['value']
    
    def support_plan(self, case_number):
        return self._tickets[case_number]['custom_fields'][15]['value']
    
    def ticket_id(self, case_number):
        return self._tickets[case_number]['id']
    
    def group_id(self, case_number):
        return self._tickets[case_number]['group_id']
    
    def jira_id(self, case_number):
        return self._tickets[case_number]['custom_fields'][24]['value']
    
    def jira_stat(self, case_number):
        return self._tickets[case_number]['custom_fields'][25]['value']

    def view_id(self, view_number):
        return self._views[view_number]['id']

    def view_title(self, view_number):
        return self._views[view_number]['title']

    def is_active_view(self, view_number):
        return self._views[view_number]['active']


    #JIRA functions

    # def jira_status_view(self):
    #     """ This function is preparing a new list of dict that will
    #         have details about JIRA tickets(number and status)."""
    #     _tickets = []
    #     for case_number in range(self._count):
    #         (jira_number, jira_status) = (self.jira_id(case_number),
    #                                       self.jira_stat(case_number))
    #         if (isinstance(jira_number, str) and 'Waiting For Customer' in jira_status):
    #             jira_ticket = b.jira_ticket
    #             jira_ticket['number'] = jira_number
    #             jira_ticket['status'] = jira_status
    #             _tickets.append(jira_ticket)
    #     return _tickets

    # def jira_not_updated(self):
    #     #TODO:
    #     # Check if ticket was updated lass than 3 days ago
    #     """ This function is preparing a new list of dict that will
    #         have details about JIRA tickets(number and status)."""
    #     jira_tickets = []
    #     for case_number in range(self._count):
    #         jira_number = self.jira_id(case_number)
    #         if isinstance(jira_number, str):
    #             jira_tickets.append(jira_number)
    #     return jira_tickets