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
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
        framing = models.StringField(choices=['positive', 'negative', 'neutral'])
    
    

class Player(BasePlayer):
    time_start = models.StringField(initial="-999")
    
    # pretreatment page
    eco_poli_affiliation = models.IntegerField(
        label="Wie ist Ihre politische Ausrichtung in Bezug auf wirtschaftliche Themen? (1 - Umverteilung, Sozialistisch / 10 - Konservativ, offene Märkte)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    soci_poli_affiliation = models.IntegerField(
        label="Wie ist Ihre politische Ausrichtung in Bezug auf gesellschaftliche Themen? (1-Liberal bezüglich Lebensstile-Kulturen / 10-Konservativ, traditionelle Familienwerte)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )
    
    concept_freetrade = models.IntegerField(
        label="Wie vertraut sind Sie mit dem Konzept von Freihandelsabkommen? (1-Überhaupt nicht vertraut/ 10-Sehr vertraut)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    mercosur_freetrade = models.IntegerField(
        label="Wie vertraut sind Sie mit dem Mercosur-Freihandelsabkommen?(1-Überhaupt nicht vertraut/ 10-Sehr vertraut)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    supportive_freetrade = models.IntegerField(
        label="Wie sehr unterstüzen Sie im Allgemeinen Freihandelsabkommen? (1-Keine Unterstüzung / 10-Volle Unterstüzung)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    trust_government = models.IntegerField(
        label="Wie sehr vertrauen Sie der Regierung (Poilitik/Staat), faire Handelsabkommen auszuhandeln?(1-Kein Vertrauen/10-Volles Vertrauen)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    trust_media = models.IntegerField(
        label="Wie sehr vertrauen Sie der Medienberichterstattung über internationale Handelsabkommen?(1-Kein Vertrauen/10-Volles Vertrauen)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
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

# Framing Treatment Page
    assigned_treatment = models.StringField()
    treatment = models.StringField()
    time_popout = models.StringField(initial='-999',blank=True)


#manipulation checks page
    select_proceed = models.BooleanField(
        label="Sie haben das Ende des Experiments erreicht. Um fortzufahren, wählen Sie bitte 'Nein' unten aus.",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    describe_tone = models.IntegerField(
        label="Wie würden Sie den Ton der Beschreibung des Mercosur-Abkommens einschätzen, die Sie zuvor gelesen haben?(1-Sehr negativ/10-Sehr positiv)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )

    mentioned_points = models.StringField(
        label="Welche der folgenden Punkte wurden in der Beschreibung des Mercosur-Abkommens erwähnt, die Sie gelesen haben? (Wählen Sie alle aus, die zutreffen.)",
        choices=[(1, "Das Abkommen wird das Wirtschaftswachstum fördern und Arbeitsplätze schaffen."), 
                 (2, "Das Abkommen zielt darauf ab, die Kosten für Verbraucher zu senken."),
                 (3, "Kritiker warnen vor erhöhtem Wettbewerb für lokale Industrien.")],
        widget= widgets.RadioSelect,
    )
    
    overall_message = models.StringField(
        label="Was war die allgemeine Botschaft der Beschreibung, die Sie über das Mercosur-Abkommen gelesen haben?",
        choices=[(1,"Das Abkommen wurde positiv dargestellt."), 
                 (2,"Das Abkommen wurde negativ dargestellt."), 
                 (3,"Das Abkommen wurde neutral dargestellt."), 
                 (4,"Ich bin mir nicht sicher.")],
        widget=widgets.RadioSelect,
    )
    
# posttreatment page
    supportive_mercosur = models.IntegerField(
        label="1-Nach dem Lesen dieser Beschreibung, wie unterstützend stehen Sie dem Mercosur-Abkommen gegenüber?(1-Keine Unterstützung /10-Volle Unterstützung)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelect,
    )

    relevant_mercosur = models.IntegerField(
        label="2- Wie relevant erscheint Ihnen persönlich das Mercosur-Abkommen?(1-Nicht relevant/10-Sehr relevant)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelect,
    )  

    concerns_mercosur = models.StringField(
        label="3-Was bereitet Ihnen am meisten Sorgen im Zusammenhang mit dem Mercosur-Abkommen? (Wählen Sie bis zu 2 aus)",
        blank=True,
        choices=[(1, 'Potenzieller Schaden für lokale Landwirte und Unternehmen in der EU.'),
            (2, 'Wirtschaftliche Instabilität für gefährdete Sektoren.'),
            (3, 'Erhöhte Abhängigkeit von ausländischen Importen.'),
            (4, 'Risiko unzureichender Durchsetzung von Regulierungsstandards.')],
        widget=widgets.RadioSelect,
    )

    other_concerns_mercosur = models.StringField(
        blank=True,
        label="• Sonstiges(bitte angeben)......:"
    )
   
    positive_impact_mercosur = models.StringField(
        label="4- Was halten Sie für die positivste Auswirkung des Mercosur-Abkommens? (Wählen Sie bis zu 2 aus)",
        blank=True,
        choices=[(1,"Geringere Kosten für Verbraucher durch reduzierte Zölle."),
            (2,"Stärkere internationale Handelsbeziehungen."),
            (3,"Potenzielles Wirtschaftswachstum in beiden Regionen."),
            (4,"Erhöhte Exportmöglichkeiten für europäische Unternehmen.")],
        widget=widgets.RadioSelect 
    )
    
    other_positive_impact_mercosur = models.StringField(
        blank=True,
        label="• Sonstiges(bitte angeben)......:"
    )

    aspect_mercosur = models.StringField(
        label="5- Welcher Aspekt des Mercosur-Abkommens erfordert Ihrer Meinung nach die größte Aufmerksamkeit? (Wählen Sie bis zu 2 aus)",
        blank=True,
        choices=[(1,"Sicherstellung eines fairen Wettbewerbs für lokale Industrien."),
            (2,"Unterstützung der Arbeitsplatzsicherheit in betroffenen Sektoren."),
            (3,"Aufrechterhaltung hoher regulatorischer und Sicherheitsstandards."),
            (4,"Ausgewogenheit zwischen kurzfristigen wirtschaftlichen Gewinnen und langfristigen Auswirkungen.")]
        widget=widgets.RadioSelect        
    )
    
    other_aspect_mercosur = models.StringField(
        blank=True,
        label="• Sonstiges(bitte angeben)......:"
    )

    post_talk_friends = models.IntegerField(
        label="• Mit Freunden oder der Familie darüber gesprochen: (1-Unwahrscheinlich/10-Sehr wahrscheinlich)" ,
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_share_socialmedia = models.IntegerField(
        label="• Ihre Meinung in sozialen Medien geteilt:(1-Unwahrscheinlich/ 10-Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    
    post_consider_voting = models.IntegerField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigt:(1-Unwahrscheinlich/10-Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_support_petition = models.IntegerField(
        label="Eine Online-Petition unterstützt: (1-Unwahrscheinlich/10-Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_attend_protest = models.IntegerField(
        label="An einer Demonstration oder einem Protest teilgenommen: (1-Unwahrscheinlich /10-Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_legal_action = models.IntegerField(
        label="Rechtliche Schritte in Form einer Sammelklage eingeleitet: (1-Unwahrscheinlich/10-Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    

    
