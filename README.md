# twitchTransFreeNext
Next Generation of twitchTransFree!!!!

# Official Webpage
http://www.sayonari.com/trans_asr/

# USAGE
1. rewrite `config.py`
2. double-click `twitchTransFN.exe`

That's all!

NOTE: The file type of config was chaged from .txt to .py!

# I support my wife 24/7 :-) 
This software is made for my wife!  
http://twitch.tv/saatan_pion/  
If you are satisfied by this software, please watch my wife's stream! We are waiting for comming you! and subscribe! donation!

# We welcome your DONATE!!!!
Donation is possible from the following link!  
もし便利だなと思ったら．以下からDONATEしてください．開発中に食べるお菓子代にします！！！  
https://twitch.streamlabs.com/saatan_pion#/

# Please link from your page!
プログラム使うときには，twitchページからリンクを張ってくれたら嬉しいです！（強制ではないです）

さぁたんチャンネルと，翻訳ちゃんのページにリンクを貼っていただけると良いですが，紹介文は各自で考えてくださいρ

[example]  
Twitch: saatan  
http://twitch.tv/saatan_pion/ 

Software: twitchTransFreeNext  
https://github.com/sayonari/twitchTransFreeNext

紹介用の絵も頂いちゃいました．使ってください．  
![trans_anomon](https://user-images.githubusercontent.com/16011609/49361210-c1f5ef80-f71e-11e8-8cff-6fd760e8738a.png)  
Painted by anomon  
https://www.twitch.tv/anomomm

# config.py
```python
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

```

| Option| Description |
| -- | -- |
| Twitch_Channel | The target chat room for translation. |
| Trans_Username | username for translation |
| Trans_OAUTH | Get key for Trans_Username at https://twitchapps.com/tmi/ |
| Trans_TextColor  | You can change text color of translator. |
| lang_TransToHome | If set it to [`ja`], all texts will be translated to the JAPANESE! |
| lang_HomeToOther | If set it to [`en`], the language in [`lang_TransToHome`] is trans to [`en`]. |
| Show_ByName | If it is set to `True`, user name is shown after translated text. |
| Show_ByLang | If it is set to `True`, the source language is shown after translated text. |
| Ignore_Lang | You can set some languages : [ja,en, ...] |
| Ignore_Users | You can set some users : [Nightbot, BikuBikuTest, someotheruser, ...] |
| Ignore_Line | If the words are in message, the message will be ignored.|
| Ignore_WWW | Ignore Tanshiba(単芝:just only 'w'）line. |
| Delete_Words | The words will be removed from message. |
| TTS_Kind | The kind of TTS, "gTTS"(default) or "CeVIO" or "Bouyomi"(棒読みちゃん). If you want to use CeVIO, you need to install CeVIO AI in your local computer. |
| TTS_In | Input text will be read by TTS voice! |
| TTS_Out | Bot output text will be read by TTS voice! |
| Bouyomiport | Set BouyomiChan HTTP Port |
| Send | if True then Send Translated Chat |
| WakeupMessage | when run application send to Chat Message |
| OnWakeup | Send WakeupMessage for Twitch Chat |
| AutoDL | AutoDownload FFMpeg 1st time only |
| speed | if use gTTS then set Read Text Speed lower 0.5 upper 2.0 |
| gTTS_In | It's deprecated config, please use TTS_In instead. |
| gTTS_Out | It's deprecated config, please use TTS_Out instead. |
| TTS_TextMaxLength | You can specify TTS's read comment max length. If comment has over length from this, it will omit and added TTS_MessageForOmitting on postfix. |
| TTS_MessageForOmitting | A message for omitting TTS's read comment. The TTS puts this message  on the omitted message. |
| CeVIO_Cast | The cast name of CeVIO, for example "さとうささら". This option is enabled only when TTS_Kind = "CeVIO". |
| ReadOnlyTheseLang | You can set the TTS language! |
| Debug | You can check some error message using Debug mode (Debug = True)|


# memo
## support language (google translator)
https://cloud.google.com/translate/docs/languages

# secret functions
## choose trans destination language (for one text)
At the time of translation, you can select the target language like `en:` at the beginning of the sentence.  
Example) ru: Hello -> привет там

NOTE: When rewriting config.txt, please delete the `#` mark at the beginning of each setting value!

## command: (version)
`!ver`: print the software version.

`!sound xxxx`: play sound (xxxx.mp3), if you put sound data at sound folder.

# Thanks
Thanks to Pioneers!
The developer of ...
- Google
- googletrans by ssut
    - https://github.com/ssut/py-googletrans
- gtts by pndurette
    - https://github.com/pndurette/gTTS
- playsound by TaylorSMarks
    - https://github.com/TaylorSMarks/playsound
- TwitchIO
    - https://github.com/TwitchIO/TwitchIO

# Developer Info.

| Title | Automatic Translator for Twitch Chat (Next Generation) |
|--|--|
| Developer | husband_sayonari_omega |
| github | https://github.com/sayonari/twitchTransFreeNext |
| Webpage | http://www.sayonari.com/trans_asr/ |
| mail | sayonari@gmail.com |
| Twitter | [sayonari](https://twitter.com/sayonari) |
