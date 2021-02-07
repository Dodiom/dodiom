from enum import Enum, auto
import random


class Token(Enum):
    TODAYS_MWE = auto()
    SUBMIT = auto()
    REVIEW = auto()
    CHANGE_LANGUAGE = auto()
    SHOW_SCOREBOARD = auto()
    LANGUAGE_ENGLISH = auto()
    LANGUAGE_TURKISH = auto()
    LANGUAGE_ITALIAN = auto()
    TODAYS_MWE_REPLY_TEXT = auto()
    SELECT_LANGUAGE = auto()
    LANGUAGE_CHANGE_SUCCESSFUL = auto()
    PLEASE_SELECT_VALID_LANGUAGE = auto()
    WELCOME_MESSAGE = auto()
    PLEASE_ENTER_EXAMPLE = auto()
    ENTER_VALID_MWE_CATEGORY = auto()
    THANKS_FOR_SUBMISSION = auto()
    AGREE_NICE_EXAMPLE = auto()
    DO_NOT_LIKE_EXAMPLE = auto()
    SKIP_THIS_ONE = auto()
    QUIT_REVIEWING = auto()
    SOMEONE_LOVED_YOUR_EXAMPLE = auto()
    PLEASE_ENTER_VALID_REVIEW = auto()
    TOP_FIVE_USERS = auto()
    NO_SUBMISSIONS = auto()
    ENTER_VALID_COMMAND = auto()
    SUBMISSION_DOES_NOT_CONTAIN_MWE = auto()
    CANCEL = auto()
    REVIEW_CANCELLED = auto()
    HELP = auto()
    HELP_MESSAGE = auto()
    DOES_WORDS_FORM_SPECIAL_MEANING = auto()
    FORMS_SPECIAL_MEANING = auto()
    DOES_NOT_FORM_SPECIAL_MEANING = auto()
    AND = auto()
    REVIEW_QUESTION_POSITIVE = auto()
    REVIEW_QUESTION_NEGATIVE = auto()
    PLEASE_ENTER_ONE_SENTENCE = auto()
    FEEDBACK = auto()
    FEEDBACK_MESSAGE = auto()
    FEEDBACK_URL = auto()
    YOU = auto()
    GAME_HOURS_FINISHED = auto()
    GAME_STARTED = auto()
    GAME_ENDED = auto()
    THANKS_FOR_REVIEW = auto()
    WELCOME_MESSAGE_1 = auto()
    WELCOME_MESSAGE_2 = auto()
    WELCOME_MESSAGE_3 = auto()
    WELCOME_MESSAGE_4 = auto()
    WELCOME_MESSAGE_5 = auto()
    WELCOME_MESSAGE_6 = auto()
    WELCOME_MESSAGE_7 = auto()
    WELCOME_MESSAGE_8 = auto()
    TODAYS_MWE_HELP_MESSAGE_1 = auto()
    TODAYS_MWE_HELP_MESSAGE_2 = auto()
    SUBMISSION_HELP_MESSAGE_1 = auto()
    REVIEW_HELP_MESSAGE_1 = auto()
    REVIEW_HELP_MESSAGE_2 = auto()
    HINT_MESSAGE_1 = auto()
    HINT_MESSAGE_2 = auto()
    HINT_MESSAGE_3 = auto()
    ERROR_OCCURRED = auto()
    NO_SUB_LEFT_TO_REVIEW = auto()
    SCOREBOARD_EMPTY = auto()
    SUBMISSION_CANCELLED = auto()
    SUBMISSION_CONTAINS_ERROR = auto()
    ACHIEVEMENTS = auto()
    LEVEL_MESSAGE = auto()
    FIRST_SUB_ACH_NAME = auto()
    FIRST_SUB_ACH_DESC = auto()
    FIRST_SUB_ACH_CONGRATS_MSG = auto()
    EARLY_BIRD_ACH_NAME = auto()
    EARLY_BIRD_ACH_DESC = auto()
    EARLY_BIRD_ACH_CONGRATS_MSG = auto()
    UNLOCKED_ACHIEVEMENTS = auto()
    SUB_LVL_1_ACH_NAME = auto()
    SUB_LVL_1_ACH_DESC = auto()
    SUB_LVL_1_ACH_CONGRATS_MSG = auto()
    LOCKED_ACHIEVEMENTS = auto()
    SUB_LVL_2_ACH_NAME = auto()
    SUB_LVL_2_ACH_DESC = auto()
    SUB_LVL_2_ACH_CONGRATS_MSG = auto()
    SUB_LVL_3_ACH_NAME = auto()
    SUB_LVL_3_ACH_DESC = auto()
    SUB_LVL_3_ACH_CONGRATS_MSG = auto()
    SUB_LVL_4_ACH_NAME = auto()
    SUB_LVL_4_ACH_DESC = auto()
    SUB_LVL_4_ACH_CONGRATS_MSG = auto()
    SUB_LVL_5_ACH_NAME = auto()
    SUB_LVL_5_ACH_DESC = auto()
    SUB_LVL_5_ACH_CONGRATS_MSG = auto()
    REVIEW_LVL_1_ACH_NAME = auto()
    REVIEW_LVL_1_ACH_DESC = auto()
    REVIEW_LVL_1_ACH_CONGRATS_MSG = auto()
    REVIEW_LVL_2_ACH_NAME = auto()
    REVIEW_LVL_2_ACH_DESC = auto()
    REVIEW_LVL_2_ACH_CONGRATS_MSG = auto()
    REVIEW_LVL_3_ACH_NAME = auto()
    REVIEW_LVL_3_ACH_DESC = auto()
    REVIEW_LVL_3_ACH_CONGRATS_MSG = auto()
    REVIEW_LVL_4_ACH_NAME = auto()
    REVIEW_LVL_4_ACH_DESC = auto()
    REVIEW_LVL_4_ACH_CONGRATS_MSG = auto()
    REVIEW_LVL_5_ACH_NAME = auto()
    REVIEW_LVL_5_ACH_DESC = auto()
    REVIEW_LVL_5_ACH_CONGRATS_MSG = auto()
    USER_DAILY_PLAY_DETAILS_MESSAGE = auto()
    BECOME_NUMBER_ONE_ACH_NAME = auto()
    BECOME_NUMBER_ONE_ACH_DESC = auto()
    BECOME_NUMBER_ONE_ACH_CONGRATS_MSG = auto()
    CHAMPION_ACH_NAME = auto()
    CHAMPION_ACH_DESC = auto()
    CHAMPION_ACH_CONGRATS_MSG = auto()
    LOST_FIRST_FIVE = auto()
    YOUVE_BECOME_LEADER = auto()
    POS_SEP_WORTH_MORE = auto()
    POS_TOG_WORTH_MORE = auto()
    NEG_TOG_WORTH_MORE = auto()
    REPORT_SUBMISSION = auto()
    REPORT_SUBMISSION_REPLY = auto()
    USER_IS_BANNED_MESSAGE = auto()
    LOST_FIRST_THREE = auto()
    REVIEW_WORTH_MORE = auto()
    LOST_FIRST = auto()
    HINT_MESSAGE_4 = auto()
    ASKFORHELP = auto()
    TODAYS_TARGET = auto()
    TWITTER_TIP = auto()
    GAME_TEMPORARILY_STOPPED = auto()
    DISCLAIMER = auto()
    ADD_EMAIL = auto()
    ADD_EMAIL_START = auto()
    INVALID_EMAIL = auto()
    CONFIRM_EMAIL = auto()
    YES = auto()
    NO = auto()
    EMAIL_SET = auto()
    EMAIL_CANCELLED = auto()
    TODAYS_WINNER_WITH_EMAIL = auto()
    TODAYS_WINNER_WITHOUT_EMAIL = auto()
    GAME_STARTED_AGAIN_ANNOUNCEMENT = auto()
    CHAMP_BUT_NO_EMAIL = auto()
    GIFT_CARD_RECIPIENT_NAME = auto()
    GIFT_CARD_MESSAGE = auto()
    SURVEY_MESSAGE = auto()


