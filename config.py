######################################################
# PLEASE CHANGE FOLLOWING CONFIGS ####################
Twitch_Channel          = 'your_channel_name'

Trans_Username          = 'your_bot_name'
Trans_OAUTH             = 'bot_oauth_key'

#######################################################
# OPTIONAL CONFIGS ####################################
Trans_TextColor         = 'GoldenRod'
# Blue, Coral, DodgerBlue, SpringGreen, YellowGreen, Green, OrangeRed, Red, GoldenRod, HotPink, CadetBlue, SeaGreen, Chocolate, BlueViolet, and Firebrick

lang_TransToHome        = 'ja'
lang_HomeToOther        = 'en'

Show_ByName             = True
Show_ByLang             = True

Ignore_Lang             = ['']
Ignore_Users            = ['Nightbot', 'BikuBikuTest']
Ignore_Line             = ['http', 'BikuBikuTest', '888', '８８８']
Ignore_WWW              = ['w', 'ｗ', 'W', 'Ｗ', 'ww', 'ｗｗ', 'WW', 'ＷＷ', 'www', 'ｗｗｗ', 'WWW', 'ＷＷＷ', '草']
Delete_Words            = ['saatanNooBow', 'BikuBikuTest']

# Any emvironment, set it to `True`, then text will be read by TTS voice!
# TTS_In:User Input Text, TTS_Out:Bot Output Text
TTS_In                  = True
TTS_Out                 = True
TTS_Kind                = "gTTS" # You can choice "CeVIO" or "Bouyomi" if you want to use CeVIO or BouyomiChan as TTS.
Bouyomiport             = 50080 # set your Bouyomichan HTTP Port
# CeVIO_Cast            = "さとうささら" # When you are using CeVIO, you must set voice cast name.
TTS_TextMaxLength       = 30
TTS_MessageForOmitting  = ""

# if you make TTS for only few lang, please add langID in the list
# for example, ['ja'] means Japanese only, ['ko','en'] means Korean and English are TTS!
ReadOnlyTheseLang       = []

# Select the translate engine ('deepl' or 'google')
Translator              = 'google'

# if you want to Send Translate Chat then Set True.
Send                    = True

# Use Google Apps Script for tlanslating
# e.g.) GAS_URL         = 'https://script.google.com/macros/s/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec'
GAS_URL                 = ''

# set WakeupMessage. default:TwitchTransFreeNext v.{version}, by さぁたん @saatan_pion and さよなりω @husband_sayonari_omega
WakeupMessage           = 'TwitchTransFreeNext v.{version}, by さぁたん @saatan_pion and さよなりω @husband_sayonari_omega'
OnWakeup                = True
# Enter the suffix of the Google Translate URL you normally use.
# Example: translate.google.co.jp -> 'co.jp'
#          translate.google.com   -> 'com'
GoogleTranslate_suffix  = 'co.jp'

# Download FFmpeg from https://ffmpeg.org/download.html you can change talk speed >=0.5 <=2.0
AutoDL                  = True
speed                   = 1.0

# If you meet any bugs, You can check some error message using Debug mode (Debug = True)
Debug                   = False
