import discord
import asyncio
import random
import requests
import math
import sqlite3
import os
import pickle


from discord.ext import commands
from discord.utils import get
from discord import Client






# note: you dont import the subscripts inside setup you do that in main

client = commands.Bot(command_prefix = '.')

bot = commands.Bot(command_prefix='!')
