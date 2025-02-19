from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *
import random


class Welcome(Page):
    form_model = Player
    form_fields = ['time_start']
     
        
    def vars_for_template(self):
        return {
            "participant_label": self.participant.label
        }   

class PreTreatment(Page):
    form_model = Player
    form_fields = ['eco_poli_affiliation', 
                   'soci_poli_affiliation', 
                   'concept_freetrade', 
                   'mercosur_freetrade', 
                   'supportive_freetrade',
                   'political_stance_trade', 
                   'trust_institutions', 
                   'interest_politics',
                   'pre_talk_friends',
                   'pre_share_socialmedia',
                   'pre_consider_voting',
                   'pre_support_petition',
                   'pre_attend_protest',
                   'pre_legal_action',
                   'pre_last_vote',
                   'pre_contact_politics',
                   'pre_boycott']

    def before_next_page(self):
        # List of available treatments
        treatments = ['positive_prognostic', 
                      'positive_diagnostic', 
                      'negativ_prognostic', 
                      'negative_diagnostic']

        # Assign a random treatment
        self.participant.vars['assigned_treatment'] = random.choice(treatments)
        self.player.treatment = self.participant.vars['assigned_treatment']


class FramingTreatment(Page):
    form_model = Player
    form_fields = ['time_popout', 'select_proceed']
    
    def vars_for_template(self):
        return {'treatment': self.participant.vars.get('assigned_treatment')} 
    
class Bye(Page):
    form_model = Player
    form_fields = []
    

class ManipulationCheck(Page):
    form_model = Player
    form_fields = ['overall_tone',
                   'impact_time']

class PostTreatment(Page):
    form_model = Player
    form_fields = ['post_talk_friends',
                    'post_share_socialmedia',
                    'post_consider_voting',
                    'post_support_petition',
                    'post_attend_protest',
                    'post_legal_action',
                    'post_next_vote',
                    'post_contact_politics',
                    'post_boycott',
                    'supportive_mercosur',
                    'convincing_arguments',
                    'important_mercosur_state',
                    'important_mercosur_you']


#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                PreTreatment,
                PreTreatmentII,
                FramingTreatment,
                PostTreatment,
                 
                ManipulationCheck,
                Bye]