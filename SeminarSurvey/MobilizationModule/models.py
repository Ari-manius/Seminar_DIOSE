from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random 

author = 'group 2'
doc = 'Goal: social movement'

class Constants(BaseConstants):
    name_in_url = 'survey-group2'
    players_per_group = None
    num_rounds = 1
    question_options = {
        'mentioned_points': [
            "Das Abkommen wird das Wirtschaftswachstum fördern und Arbeitsplätze schaffen.",
            "Das Abkommen zielt darauf ab, die Kosten für Verbraucher zu senken.",
            "Kritiker warnen vor erhöhtem Wettbewerb für lokale Industrien.",
        ],
        'concerns_mercosur': [
            "Potenzieller Schaden für lokale Landwirte und Unternehmen in der EU.",
            "Wirtschaftliche Instabilität für gefährdete Sektoren.",
            "Erhöhte Abhängigkeit von ausländischen Importen.",
            "Risiko unzureichender Durchsetzung von Regulierungsstandards.",
        ],
        'positive_impact_mercosur': [
            "Geringere Kosten für Verbraucher durch reduzierte Zölle.",
            "Stärkere internationale Handelsbeziehungen.",
            "Potenzielles Wirtschaftswachstum in beiden Regionen.",
            "Erhöhte Exportmöglichkeiten für europäische Unternehmen.",
        ],
        'aspect_mercosur': [
            "Sicherstellung eines fairen Wettbewerbs für lokale Industrien.",
            "Unterstützung der Arbeitsplatzsicherheit in betroffenen Sektoren.",
            "Aufrechterhaltung hoher regulatorischer und Sicherheitsstandards.",
            "Ausgewogenheit zwischen kurzfristigen wirtschaftlichen Gewinnen und langfristigen Auswirkungen.",
        ],
    }

    
    treatment_texts = {
        'positive': "Das Mercosur-Freihandelsabkommen zielt darauf ab, das Wirtschaftswachstum anzukurbeln, indem neue Märkte erschlossen, Exporte gesteigert und die Zusammenarbeit zwischen der Europäischen Union und südamerikanischen Ländern gefördert werden. Es soll Arbeitsplätze schaffen und die Kosten für Verbraucher durch den Abbau von Handelsbarrieren senken.",
        'negative': "Das Mercosur-Freihandelsabkommen könnte lokale Industrien durch verstärkten Wettbewerb aus Südamerika schädigen. Es gibt Bedenken hinsichtlich des Verlusts von Arbeitsplätzen in sensiblen Branchen und der Senkung von Regulierungsstandards. Kritiker warnen, dass es möglicherweise nur großen Unternehmen zugutekommt und Bürger benachteiligt.",
        'neutral': "Das Mercosur-Freihandelsabkommen ist ein Handelsabkommen zwischen der Europäischen Union und südamerikanischen Ländern. Es zielt darauf ab, Handelsbarrieren abzubauen und den Handel zwischen den beiden Regionen zu erleichtern. Das Abkommen birgt sowohl potenzielle Vorteile als auch Herausforderungen, die derzeit Gegenstand öffentlicher Debatten sind."
    }
    
   


class Subsession(BaseSubsession):
    pass
        


class Group(BaseGroup):
        framing = models.StringField(choices=['positive', 'negative', 'neutral'])
    
    

