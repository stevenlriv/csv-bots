import sys
import os

# We load custom packages
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'src'))

# We import the packages
import bot_request
import bot_files
import bot_scheduler