from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *

class Welcome(Page): 
    form_model = Player
    form_fields = ['treatment', 'time_start', 'device_type', 'operating_system', 'browser', 'use_of_device']
    
    def before_next_page(self):
        self.participant.vars['treatment'] = self.player.treatment

class Baseline(Page): 
    form_model = Player
    form_fields = []

    def before_next_page(self):
        self.participant.vars['treatment'] = self.player.treatment

class Framing(Page): 
    form_model = Player
    form_fields = []
    
    def before_next_page(self):
        self.participant.vars['treatment'] = self.player.treatment

class PostTreatment(Page): 
    form_model = Player
    form_fields = []
    
    def before_next_page(self):
        self.participant.vars['treatment'] = self.player.treatment

page_sequence = [Welcome] 
