from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    currency_range,
)
import random 

author = 'group 2'
doc = 'Goal: social movement'

class Constants(BaseConstants):
    name_in_url = 'survey-group2'
    players_per_group = None
    num_rounds = 1
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
        framing = models.StringField(choices=['positive_diagnostic', 'positive_prognostic', 'negative_diagnostic', 'negative_prognostic'])
    

class Player(BasePlayer):
    time_start = models.StringField(initial="-999")
    
    # Keep political attributes in Pretest or move to Demographics?
    eco_poli_affiliation = models.IntegerField(
        label="<b>Wie ist Ihre politische Einstellung in wirtschaftlichen Fragen?</b> <i>(1: Links, Umverteilung, Sozialistisch bis 10: Konservativ, offene liberale Märkte)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )
    soci_poli_affiliation = models.IntegerField(
        label="<b>Wie ist Ihre politische Einstellung in gesellschaftlichen Fragen?</b> <i>(1: Liberal bezüglich Lebensstile/Kulturen bis 10: Konservativ, traditionelle Familienwerte)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )
    
    # Pre-Treatment 
    concept_freetrade = models.IntegerField(
        label="<b>Wie vertraut sind Sie mit dem Konzept von Freihandelsabkommen?</b> <i>(1: Gar nicht vertraut bis 10: Sehr vertraut)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )

    mercosur_freetrade = models.IntegerField(
        label="<b>Wie vertraut sind Sie mit dem Mercosur-Freihandelsabkommen?</b> <i>(1: Gar nicht vertraut bis 10: Sehr vertraut)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )

    supportive_freetrade = models.IntegerField(
        label="<b>Wie unterstützend stehen Sie im Allgemeinen Freihandelsabkommen gegenüber?</b> <i>(1:Gar nicht unterstützend bis 10:Sehr unterstützend))</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )

    political_stance_trade = models.IntegerField(
        label="<b>Wie würden Sie Ihre politische Haltung zu Handelsabkommen, einschließlich Mercosur, beschreiben?</b>",
        choices=[(1, 'Sehr progressiv'),
            (2, 'Progressiv'),
            (3, 'Moderat'),
            (4, 'Konservativ'),
            (5, 'Sehr konservativ')],
        widget=widgets.RadioSelect,        
    )

    trust_institutions = models.IntegerField(
        label="<b>Wie sehr vertrauen Sie Institutionen (z. B. Regierung, Medien), um faire und genaue Informationen über Handelsabkommen bereitzustellen?</b> <i>(1: Überhaupt nicht bis 10: Vollständig)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )

    interest_politics = models.IntegerField(
        label="<b>Wie interessiert sind Sie im Allgemeinen an Politik?</b> <i>(1:Sehr interessiert bis 10:Gar nicht interessiert)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )

    ##Neue seite
    pre_talk_friends = models.IntegerField(
        label="• Mit Freunden oder der Familie darüber gesprochen:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    pre_share_socialmedia = models.IntegerField(
        label="• Ihre Meinung in sozialen Medien geteilt:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_consider_voting = models.IntegerField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigt:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_support_petition = models.IntegerField(
        label="• Eine Online-Petition unterstützt:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_attend_protest = models.IntegerField(
        label="• An einer Demonstration oder einem Protest teilgenommen:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_legal_action = models.IntegerField(
        label="• Rechtliche Schritte etwa in Form einer Sammelklage eingeleitet:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_last_vote = models.IntegerField(
        label="•  Bei der letzten Bundestagswahl gewählt:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )    
    pre_contact_politics = models.IntegerField(
        label="•  Einen Politiker oder einen offizielles Mitglied der Regierung  kontaktiert:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_boycott = models.IntegerField(
        label="•  Bestimmte Produkte boykottiert:",
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [0, "Trifft nicht zu"]
        ],
        widget=widgets.RadioSelectHorizontal
    )    


## Framing Treatment Page
    #assigned_treatment = models.StringField()
    treatment = models.StringField()
    time_popout = models.StringField(initial='-999',blank=True)

    select_proceed = models.BooleanField(
    blank=False,
    label="<b>Um zu bestätigen, dass Sie den Text gelesen haben, wählen Sie bitte 'Nein' aus.</b>", #to be changed not a fan of this type of question 
    choices=[
        [True, "Ja"],
        [False, "Nein"]
    ],
    widget=widgets.RadioSelectHorizontal
    )

    
## posttreatment page
    #Wie wahrscheinlich ist es, dass Sie eine der folgenden Handlungen durchführen in Bezug auf das Mercosur Handelsabkommen?
    post_talk_friends = models.IntegerField(
        label="• Mit Freunden oder der Familie darüber sprechen: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>" ,
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    post_share_socialmedia = models.IntegerField(
        label="• Ihre Meinung in sozialen Medien teilen: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    ) 
    post_consider_voting = models.IntegerField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigen: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    
    post_support_petition = models.IntegerField(
        label="• Eine Online-Petition unterstützten: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    post_attend_protest = models.IntegerField(
        label="• An einer Demonstration oder einem Protest teilnehmen: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    post_legal_action = models.IntegerField(
        label="• Rechtliche Schritte etwa in Form einer Sammelklage einleiten: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    post_next_vote = models.IntegerField(
        label="• Bei der nächsten Bundestagswahl wählen: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    post_contact_politics = models.IntegerField(
        label="• Einen Politiker oder einen offizielles Mitglied der Regierung  kontaktieren: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    post_boycott = models.IntegerField(
        label="• Bestimmte Produkte boykottieren: <i>1:Sehr Unwahrscheinlich bis 10:Sehr wahrscheinlich [zusätzlich 0 „Nicht sicher“]</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal
    )
    
    ##neue seite
    supportive_mercosur = models.IntegerField(
        label="<b>Wie unterstützend stehen Sie nach dem Lesen der Beschreibungen dem Mercosur-Abkommen gegenüber?</b> <i>(1:Gar nicht unterstützend bis 10:Sehr unterstützend))</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )
    convincing_arguments = models.IntegerField(
        label="<b>Wie überzeugend fanden Sie die vorgelegten Argumente?</b> <i>(1: Nicht überzeugend bis 10: Sehr überzeugend)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )
    important_mercosur_state = models.IntegerField(
        label="<b>Wie wichtig halten Sie das Mercosur-Abkommen für die wirtschaftliche Entwicklung der Mitgliedsstaaten?</b> <i>(1: Nicht wichtig bis 10: Sehr wichtig)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )  
    important_mercosur_you = models.IntegerField(
        label="<b>Wie wichtig ist das Mercosur-Abkommen für Sie persönlich und für Bürger wie Sie?</b> <i>(1: Nicht wichtig bis 10: Sehr wichtig)</i>",
        choices=[(i, str(i)) for i in range(1, 11)],
        #widget=widgets.RadioSelectHorizontal,
    )  

## Manipulation Checks 
    overall_tone = models.StringField(
        label="<b>Wie war der allgemeine Ton der Beschreibung, die Sie über das Mercosur-Abkommen gelesen haben?</b>",
        choices=[(1,"Überwiegend positiv"), 
                 (2,"Neutral"), 
                 (3,"Überwiegend negativ"), 
                 (0,"Unklar")],
        widget=widgets.RadioSelect,
    )
    impact_time = models.StringField(
        label="<b>Hat sich die Beschreibung, die Sie gelesen haben, mehr auf aktuelle Auswirkungen oder auf zukünftige Möglichkeiten konzentriert?</b>",
        choices=[(1,"Aktuelle Auswirkungen"), 
                 (2,"Zukünftige Möglichkeiten"), 
                 (0,"Keines von beiden")],
        widget=widgets.RadioSelect,
    )
    