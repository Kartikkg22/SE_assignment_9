import gettext
import locale

# Set the locale for the program (change 'es_ES' to your desired locale)
locale.setlocale(locale.LC_ALL, 'es_ES')

# Load the translation for the 'messages' domain
lang = gettext.translation('messages', localedir='locales', languages=['es'], fallback=True)
lang.install()

# Define _() as an alias for the translation function
_ = lang.gettext

# Example usage
print(_("Hello, World!"))
print(_("Welcome to the application!"))