class Language(Enum):
    ENGLISH = auto()
    TURKISH = auto()
    ITALIAN = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get(self, token: Token):
        if self == Language.ENGLISH:
            return translations[token]["en"]
        elif self == Language.TURKISH:
            return translations[token]["tr"]
        elif self == Language.ITALIAN:
            return translations[token]["it"]


translations = {
    Token.TODAYS_MWE: {
        "en": "Today\'s Idiom",
        "tr": "Günün Deyimi",
        "it": "Modo di dire del giorno"
    },
    Token.SUBMIT: {
        "en": "Submit",
        "tr": "Örnek gönder",
        "it": "Suggerisci"
    },
    Token.REVIEW: {
        "en": "Review",
        "tr": "Örnekleri oyla",
        "it": "Valuta"
    },
    Token.CHANGE_LANGUAGE: {
        "en": "Change language",
        "tr": "Dili değiştir",
        "it": "Cambia lingua"
    },
    Token.SHOW_SCOREBOARD: {
        "en": "Show Scoreboard",
        "tr": "Sıralamaları göster",
        "it": "Mostra la classifica"
    },
    Token.LANGUAGE_ENGLISH: {
        "en": "English (EN) 🇬🇧",
        "tr": "English (EN) 🇬🇧",
        "it": "Inglese (EN) 🇬🇧"
    },
    Token.LANGUAGE_TURKISH: {
        "en": "Türkçe (TR) 🇹🇷",
        "tr": "Türkçe (TR) 🇹🇷",
        "it": "Turco (TR) 🇹🇷"
    },
    Token.LANGUAGE_ITALIAN: {
        "en": "Italian (IT) 🇮🇹",
        "tr": "İtalyanca (IT) 🇮🇹",
        "it": "Italiano (IT) 🇮🇹"
    },
    Token.TODAYS_MWE_REPLY_TEXT: {
        "en": "Today\'s idiom is \'<b><u>%s</u></b>\', meaning: <i>%s</i>",
        "tr": "Günün deyimi \'<b><u>%s</u></b>\', anlamı da: <i>%s</i>",
        "it": "Il modo di dire di oggi è  \'<b><u>%s</u></b>\', che significa: <i>%s</i>"
    },
    Token.SELECT_LANGUAGE: {
        "en": "Please select a language",
        "tr": "Lütfen bir dil seçin.",
        "it": "Seleziona la lingua"
    },
    Token.LANGUAGE_CHANGE_SUCCESSFUL: {
        "en": "Language set to *English*.",
        "tr": "Dil *Türkçe* olarak ayarlandı.",
        "it": "La lingua è *italiano*."
    },
    Token.PLEASE_SELECT_VALID_LANGUAGE: {
        "en": "Please select a valid language",
        "tr": "Lütfen geçerli bir dil seçin.",
        "it": "Seleziona una lingua valida"
    },
    Token.WELCOME_MESSAGE: {
        "en": "Welcome to Dodiom, *%s*",
        "tr": "Dodiom\'a hoşgeldiniz, *%s*",
        "it": "Benvenuti in Dodiom, *%s*"
    },
    Token.PLEASE_ENTER_EXAMPLE: {
        "en": "Please enter an example sentence containing the words \'<b><u>%s</u></b>\'.",
        "tr": "Lütfen \'%s\' sözcüklerini  içeren örnek bir cümle girin.",
        "it": "Inserisci una frase di esempio che contiene le parole <b><u>%s</u></b>\'."
    },
    Token.ENTER_VALID_MWE_CATEGORY: {
        "en": "Please select a valid category",
        "tr": "Lütfen geçerli bir kategori seçin",
        "it": "Seleziona una categoria valida"
    },
    Token.THANKS_FOR_SUBMISSION: {
        "en": "%s! Thank you for your submission! You\'ll earn %d points every time someone likes your example.",
        "tr": "%s! Gönderiniz için teşekkürler, başka bir oyuncu gönderinizi her beğendiğinde %d puan kazanacaksınız.",
        "it": "%s! Grazie per il tuo suggerimento, guadagnerai %d punti ogni volta che a qualcuno piace il tuo esempio."
    },
    Token.AGREE_NICE_EXAMPLE: {
        "en": "👍 I agree. Nice example",
        "tr": "👍 Katılıyorum. Doğru tespit.",
        "it": "👍 Bell\'esempio, sono d\'accordo."
    },
    Token.DO_NOT_LIKE_EXAMPLE: {
        "en": "👎 I do not like this example",
        "tr": "👎 Bu örneği beğenmedim.",
        "it": "👎 Questo esempio non mi piace"
    },
    Token.SKIP_THIS_ONE: {
        "en": "⏭ Skip this one",
        "tr": "⏭ Bu örneği geç",
        "it": "⏭ Salta questo esempio"
    },
    Token.QUIT_REVIEWING: {
        "en": "😱 Quit reviewing",
        "tr": "😱 İncelemeyi bitir",
        "it": "😱 Abbandona la valutazione"
    },
    Token.SOMEONE_LOVED_YOUR_EXAMPLE: {
        "en": "%s! A fellow player liked your example! Check your new place on the scoreboard.",
        "tr": "%s! Örneklerin şu anda beğeni alıyor. Sıralamalardaki yeni yerini merak etmiyor musun?",
        "it": "%s! I tuoi esempi piacciono. Controlla il tuo punteggio sulla classifica"
    },
    Token.PLEASE_ENTER_VALID_REVIEW: {
        "en": "Please enter a valid review",
        "tr": "Lütfen geçerli bir inceleme seçin",
        "it": "Inserisci una valutazione valida"
    },
    Token.TOP_FIVE_USERS: {
        "en": "Here are today\'s top 5 players:\n",
        "tr": "İşte bugünün ilk beşi:\n",
        "it": "Ecco i 5 giocatori top di oggi:\n"
    },
    Token.NO_SUBMISSIONS: {
        "en": "That\'s all the examples we have for you to review right now.",
        "tr": "Şu anda oylayabileceğin başka örnek yok.",
        "it": "Non ci sono altri esempi da valutare."
    },
    Token.ENTER_VALID_COMMAND: {
        "en": "Please enter a valid command",
        "tr": "Lütfen geçerli bir komut girin.",
        "it": "Inserisci un comando valido"
    },
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: {
        "en": "It looks like your submission does not contain the words (*%s*), please enter again.",
        "tr": "Öyle görünüyor ki girdiğin örnekte (*%s*) sözcükleri bulunmamakta, lütfen tekrar gir.",
        "it": "Sembra che il tuo suggerimento non contenga le parole (*%s*), inserisci un nuovo esempio."
    },
    Token.CANCEL: {
        "en": "Cancel",
        "tr": "İptal",
        "it": "Cancella"
    },
    Token.REVIEW_CANCELLED: {
        "en": "Thank you for your reviews.",
        "tr": "İncelemeleriniz için teşekkürler.",
        "it": "Grazie per le tue valutazioni"
    },
    Token.HELP: {
        "en": "Help",
        "tr": "Yardım",
        "it": "Aiuto"
    },
    Token.HELP_MESSAGE: {
        "en": """
Hello 😊

Dodo is trying to learn English, but has a hard time learning English idioms. Could you help him? We ask you to give Dodo plenty of examples, to understand how people use idioms in their daily speech.

Dodo needs lots of  idiom and non-idiom examples.
For example, to learn the idiom \"pull (one\'s leg)\"\nhe needs an idiom example such as \"I don\'t believe you, you\'re just pulling my leg.\" \nand a non-idiom example such as \"For next exercise, pull your leg to your chest.\"
""",
        "tr": """
Merhaba 😊 

Dodo Türkçe öğrenmeye çalışıyor ancak Türkçe deyimleri öğrenmekte çok zorlanıyor. 
Ona yardım eder misin? Senden ricamız Dodo’ya deyimlerin nasıl kullanıldığını anlaması için ona bol bol örnek vermen. 

Dodo’nun deyim olan ve olmayan pek çok örneğe ihtiyacı var.
Mesela “ayvayı yemek” deyimini öğrenmesi için 
“İşte şimdi ayvayı yedik.” deyim örneği ve
“Az önce iki ayva yedim.” deyim olmayan örneği olabilir.

Hadi hemen Dodo’ya yardıma başla.
""",
        "it": """
Ciao 😊
Dodo sta imparando l\'italiano, ma è difficile imparare i modi di dire. Lo puoi aiutare? Ti chiediamo di fornire a Dodo molti esempi per capire come vengono usati i modi di dire. 

A Dodo servono molti esempi di modi di dire italiani e di frasi in cui le stesse espressioni non sono usate come modi di dire ma nei loro significati letterali. Per esempio per imparare l\'espressione  \"prendere\n all\'amo\" ha bisogno di un esempio idiomatico come \"Sa \n come prendere all\'amo il suo capo\" e un esempio non idiomatico come \"Ha preso\n all\'amo una bella trota.\"
"""
    },
    Token.DOES_WORDS_FORM_SPECIAL_MEANING: {
        "en": "Are the words <b><u>%s</u></b> used together as an idiom in this example?",
        "tr": "<b><u>%s</u></b> sözcükleri bu örnekte birlikte deyim olarak kullanılıyor mu?",
        "it": "In questo esempio, le parole <b><u>%s</u></b> sono usate insieme in un modo di dire?"
    },
    Token.FORMS_SPECIAL_MEANING: {
        "en": "Yes, they are.",
        "tr": "Evet",
        "it": "Sì, certo!"
    },
    Token.DOES_NOT_FORM_SPECIAL_MEANING: {
        "en": "Nope",
        "tr": "Hayır",
        "it": "No, per niente!"
    },
    Token.AND: {
        "en": "and",
        "tr": "ve",
        "it": "e"
    },
    Token.REVIEW_QUESTION_POSITIVE: {
        "en": "In the sentence: \n\n%s\n\nDodo was told that the words <b><u>%s</u></b> are used together as an idiom ✔️, would you agree?",
        "tr": "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak kullanılıyor ✔️ denmiş, buna katılıyor musunuz?",
        "it": "In questa frase: \n\n%s\n\n hanno detto  a Dodo che le parole <b><u>%s</u></b> vengono usate insieme con un significato idiomatico ✔️, sei d\'accordo?"
    },
    Token.REVIEW_QUESTION_NEGATIVE: {
        "en": "In the sentence: %s\n\nIt\'s said that words %s are <b><u>NOT</u></b> used together as an idiom❌, would you agree?",
        "tr": "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak <b><u>KULLANILMIYOR</u></b>❌ denmiş, buna katılıyor musunuz?",
        "it": "In questa frase: %s\n\nsi dice che le  parole %s  <b><u>NON </u></b> sono usate insieme con un significato idiomatico❌, sei d\'accordo?"
    },
    Token.PLEASE_ENTER_ONE_SENTENCE: {
        "en": "Your submission contains %d sentences. Please enter just one sentence.",
        "tr": "Gönderiniz %d cümle içeriyor, lütfen sadece bir cümle girin.",
        "it": "La tua proposta contiene %d frasi, inserisci solo una frase."
    },
    Token.FEEDBACK: {
        "en": "Send Feedback",
        "tr": "Geri bildirim gönder",
        "it": "Manda un feedback"
    },
    Token.FEEDBACK_MESSAGE: {
        "en": "Thank you for your interest! You can send a feedback using the following link.",
        "tr": "İlginiz için teşekkürler, geri bildirim yapmak için aşağıdaki linki kullanabilirsiniz.",
        "it": "Grazie per il tuo interesse, puoi inviare un feedback usando il link seguente"
    },
    Token.FEEDBACK_URL: {
        "en": "https://docs.google.com/forms/d/e/1FAIpQLSdLLHB0DyGI_7piMq1WESPWk5wZGfe3knMFnMw3b0-GgBU3-Q/viewform?usp=pp_url&entry.1179483000=%s",
        "tr": "https://docs.google.com/forms/d/e/1FAIpQLSdLLHB0DyGI_7piMq1WESPWk5wZGfe3knMFnMw3b0-GgBU3-Q/viewform?usp=pp_url&entry.1179483000=%s",
        "it": ""
    },
    Token.YOU: {
        "en": "You",
        "tr": "Sen",
        "it": "Tu"
    },
    Token.GAME_HOURS_FINISHED: {
        "en": "Today\'s game has ended. The new game will start at %d am UTC.",
        "tr": "Oyun bugünlük bitti, yeni günün oyunu saat %d\'de tekrar başlayacak.",
        "it": "Il gioco di oggi è terminato, il nuovo gioco inizierà alle %d di mattina"
    },
    Token.GAME_STARTED: {
        "en": "Good morning! Dodo has started a new game.",
        "tr": "Günaydın, yeni oyun başladı.",
        "it": "Buon giorno! Un nuovo gioco è iniziato. Vi ricordo che oggi il 🎖 Campione del giorno  riceverà un buono di € 5,00 da spendere su http://Amazon.it digitale."
    },
    Token.GAME_ENDED: {
        "en": "The game has ended for today. Thank you for playing!",
        "tr": "Oyun bugünlük bitti, oynadığınız için teşekkürler. Yeni günün oyunu yarın saat 9:00\'da başlayacak.",
        "it": "Il gioco è terminato per oggi, grazie per aver giocato."
    },
    Token.THANKS_FOR_REVIEW: {
        "en": "%s! You earned %d points.",
        "tr": "%s! %d puan kazandın.",
        "it": "%s! Hai guadagnato %d punti."
    },
    Token.WELCOME_MESSAGE_1: {
        "en": "Hello, my name is Dodo.",
        "tr": "Merhaba ben Dodo.",
        "it": "Ciao, sono Dodo."
    },
    Token.WELCOME_MESSAGE_2: {
        "en": "I\'m trying to learn English, but I have trouble understanding idioms.",
        "tr": "Türkçe öğrenmeye çalışıyorum ancak deyimleri anlamakta çok zorlanıyorum.",
        "it": "Sto cercando di imparare l\'italiano ma ho difficoltà a capire i modi di dire."
    },
    Token.WELCOME_MESSAGE_3: {
        "en": "Can you help me?",
        "tr": "Bana yardım eder misin?",
        "it": "Mi aiuti?"
    },
    Token.WELCOME_MESSAGE_4: {
        "en": "Wonder how?",
        "tr": "Nasıl mı?",
        "it": "Ti chiedi come puoi aiutarmi?"
    },
    Token.WELCOME_MESSAGE_5: {
        "en": "I need plenty of idiom  and non-idiom examples.",
        "tr": "Bana hem deyim olan hem de deyim olmayan bol bol örnek lazım.",
        "it": "Semplice! Dammi diversi esempi di modi di dire italiani e di frasi in cui le stesse espressioni non sono usate come modi di dire ma nei loro significati letterali."
    },
    Token.WELCOME_MESSAGE_6: {
        "en": "For example, in order to learn the idiom \"pull (one\'s) leg\"\nI need an idiom example such as \"I don\'t believe you, you\'re just pulling my leg.\" \n and a non-idiom example such as \"For next exercise, pull your leg to your chest.\"",
        "tr": "Mesela “ayvayı yemek” deyimini öğrenmem için\n“İşte şimdi ayvayı yedik.” deyim örneği\n“Az önce iki ayva yedim.” deyim olmayan örnek",
        "it": "Per esempio, per imparare il modo di dire \"prendere all\'amo\"\n ho bisogno di una frase come \"Sa come prendere all\'amo il suo capo\" \n  e un di un’altra in cui la stessa espressione non viene usata in modo  idiomatico. Ad esempio: \"Ha preso all\'amo una bella trota\"."
    },
    Token.WELCOME_MESSAGE_7: {
        "en": "Now, click on <b><u>Today\'s Idiom</u></b> from the keyboard.",
        "tr": "Şimdi bugünün deyimini seçmek için klavyeden <b><u>Günün Deyimi</u></b>\'ni seç",
        "it": "Ora, clicca su <b><u>Modo di dire del giorno</u></b> sulla tastiera."
    },
    Token.WELCOME_MESSAGE_8: {
        "en": "If you can\'t see the keyboard, click on the rectangular shape as shown in the picture.",
        "tr": "Eğer klavyeyi göremiyorsan resimde görülen içinde dört tane daire olan dikdörtgene tıkla.",
        "it": "Se non vedi la tastiera clicca sulla forma rettangolare come nella figura."
    },
    Token.TODAYS_MWE_HELP_MESSAGE_1: {
        "en": "Awesome, now that you know today\'s idiom, you can help me learn it by sending me some examples.",
        "tr": "Harika, günün deyimini öğrendiğine göre artık örnek göndererek öğrenmeme yardımcı olabilirsin..",
        "it": "Benissimo, ora che conosci il modo di dire di oggi, mi puoi aiutare a impararlo suggerendo qualche esempio."
    },
    Token.TODAYS_MWE_HELP_MESSAGE_2: {
        "en": "To send an example, click <b><u>Submit</u></b> from the keyboard.",
        "tr": "Örnek göndermek için klavyeden <b><u>Örnek Gönder</u></b>\'e tıkla..",
        "it": "Per suggerire un esempio, clicca <b><u>Suggerisci</u></b> sulla tastiera."
    },
    Token.SUBMISSION_HELP_MESSAGE_1: {
        "en": "In this section, you can submit an example for the idiom of the day. You\'ll start earning points when other players like your example.",
        "tr": "Bu kısımda günün deyimi için örnek gönderebilirsin. Daha sonra diğer oyuncular senin örneğini beğendiğinde puan kazanacaksın.",
        "it": "In questa sezione, puoi suggerire un esempio per il modo di dire di oggi."
    },
    Token.REVIEW_HELP_MESSAGE_1: {
        "en": "In this section, you can review other players\' submissions.",
        "tr": "Bu kısımda diğer oyuncuların gönderdiği örnekleri oylayabilirsin.",
        "it": "In questa sezione, puoi valutare i suggerimenti degli altri giocatori."
    },
    Token.REVIEW_HELP_MESSAGE_2: {
        "en": "Both you and the players you review will earn points.",
        "tr": "Hem sen hem de örneklerini oyladığın kişiler puan kazanacak.",
        "it": "Sia tu che il giocatore che valuti guadagnerete punti."
    },
    Token.HINT_MESSAGE_1: {
        "en": "For example, in order to learn the idiom \"pull (one\'s) leg\"\nI need an idiom example such as \"I don\'t believe you, you\'re just pulling my leg.\" \n and a non-idiom example such as \"For next exercise, pull your leg to your chest.\"",
        "tr": "Acele et! Deyimi oluşturan sözcüklerin cümle içerisinde yanyana geldiği ancak deyim anlamı oluşturmadıkları örnekler şu anda daha çok puan kazandırıyor. Örn: “Bugün üç <b><u>ayva yedim</u></b>.",
        "it": "Forza dai! Esempi in cui le parole che compongono il modo di dire sono vicine ma non vengono usate in senso idiomatico guadagnano ora più punti. Es.: Ha preso all\'amo una bella trota."
    },
    Token.HINT_MESSAGE_2: {
        "en": "Review others\' submissions to earn more points.",
        "tr": "Daha fazla puan kazanmak için başkalarının örneklerini oylayabilirsin.",
        "it": "Valuta i suggerimenti degli altri per guadagnare più punti."
    },
    Token.HINT_MESSAGE_3: {
        "en": "Might some other words appear between the idiom\'s words?  \nExample: </u></b>Will you <b><u>give</u></b> smoking <b><u>up</u></b>?\nI have very few examples like this.😢  Help me out - you win more points with such examples.",
        "tr": "Deyimi oluşturan sözcüklerin arasına başka sözcükler de girebiliyormuş.\nÖrn: “İyi mi olur yoksa <b><u>ayvayı</u></b> mı <b><u>yeriz</u></b> göreceğiz”.\nBöyle örneğim çok az 😢 Acele et. Şu anda bu tür örneklerle daha fazla puan kazanabilirsin.",
        "it": "Sai che talvolta ci possono essere altre parole tra le parole del modo di dire? \nEsempio: L\'ha <b><u>preso</u></b> proprio <b><u>all\'amo</u></b>il suo capo!\nHo pochi esempi di questo tipo.😢 Dai forza! Puoi guadagnare più punti con questi esempi."
    },
    Token.ERROR_OCCURRED: {
        "en": "Drat, I had a hiccup. Can you give me a little while and try again?",
        "tr": "Bir hata oldu, lütfen daha sonra tekrar dene.",
        "it": "C\'è stato un errore, prova di nuovo più tardi."
    },
    Token.NO_SUB_LEFT_TO_REVIEW: {
        "en": "I\'m out of submissions for you to review for now. Please come back later! Thank you for your reviews.",
        "tr": "Şu anlık oylayabileceğin başka bir örnek kalmadı, daha sonra tekrar oylamayı deneyebilirsin. Örnekleri oyladığın için teşekkürler.",
        "it": "Non ci sono altri suggerimenti da valutare per ora, prova dopo. Grazie per il tuo aiuto."
    },
    Token.SCOREBOARD_EMPTY: {
        "en": "Scoreboard is empty for now. You can get a head start by sending submissions.",
        "tr": "Bugün sıralamalar henüz oluşmamış. Örnek gönderip oylayarak sıralamalarda öne geçebilirsin.",
        "it": "La classifica ora è vuota. Puoi iniziare subito a guadagnare punti inviando i tuoi suggerimenti."
    },
    Token.SUBMISSION_CANCELLED: {
        "en": "Submission cancelled.",
        "tr": "Gönderi iptal edildi.",
        "it": "Suggerimento cancellato."
    },
    Token.SUBMISSION_CONTAINS_ERROR: {
        "en": "An error occured when I was trying to process your submission. Please enter a different one.",
        "tr": "Girdiğin örneği işlemeye çalışırken bir hatayla karşılaştım, lütfen başka bir örnek gir.",
        "it": "Si è verificato un errore durante il tentativo di elaborare il tuo suggerimento, proponine un altro."
    },
    Token.ACHIEVEMENTS: {
        "en": "Achievements",
        "tr": "Başarımlar",
        "it": "Obiettivi"
    },
    Token.LEVEL_MESSAGE: {
        "en": "<b>Your score:</b> %.2f\n<b>Your level:</b>%d (next: %d points)",
        "tr": "<b>Toplam Skorun:</b> %.2f\n<b>Seviyen:</b> %d (Bir sonraki: %d puanda)",
        "it": "<b>Il tuo punteggio:</b> %.2f\n<b>Il tuo livello:</b>%d (dopo: %d punti)"
    },
    Token.FIRST_SUB_ACH_NAME: {
        "en": "First submission!",
        "tr": "İlk Gönderi!",
        "it": "Primo suggerimento!"
    },
    Token.FIRST_SUB_ACH_DESC: {
        "en": "Send the first submission of the day.",
        "tr": "Günün ilk gönderisini gönder.",
        "it": "Invia il tuo primo suggerimento del giorno."
    },
    Token.FIRST_SUB_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent the first submission of the day and won the 🌅 <b><u>First Submission!</u></b> achievement.",
        "tr": "Tebrikler! Günün ilk gönderisini gönderdin ve 🌅 <b><u>İlk Gönderi</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato il primo suggerimento del giorno e hai raggiunto l\'obiettivo 🌅 <b> <u> Primo suggerimento! </u> </b>."
    },
    Token.EARLY_BIRD_ACH_NAME: {
        "en": "Early Bird",
        "tr": "Erkenci Kuş",
        "it": "Mattiniero"
    },
    Token.EARLY_BIRD_ACH_DESC: {
        "en": "Send a submission in the first half hour after the game started.",
        "tr": "Oyun başladıktan sonraki ilk yarım saat içerisinde bir örnek gönder.",
        "it": "Invia un suggerimento nella prima mezz\'ora dall\'inizio del gioco."
    },
    Token.EARLY_BIRD_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent a submission in the first half hour and won the 🐦 <b><u>Early Bird</u></b> achievement.",
        "tr": "Tebrikler! Oyunun ilk yarım saatinde örnek gönderdin ve 🐦 <b><u>Erkenci Kuş</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato un suggerimento nella prima mezz\'ora e hai raggiunto l\'obiettivo 🐦 <b><u>Mattiniero</u></b>."
    },
    Token.UNLOCKED_ACHIEVEMENTS: {
        "en": "<b>Unlocked achievements</b>",
        "tr": "<b>Açılan başarımlar</b>",
        "it": "<b>Obiettivi sbloccati</b>"
    },
    Token.SUB_LVL_1_ACH_NAME: {
        "en": "Just starting out",
        "tr": "Daha yeni başlıyorum",
        "it": "Appena iniziato"
    },
    Token.SUB_LVL_1_ACH_DESC: {
        "en": "Send 5 submissions in a day.",
        "tr": "Bir günde 5 gönderi gönder.",
        "it": "Invia 5 suggerimenti al giorno."
    },
    Token.SUB_LVL_1_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent your fifth submission and won the <b><u>Just starting out</u></b> achievement.",
        "tr": "Tebrikler! Beşinci gönderini gönderdin ve 🎇 <b><u>Daha yeni başlıyorum</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato il tuo quinto suggerimento e hai raggiunto l\'obiettivo  <b><u>Appena iniziato</u></b> ."
    },
    Token.LOCKED_ACHIEVEMENTS: {
        "en": "<b>Locked achivements</b>",
        "tr": "<b>Kilitli başarımlar</b>",
        "it": "<b>Obiettivi bloccati</b>"
    },
    Token.SUB_LVL_2_ACH_NAME: {
        "en": "Author",
        "tr": "Yazar",
        "it": "Autore"
    },
    Token.SUB_LVL_2_ACH_DESC: {
        "en": "Send 10 submissions in a day.",
        "tr": "Bir günde 10 gönderi gönder.",
        "it": "Invia 10 suggerimenti al giorno."
    },
    Token.SUB_LVL_2_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent your tenth submission and won the ✍️<b><u>Author</u></b> achievement.",
        "tr": "Tebrikler! Onuncu gönderini gönderdin ve ✍️<b><u>Yazar</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato il tuo decimo suggerimento e hai raggiunto l\'obiettivo  <b><u>Autore</u></b> ."
    },
    Token.SUB_LVL_3_ACH_NAME: {
        "en": "Master of Submissions",
        "tr": "Gönderi Üstadı",
        "it": "Campione di suggerimenti"
    },
    Token.SUB_LVL_3_ACH_DESC: {
        "en": "Send 20 submissions in a day.",
        "tr": "Bir günde 20 gönderi gönder.",
        "it": "Invia 20 suggerimenti al giorno"
    },
    Token.SUB_LVL_3_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent your twentieth submission and won the 🗿 <b><u>Master of Submissions</u></b> achievement.",
        "tr": "Tebrikler! Yirminci gönderini gönderdin ve 🗿 <b><u>Gönderi Üstadı</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato il tuo ventesimo suggerimento e ti è stato attribuito l\'obiettivo  <b><u>Campione dei suggerimenti</u></b> ."
    },
    Token.SUB_LVL_4_ACH_NAME: {
        "en": "Idioms Dictionary",
        "tr": "Deyimler Sözlüğü",
        "it": "Dizionario dei modi di dire"
    },
    Token.SUB_LVL_4_ACH_DESC: {
        "en": "Send 40 submissions in a day.",
        "tr": "Bir günde 40 gönderi gönder.",
        "it": "Invia 40 suggerimenti al giorno"
    },
    Token.SUB_LVL_4_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent your fortieth submission and won the 📚 <b><u>Idioms Dictionary</u></b> achievement.",
        "tr": "Tebrikler! Kırkıncı gönderini gönderdin ve 📚 <b><u>Deyimler Sözlüğü</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato il tuo quarantesimo suggerimento e ti è stato attribuito l\'obiettivo  <b><u>Dizionario dei modi di dire</u></b> ."
    },
    Token.SUB_LVL_5_ACH_NAME: {
        "en": "Human Corpus",
        "tr": "İki Ayaklı Derlem",
        "it": "Libro vivente"
    },
    Token.SUB_LVL_5_ACH_DESC: {
        "en": "Send 70 submissions in a day.",
        "tr": "Bir günde 70 gönderi gönder.",
        "it": "Invia 70 suggerimenti al giorno"
    },
    Token.SUB_LVL_5_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve sent your seventieth submission and won the 🦄 <b><u>Human Corpus</u></b> achievement.",
        "tr": "Tebrikler! Yetmişinci gönderini gönderdin ve 🦄 <b><u>İki Ayaklı Derlem</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai inviato il tuo settantesimo suggerimento e ti è stato attribuito l\'obiettivo  <b><u>Libro vivente</u></b> ."
    },
    Token.REVIEW_LVL_1_ACH_NAME: {
        "en": "Helpful",
        "tr": "Yardımsever",
        "it": "Collaborativo"
    },
    Token.REVIEW_LVL_1_ACH_DESC: {
        "en": "Review 10 submissions in a day.",
        "tr": "Bir günde 10 gönderiyi oyla.",
        "it": "Valuta 10 suggerimenti in un giorno."
    },
    Token.REVIEW_LVL_1_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve rated ten submissions and earned the 🤝 <b><u>Helpful</u></b> achievement.",
        "tr": "Tebrikler! On gönderiyi oyladın ve 🤝 <b><u>Yardımsever</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai valutato 10  suggerimenti e ti è stato attribuito l\'obiettivo  <b><u>Collaborativo</u></b> ."
    },
    Token.REVIEW_LVL_2_ACH_NAME: {
        "en": "Voter",
        "tr": "Seçmen",
        "it": "Cavallo di razza"
    },
    Token.REVIEW_LVL_2_ACH_DESC: {
        "en": "Review 20 submissions in a day.",
        "tr": "Bir günde 20 gönderiyi oyla.",
        "it": "Valuta 20 suggerimenti in un giorno."
    },
    Token.REVIEW_LVL_2_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve rated twenty submissions and earned the <b><u>Voter</u></b> achievement.",
        "tr": "Tebrikler! Yirmi gönderiyi oyladın ve 🗳️ <b><u>Seçmen</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai valutato 20  suggerimenti e ti è stato attribuito l\'obiettivo  <b><u>Cavallo di razza</u></b> ."
    },
    Token.REVIEW_LVL_3_ACH_NAME: {
        "en": "Critique",
        "tr": "Kritik",
        "it": "Critico"
    },
    Token.REVIEW_LVL_3_ACH_DESC: {
        "en": "Review 40 submissions in a day.",
        "tr": "Bir günde 40 gönderiyi oyla.",
        "it": "Valuta 40 suggerimenti in un giorno."
    },
    Token.REVIEW_LVL_3_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve rated forty submissions and earned the ✨ <b><u>Critique</u></b> achievement.",
        "tr": "Tebrikler! Kırk gönderiyi oyladın ve ✨ <b><u>Kritik</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai valutato 40 suggerimenti e ti è stato attribuito l\'obiettivo  <b><u>Critico</u></b> ."
    },
    Token.REVIEW_LVL_4_ACH_NAME: {
        "en": "Gourmet",
        "tr": "Gurme",
        "it": "Intenditore"
    },
    Token.REVIEW_LVL_4_ACH_DESC: {
        "en": "Review 80 submissions in a day.",
        "tr": "Bir günde 80 gönderiyi oyla.",
        "it": "Valuta 80 suggerimenti in un giorno."
    },
    Token.REVIEW_LVL_4_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve rated eighty submissions and earned the 🧑‍🍳 <b><u>Gourmet</u></b> achievement.",
        "tr": "Tebrikler! Seksen gönderiyi oyladın ve 🧑‍🍳 <b><u>Gurme</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai valutato 80 suggerimenti e ti è stato attribuito l\'obiettivo  <b><u>Intenditore</u></b> ."
    },
    Token.REVIEW_LVL_5_ACH_NAME: {
        "en": "Reviewer",
        "tr": "Eleştirmen",
        "it": "Revisore"
    },
    Token.REVIEW_LVL_5_ACH_DESC: {
        "en": "Review 160 submissions in a day.",
        "tr": "Bir günde 160 gönderiyi oyla.",
        "it": "Valuta 160 suggerimenti in un giorno."
    },
    Token.REVIEW_LVL_5_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve rated one hundred and sixty submissions and earned the 🕶️ <b><u>Reviewer</u></b> achievement.",
        "tr": "Tebrikler! Yüz altmış gönderiyi oyladın ve 🕶️ <b><u>Eleştirmen</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai valutato 160 suggerimenti e ti è stato attribuito l\'obiettivo  <b><u>Revisore</u></b> ."
    },
    Token.USER_DAILY_PLAY_DETAILS_MESSAGE: {
        "en": "Your submission count today: <b><u>%d</u></b>\nYour review count today: <b><u>%d</u></b>",
        "tr": "Bugünkü gönderi sayınız: <b><u>%d</u></b>\nBugünkü inceleme sayınız: <b><u>%d</u></b>",
        "it": "Numero di tuoi suggerimenti di oggi: <b><u>%d</u></b>\nNumero di tue revisioni di oggi: <b><u>%d</u></b>"
    },
    Token.BECOME_NUMBER_ONE_ACH_NAME: {
        "en": "Leader",
        "tr": "Lider",
        "it": "Leader"
    },
    Token.BECOME_NUMBER_ONE_ACH_DESC: {
        "en": "Be at the top of the scoreboard.",
        "tr": "Sıralamalarda birinci ol.",
        "it": "Sali in cima alla classifica"
    },
    Token.BECOME_NUMBER_ONE_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve risen to the top of the rankings and been awarded with the 🥇 <b><u>Leader</u></b> achievement.",
        "tr": "Tebrikler! Sıralamalarda birinci sıraya yerleştin ve 🥇 <b><u>Lider</u></b> başarımını açtın.",
        "it": "Congratulazioni! Sei salito in cima alla classifica e ti è stato attribuito l\'obiettivo  <b><u>Leader</u></b> ."
    },
    Token.CHAMPION_ACH_NAME: {
        "en": "Champion!",
        "tr": "Şampiyon!",
        "it": "Campione"
    },
    Token.CHAMPION_ACH_DESC: {
        "en": "Finish the day as the leader.",
        "tr": "Günü birinci bitir.",
        "it": "Concludi il giorno da leader"
    },
    Token.CHAMPION_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You\'ve finished the day as the leader and been awarded with the 🎖️ <b><u>Champion!</u></b> achievement.",
        "tr": "Tebrikler! Günü birinci bitirdin ve 🎖️ <b><u>Şampiyon!</u></b> başarımını açtın.",
        "it": "Congratulazioni! Hai concluso il tuo giorno da leader e ti è stato attribuito l\'obiettivo  <b><u>Campione</u></b> ."
    },
    Token.LOST_FIRST_FIVE: {
        "en": "😰 Whoops! You\'ve been bumped out of the leaderboard. No worries, you can increase your ranking by submitting new examples and rating others.",
        "tr": "😰 Tüh, sıralamalarda ilk beşten düştün. Endişelenme! Hemen geri dönüp oynamaya devam et!",
        "it": "😰 Ops! Sei uscito dalla classifica. Non ti preoccupare, puoi scalare la classifica inviando nuovi esempi e valutando gli altri esempi."
    },
    Token.YOUVE_BECOME_LEADER: {
        "en": "🥳 Congratulations! You reached the first place on the leaderboard.",
        "tr": "🥳 Tebrikler! Sıralamalarda ilk sıraya yerleştin.",
        "it": "🥳 Congratulazioni! Sei in cima alla classifica."
    },
    Token.POS_SEP_WORTH_MORE: {
        "en": "Psst! For a limited time, the idiom examples where the idiom\'s words are not adjacent to each other earn 15 points instead of 10 points. (Ex: I <b><u>gave</u></b> <i>everything</i> <b><u>up</u></b> for you.).",
        "tr": "Selam, kısa bir süreliğine deyim olan ama kelimeleri ayrı olan örnekler (Örneğin: Bugün de <b><u>ayvayı</u></b> <i>ben</i> <b><u>yedim</u></b>.) 10 puan yerine 15 puan kazandırıyor.",
        "it": "Sbrigati, per un tempo limitato gli esempi dove le parole del modo di dire non sono vicine  valgono 15 punti, invece di 10. (Ex: Ha<b><u>preso</u></b> <i>il suo capo proprio</i> <b><u>all\'amo</u></b> .)."
    },
    Token.POS_TOG_WORTH_MORE: {
        "en": "Psst! For a limited time idiomatic examples are worth 15 points, instead of 10.",
        "tr": "Acele et, kısa bir süreliğine deyim olan örnekler 10 puan yerine 15 puan kazandırıyor.",
        "it": "Sbrigati, per un tempo limitato gli esempi idiomatici valgono 15 punti, invece di 10."
    },
    Token.NEG_TOG_WORTH_MORE: {
        "en": "Psst! For a limited time, non-idiom examples (such as: For next exercise, <b><u>pull</u></b> your <b><u>leg</u></b> to your chest.) are worth 15 points, instead of 10.",
        "tr": "Acele et, kısa bir süreliğine deyim olmayan örnekler 10 puan yerine 15 puan kazandırıyor.",
        "it": "Sbrigati, per un tempo limitato, esempi non idiomatici (es: \"Ha <b><u>preso all\'amo</u></b> una bella trota\" ) valgono 15 punti, invece di 10."
    },
    Token.REPORT_SUBMISSION: {
        "en": "❗ Report submission",
        "tr": "❗ Örneği şikayet et",
        "it": "❗Segnala un suggerimento"
    },
    Token.REPORT_SUBMISSION_REPLY: {
        "en": "Thanks for keeping Dodiom a better place by reporting bad submissions.",
        "tr": "Kötü örnekleri şikayet ederek Dodiom\'u daha iyi bir yer haline getirdiğin için teşekkür ederiz.",
        "it": "Grazie per rendere Dodiom un posto migliore segnalando suggerimenti inappropriati."
    },
    Token.USER_IS_BANNED_MESSAGE: {
        "en": "Unfortunately, your account has been banned from participating.",
        "tr": "Üzülerek belirtirim ki senin hesabın oynamaktan men edilmiş.",
        "it": "Ci dispiace, il tuo account è stato sospeso."
    },
    Token.LOST_FIRST_THREE: {
        "en": "😰 Bad news. You\'ve lost your place in the Top 3. Keep playing and regain your ranking!",
        "tr": "😰 Çok üzücü. İlk üçteki yerini kaybettin. Oynamaya devam et! Yerini geri kazan!",
        "it": "😰 Cattive notizie. Hai perso la tua posizione tra i primi 3. Continua a giocare e riconquista la tua posizione."
    },
    Token.REVIEW_WORTH_MORE: {
        "en": "Lucky minutes! Review scores has been doubled for a limited time.",
        "tr": "Şanslı Dakikalar! Kısa süreliğine oylama yapmak 2 kat puan kazandırıyor.",
        "it": "Minuti fortunati, il punteggio per le valutazioni è stato raddoppiato per un periodo di tempo limitato."
    },
    Token.LOST_FIRST: {
        "en": "Someone grabbed first place from you. Keep playing to get it back!",
        "tr": "Başka biri birinciliği elinden aldı. Acil müdahale etmelisin!",
        "it": "Qualcuno ti ha soffiato il primo posto, sbrigati a riconquistarlo."
    },
    Token.HINT_MESSAGE_4: {
        "en": "Idiom examples are worth more points now. Keep on submitting examples.",
        "tr": "Deyim olan örnekler şu anda daha çok puan kazandırıyor. Örnek girmeye devam et!",
        "it": "Ora gli esempi di modi di dire valgono più punti. Continua a inviare suggerimenti."
    },
    Token.ASKFORHELP: {
        "en": "Dodo needs %d more examples to learn today\'s idiom. Could you please help?",
        "tr": "Dodonun bugünkü deyimi öğrenebilmesi için halen %d tane örneğe ihtiyacı var. Lütfen yardım eder misin?",
        "it": "Dodo ha bisogno di altri %d esempi per imparare il modo di dire di oggi. Puoi aiutarlo?"
    },
    Token.TODAYS_TARGET: {
        "en": "Dodo needs %d more examples to learn today\'s idiom.",
        "tr": "Dodonun bugünkü deyimi öğrenebilmesi için halen %d tane örneğe ihtiyacı var.",
        "it": "Dodo ha bisogno di altri %d esempi per imparare il modo di dire di oggi."
    },
    Token.TWITTER_TIP: {
        "en": "Pro tip! Search Twitter with today\'s idiom to find examples from the real world. Make sure to edit away bad spelling, #hashtags, and the like.",
        "tr": "",
        "it": "Suggerimento: Cerca su Twitter il modo di dire di oggi per trovare degli esempi d\'uso reali. Assicurati di usare l\'ortografia corretta e di evitare #hashtag o simili."
    },
    Token.GAME_TEMPORARILY_STOPPED: {
        "en": "Thank you for your interest, Dodo took a break from learning for now and will come back with surprises, stay tuned.",
        "tr": "Oyuna ilgin için teşekkürler. Dodo şimdilik öğrenmeye ara verdi ama sürprizlerle geri dönecek, beklemede kal.",
        "it": "Grazie per il tuo interesse, Dodo si è preso una pausa ma tornerà presto con delle sorprese. Rimanete sintonizzati!"
    },
    Token.DISCLAIMER: {
        "en": "Dodiom is a developed for research purposes. In using this bot you accept that the data you add can be used to develop linguistic models. No personal data will be used or forwarded to third parties.",
        "tr": "Dodiom akademik amaçla tasarlanmıştır. Bu botu kullanarak eklediğiniz verinin dil modelleri için kullanılmasını kabul etmiş sayılırsınız. Kişisel veriler kullanılmamakta ve üçüncü şahıslarla paylaşılmamaktadır.",
        "it": "Dodiom è un sistema sviluppato a scopi di ricerca scientifica. Nell\'utilizzare questo bot accetti che i dati che inserisci potranno essere usati per sviluppare modelli linguistici. Nessun dato personale verrà utilizzato o inviato a terze parti."
    },
    Token.ADD_EMAIL: {
        "en": "Add Email",
        "tr": "E-posta Ekle",
        "it": "Aggiungi la tua e-mail"
    },
    Token.ADD_EMAIL_START: {
        "en": "Please enter your e-mail address which you use in the <Book Store Name here>",
        "tr": "Lütfen D&R online mağazasında kullandığın e-posta adresini gir:",
        "it": "Per favore inserisci l\'indirizzo e-mail che usi per Amazon.it digitale."
    },
    Token.INVALID_EMAIL: {
        "en": "It looks like the e-mail address you entered is invalid, please try again.",
        "tr": "Girdiğin e-posta adresinde bir hata var gibi, lütfen tekrar gir.",
        "it": "Il tuo indirizzo e-mail non è valido, per favore riprova."
    },
    Token.CONFIRM_EMAIL: {
        "en": "I saved your e-mail address as <b><u>%s</u></b>, do you accept?",
        "tr": "E-posta adresini <b><u>%s</u></b> olarak aldım, onaylıyor musun?",
        "it": "Ho salvato il tuo indirizzo e-mail come <b><u>%s</u></b>, accetti?"
    },
    Token.YES: {
        "en": "Yes",
        "tr": "Evet",
        "it": "Sì"
    },
    Token.NO: {
        "en": "No",
        "tr": "Hayır",
        "it": "No"
    },
    Token.EMAIL_SET: {
        "en": "I saved your e-mail address as <b><u>%s</u></b>, thank you? You can always update it with: /add_email",
        "tr": "Email\'ini <b><u>%s</u></b> olarak kaydettim, teşekkür ederim. İleride değiştirmek istersen buraya tıklayabilirsin: /eposta_ekle",
        "it": "Ho salvato il tuo indirizzo e-mail come <b><u>%s</u></b>, grazie! Lo puoi sempre aggiornare con: /aggiungi_email"
    },
    Token.EMAIL_CANCELLED: {
        "en": "You cancelled adding email",
        "tr": "Email ekleme işlemi iptal edildi.",
        "it": "Hai cancellato il tuo indirizzo e-mail."
    },
    Token.TODAYS_WINNER_WITH_EMAIL: {
        "en": "We\'ll send ₺25 gift card to you e-mail: <b><u>%s</u></b>",
        "tr": "<b><u>%s</u></b> e-posta adresine 25₺ D&R hediye çeki göndereceğiz.",
        "it": "Ti invieremo un buono regalo Amazon.it digitale di € 5 alla tua e-mail: <b><u>%s</u></b>"
    },
    Token.TODAYS_WINNER_WITHOUT_EMAIL: {
        "en": "To get a ₺25 <BOOK STORE NAME> gift card, please /add_email",
        "tr": "D&R\'dan 25₺ hediye çekini almak için lütfen e-posta adresini ekle: /eposta_ekle",
        "it": "Per ottenere il buono regalo Amazon.it digitale di € 5  per favore /aggiungi_email"
    },
    Token.GAME_STARTED_AGAIN_ANNOUNCEMENT: {
        "en": "Hello, Dodiom is back again. Also now you can win ₺25 gift card from <BOOK STORE NAME> if you finish the day in the first place.",
        "tr": "Selam, Dodiom bütün hızıyla geri döndü, üstelik şimdi günü birinci tamamlayarak D&R online mağazasında kullanabileceğin 25TL\'lik hediye çeki kazanabilirsin.",
        "it": "Ciao, Dodiom è di nuovo qui. Puoi vincere un buono regalo Amazon.it digitale di € 5 se diventi il campione del giorno."
    },
    Token.CHAMP_BUT_NO_EMAIL: {
        "en": "You\'ve became champion recently but haven\'t add email, to get ₺25 <BOOK STORE NAME> gift card, please /add_email",
        "tr": "",
        "it": "Sei diventato il campione ma non hai aggiunto la tua  e-mail, per ottenere il buono regalo Amazon.it digitale di € 5,  per favore /aggiungi_email"
    },
    Token.GIFT_CARD_RECIPIENT_NAME: {
        "en": "Dodiom Champion",
        "tr": "Dodiom Şampiyonu",
        "it": "Campione di Dodiom"
    },
    Token.GIFT_CARD_MESSAGE: {
        "en": "Congratulations, you finished today in the first place and won €2.5 gift card from Amazon. Thank you for playing Dodiom. :)",
        "tr": "Tebrikler, günü birinci bitirdin ve 25 TL D&R hediye çeki kazandın. Dodiom\'u oynadığınız için teşekkür ederim, iyi harcamalar. :)",
        "it": "Congratulazioni, sei il campione del giorno e hai vinto un buono regalo Amazon da € 5. Grazie per aver giocato a Dodiom. :)"
    },
    Token.SURVEY_MESSAGE: {
        "en": "Hey, today Dodo has some very important questions for you: <survey link>",
        "tr": "Hey, Dodo\'nun sana çok önemli soruları var. https://forms.gle/95KvzQ4HpubCxN7W9",
        "it": "Ciao, oggi Dodo ha delle domande molto importanti da farti:  <survey link>"
    },
}


congrats_messages = {
    Language.ENGLISH: [
        "Nice job",
        "Well done",
        "Super",
        "Awesome",
        "Magnificent",
        "Swell",
        "Superb",
        "Monumental",
        "Fantastic",
        "Grand",
        "Wonderful",
        "Majestic",
        "Stupendous",
        "Spectacular",
        "Colossal",
        "Dynamite",
        "Fabulous",
        "Astounding",
        "Great",
        "Marvelous",
        "Phenomenal",
        "Smashing",
        "Terrific",
        "Tremendous",
        "Prodigious",
        "Cool",
        "Groovy",
        "Extraordinary",
        "Tops",
        "Exemplary",
        "Champion",
        "Superhero"
    ],
    Language.TURKISH: [
        "Harika",
        "Süper",
        "Yaşasın",
        "Muhteşem"
    ],
    Language.ITALIAN: [
        "Bel lavoro",
        "Molto bene",
        "Super",
        "Eccezionale"
    ]
}


def get_random_congrats_message(language: Language) -> str:
    return congrats_messages[language][random.randint(0, len(congrats_messages[language]) - 1)]
