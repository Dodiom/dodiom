from enum import Enum, auto
import random


class Token(Enum):
    MAIN_KEYBOARD = auto()
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
    I_NEED_PT_EXAMPLES = auto()
    I_NEED_PS_EXAMPLES = auto()
    I_NEED_NT_EXAMPLES = auto()
    I_NEED_NS_EXAMPLES = auto()
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
        "en": "Today's MWE",
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
        "en": "Today's MWE is '<b><u>%s</u></b>', meaning: <i>%s</i>",
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
        "en": "Please enter your example for the MWE: '<b><u>%s</u></b>'",
        "tr": "Lütfen '%s' sözcüklerini  içeren örnek bir cümle girin."
    },
    Token.ENTER_VALID_MWE_CATEGORY: {
        "en": "Please enter a valid category",
        "tr": "Lütfen geçerli bir kategori seçin"
    },
    Token.THANKS_FOR_SUBMISSION: {
        "en": "%s! Thank you for your submission, you'll win %d points every time someone likes your example.",
        "tr": "%s! Gönderiniz için teşekkürler, başka bir oyuncu gönderinizi her beğendiğinde %d puan kazanacaksınız."
    },
    Token.AGREE_NICE_EXAMPLE: {
        "en": '👍 I agree. Nice example for this category',
        "tr": '👍 Katılıyorum. Doğru tespit.'
    },
    Token.DO_NOT_LIKE_EXAMPLE: {
        "en": '👎 I do not like this example',
        "tr": '👎 Bu örneği beğenmedim.'
    },
    Token.SKIP_THIS_ONE: {
        "en": '⏭ Skip this one',
        "tr": '⏭ Bu örneği geç'
    },
    Token.QUIT_REVIEWING: {
        "en": '😱 Quit reviewing',
        "tr": '😱 İncelemeyi bitir'
    },
    Token.SOMEONE_LOVED_YOUR_EXAMPLE: {
        "en": "%s! Someone else loved your great example, and you’ve earned %d points",
        "tr": "%s! Birisi örneğini beğendi, sen de %d puan kazandın."
    },
    Token.PLEASE_ENTER_VALID_REVIEW: {
        "en": "Please enter a valid review",
        "tr": "Lütfen geçerli bir inceleme seçin"
    },
    Token.TOP_FIVE_USERS: {
        "en": "Here are the top 5 users for today:\n",
        "tr": "İşte bugünün ilk beşi:\n"
    },
    Token.NO_SUBMISSIONS: {
        "en": "There are no submissions and users at this time.",
        "tr": "Şu anda oylayabileceğin başka örnek yok."
    },
    Token.ENTER_VALID_COMMAND: {
        "en": "Please enter a valid command",
        "tr": "Lütfen geçerli bir komut girin."
    },
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: {
        "en": "It looks like your submission does not contain todays MWE (*%s*), please enter again.",
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
        "en": """\
Hello and welcome to Dodiom,

The game has two modes. You either *submit* an MWE example or you *review* \
examples submitted by others.

*What is an MWE?*
TODO: Describe MWE here

*What are MWE categories*
After submitting an example, you'll be asked to give a category, a category \
is simply whether the words of the MWE form an MWE sense (called positive)\
(kind of like a figurative meaning) or a non-MWE sense (called negative)\
(kind of like literal meaning.)
For example: MWE give up can mean to admit defeat, so if you enter a sentence
for that meaning, such as _"Ok, I give up!"_, than you'd choose the positive \
category, however, if you enter a sentence like _"Can you give that book up to \
me?"_ in which give up means to pass something to someone, it'd be literal \
meaning.
Keep in mind that the scores will be higher for examples of the second \
category.

Have fun!
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
        "en": "Do the words <b><u>%s</u></b> form a special meaning?",
        "tr": "<b><u>%s</u></b> sözcükleri bu örnekte birlikte deyim olarak kullanılıyor mu?"
    },
    Token.FORMS_SPECIAL_MEANING: {
        "en": "Yes, they do",
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
        "en": "In the sentence: \n\n%s\n\nIt's said that words <b><u>%s</u></b> does ✔️ form a \
special meaning together, would you agree?",
        "tr": "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak kullanılıyor ✔️ denmiş, buna katılıyor musunuz?"
    },
    Token.REVIEW_QUESTION_NEGATIVE: {
        "en": "%s\n\nIt's said that words %s does <b><u>NOT</u></b>❌ form a \
special meaning together, would you agree?",
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
        "en": "Thank you for your interest, you can send a feedback using \
following link.",
        "tr": "İlginiz için teşekkürler, geri bildirim yapmak için \
aşağıdaki linki kullanabilirsiniz."
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
        "en": "Game is finished for today, you should wait for %d am. to play.",
        "tr": "Oyun bugünlük bitti, yeni günün oyunu saat %d'da tekrar başlayacak."
    },
    Token.GAME_STARTED: {
        "en": "A new game is started.",
        "tr": "Günaydın, yeni oyun başladı."
    },
    Token.GAME_ENDED: {
        "en": "The game is ended for today, thank you for playing.",
        "tr": "Oyun bugünlük bitti, oynadığınız için teşekkürler. Yeni günün oyunu yarın saat 9:00'da başlayacak."
    },
    Token.THANKS_FOR_REVIEW: {
        "en": "%s! You earned %d points.",
        "tr": "%s! %d puan kazandın."
    },
    Token.I_NEED_PT_EXAMPLES: {
        "en": "",
        "tr": """
Eyvah, işte şimdi <b><u>ayvayı</u></b> <b><u>yedim</u></b>.

Şu an buna benzer, deyimdeki kelimelerin yanyana geçtiği ve deyim olan örnekler arıyorum.

Buna benzer örnekler verebilir misin? Acele et, böyle örnekler %d puan değerinde.
"""
    },
    Token.I_NEED_PS_EXAMPLES: {
        "en": "",
        "tr": """
Eyvah, işte <b><u>ayvayı</u></b> şimdi <b><u>yedim</u></b>.

Şu an buna benzer, deyimdeki kelimelerin birbirinden uzakta olduğu ama deyim olan örnekler arıyorum.

Buna benzer örnekler verebilir misin? Acele et, böyle örnekler %d puan değerinde.
"""
    },
    Token.I_NEED_NT_EXAMPLES: {
        "en": "",
        "tr": """
Annemin bana soyduğu <b><u>ayvayı</u></b> <b><u>yedim</u></b>.

Şu an buna benzer, deyimdeki kelimelerin yanyana geçtiği ama deyim <u>olmayan</u> örnekler arıyorum.

Buna benzer örnekler verebilir misin? Acele et, böyle örnekler %d puan değerinde.
"""
    },
    Token.I_NEED_NS_EXAMPLES: {
        "en": "",
        "tr": """
Annemin bana soyduğu <b><u>ayvayı</u></b> bir güzel <b><u>yedim</u></b>.

Şu an buna benzer, deyimdeki kelimelerin birbirinden uzakta olduğu ve deyim <u>olmayan</u> örnekler arıyorum.

Buna benzer örnekler verebilir misin? Acele et, böyle örnekler %d puan değerinde.
"""
    },
    Token.WELCOME_MESSAGE_1: {
        "en": "",
        "tr": "Merhaba ben Dodo."
    },
    Token.WELCOME_MESSAGE_2: {
        "en": "",
        "tr": "Türkçe öğrenmeye çalışıyorum ancak deyimleri anlamakta çok zorlanıyorum."
    },
    Token.WELCOME_MESSAGE_3: {
        "en": "",
        "tr": "Bana yardım eder misin?"
    },
    Token.WELCOME_MESSAGE_4: {
        "en": "",
        "tr": "Nasıl mı?"
    },
    Token.WELCOME_MESSAGE_5: {
        "en": "",
        "tr": "Bana hem deyim olan hem de deyim olmayan bol bol örnek lazım."
    },
    Token.WELCOME_MESSAGE_6: {
        "en": "",
        "tr": """
Mesela “ayvayı yemek” deyimini öğrenmem için 
“İşte şimdi ayvayı yedik.” deyim örneği
“Az önce iki ayva yedim.” deyim olmayan örnek
"""
    },
    Token.WELCOME_MESSAGE_7: {
        "en": "",
        "tr": "Şimdi bugünün deyimini seçmek için klavyeden <b><u>Günün Deyimi</u></b>'ni seç"
    },
    Token.WELCOME_MESSAGE_8: {
        "en": "",
        "tr": "Eğer klavyeyi göremiyorsan resimde görülen içinde dört tane daire olan dikdörtgene tıkla."
    },
    Token.TODAYS_MWE_HELP_MESSAGE_1: {
        "en": "",
        "tr": "Harika, günün deyimini öğrendiğine göre artık örnek göndererek öğrenmeme yardımcı olabilirsin.."
    },
    Token.TODAYS_MWE_HELP_MESSAGE_2: {
        "en": "",
        "tr": "Örnek göndermek için klavyeden <b><u>Örnek Gönder</u></b>'e tıkla.."
    },
    Token.SUBMISSION_HELP_MESSAGE_1: {
        "en": "",
        "tr": "Bu kısımda günün deyimi için örnek gönderebilirsin. Daha sonra \
diğer oyuncular senin örneğini beğendiğinde puan kazanacaksın."
    },
    Token.REVIEW_HELP_MESSAGE_1: {
        "en": "",
        "tr": "Bu kısımda diğer oyuncuların gönderdiği örnekleri oylayabilirsin."
    },
    Token.REVIEW_HELP_MESSAGE_2: {
        "en": "",
        "tr": "Hem sen hem de örneklerini oyladığın kişiler puan kazanacak."
    },
    Token.HINT_MESSAGE_1: {
        "en": "",
        "tr": "Acele et. Deyim olmayan örnekler şu anda daha çok puan kazandırıyor."
    },
    Token.HINT_MESSAGE_2: {
        "en": "",
        "tr": "Daha fazla puan kazanmak için başkalarının örneklerini oylayabilirsin."
    },
    Token.HINT_MESSAGE_3: {
        "en": "",
        "tr": """
Deyimi oluşturan sözcüklerin arasına başka sözcükler de girebiliyormuş.

Örn: “İyi mi olur yoksa <b><u>ayvayı</u></b> mı <b><u>yeriz</u></b> göreceğiz”.

Böyle örneğim çok az 😢 Acele et. Şu anda bu tür örneklerle daha fazla puan kazanabilirsin.
"""
    },
    Token.ERROR_OCCURRED: {
        "en": "An error occurred, please try again later.",
        "tr": "Bir hata oldu, lütfen daha sonra tekrar dene."
    },
    Token.NO_SUB_LEFT_TO_REVIEW: {
        "en": "",
        "tr": "Şu anlık oylayabileceğin başka bir örnek kalmadı, daha sonra \
tekrar oylamayı deneyebilirsin. Örnekleri oyladığın için teşekkürler."
    },
    Token.SCOREBOARD_EMPTY: {
        "en": "",
        "tr": "Bugün sıralamalar henüz oluşmamış. Örnek gönderip oylayarak \
sıralamalarda öne geçebilirsin."
    },
    Token.SUBMISSION_CANCELLED: {
        "en": "Submission is cancelled.",
        "tr": "Gönderi iptal edildi."
    }
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
