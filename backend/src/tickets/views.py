#bridge between backend and frontend

from .models import  Ticket
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
import datetime
