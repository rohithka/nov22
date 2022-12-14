from pickle import NONE
from time import time
from django import forms
from django.forms import ModelForm
# from requests import request
# from django.contrib.auth import authenticate
from .models import *
from datetime import datetime
from pytz import timezone
from dashboard.models import CategoriesModel


class RequestForm(ModelForm):
    category = forms.ModelChoiceField(queryset=CategoriesModel.objects.all(),widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.HiddenInput())
    start_time = forms.TimeField(widget=forms.HiddenInput())
    end_time = forms.TimeField(widget=forms.HiddenInput())
    username= forms.ModelChoiceField(queryset=UserModel.objects.all(),widget=forms.HiddenInput())
    locality=forms.CharField(widget=forms.HiddenInput())
    status=forms.CharField(widget=forms.HiddenInput())
    # match_id= forms.ModelMultipleChoiceField(queryset=RequestModel.objects.all())
    match_id=forms.IntegerField(widget=forms.HiddenInput())
    phoneno=forms.IntegerField(widget=forms.HiddenInput())
    class Meta():
        model = RequestModel    
        # exclude = '__all__'
        fields =('category','date','start_time','end_time','username','locality','status','phoneno')
    

    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RequestForm, self).__init__(*args, **kwargs)
        # self.fields['category'].disabled = True



    def clean(self):
        print("---------------Inside RequestForm's Clean Method-------------------")
        self.cleaned_data = super().clean()
        print(self.cleaned_data.get('match_id'))
        print(self.cleaned_data.get('category'))
        match=MatchModel.objects.get(id=int(self.cleaned_data.get('match_id')))
        user=UserModel.objects.get(id=self.request.user.pk)
        print(self.cleaned_data.get('username'))
        print(match.category)
        if self.cleaned_data.get('category') != match.category:
            self._errors['category']=self.error_class(['Do not change the category'])
            print(" category  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('date')!=match.date:
            self._errors['date']=self.error_class(['Do not change the date'])
            print("date  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('start_time')!=match.start_time.astimezone(timezone('Asia/Kolkata')).time():
            self._errors['start_time']=self.error_class(['Do not change the start_time'])
            print("start_time   erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('end_time')!=match.end_time.astimezone(timezone('Asia/Kolkata')).time():
            self._errors['end_time']=self.error_class(['Do not change the end_time'])
            print("end_time  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('locality')!=match.locality:
            self._errors['locality']=self.error_class(['Do not change the locality'])
            print("locality  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")   
        if self.cleaned_data.get('username')!=user:
            self._errors['username']=self.error_class(['Do not change the user'])
            print("username  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")  
        # self.cleaned_data['username']=user
        # print("phone number in form",self.cleaned_data.get('phoneno'),"its type is",type(self.cleaned_data.get('phoneno')))
        # print("phone number in session",self.request.user.phone,"its type is",type(self.request.user.phone))
        if self.cleaned_data.get('phoneno')!=int(self.request.user.phone):
            self._errors['phoneno']=self.error_class(['Do not change the phone number'])
            print("phone number  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr") 
        if self.cleaned_data.get('status')!="Pending":
            self._errors['status']=self.error_class(['Do not change the status'])
            print("status  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        else:
            print("no erorrrrrrrrrrrrrrrrrrrrrrr")
        return self.cleaned_data

# choices=OPTIONS


class creatematchForm(ModelForm):

    options =[
        ("Cricket", "Cricket"),
        ("Football", "Football"),
        ("Baseball", "Baseball"),
        ("Badminton", "Badminton"),
        ("Tennis", "Tennis"),
        ("Volleyball","Volleyball"),
        ("Basketball","Basketball")
    ]
    # cat=CategoriesModel.objects.all().values_list('category')
    # print(cat)
    # print("------------------------hardcoded options--------------------------",options)
    # options1 =[
    #     # for c in cat:
    #     #     (c,c)
    # ] 
    # print(options1)

    category= forms.ModelChoiceField(queryset=CategoriesModel.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time_f = forms.TimeField(required=False,widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    end_time_f = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    start_time = forms.DateTimeField(widget=forms.HiddenInput())
    end_time = forms.DateTimeField(widget=forms.HiddenInput())
    slots = forms.IntegerField()#nos = number of slots           
    creator= forms.ModelChoiceField(queryset=UserModel.objects.all(),widget=forms.HiddenInput())
    locality=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    # status=forms.CharField(widget=forms.HiddenInput())
    slot_available=forms.IntegerField(widget=forms.HiddenInput())
    # cron=forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = MatchModel
        fields = 'category','date','start_time_f','end_time_f','start_time','end_time','slots','city','locality','creator'
    
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(creatematchForm, self).__init__(*args, **kwargs)

    def clean(self):
        print("hasgfsdyfgsdhjfdg")
        self.cleaned_data = super().clean()
        slots=self.cleaned_data.get('slots')
        creator=self.cleaned_data.get('creator')
        status=self.cleaned_data.get('status')
        user=UserModel.objects.get(id=self.request.user.pk)
        city=self.cleaned_data.get('city')
        if city :
            list=city.split(", ")
            if len(list) ==3:
                check_city=CitiesModel.objects.filter(name=list[0],subcountry=list[1],country=list[2])
                if len(check_city) == 0:
                     self._errors['city']=self.error_class(['Please Select a City from the provided list'])
            else:
                self._errors['city']=self.error_class(['Please Select a City from the provided list'])
        start_time_f=self.cleaned_data.get('start_time_f')
        end_time_f=self.cleaned_data.get('end_time_f')
        print(slots)
        if slots != None and slots >= 2:
            self.cleaned_data['slot_available']=slots-1
        else :
            self._errors['slots']=self.error_class(['No of slots can not be less than 2'])
        self.cleaned_data['creator']=user
        print()
        # if creator !=  self.request.user.username:
        #     self._errors['creator']=self.error_class([''])
        # if status != "Upcoming":
        #     self._errors['status']=self.error_class([''])
        self.cleaned_data['status']="Upcoming"
        if   start_time_f != None and end_time_f !=None :
                if start_time_f >= end_time_f:
                    self._errors['start_time_f']=self.error_class(['Start time can not be more than end time'])
        elif  start_time_f == None:
                self._errors['start_time_f']=self.error_class(['Start time must be time type'])
        elif  end_time_f == None:
                self._errors['end_time_f']=self.error_class(['End time must be time type'])
        print("khsfdagjfdghsuj",slots,self.cleaned_data['slot_available'])
        return self.cleaned_data



class updatematchform(ModelForm):

    options =[
        ("Cricket", "Cricket"),
        ("Football", "Football"),
        ("Baseball", "Baseball"),
        ("Badminton", "Badminton"),
        ("Tennis", "Tennis"),
        ("Volleyball","Volleyball"),
        ("Basketball","Basketball")
    ]

    match_id = forms.ModelChoiceField(queryset=MatchModel.objects.all(),widget=forms.HiddenInput())
    category= forms.ModelChoiceField(queryset=CategoriesModel.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time_f = forms.TimeField(required=False,widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    end_time_f = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    start_time = forms.DateTimeField(widget=forms.HiddenInput())
    end_time = forms.DateTimeField(widget=forms.HiddenInput())
    slots = forms.IntegerField()#nos = number of slots           
    creator= forms.CharField(widget=forms.HiddenInput())
    locality=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    # status=forms.CharField(widget=forms.HiddenInput())
    slot_available=forms.IntegerField(widget=forms.HiddenInput())
    # cron=forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = MatchModel
        fields = 'category','date','start_time_f','end_time_f','start_time','end_time','slots','city','locality','creator'
    
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(updatematchform, self).__init__(*args, **kwargs)

    def clean(self):
        print("hasgfsdyfgsdhjfdg")
        self.cleaned_data = super().clean()
        slots=self.cleaned_data.get('slots')
        creator=self.cleaned_data.get('creator')
        status=self.cleaned_data.get('status')
        start_time_f=self.cleaned_data.get('start_time_f')
        end_time_f=self.cleaned_data.get('end_time_f')
        city=self.cleaned_data.get('city')
        if city :
            list=city.split(", ")
            if len(list) ==3:
                check_city=CitiesModel.objects.filter(name=list[0],subcountry=list[1],country=list[2])
                if len(check_city) == 0:
                     self._errors['city']=self.error_class(['Please Select a City from the provided list'])
            else:
                self._errors['city']=self.error_class(['Please Select a City from the provided list'])
        print(slots)
        if slots != None and slots >= 2:
            self.cleaned_data['slot_available']=slots-1
        else :
            self._errors['slots']=self.error_class(['No of slots can not be less than 2'])
        self.cleaned_data['creator']=self.request.user.username
        if creator !=  self.request.user.username:
            self._errors['creator']=self.error_class([''])
        # if status != "Upcoming":
        #     self._errors['status']=self.error_class([''])
        self.cleaned_data['status']="Upcoming"
        if   start_time_f != None and end_time_f !=None :
                if start_time_f >= end_time_f:
                    self._errors['start_time_f']=self.error_class(['Start time can not be more than end time'])
        elif  start_time_f == None:
                self._errors['start_time_f']=self.error_class(['Start time must be time type'])
        elif  end_time_f == None:
                self._errors['end_time_f']=self.error_class(['End time must be time type'])
        print("khsfdagjfdghsuj",slots,self.cleaned_data['slot_available'])
        return self.cleaned_data


#----------------------------------------------------------Tournament Section--------------------------------------------------------------------------------
class createtournamentForm(ModelForm):


    category= forms.ModelChoiceField(queryset=CategoriesModel.objects.all())
    
    # team_name =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time_f = forms.TimeField(required=False,widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    end_time_f = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    start_time = forms.DateTimeField(widget=forms.HiddenInput())
    end_time = forms.DateTimeField(widget=forms.HiddenInput())
    teams = forms.IntegerField()#nos = number of slots           
    creator= forms.CharField(widget=forms.HiddenInput())
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    locality=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    # status=forms.CharField(widget=forms.HiddenInput())
    team_space_available=forms.IntegerField(widget=forms.HiddenInput())
    # cron=forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = TournamentModel
        fields = 'category','start_date','end_date','start_time_f','end_time_f','start_time','end_time','teams','team_space_available','creator','locality','city'
    
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(createtournamentForm, self).__init__(*args, **kwargs)

    def clean(self):
        print("hasgfsdyfgsdhjfdg")
        self.cleaned_data = super().clean()
        teams=self.cleaned_data.get('teams')
        creator=self.cleaned_data.get('creator')
        team_name=self.cleaned_data.get('team_name')
        status=self.cleaned_data.get('status')
        start_time_f=self.cleaned_data.get('start_time_f')
        end_time_f=self.cleaned_data.get('end_time_f')
        print(teams)
        city=self.cleaned_data.get('city')
        if city :
            list=city.split(", ")
            if len(list) ==3:
                check_city=CitiesModel.objects.filter(name=list[0],subcountry=list[1],country=list[2])
                if len(check_city) == 0:
                     self._errors['city']=self.error_class(['Please Select a City from the provided list'])
            else:
                self._errors['city']=self.error_class(['Please Select a City from the provided list'])
        if team_name == None:
            self.cleaned_data['team_space_available']=teams
        elif team_name != None:
            self.cleaned_data['team_space_available']=teams-1
        else :
            self._errors['teams']=self.error_class(['No of teams can not be less than 2'])
        self.cleaned_data['creator']=self.request.user.username
        if creator !=  self.request.user.username:
            self._errors['creator']=self.error_class([''])
        # if status != "Upcoming":
        #     self._errors['status']=self.error_class([''])
        self.cleaned_data['status']="Upcoming"
        if   start_time_f != None and end_time_f !=None :
                if start_time_f >= end_time_f:
                    self._errors['start_time_f']=self.error_class(['Start time can not be more than end time'])
        elif  start_time_f == None:
                self._errors['start_time_f']=self.error_class(['Start time must be time type'])
        elif  end_time_f == None:
                self._errors['end_time_f']=self.error_class(['End time must be time type'])
        print("khsfdagjfdghsuj",teams,self.cleaned_data['team_space_available'])
        return self.cleaned_data


class updatetournamentform(ModelForm):
    options =[
        ("Cricket", "Cricket"),
        ("Football", "Football"),
        ("Baseball", "Baseball"),
        ("Badminton", "Badminton"),
        ("Tennis", "Tennis"),
        ("Volleyball","Volleyball"),
        ("Basketball","Basketball")
    ]



    tournament_id = forms.ModelChoiceField(queryset=TournamentModel.objects.all(),widget=forms.HiddenInput())
    category= forms.ModelChoiceField(queryset=CategoriesModel.objects.all())
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time_f = forms.TimeField(required=False,widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    end_time_f = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time','step' : '1'}))
    start_time = forms.DateTimeField(widget=forms.HiddenInput())
    end_time = forms.DateTimeField(widget=forms.HiddenInput())
    teams = forms.IntegerField()#nos = number of slots           
    creator= forms.CharField(widget=forms.HiddenInput())
    locality=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    # status=forms.CharField(widget=forms.HiddenInput())
    team_space_available=forms.IntegerField(widget=forms.HiddenInput())
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    # cron=forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = TournamentModel
        fields = 'category','start_date','end_date','start_time_f','end_time_f','start_time','end_time','teams','creator','locality','city'
    
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(updatetournamentform, self).__init__(*args, **kwargs)

    def clean(self):
        print("hasgfsdyfgsdhjfdg")
        self.cleaned_data = super().clean()
        teams=self.cleaned_data.get('teams')
        team_name = self.cleaned_data.get('team_name')
        creator=self.cleaned_data.get('creator')
        status=self.cleaned_data.get('status')
        start_time_f=self.cleaned_data.get('start_time_f')
        end_time_f=self.cleaned_data.get('end_time_f')
        print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",type(teams))
        city=self.cleaned_data.get('city')
        if city :
            list=city.split(", ")
            if len(list) ==3:
                check_city=CitiesModel.objects.filter(name=list[0],subcountry=list[1],country=list[2])
                if len(check_city) == 0:
                     self._errors['city']=self.error_class(['Please Select a City from the provided list'])
            else:
                self._errors['city']=self.error_class(['Please Select a City from the provided list'])
        if teams != None and teams >= 2:
            self.cleaned_data['team_space_available']=teams-1
        else :
            self._errors['teams']=self.error_class(['No of teams can not be less than 2'])
        if creator !=  self.request.user.username:
            self._errors['creator']=self.error_class([''])
        # if status != "Upcoming":
        #     self._errors['status']=self.error_class([''])
        self.cleaned_data['status']="Upcoming"
        if   start_time_f != None and end_time_f !=None :
                if start_time_f >= end_time_f:
                    self._errors['start_time_f']=self.error_class(['Start time can not be more than end time'])
        elif  start_time_f == None:
                self._errors['start_time_f']=self.error_class(['Start time must be time type'])
        elif  end_time_f == None:
                self._errors['end_time_f']=self.error_class(['End time must be time type'])
        print("khsfdagjfdghsuj",teams,self.cleaned_data['team_space_available'])
        return self.cleaned_data



class TournamentRequestForm(ModelForm):
    category = forms.ModelChoiceField(queryset=CategoriesModel.objects.all(),widget=forms.HiddenInput())
    # team_name =forms.ModelChoiceField(queryset=CreateTeamModel.objects.all())
    image=forms.ImageField(required=True,widget=forms.FileInput(attrs={'class':"form-control" }))
    team_name =forms.CharField(required=True,widget=forms.TextInput(attrs={"class":'form-control'}))
    start_date =forms.DateField(widget=forms.HiddenInput())
    end_date = forms.DateField(widget=forms.HiddenInput())
    start_time = forms.TimeField(widget=forms.HiddenInput())
    end_time = forms.TimeField(widget=forms.HiddenInput())
    username= forms.CharField(widget=forms.HiddenInput())
    locality=forms.CharField(widget=forms.TextInput())
    status=forms.CharField(widget=forms.HiddenInput())
    # match_id= forms.ModelMultipleChoiceField(queryset=RequestModel.objects.all())
    tournament_id=forms.IntegerField(widget=forms.HiddenInput())
    phoneno=forms.IntegerField(widget=forms.HiddenInput())
    class Meta():
        model = TournamentRequestModel    
        # exclude = '__all__'
        fields =('category','team_name','start_date','end_date','start_time','end_time','username','locality','status','phoneno','image')
    

    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TournamentRequestForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        print("---------------Inside RequestForm's Clean Method-------------------")
        self.cleaned_data = super().clean()
        team_name = self.cleaned_data.get('team_name')

        print(self.cleaned_data.get('tournament_id'))
        print(self.cleaned_data.get('category'))
        tournament=TournamentModel.objects.get(id=int(self.cleaned_data.get('tournament_id')))
        print(tournament.category)
        if self.cleaned_data.get('category') != tournament.category:
            self._errors['category']=self.error_class(['Do not change the category'])
            print(" category  er0rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        # if self.cleaned_data.get('team_name') != tournament.team_name:
        #     self._errors['team_name']=self.error_class(['Do not change the team_name'])
        #     print(" team_name  er0rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('start_date')!=tournament.start_date:
            self._errors['start_date']=self.error_class(['Do not change the date'])
        if self.cleaned_data.get('end_date')!=tournament.end_date:
            self._errors['end_date']=self.error_class(['Do not change the date'])
            print("end_date  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('start_time')!=tournament.start_time.astimezone(timezone('Asia/Kolkata')).time():
            self._errors['start_time']=self.error_class(['Do not change the start_time'])
            print("start_time   erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('end_time')!=tournament.end_time.astimezone(timezone('Asia/Kolkata')).time():
            self._errors['end_time']=self.error_class(['Do not change the end_time'])
            print("end_time  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if self.cleaned_data.get('locality')!=tournament.locality:
            self._errors['locality']=self.error_class(['Do not change the locality'])
            print("locality  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")   
        if self.cleaned_data.get('username')!=self.request.user.username:
            self._errors['username']=self.error_class(['Do not change the username'])
            print("username  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")  
        if self.cleaned_data.get('phoneno')!=int(self.request.user.phone):
            self._errors['phoneno']=self.error_class(['Do not change the phone number'])
            print("phone number  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr") 
        if self.cleaned_data.get('status')!="Pending":
            self._errors['status']=self.error_class(['Do not change the status'])
            print("status  erorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        else:
            print("no erorrrrrrrrrrrrrrrrrrrrrrr")
        return self.cleaned_data


class TeamCreationForm(forms.ModelForm):

    team_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # category= forms.ModelChoiceField(queryset=CategoriesModel.objects.all())
    # members = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # tournament_id =forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = CreateTeamModel
        fields = ('team_name',)

    # def clean(self):
    #     self.cleaned_data = super().clean()
    #     team=CreateTeamModel.objects.get(id=int(self.cleaned_data.get('tournament_id')))
    #     print(team.category)
    #     if self.cleaned_data.get('category') != team.category:
    #         self._errors['category']=self.error_class(['Do not change the category'])
    #         print(" category  er0rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
      

    


        
# class CreateTurfCommentForm(forms.Form):
#     comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':"2" , 'placeholder':"Add Your Comment "}))
#     # class Meta():
#     #     model = TurfCommentsModel
#     #     fields =('turf','commenter','comment','date')

class contact_usForm(ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email'}))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={'type':'tel','placeholder':'Your Phone Number'}), required=False)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message =forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Your Message'}))

    class Meta:
        model = contact_usModel    
        fields =('first_name','last_name','email','phone','subject','message')
    def clean_phone(self, *args, **kwargs):
        phone = self.cleaned_data.get("phone")
        if not len(str(phone)) <= 15 or not len(str(phone)) >= 7 or not phone >0:
            raise forms.ValidationError("Enter a valid phone number")
        return phone