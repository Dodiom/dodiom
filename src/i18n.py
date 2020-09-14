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
    OPERATION_CANCELLED = auto()
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
        "tr": "Bugünün MWEsi"
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
        "en": "Today's MWE is '*%s*', meaning: _%s_",
        "tr": "Bugünün MWEsi '*%s*', anlamı da: _%s_"
    },
    Token.SELECT_LANGUAGE: {
        "en": "Please select a language",
        "tr": "Lütfen bir dil seçin"
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
        "en": "Welcome to MWExpress, *%s*",
        "tr": "MWExpress'e hoşgeldiniz, *%s*"
    },
    Token.PLEASE_ENTER_EXAMPLE: {
        "en": "Please enter your example for the MWE: '*%s*'",
        "tr": "Lütfen MWE '*%s*' için örneğinizi girin"
    },
    Token.ENTER_VALID_MWE_CATEGORY: {
        "en": "Please enter a valid category",
        "tr": "Lütfen geçerli bir kategori seçin"
    },
    Token.THANKS_FOR_SUBMISSION: {
        "en": "%s! Thank you for your submission, you'll win %.2f points when someone likes your example.",
        "tr": "%s! Gönderiniz için teşekkürler, birisi sizin gönderinizi beğendiğinde %.2f puan kazanacaksınız."
    },
    Token.AGREE_NICE_EXAMPLE: {
        "en": '👍 I agree. Nice example for this category',
        "tr": '👍 Katılıyorum. Bu kategori için güzel bir örnek'
    },
    Token.DO_NOT_LIKE_EXAMPLE: {
        "en": '👎 I do not like this example',
        "tr": '👎 Bu örneği beğenmedim'
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
        "tr": "Henüz gönderi ya da oylama yok."
    },
    Token.ENTER_VALID_COMMAND: {
        "en": "Please enter a valid command",
        "tr": "Lütfen geçerli bir komut girin."
    },
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: {
        "en": "It looks like your submission does not contain todays MWE (*%s*), please enter again.",
        "tr": "Öyle görünüyor ki girdiğin örnekte günün MWE'si (*%s*) bulunmamakta, lütfen tekrar gir."
    },
    Token.CANCEL: {
        "en": "Cancel",
        "tr": "İptal"
    },
    Token.OPERATION_CANCELLED: {
        "en": "Operation cancelled",
        "tr": "İşlem iptal edildi."
    },
    Token.HELP: {
        "en": "Help",
        "tr": "Yardım"
    },
    Token.HELP_MESSAGE: {
        "en": """\
Hello and welcome to MWExpress,

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
        "tr": """\
MWExpress'e hoşgeldiniz,

Bu oyunda iki mod bulunmaktadır. *Örnek gönderebilir* ya da diğerlerinin \
gönderdiği örnekleri *inceleyebilirsiniz*.

*MWE nedir?*
TODO: Describe MWE here

*MWE kategorileri nelerdir?*
Bir örnek gönderdikten sonra sana örneğin kategorisinin ne olduğunu soracağız, \
bu kategori basitçe örneğin MWE olup olmadığıyla ilgili. Örnek MWE olabilir \
(pozitif)(mecazi anlammış gibi düşünün) ya da olmayabilir (negatif)(gerçek \
anlamında kullanılmış gibi).
Örneğin, MWE ayvayı yemek kötü bir duruma düşmek anlamında kullanılır ve eğer \
_"İşte şimdi ayvayı yedim."_ gibi bu anlamda kullanılan bir cümle girerseniz \
pozitif kategorisini seçin ama _"Annemin bana uzattığı ayvayı yedim."?_ gibi \
bir cümle girerseniz ise negatif anlamı seçin çünkü bu cümlede ayvayı yemek \
kötü bir duruma düşmekten ziyade meyve olan ayvayı yemek gibi gerçek anlamıyla \
kullanılmış.
İpucu: Eğer ikinci kategoride örnekler girerseniz daha yüksek puan alacaksınız.

İyi eğlenceler!
"""
    },
    Token.DOES_WORDS_FORM_SPECIAL_MEANING: {
        "en": "Do the words *%s* form a special meaning?",
        "tr": "*%s* kelimeleri bu örnekte özel bir anlam ifade ediyor mu?"
    },
    Token.FORMS_SPECIAL_MEANING: {
        "en": "Yes, they do",
        "tr": "Evet, ediyor"
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
        "en": "In the sentence: \n\n%s\n\nIt's said that words %s does form a \
special meaning together, would you agree?",
        "tr": "%s\n\nCümlesinde %s kelimeleri birlikte özel bir anlam ifade \
ediyor denmiş, buna katılıyor musunuz?"
    },
    Token.REVIEW_QUESTION_NEGATIVE: {
        "en": "In the sentence: \n\n%s\n\nIt's said that words %s does *not* form a \
special meaning together, would you agree?",
        "tr": "%s\n\nCümlesinde %s kelimeleri birlikte özel bir anlam ifade \
*etmiyor* denmiş, buna katılıyor musunuz?"
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
        "tr": "Oyun bugünlük bitti, yeni günün onunu saat %d'da tekrar başlayacak."
    },
    Token.GAME_STARTED: {
        "en": "Good morning, the game is started.",
        "tr": "Günaydın, oyun başladı."
    },
    Token.GAME_ENDED: {
        "en": "The game is ended for today, thank you for playing.",
        "tr": "Oyun bugünlük bitti, oynadığınız için teşekkürler."
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
