import pprint
from rgb import *
from datetime import datetime

now = datetime.now()
DATE = now.strftime("%Y-%m-%d %H:%M:%S")

def filler(string):
    max_size = 15
    prefix = ' |'
    string = string[:max_size]
    message = f' %{-max_size}s' % string
    return (prefix + message)
class Colors:
    class Background:

        ERROR = bg_rgb(192, 57, 43)
        WARNING = bg_rgb(243, 156, 45)
        INFORMATION = bg_rgb(87, 215, 40)
        DEBUG = bg_rgb(155, 89, 182)
        SPONSOR = bg_rgb(66, 161, 133)
        STACKOVERFLOW = bg_rgb(41, 128, 185)
        DOCUMENTATION = bg_rgb(236, 135, 191)
        DATEBG = bg_rgb(43, 62, 80)
        RESET = '\u001b[0m'

    class Foreground:

        ERROR = fg_rgb(192, 57, 43)
        WARNING = fg_rgb(243, 156, 45)
        INFORMATION = fg_rgb(87, 215, 40)
        DEBUG = fg_rgb(155, 89, 182)
        SPONSOR = fg_rgb(66, 161, 133)
        STACKOVERFLOW = fg_rgb(41, 128, 185)
        DOCUMENTATION = fg_rgb(236, 135, 191)
        RESET = '\u001b[37m'

    RESET_ALL = Background.RESET + Foreground.RESET
class Logger():

    def __init__(self, options):

        self.options = {
            
            'language': options.get('language', 'en'),
            'colors': options.get('colors', True),#options["colors"] or True,
            'debug': options.get('debug', True),
            'info': options.get('info', True),
            'warning': options.get('warning', True),
            'error': options.get('error', True),
            'sponsor': options.get('sponsor', True),
            'write': options.get('write', False),
            'type': options.get('type', 'Log'),
            'path': options.get('path', {
                'debug_log': './debug.log',
                'error_log': './error.log'
            })       
        }
    def default(self):
        return Colors.RESET_ALL
    def getLanguage(self):
        return self.options["language"]
    def statusColors(self):
        return self.options["colors"]
    def statusDebug(self):
        return self.options["debug"]
    def statusInfo(self):
        return self.options["info"]
    def statusWarning(self):
        return self.options["warning"]
    def statusError(self):
        return self.options["error"]
    def statusSponsor(self):
        return self.options["sponsor"]
    def statusWrite(self):
        return self.options["write"]
    def warning(self, message):
        if self.options['warning']:
            if self.options['colors']:
                PREFIX_BG = Colors.Background.WARNING
                PREFIX_TEXT = filler('WARNING')
                Message = f"{Colors.RESET_ALL}{PREFIX_BG}{PREFIX_TEXT}{Colors.Background.DATEBG} {DATE} {Colors.Background.WARNING} {Colors.RESET_ALL}{Colors.Foreground.WARNING} {message}{Colors.RESET_ALL}"
            else:
                Message = f'[WARNING - {DATE}] {message}'
            return Message
        else:
            raise Exception('Warning messages are not enabled! Please enable it inside Logger options.')


    def information(self, message):
        if self.options['info']:
            if self.options['colors']:
                PREFIX_BG = Colors.Background.INFORMATION
                PREFIX_TEXT = filler('INFORMATION')
                Message = f"{Colors.RESET_ALL}{PREFIX_BG}{PREFIX_TEXT}{Colors.Background.DATEBG} {DATE} {Colors.Background.INFORMATION} {Colors.RESET_ALL}{Colors.Foreground.INFORMATION} {message}{Colors.RESET_ALL}"
            else:
                Message = f'[INFORMATION - {DATE}] {message}'
            return Message
        else:
            raise Exception('Information messages are not enabled! Please enable it inside Logger options.')

    def error(self, message):
        if self.options['error']:
            if self.options['colors']:
                PREFIX_BG = Colors.Background.ERROR
                PREFIX_TEXT = filler('ERROR')
                Message = f"{Colors.RESET_ALL}{PREFIX_BG}{PREFIX_TEXT}{Colors.Background.DATEBG} {DATE} {Colors.Background.ERROR} {Colors.RESET_ALL}{Colors.Foreground.ERROR} {message}{Colors.RESET_ALL}"
            else:
                Message = f'[ERROR - {DATE}] {message}'
            return Message
        else:
            raise Exception('Error messages are not enabled! Please enable it inside Logger options.')


    def sponsor(self, message):
        if self.options['sponsor']:
            if self.options['colors']:
                PREFIX_BG = Colors.Background.SPONSOR
                PREFIX_TEXT = filler('SPONSOR')
                Message = f"{Colors.RESET_ALL}{PREFIX_BG}{PREFIX_TEXT}{Colors.Background.DATEBG} {DATE} {Colors.Background.SPONSOR} {Colors.RESET_ALL}{Colors.Foreground.SPONSOR} {message}{Colors.RESET_ALL}"
            else:
                Message = f'[SPONSOR - {DATE}] {message}'
            return Message
        else:
            raise Exception('Sponsor messages are not enabled! Please enable it inside Logger options.')

    def debug(self, message):
        if self.options['debug']:
            if self.options['colors']:
                PREFIX_BG = Colors.Background.DEBUG
                PREFIX_TEXT = filler('DEBUG')
                Message = f"{Colors.RESET_ALL}{PREFIX_BG}{PREFIX_TEXT}{Colors.Background.DATEBG} {DATE} {Colors.Background.DEBUG} {Colors.RESET_ALL}{Colors.Foreground.DEBUG} {message}{Colors.RESET_ALL}"
            else:
                Message = f'[DEBUG - {DATE}] {message}'
            return Message
        else:
            raise Exception('Debug messages are not enabled! Please enable it inside Logger options.')
#TODO: devo creare una classe Logger in cui come parametro iniziale devo passare un dizionario tipo:

options = {
 	"language": "italiano",
 	"write": False,
}

log = Logger(options)
print(log.warning("attenzione"))
print(log.error("errore"))
print(log.sponsor("sponsor message"))
print(log.information("informazione"))

# Language => [EN]/IT 
# Colors => [True]/False
# Debug => [True]/False
# Info => [True]/False
# Warning => [True]/False
# Error => [True]/False
# Sponsor => [True]/False
# Write => True/[False]
# Type => [Log]/JSON
# Path => Dictionary => {"debug_log": "/path/to/debug.log",
#                       "error_log": "/path/to/error.log"}


# The above ANSI escape code will set the text colour to bright green. The format is;
#      \033 = Escape code, this is always the same
#      1 = Style, 1 for normal.
#      32 = Text colour, 32 for bright green.
#      40m = Background colour, 40 is for black.


# For more infos check https://ozzmaker.com/add-colour-to-text-in-python/


# INFORMATION WITH GREEN BG AND White FG
# DATE WITH WHITE FG and GREY BG
#  " | INFORMATION    " "2020-03-08 01:05:34" "<SPACE>" 