class Player(BasePlayer):

    # Welcome page
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    browser = models.IntegerField()
    language = models.IntegerField() 
    use_of_device = models.IntegerField(blank=True, max=3, min=1, label="")
    time_start = models.StringField(initial="-999")
    
    
    # pretreatment page
    eco_poli_affiliation = models.IntegerField(
        label="1- Wie ist Ihre politische Ausrichtung in Bezug auf die Wirtschaft?",
        choices=[(1, '1 - Links, Umverteilung, sozialistisch'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Konservativ, offene Märkte')],
        widget=widgets.RadioSelectHorizontal,
    )

    soci_poli_affiliation = models.IntegerField(
        label="2- Wie ist Ihre politische Ausrichtung in Bezug auf gesellschaftliche Themen?",
        choices=[(1, '1 - Liberal bezüglich Lebensstile/Kulturen'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Konservativ, traditionelle Familienwerte')],
        widget=widgets.RadioSelectHorizontal,
    )
    
    concept_freetrade = models.IntegerField(
        label="3- Wie vertraut sind Sie mit dem Konzept von Freihandelsabkommen?",
        choices=[(1, '1 - Überhaupt nicht vertraut'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr vertraut')],
        widget=widgets.RadioSelectHorizontal,
    )

    mercosur_freetrade = models.IntegerField(
        label="4- Wie vertraut sind Sie mit dem Mercosur-Freihandelsabkommen?",
        choices=[(1, '1 - Überhaupt nicht vertraut'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr vertraut')],
        widget=widgets.RadioSelectHorizontal,
    )

    supportive_freetrade = models.IntegerField(
        label="5- Wie unterstützend stehen Sie im Allgemeinen Freihandelsabkommen gegenüber?",
        choices=[(1, '1 - Überhaupt nicht vertraut'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr vertraut')],
        widget=widgets.RadioSelectHorizontal,
    )

    trust_government = models.IntegerField(
        label="6- Wie sehr vertrauen Sie der Regierung, faire Handelsabkommen auszuhandeln?",
        choices=[(1, '1 - Überhaupt nicht vertraut'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr vertraut')],
        widget=widgets.RadioSelectHorizontal,
    )

    trust_media = models.IntegerField(
        label="2- Wie sehr vertrauen Sie der Medienberichterstattung über internationale Handelsabkommen?",
        choices=[(1, '1 - Überhaupt nicht vertraut'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr vertraut')],
        widget=widgets.RadioSelectHorizontal,
    )

    
    pre_talk_friends = models.BooleanField(
        label="• Mit Freunden oder der Familie darüber gesprochen:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_share_socialmedia = models.BooleanField(
        label="• Ihre Meinung in sozialen Medien geteilt:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_consider_voting = models.BooleanField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigt:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_support_petition = models.BooleanField(
        label="• Eine Online-Petition unterstützt:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_attend_protest = models.BooleanField(
        label="• An einer Demonstration oder einem Protest teilgenommen:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_legal_action = models.BooleanField(
        label="• Rechtliche Schritte in Form einer Sammelklage eingeleitet:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    #hidden_input = models.IntegerField(initial=50, blank=True)

# Framing Treatment Page
    assigned_treatment = models.StringField()
    time_popout = models.StringField(initial='-999',blank=True)


#manipulation checks page
    select_proceed = models.BooleanField(
        label="1-Sie haben das Ende des Experiments erreicht. Um fortzufahren, wählen Sie bitte 'Nein' unten aus.",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    describe_tone = models.IntegerField(
        label="2-Wie würden Sie den Ton der Beschreibung des Mercosur-Abkommens einschätzen, die Sie zuvor gelesen haben?",
        choices=[(1, '1 - Sehr negativ'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr positiv')],
        widget=widgets.RadioSelectHorizontal
    )

    mentioned_points = models.StringField(
        label="3-Welche der folgenden Punkte wurden in der Beschreibung des Mercosur-Abkommens erwähnt, die Sie gelesen haben? (Wählen Sie alle aus, die zutreffen.)",
    )
    
    overall_message = models.StringField(
        label="4- Was war die allgemeine Botschaft der Beschreibung, die Sie über das Mercosur-Abkommen gelesen haben?",
        choices=["Das Abkommen wurde positiv dargestellt.", "Das Abkommen wurde negativ dargestellt.", "Das Abkommen wurde neutral dargestellt.", "Ich bin mir nicht sicher."],
        widget=widgets.RadioSelect,
    )
    
    
    

# posttreatment page
    supportive_mercosur = models.IntegerField(
        label="1- Nach dem Lesen dieser Beschreibung, wie unterstützend stehen Sie dem Mercosur-Abkommen gegenüber?",
        choices=[(1, '1 - Nicht unterstützend'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr unterstützend')],
        widget=widgets.RadioSelect,
    )

    relevant_mercosur = models.IntegerField(
        label="2- Wie relevant erscheint Ihnen persönlich das Mercosur-Abkommen?",
        choices=[(1, '1 - Nicht relevant'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr relevant')],
        widget=widgets.RadioSelect,
    )  

    concerns_mercosur = models.StringField(
        label="3-Was bereitet Ihnen am meisten Sorgen im Zusammenhang mit dem Mercosur-Abkommen? (Wählen Sie bis zu 2 aus)",
        blank=True,
    )
    other_concerns_mercosur = models.StringField(
        blank=True,
        label="• Sonstiges(bitte angeben)......:"
    )
   
    positive_impact_mercosur = models.StringField(
        label="4- Was halten Sie für die positivste Auswirkung des Mercosur-Abkommens? (Wählen Sie bis zu 2 aus)",
        blank=True,
    )
    other_positive_impact_mercosur = models.StringField(
        blank=True,
        label="• Sonstiges(bitte angeben)......:"
    )

    aspect_mercosur = models.StringField(
        label="5- Welcher Aspekt des Mercosur-Abkommens erfordert Ihrer Meinung nach die größte Aufmerksamkeit? (Wählen Sie bis zu 2 aus)",
        blank=True,
    )
    other_aspect_mercosur = models.StringField(
        blank=True,
        label="• Sonstiges(bitte angeben)......:"
    )

    post_talk_friends = models.IntegerField(
        label="• Mit Freunden oder der Familie darüber gesprochen:",
        choices=[(1, '1 - Unwahrscheinlich'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr wahrscheinlich')],
        widget=widgets.RadioSelectHorizontal
    )
    post_share_socialmedia = models.IntegerField(
        label="• Ihre Meinung in sozialen Medien geteilt:",
        choices=[(1, '1 - Unwahrscheinlich'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr wahrscheinlich')],
        widget=widgets.RadioSelectHorizontal
    )
    post_consider_voting = models.IntegerField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigt:",
        choices=[(1, '1 - Unwahrscheinlich'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr wahrscheinlich')],
        widget=widgets.RadioSelectHorizontal
    )
    post_support_petition = models.IntegerField(
        label="• Eine Online-Petition unterstützt:",
        choices=[(1, '1 - Unwahrscheinlich'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr wahrscheinlich')],
        widget=widgets.RadioSelectHorizontal
    )
    post_attend_protest = models.IntegerField(
        label="• An einer Demonstration oder einem Protest teilgenommen:",
        choices=[(1, '1 - Unwahrscheinlich'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr wahrscheinlich')],
        widget=widgets.RadioSelectHorizontal
    )
    post_legal_action = models.IntegerField(
        label="• Rechtliche Schritte in Form einer Sammelklage eingeleitet:",
        choices=[(1, '1 - Unwahrscheinlich'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10 - Sehr wahrscheinlich')],
        widget=widgets.RadioSelectHorizontal
    )
    

    
