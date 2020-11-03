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


class Language(Enum):
    ENGLISH = auto(),
    TURKISH = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get(self, token: Token):
        if self == Language.ENGLISH:
            return translations[token]["en"]
        elif self == Language.TURKISH:
            return translations[token]["tr"]


translations = {
    Token.TODAYS_MWE: {
        "en": "Today's Idiom",
        "tr": "Günün Deyimi"
    },
    Token.SUBMIT: {
        "en": "Submit",
        "tr": "Örnek gönder"
    },
    Token.REVIEW: {
        "en": "Review",
        "tr": "Örnekleri oyla"
    },
    Token.CHANGE_LANGUAGE: {
        "en": "Change language",
        "tr": "Dili değiştir"
    },
    Token.SHOW_SCOREBOARD: {
        "en": "Show Scoreboard",
        "tr": "Sıralamaları göster"
    },
    Token.LANGUAGE_ENGLISH: {
        "en": "English (EN) 🇬🇧",
        "tr": "English (EN) 🇬🇧"
    },
    Token.LANGUAGE_TURKISH: {
        "en": "Türkçe (TR) 🇹🇷",
        "tr": "Türkçe (TR) 🇹🇷"
    },
    Token.TODAYS_MWE_REPLY_TEXT: {
        "en": "Today's idiom is '<b><u>%s</u></b>', meaning: <i>%s</i>",
        "tr": "Günün deyimi '<b><u>%s</u></b>', anlamı da: <i>%s</i>"
    },
    Token.SELECT_LANGUAGE: {
        "en": "Please select a language",
        "tr": "Lütfen bir dil seçin."
    },
    Token.LANGUAGE_CHANGE_SUCCESSFUL: {
        "en": "Language set to *English*.",
        "tr": "Dil *Türkçe* olarak ayarlandı."
    },
    Token.PLEASE_SELECT_VALID_LANGUAGE: {
        "en": "Please select a valid language",
        "tr": "Lütfen geçerli bir dil seçin."
    },
    Token.WELCOME_MESSAGE: {
        "en": "Welcome to Dodiom, *%s*",
        "tr": "Dodiom'a hoşgeldiniz, *%s*"
    },
    Token.PLEASE_ENTER_EXAMPLE: {
        "en": "Please enter an example sentence containing the words '<b><u>%s</u></b>'.",
        "tr": "Lütfen '%s' sözcüklerini  içeren örnek bir cümle girin."
    },
    Token.ENTER_VALID_MWE_CATEGORY: {
        "en": "Please select a valid category",
        "tr": "Lütfen geçerli bir kategori seçin"
    },
    Token.THANKS_FOR_SUBMISSION: {
        "en": "%s! Thank you for your submission, you'll earn %d points every time someone likes your example.",
        "tr": "%s! Gönderiniz için teşekkürler, başka bir oyuncu gönderinizi her beğendiğinde %d puan kazanacaksınız."
    },
    Token.AGREE_NICE_EXAMPLE: {
        "en": "👍 I agree. Nice example ",
        "tr": "👍 Katılıyorum. Doğru tespit."
    },
    Token.DO_NOT_LIKE_EXAMPLE: {
        "en": "👎 I do not like this example",
        "tr": "👎 Bu örneği beğenmedim."
    },
    Token.SKIP_THIS_ONE: {
        "en": "⏭ Skip this one",
        "tr": "⏭ Bu örneği geç"
    },
    Token.QUIT_REVIEWING: {
        "en": "😱 Quit reviewing",
        "tr": "😱 İncelemeyi bitir"
    },
    Token.SOMEONE_LOVED_YOUR_EXAMPLE: {
        "en": "%s! Your samples are currently being liked. Check your new place on the scoreboard.",
        "tr": "%s! Örneklerin şu anda beğeni alıyor. Sıralamalardaki yeni yerini merak etmiyor musun?"
    },
    Token.PLEASE_ENTER_VALID_REVIEW: {
        "en": "Please enter a valid review",
        "tr": "Lütfen geçerli bir inceleme seçin"
    },
    Token.TOP_FIVE_USERS: {
        "en": "Here are the top 5 players today:\n",
        "tr": "İşte bugünün ilk beşi:\n"
    },
    Token.NO_SUBMISSIONS: {
        "en": "There are currently no other examples you may review.",
        "tr": "Şu anda oylayabileceğin başka örnek yok."
    },
    Token.ENTER_VALID_COMMAND: {
        "en": "Please enter a valid command",
        "tr": "Lütfen geçerli bir komut girin."
    },
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: {
        "en": "It looks like your submission does not contain the words (*%s*), please enter again.",
        "tr": "Öyle görünüyor ki girdiğin örnekte (*%s*) sözcükleri bulunmamakta, lütfen tekrar gir."
    },
    Token.CANCEL: {
        "en": "Cancel",
        "tr": "İptal"
    },
    Token.REVIEW_CANCELLED: {
        "en": "Thank you for your reviews.",
        "tr": "İncelemeleriniz için teşekkürler."
    },
    Token.HELP: {
        "en": "Help",
        "tr": "Yardım"
    },
    Token.HELP_MESSAGE: {
        "en": """
Hello 😊

Dodo is trying to learn English but has a hard time learning English idioms. Could you help him? We ask you to give Dodo plenty of examples to understand how idioms are used.

Dodo needs lots of  idiom  and non-idiom examples.
For example, to learn the idiom give up\"\nit needs an idiom example such as \"Ok, I give up now.\" \n and a non-idiom example such as \"Can you give that book up to me?\"
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
"""
    },
    Token.DOES_WORDS_FORM_SPECIAL_MEANING: {
        "en": "Are the words <b><u>%s</u></b> used together as an idiom in this example?        ",
        "tr": "<b><u>%s</u></b> sözcükleri bu örnekte birlikte deyim olarak kullanılıyor mu?"
    },
    Token.FORMS_SPECIAL_MEANING: {
        "en": "Come on, start helping Dodo now. \"",
        "tr": "Evet"
    },
    Token.DOES_NOT_FORM_SPECIAL_MEANING: {
        "en": "Nope",
        "tr": "Hayır"
    },
    Token.AND: {
        "en": "and",
        "tr": "ve"
    },
    Token.REVIEW_QUESTION_POSITIVE: {
        "en": "In the sentence: \n\n%s\n\nIt's said that the words <b><u>%s</u></b> are used together as an idiom ✔️, would you agree?",
        "tr": "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak kullanılıyor ✔️ denmiş, buna katılıyor musunuz?"
    },
    Token.REVIEW_QUESTION_NEGATIVE: {
        "en": "In the sentence: %s\n\nIt's said that words %s are <b><u>NOT</u></b> used together as an idiom❌, would you agree?",
        "tr": "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak <b><u>KULLANILMIYOR</u></b>❌ denmiş, buna katılıyor musunuz?"
    },
    Token.PLEASE_ENTER_ONE_SENTENCE: {
        "en": "Your submission contains %d sentences, please enter just one sentence.",
        "tr": "Gönderiniz %d cümle içeriyor, lütfen sadece bir cümle girin."
    },
    Token.FEEDBACK: {
        "en": "Send Feedback",
        "tr": "Geri bildirim gönder"
    },
    Token.FEEDBACK_MESSAGE: {
        "en": "Thank you for your interest, you can send a feedback using the following link.",
        "tr": "İlginiz için teşekkürler, geri bildirim yapmak için aşağıdaki linki kullanabilirsiniz."
    },
    Token.FEEDBACK_URL: {
        "en": "https://docs.google.com/forms/d/e/1FAIpQLSdLLHB0DyGI_7piMq1WESPWk5wZGfe3knMFnMw3b0-GgBU3-Q/viewform?usp=pp_url&entry.1179483000=%s",
        "tr": "https://docs.google.com/forms/d/e/1FAIpQLSdLLHB0DyGI_7piMq1WESPWk5wZGfe3knMFnMw3b0-GgBU3-Q/viewform?usp=pp_url&entry.1179483000=%s"
    },
    Token.YOU: {
        "en": "You",
        "tr": "Sen"
    },
    Token.GAME_HOURS_FINISHED: {
        "en": "Today's game has ended,  the new game will start at %d am.",
        "tr": "Oyun bugünlük bitti, yeni günün oyunu saat %d'da tekrar başlayacak."
    },
    Token.GAME_STARTED: {
        "en": "Good morning! A new game has been started.",
        "tr": "Günaydın, yeni oyun başladı."
    },
    Token.GAME_ENDED: {
        "en": "The game has ended for today, thank you for playing.",
        "tr": "Oyun bugünlük bitti, oynadığınız için teşekkürler. Yeni günün oyunu yarın saat 9:00'da başlayacak."
    },
    Token.THANKS_FOR_REVIEW: {
        "en": "%s! You earned %d points.",
        "tr": "%s! %d puan kazandın."
    },
    Token.WELCOME_MESSAGE_1: {
        "en": "Hello, my name is Dodo.",
        "tr": "Merhaba ben Dodo."
    },
    Token.WELCOME_MESSAGE_2: {
        "en": "I'm trying to learn English but having troubles understanding idioms.",
        "tr": "Türkçe öğrenmeye çalışıyorum ancak deyimleri anlamakta çok zorlanıyorum."
    },
    Token.WELCOME_MESSAGE_3: {
        "en": "Can you help me?",
        "tr": "Bana yardım eder misin?"
    },
    Token.WELCOME_MESSAGE_4: {
        "en": "Wonder how?",
        "tr": "Nasıl mı?"
    },
    Token.WELCOME_MESSAGE_5: {
        "en": "I need plenty of  idiom  and non-idiom examples.",
        "tr": "Bana hem deyim olan hem de deyim olmayan bol bol örnek lazım."
    },
    Token.WELCOME_MESSAGE_6: {
        "en": "For example, in order to learn the idiom \"Give up\"\nI need an idiom example such as \"Ok, I give up now.\" \n and a non-idiom example such as \"Can you give that book up to me?\" ",
        "tr": "Mesela “ayvayı yemek” deyimini öğrenmem için\n“İşte şimdi ayvayı yedik.” deyim örneği\n“Az önce iki ayva yedim.” deyim olmayan örnek"
    },
    Token.WELCOME_MESSAGE_7: {
        "en": "Now,  click on <b><u>Today's Idiom</u></b> from the keyboard.",
        "tr": "Şimdi bugünün deyimini seçmek için klavyeden <b><u>Günün Deyimi</u></b>'ni seç"
    },
    Token.WELCOME_MESSAGE_8: {
        "en": "If you can't see the keyboard, click on the rectangular shape as shown in the picture.",
        "tr": "Eğer klavyeyi göremiyorsan resimde görülen içinde dört tane daire olan dikdörtgene tıkla."
    },
    Token.TODAYS_MWE_HELP_MESSAGE_1: {
        "en": "Awesome, now that you know today's idiom, you can help me learn it by sending some examples.",
        "tr": "Harika, günün deyimini öğrendiğine göre artık örnek göndererek öğrenmeme yardımcı olabilirsin.."
    },
    Token.TODAYS_MWE_HELP_MESSAGE_2: {
        "en": "To send an example, click <b><u>Submit</u></b> from the keyboard.",
        "tr": "Örnek göndermek için klavyeden <b><u>Örnek Gönder</u></b>'e tıkla.."
    },
    Token.SUBMISSION_HELP_MESSAGE_1: {
        "en": "In this section, you can submit an example for the idiom of the day. You'll start earning points when other players like your example.",
        "tr": "Bu kısımda günün deyimi için örnek gönderebilirsin. Daha sonra diğer oyuncular senin örneğini beğendiğinde puan kazanacaksın."
    },
    Token.REVIEW_HELP_MESSAGE_1: {
        "en": "In this section, you can review other players' submissions.",
        "tr": "Bu kısımda diğer oyuncuların gönderdiği örnekleri oylayabilirsin."
    },
    Token.REVIEW_HELP_MESSAGE_2: {
        "en": "Both you and the players you review will earn points.",
        "tr": "Hem sen hem de örneklerini oyladığın kişiler puan kazanacak."
    },
    Token.HINT_MESSAGE_1: {
        "en": "Hurry up! Examples where the words that make up the phrase are next to each other within a sentence but do not form an idiom now earn more points. Ex: Will you please <b><u>give up</u></b> that book to me?",
        "tr": "Acele et! Deyimi oluşturan sözcüklerin cümle içerisinde yanyana geldiği ancak deyim anlamı oluşturmadıkları örnekler şu anda daha çok puan kazandırıyor. Örn: “Bugün üç <b><u>ayva yedim</u></b>."
    },
    Token.HINT_MESSAGE_2: {
        "en": "Review others' submissions to earn more points.",
        "tr": "Daha fazla puan kazanmak için başkalarının örneklerini oylayabilirsin."
    },
    Token.HINT_MESSAGE_3: {
        "en": "Do you know, that some other words may appear between the idiom's words.\nExample: Will you <b><u>give</u></b> smoking <b><u>up</u></b>?\nI have very few examples like this.😢 Hurry up, you can earn more points with such examples.",
        "tr": "Deyimi oluşturan sözcüklerin arasına başka sözcükler de girebiliyormuş.\nÖrn: “İyi mi olur yoksa <b><u>ayvayı</u></b> mı <b><u>yeriz</u></b> göreceğiz”.\nBöyle örneğim çok az 😢 Acele et. Şu anda bu tür örneklerle daha fazla puan kazanabilirsin."
    },
    Token.ERROR_OCCURRED: {
        "en": "An error occurred, please try again later.",
        "tr": "Bir hata oldu, lütfen daha sonra tekrar dene."
    },
    Token.NO_SUB_LEFT_TO_REVIEW: {
        "en": "There are no more submissions left to review for now, please try later. Thank you for your reviews.",
        "tr": "Şu anlık oylayabileceğin başka bir örnek kalmadı, daha sonra tekrar oylamayı deneyebilirsin. Örnekleri oyladığın için teşekkürler."
    },
    Token.SCOREBOARD_EMPTY: {
        "en": "Scoreboard is empty for now. You can get a head start by sending submissions.",
        "tr": "Bugün sıralamalar henüz oluşmamış. Örnek gönderip oylayarak sıralamalarda öne geçebilirsin."
    },
    Token.SUBMISSION_CANCELLED: {
        "en": "Submission cancelled.",
        "tr": "Gönderi iptal edildi."
    },
    Token.SUBMISSION_CONTAINS_ERROR: {
        "en": "An error occured when I was trying to process your submission, please enter a different one.",
        "tr": "Girdiğin örneği işlemeye çalışırken bir hatayla karşılaştım, lütfen başka bir örnek gir."
    },
    Token.ACHIEVEMENTS: {
        "en": "Achievements",
        "tr": "Başarımlar"
    },
    Token.LEVEL_MESSAGE: {
        "en": "<b>Your score:</b> %.2f\n<b>Your level:</b>%d (next: %d points)",
        "tr": "<b>Toplam Skorun:</b> %.2f\n<b>Seviyen:</b> %d (Bir sonraki: %d puanda)"
    },
    Token.FIRST_SUB_ACH_NAME: {
        "en": "First Submission!",
        "tr": "İlk Gönderi!"
    },
    Token.FIRST_SUB_ACH_DESC: {
        "en": "Send the first submission of the day.",
        "tr": "Günün ilk gönderisini gönder."
    },
    Token.FIRST_SUB_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent the first submission of the day and awarded with the 🌅 <b><u>First Submission!</u></b> achievement.",
        "tr": "Tebrikler! Günün ilk gönderisini gönderdin ve 🌅 <b><u>İlk Gönderi</u></b> başarımını açtın."
    },
    Token.EARLY_BIRD_ACH_NAME: {
        "en": "Early Bird",
        "tr": "Erkenci Kuş"
    },
    Token.EARLY_BIRD_ACH_DESC: {
        "en": "Send a submission in the first half hour after the game started.",
        "tr": "Oyun başladıktan sonraki ilk yarım saat içerisinde bir örnek gönder."
    },
    Token.EARLY_BIRD_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent a submission in the first half hour and awarded with the 🐦 <b><u>Early Bird</u></b> achievement.",
        "tr": "Tebrikler! Oyunun ilk yarım saatinde örnek gönderdin ve 🐦 <b><u>Erkenci Kuş</u></b> başarımını açtın."
    },
    Token.UNLOCKED_ACHIEVEMENTS: {
        "en": "<b>Unlocked achivements</b>",
        "tr": "<b>Açılan başarımlar</b>"
    },
    Token.SUB_LVL_1_ACH_NAME: {
        "en": "Just starting out",
        "tr": "Daha yeni başlıyorum"
    },
    Token.SUB_LVL_1_ACH_DESC: {
        "en": "Send 5 submissions in a day.",
        "tr": "Bir günde 5 gönderi gönder."
    },
    Token.SUB_LVL_1_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent your fifth submission and awarded with the <b><u>Just starting out</u></b> achievement.",
        "tr": "Tebrikler! Beşinci gönderini gönderdin ve 🎇 <b><u>Daha yeni başlıyorum</u></b> başarımını açtın."
    },
    Token.LOCKED_ACHIEVEMENTS: {
        "en": "<b>Locked achivements</b>",
        "tr": "<b>Kilitli başarımlar</b>"
    },
    Token.SUB_LVL_2_ACH_NAME: {
        "en": "Author",
        "tr": "Yazar"
    },
    Token.SUB_LVL_2_ACH_DESC: {
        "en": "Send 10 submissions in a day.",
        "tr": "Bir günde 10 gönderi gönder."
    },
    Token.SUB_LVL_2_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent your tenth submission and awarded with the ✍️<b><u>Author</u></b> achievement.",
        "tr": "Tebrikler! Onuncu gönderini gönderdin ve ✍️<b><u>Yazar</u></b> başarımını açtın."
    },
    Token.SUB_LVL_3_ACH_NAME: {
        "en": "Master of Submissions",
        "tr": "Gönderi Üstadı"
    },
    Token.SUB_LVL_3_ACH_DESC: {
        "en": "Send 20 submissions in a day.",
        "tr": "Bir günde 20 gönderi gönder."
    },
    Token.SUB_LVL_3_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent your twentieth submission and awarded with the 🗿 <b><u>Master of Submissions</u></b> achievement.",
        "tr": "Tebrikler! Yirminci gönderini gönderdin ve 🗿 <b><u>Gönderi Üstadı</u></b> başarımını açtın."
    },
    Token.SUB_LVL_4_ACH_NAME: {
        "en": "Idioms Dictionary",
        "tr": "Deyimler Sözlüğü"
    },
    Token.SUB_LVL_4_ACH_DESC: {
        "en": "Send 40 submissions in a day.",
        "tr": "Bir günde 40 gönderi gönder."
    },
    Token.SUB_LVL_4_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent your fortieth submission and awarded with the 📚 <b><u>Idioms Dictionary</u></b> achievement.",
        "tr": "Tebrikler! Kırkıncı gönderini gönderdin ve 📚 <b><u>Deyimler Sözlüğü</u></b> başarımını açtın."
    },
    Token.SUB_LVL_5_ACH_NAME: {
        "en": "Alive Corpus",
        "tr": "İki Ayaklı Derlem"
    },
    Token.SUB_LVL_5_ACH_DESC: {
        "en": "Send 70 submissions in a day.",
        "tr": "Bir günde 70 gönderi gönder."
    },
    Token.SUB_LVL_5_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've sent your fortieth submission and awarded with the 🦄 <b><u>Human Corpus</u></b> achievement.",
        "tr": "Tebrikler! Yetmişinci gönderini gönderdin ve 🦄 <b><u>İki Ayaklı Derlem</u></b> başarımını açtın."
    },
    Token.REVIEW_LVL_1_ACH_NAME: {
        "en": "Helpful",
        "tr": "Yardımsever"
    },
    Token.REVIEW_LVL_1_ACH_DESC: {
        "en": "Review 10 submissions in a day.",
        "tr": "Bir günde 10 gönderiyi oyla."
    },
    Token.REVIEW_LVL_1_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've rated ten submissions and awarded with the 🤝 <b><u>Helpful</u></b> achievement.",
        "tr": "Tebrikler! On gönderiyi oyladın ve 🤝 <b><u>Yardımsever</u></b> başarımını açtın."
    },
    Token.REVIEW_LVL_2_ACH_NAME: {
        "en": "Voter",
        "tr": "Seçmen"
    },
    Token.REVIEW_LVL_2_ACH_DESC: {
        "en": "Review 20 submissions in a day.",
        "tr": "Bir günde 20 gönderiyi oyla."
    },
    Token.REVIEW_LVL_2_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've rated twenty submissions and awarded with the <b><u>Voter</u></b> achievement.",
        "tr": "Tebrikler! Yirmi gönderiyi oyladın ve 🗳️ <b><u>Seçmen</u></b> başarımını açtın."
    },
    Token.REVIEW_LVL_3_ACH_NAME: {
        "en": "Critique",
        "tr": "Kritik"
    },
    Token.REVIEW_LVL_3_ACH_DESC: {
        "en": "Review 40 submissions in a day.",
        "tr": "Bir günde 40 gönderiyi oyla."
    },
    Token.REVIEW_LVL_3_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've rated forty submissions and awarded with the ✨ <b><u>Critique</u></b> achievement.",
        "tr": "Tebrikler! Kırk gönderiyi oyladın ve ✨ <b><u>Kritik</u></b> başarımını açtın."
    },
    Token.REVIEW_LVL_4_ACH_NAME: {
        "en": "Gourmet",
        "tr": "Gurme"
    },
    Token.REVIEW_LVL_4_ACH_DESC: {
        "en": "Review 80 submissions in a day.",
        "tr": "Bir günde 80 gönderiyi oyla."
    },
    Token.REVIEW_LVL_4_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've rated eighty submissions and awarded with the 🧑‍🍳 <b><u>Gourmet</u></b> achievement.",
        "tr": "Tebrikler! Seksen gönderiyi oyladın ve 🧑‍🍳 <b><u>Gurme</u></b> başarımını açtın."
    },
    Token.REVIEW_LVL_5_ACH_NAME: {
        "en": "Reviewer",
        "tr": "Eleştirmen"
    },
    Token.REVIEW_LVL_5_ACH_DESC: {
        "en": "Review 160 submissions in a day.",
        "tr": "Bir günde 160 gönderiyi oyla."
    },
    Token.REVIEW_LVL_5_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've rated one hundred and sixty submissions and awarded with the 🕶️ <b><u>Reviewer</u></b> achievement.",
        "tr": "Tebrikler! Yüz altmış gönderiyi oyladın ve 🕶️ <b><u>Eleştirmen</u></b> başarımını açtın."
    },
    Token.USER_DAILY_PLAY_DETAILS_MESSAGE: {
        "en": "Your submission count today: <b><u>%d</u></b>\nYour review count today: <b><u>%d</u></b>",
        "tr": "Bugünkü gönderi sayınız: <b><u>%d</u></b>\nBugünkü inceleme sayınız: <b><u>%d</u></b>"
    },
    Token.BECOME_NUMBER_ONE_ACH_NAME: {
        "en": "Leader",
        "tr": "Lider"
    },
    Token.BECOME_NUMBER_ONE_ACH_DESC: {
        "en": "Be at the top of the scoreboard.",
        "tr": "Sıralamalarda birinci ol."
    },
    Token.BECOME_NUMBER_ONE_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've risen to the top of the rankings and awarded with the 🥇 <b><u>Leader</u></b> achievement.",
        "tr": "Tebrikler! Sıralamalarda birinci sıraya yerleştin ve 🥇 <b><u>Lider</u></b> başarımını açtın."
    },
    Token.CHAMPION_ACH_NAME: {
        "en": "Champion!",
        "tr": "Şampiyon!"
    },
    Token.CHAMPION_ACH_DESC: {
        "en": "Finish the day as the leader.",
        "tr": "Günü birinci bitir."
    },
    Token.CHAMPION_ACH_CONGRATS_MSG: {
        "en": "Congratulations! You've finished the day as the leader and awarded with the 🎖️ <b><u>Champion!</u></b> achievement.",
        "tr": "Tebrikler! Günü birinci bitirdin ve 🎖️ <b><u>Şampiyon!</u></b> başarımını açtın."
    },
    Token.LOST_FIRST_FIVE: {
        "en": "😰 Whoops! You've dropped out of the leaderboard. No worries, you can increase your ranking by submitting new examples and rating others.",
        "tr": "😰 Tüh, sıralamalarda ilk beşten düştün. Endişelenme! Hemen geri dönüp oynamaya devam et!"
    },
    Token.YOUVE_BECOME_LEADER: {
        "en": "🥳 Congratulations! You reached the first place on the leaderboard.",
        "tr": "🥳 Tebrikler! Sıralamalarda ilk sıraya yerleştin."
    },
    Token.POS_SEP_WORTH_MORE: {
        "en": "Hey, for a limited time, the idiom examples where the idiom's words are not adjacent to each other earn 15 points instead of 10 points. (Ex: I <b><u>gave</u></b> <i>everything</i> <b><u>up</u></b> for you.).",
        "tr": "Selam, kısa bir süreliğine deyim olan ama kelimeleri ayrı olan örnekler (Örneğin: Bugün de <b><u>ayvayı</u></b> <i>ben</i> <b><u>yedim</u></b>.) 10 puan yerine 15 puan kazandırıyor."
    },
    Token.POS_TOG_WORTH_MORE: {
        "en": "Hurry up, for a limited time idiomatic examples worth 15 points, instead of 10.",
        "tr": "Acele et, kısa bir süreliğine deyim olan örnekler 10 puan yerine 15 puan kazandırıyor."
    },
    Token.NEG_TOG_WORTH_MORE: {
        "en": "Hurry up, for a limited time, non-idiom examples (such as: Will you please <b><u>give up</u></b> that book to me?) worth 15 points, instead of 10.",
        "tr": "Acele et, kısa bir süreliğine deyim olmayan örnekler 10 puan yerine 15 puan kazandırıyor."
    },
    Token.REPORT_SUBMISSION: {
        "en": "❗ Report submission",
        "tr": "❗ Örneği şikayet et"
    },
    Token.REPORT_SUBMISSION_REPLY: {
        "en": "Thanks for keeping Dodiom a better place by reporting bad submissions.",
        "tr": "Kötü örnekleri şikayet ederek Dodiom'u daha iyi bir yer haline getirdiğin için teşekkür ederiz."
    },
    Token.USER_IS_BANNED_MESSAGE: {
        "en": "Unfortunately, your account has been banned from participating.",
        "tr": "Üzülerek belirtirim ki senin hesabın oynamaktan men edilmiş."
    },
    Token.LOST_FIRST_THREE: {
        "en": "😰 Bad news. You've lost your place in the top 3. Keep playing and take your place back.",
        "tr": "😰 Çok üzücü. İlk üçteki yerini kaybettin. Oynamaya devam et! Yerini geri kazan!"
    },
    Token.REVIEW_WORTH_MORE: {
        "en": "Lucky minutes, review scores has been doubled for a limited time.",
        "tr": "Şanslı Dakikalar! Kısa süreliğine oylama yapmak 2 kat puan kazandırıyor."
    },
    Token.LOST_FIRST: {
        "en": "Someone took the first place from you, you need to hurry to get it back.",
        "tr": "Başka biri birinciliği elinden aldı. Acil müdahale etmelisin!"
    },
    Token.HINT_MESSAGE_4: {
        "en": "Idiom examples worth more points now. Continue submitting examples.",
        "tr": "Deyim olan örnekler şu anda daha çok puan kazandırıyor. Örnek girmeye devam et!"
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
    ]
}


def get_random_congrats_message(language: Language) -> str:
    return congrats_messages[language][random.randint(0, len(congrats_messages[language]) - 1)]
