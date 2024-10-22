import gettext
lang = gettext.translation('messages', localedir='locales', languages=['es'])
lang.install()
print(_("Hello, World!"))  # Outputs: ¡Hola, Mundo!
