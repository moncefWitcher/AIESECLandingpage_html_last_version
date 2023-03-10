from django.db import models
import datetime
# Create your models here.
def upload_path(instance , filename):
    path = '/'.join(['covers',filename])
    path = ''.join([ path , '.jpg'])
    return path


class LCs(models.Model):
    name = models.TextField()
    vision = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)

class LCMembers(models.Model):
    name = models.TextField()
    department = models.TextField()
    role = models.TextField()
    parent = models.ForeignKey(LCs, on_delete=models.CASCADE,null=True,blank=True)

class MC(models.Model):
    name = models.TextField()
    why = models.TextField()
    how = models.TextField()
    what = models.TextField()
    vision = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)
    date =  models.DateField(("Date"), default=datetime.date.today)


class social_media_link (models.Model):
    whatsapp = models.TextField()
    insta = models.TextField()
    linkedin = models.TextField()
    facebook = models.TextField()
    departents = models.TextField() 

class MCTEAM (models.Model):
    mcParent = models.ForeignKey(MC, on_delete=models.CASCADE,null=True,blank=True)
    name  = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)
    twiter = models.TextField()
    insta = models.TextField()
    gmail = models.TextField()
    facebook = models.TextField()
    deparment = models.TextField()


class Event (models.Model):
    name  = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)
    venue_address = models.TextField()
   
    venue_address_LINK_maps = models.TextField()
    date =  models.DateField(("Date"), default=datetime.date.today ,null=True,blank=True)
    registration_link_form = models.TextField()
  
    time =  models.FloatField(null=True,blank=True)
    AIESECERS_or_youth = models.BooleanField(null=True,blank=True) # true if for AIESECER 
    link_page =  models.TextField(null=True,blank=True)
  
    limited_places_OR_nonlimited = models.BooleanField(null=True,blank=True)
    city_name = models.TextField()
    description = models.TextField()    
     
class FQ (models.Model):
    Question = models.TextField()
    Answer = models.TextField()
    link = models.TextField(null=True,blank=True)

class Forms (models.Model):
    joinAIESC =  models.TextField()
    beApartner =  models.TextField()
    EP =  models.TextField()  

class AIESEC_projects (models.Model) :
    name = models.TextField(null=True,blank=True)
    name_surtcut = models.TextField()
    desc = models.TextField()
    logo = models.ImageField(upload_to=upload_path, blank=True)
    cover = models.ImageField(upload_to=upload_path, blank=True)
    link = models.TextField(null=True,blank=True)

class projects_by_products (models.Model) :
    project = models.ForeignKey(
        AIESEC_projects,
        on_delete=models.CASCADE, 
    )
    picture = models.ImageField(upload_to=upload_path, blank=True)
    name = models.TextField()
    desc = models.TextField() 