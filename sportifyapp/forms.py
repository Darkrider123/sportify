from django import forms   
from sportifyapp import models
import datetime

class TeamForm(forms.ModelForm):
    
    class Meta:
        model = models.Echipa
        fields = ['nume']

# class MatchForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         self.team_id = kwargs.pop('team_id')
#         self.team_sport = kwargs.pop('team_sport')
#         super(MatchForm, self).__init__(*args, **kwargs)
#         self.fields['cacat'] = forms.CharField(max_length=2)
        
class MatchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # opposing_teams = ''
        # if 'team_id' in  kwargs and 'team_sport' in kwargs:
        current_team_id = kwargs.pop('team_id') 
        current_team_sport = kwargs.pop('team_sport') 
        opposing_teams = models.Echipa.objects.filter(sport=current_team_sport).exclude(id=current_team_id)

        super(MatchForm, self).__init__(*args, **kwargs)
        # self.fields['cacat'] = forms.CharField(max_length=10)
        self.fields['echipa'] = forms.ModelChoiceField(queryset=opposing_teams)
        self.fields['data'] = forms.DateField(label='date', initial=datetime.date.today(), widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_data(self):
        return self.cleaned_data['data']
    
    def clean_echipa(self):
        return self.cleaned_data['echipa']
    class Meta:
        model = models.Meci
        fields = ['data', 'echipa']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }