from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("services",views.services,name="services"),
    path("domain.html",views.domain,name="domain"),
    path("signIn",views.signIn,name="signIn"),
    path("signOut",views.signOut,name="signOut"),
    path("fixAppointment",views.fixAppointment,name="fixAppointment"),

    path("neurology",views.neurology,name="neurology"),
    path("oncology",views.oncology,name="oncology"),
    path("ophthalmologist",views.ophthalmologist,name="ophthalmologist"),
    path("cardiology",views.cardiology,name="cardiology"),
    path("therapist",views.therapist,name="therapist"),
    path("podiatrist",views.podiatrist,name="podiatrist"),





    path("option",views.option,name="option"),
    path("patSignUp",views.patSignUp,name="patSignUp"),
    path("docSignUp",views.docSignUp,name="docSignUp"),
    path("docProfile",views.docProfile,name="docProfile"),

]