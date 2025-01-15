from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *
import random

#from survey_example_appfolder.HelperFunctions import detect_screenout_age, detect_screenout_eligible, detect_quota


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
                   'trust_government', 
                   'trust_media',
                   'pre_talk_friends',
                   'pre_share_socialmedia',
                   'pre_consider_voting',
                   'pre_support_petition',
                   'pre_attend_protest',
                   'pre_legal_action']

    def before_next_page(self):
        # List of available treatments
        treatments = ['positive', 'neutral', 'negative']

        # Assign a random treatment
        self.participant.vars['assigned_treatment'] = random.choice(treatments)


class FramingTreatment(Page):
    form_model = Player
    form_fields = ['time_popout']
    
    def vars_for_template(self):
        return {'treatment': self.participant.vars.get('assigned_treatment')} 
    


class ManipulationCheck(Page):
    form_model = Player
    form_fields = ['select_proceed', 'describe_tone', 'mentioned_points', 'overall_message']

    # @staticmethod
    # def vars_for_template(player: Player):
    #     randomized_options = random.sample(
    #         Constants.question_options['mentioned_points'],
    #         len(Constants.question_options['mentioned_points'])
    #     )
    #     randomized_options.append("Keiner der oben genannten Punkte")
    #     return {
    #         'points_randomized_options': randomized_options
    #     }

    # @staticmethod
    # def error_message(player: Player, values):
    #     if 'mentioned_points' in values and values['mentioned_points']:
    #         selected_options = values['mentioned_points'].split(',')
    #         if len(selected_options) > 2:
    #             return 'Bitte wählen Sie maximal 2 Optionen aus.'
            


class PostTreatment(Page):
    form_model = Player
    form_fields = ['supportive_mercosur',
                    'relevant_mercosur',
                    'concerns_mercosur', 
                    'other_concerns_mercosur',
                    'positive_impact_mercosur',
                    'other_positive_impact_mercosur',
                    'aspect_mercosur',
                    'other_aspect_mercosur',
                    'post_talk_friends',
                    'post_share_socialmedia',
                    'post_consider_voting',
                    'post_support_petition',
                    'post_attend_protest',
                    'post_legal_action' ]

    def error_message(self, values):
        # Parse the selected options
        concern_selected_options = values.get('concerns_mercosur', '[]')
        concern_selected_list = json.loads(concern_selected_options) if concern_selected_options else []

        # Check the number of selected options
        if len(concern_selected_list) > 2:
            return "Bitte wählen Sie maximal 2 Optionen aus."
                
        positive_selected_options = values.get('positive_impact_mercosur', '[]')
        positive_selected_list = json.loads(positive_selected_options) if positive_selected_options else []

        # Check the number of selected options
        if len(positive_selected_list) > 2:
            return "Bitte wählen Sie maximal 2 Optionen aus."
        

        aspect_selected_options = values.get('aspect_mercosur', '[]')
        aspect_selected_list = json.loads(aspect_selected_options) if aspect_selected_options else []

        # Check the number of selected options
        if len(aspect_selected_list) > 2:
            return "Bitte wählen Sie maximal 2 Optionen aus."





#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                PreTreatment,
                FramingTreatment,
                ManipulationCheck,
                PostTreatment]
