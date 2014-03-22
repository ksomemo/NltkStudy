# coding: utf-8
from __future__ import division
import nltk
from nltk.book import *

def plot_dispersion():
    target = ['citizends', 'democracy', 'freedom', 'duties', 'America']
    text4.dispersion_plot(target)

def plot_freq_dist():
    fdist1 = FreqDist(text1)
    fdist1.plot(50, cumulative=True)

def machine_translation():
    babelize_shell()

def chat():
    nltk.chat.chatbots()
