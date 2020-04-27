from enum import Enum, auto
import random


class Language(Enum):
    ENGLISH = auto(),
    TURKISH = auto()


class Token(Enum):
    MAIN_KEYBOARD = auto()
    TODAYS_MWE = auto()
    SUBMIT = auto()
    REVIEW = auto()
    CHANGE_LANGUAGE = auto()
    SUGGEST_MWE = auto()
    SHOW_SCOREBOARD = auto()
    LANGUAGE_ENGLISH = auto()
    LANGUAGE_TURKISH = auto()
    TODAYS_MWE_REPLY_TEXT = auto()
    SELECT_LANGUAGE = auto()
    LANGUAGE_CHANGE_SUCCESSFUL = auto()
    PLEASE_SELECT_VALID_LANGUAGE = auto()
    WELCOME_MESSAGE = auto()
    PLEASE_ENTER_EXAMPLE = auto()
    SPECIAL_MEANING = auto()
    FORM_SPECIAL_MEANING_TOGETHER = auto()
    DOESNT_FORM_SPECIAL_MEANING_TOGETHER = auto()
    ENTER_VALID_MWE_CATEGORY = auto()
    THANKS_FOR_SUBMISSION = auto()
    ARE_WORDS_SEPARATED = auto()
    WORDS_ARE_TOGETHER = auto()
    WORDS_ARE_SEPARATED = auto()
    NO_EXAMPLES_TO_REVIEW = auto()
    AGREE_NICE_EXAMPLE = auto()
    DO_NOT_LIKE_EXAMPLE = auto()
    SKIP_THIS_ONE = auto()
    QUIT_REVIEWING = auto()
    REVIEW_MESSAGE = auto()
    SOMEONE_LOVED_YOUR_EXAMPLE = auto()
    THANKS_FOR_CONTRIBUTION = auto()
    PLEASE_ENTER_VALID_REVIEW = auto()
    TOP_FIVE_USERS = auto()
    NO_SUBMISSIONS = auto()
    ENTER_VALID_COMMAND = auto()
    SUBMISSION_DOES_NOT_CONTAIN_MWE = auto()
    PLEASE_SELECT_SUBMISSION_CATEGORY = auto()
    LITERAL = auto()
    FIGURATIVE = auto()
    CANCEL = auto()
    OPERATION_CANCELLED = auto()
    HELP = auto()
    HELP_MESSAGE = auto()
    DOES_WORDS_FORM_SPECIAL_MEANING = auto()
    FORMS_SPECIAL_MEANING = auto()
    DOES_NOT_FORM_SPECIAL_MEANING = auto()
    AND = auto()


lang_en = {
    Token.TODAYS_MWE: "Today's MWE",
    Token.SUBMIT: "Submit",
    Token.REVIEW: "Review",
    Token.CHANGE_LANGUAGE: "Change language",
    Token.SUGGEST_MWE: "Suggest MWE",
    Token.SHOW_SCOREBOARD: "Show Scoreboard",
    Token.LANGUAGE_ENGLISH: "English (EN)",
    Token.LANGUAGE_TURKISH: "Türkçe (TR)",
    Token.TODAYS_MWE_REPLY_TEXT: "Today's MWE is '*%s*', meaning: _%s_",
    Token.SELECT_LANGUAGE: "Please select a language",
    Token.LANGUAGE_CHANGE_SUCCESSFUL: "Language set to *English*.",
    Token.PLEASE_SELECT_VALID_LANGUAGE: "Please select a valid language",
    Token.WELCOME_MESSAGE: "Welcome to MWExpress, *%s*",
    Token.PLEASE_ENTER_EXAMPLE: "Please enter your example for the MWE: '*%s*'",
    Token.SPECIAL_MEANING: "Does '%s' form a special meaning in this sentence?",
    Token.FORM_SPECIAL_MEANING_TOGETHER: "Words '%s' do form a special meaning together 🙌.",
    Token.DOESNT_FORM_SPECIAL_MEANING_TOGETHER: "Words *%s* do NOT form a special meaning together ✋ 🤚.",
    Token.ENTER_VALID_MWE_CATEGORY: "Please enter a valid category",
    Token.THANKS_FOR_SUBMISSION: "%s! Thank you for your submission, you'll win %.2f points when someone likes your example.",
    Token.ARE_WORDS_SEPARATED: 'Are the words "%s" next to each other or are they separated?',
    Token.WORDS_ARE_TOGETHER: 'All the words in “%s” are 👏 together',
    Token.WORDS_ARE_SEPARATED: 'Some words in “%s” are 🙌 separated',
    Token.NO_EXAMPLES_TO_REVIEW: "Currently there are no examples ready for reviewing. 🙄 Please try later.",
    Token.AGREE_NICE_EXAMPLE: '👍 I agree. Nice example for this category',
    Token.DO_NOT_LIKE_EXAMPLE: '👎 I do not like this example',
    Token.SKIP_THIS_ONE: '⏭ Skip this one',
    Token.QUIT_REVIEWING: '😱 Quit reviewing',
    Token.REVIEW_MESSAGE: "'*%s*'. This example was provided for the category where %s.",
    Token.SOMEONE_LOVED_YOUR_EXAMPLE: "%s! Someone else loved your great example, and you’ve earned %d points",
    Token.THANKS_FOR_CONTRIBUTION: "Thank you for your contribution!",
    Token.PLEASE_ENTER_VALID_REVIEW: "Please enter a valid review",
    Token.TOP_FIVE_USERS: "Here are the top 5 users for today:\n",
    Token.NO_SUBMISSIONS: "There are no submissions and users at this time.",
    Token.ENTER_VALID_COMMAND: "Please enter a valid command",
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: "It looks like your submission does not contain todays MWE (*%s*), please enter again.",
    Token.PLEASE_SELECT_SUBMISSION_CATEGORY: "Please choose a category for your submission.",
    Token.LITERAL: "Literal",
    Token.FIGURATIVE: "Figurative",
    Token.CANCEL: "Cancel",
    Token.OPERATION_CANCELLED: "Operation cancelled",
    Token.HELP: "Help",
    Token.HELP_MESSAGE: """\
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
    Token.DOES_WORDS_FORM_SPECIAL_MEANING: "Do the words *%s* form a special meaning?",
    Token.FORMS_SPECIAL_MEANING: "Yes, they do",
    Token.DOES_NOT_FORM_SPECIAL_MEANING: "Nope",
    Token.AND: "and"
}

lang_tr = {
    Token.TODAYS_MWE: "Bugünün MWEsi",
    Token.SUBMIT: "Örnek gönder",
    Token.REVIEW: "Örnekleri oyla",
    Token.CHANGE_LANGUAGE: "Dili değiştir",
    Token.SUGGEST_MWE: "Yeni MWE öner",
    Token.SHOW_SCOREBOARD: "Sıralamaları göster",
    Token.LANGUAGE_ENGLISH: "English (EN)",
    Token.LANGUAGE_TURKISH: "Türkçe (TR)",
    Token.TODAYS_MWE_REPLY_TEXT: "Bugünün MWEsi '*%s*', anlamı da: _%s_",
    Token.SELECT_LANGUAGE: "Lütfen bir dil seçin",
    Token.LANGUAGE_CHANGE_SUCCESSFUL: "Dil *Türkçe* olarak ayarlandı.",
    Token.PLEASE_SELECT_VALID_LANGUAGE: "Lütfen geçerli bir dil seçin.",
    Token.WELCOME_MESSAGE: "MWExpress'e hoşgeldiniz, *%s*",
    Token.PLEASE_ENTER_EXAMPLE: "Lütfen MWE '*%s*' için örneğinizi girin",
    Token.SPECIAL_MEANING: "'*%s*' bu cümlede deyimsel bir anlam içeriyor mu?",
    Token.FORM_SPECIAL_MEANING_TOGETHER: "'%s' kelimeleri bir arada deyimsel bir anlam ifade ediyor 🙌.",
    Token.DOESNT_FORM_SPECIAL_MEANING_TOGETHER: "'%s' kelimeleri bir arada deyimsel bir anlam ifade ETMİYOR ✋ 🤚.",
    Token.ENTER_VALID_MWE_CATEGORY: "Lütfen geçerli bir kategori seçin",
    Token.THANKS_FOR_SUBMISSION: "%s! Gönderiniz için teşekkürler, birisi sizin gönderinizi beğendiğinde %.2f puan kazanacaksınız.",
    Token.ARE_WORDS_SEPARATED: '"%s" kelimeleri örnekte yanyana mı yoksa ayrı mı geçiyor?',
    Token.WORDS_ARE_TOGETHER: 'Örnekte “%s” kelimeleri yanyana 👏 geçiyorr',
    Token.WORDS_ARE_SEPARATED: 'Örnekte “%s” kelimeleri 🙌 ayrı geçiyor',
    Token.NO_EXAMPLES_TO_REVIEW: "Şu an incelebileceğiniz örnek yok. 🙄 Lütfen daha sonra tekrar deneyin.",
    Token.AGREE_NICE_EXAMPLE: '👍 Kaıtlıyorum. Bu kategori için güzel bir örnek',
    Token.DO_NOT_LIKE_EXAMPLE: '👎 Bu örneği beğenmedim',
    Token.SKIP_THIS_ONE: '⏭ Bu örneği geç',
    Token.QUIT_REVIEWING: '😱 İncelemeyi bitir',
    Token.REVIEW_MESSAGE: "'*%s*'. Bu örnek %s kategorisinde verilmiş.",
    Token.SOMEONE_LOVED_YOUR_EXAMPLE: "%s! Birisi örneğini beğendi, sen de %d puan kazandın.",
    Token.THANKS_FOR_CONTRIBUTION: "Katkılarınız için teşekkürler!",
    Token.PLEASE_ENTER_VALID_REVIEW: "Lütfen geçerli bir inceleme seçin",
    Token.TOP_FIVE_USERS: "İşte bugünün ilk beşi:\n",
    Token.NO_SUBMISSIONS: "Henüz gönderi ya da oylama yok.",
    Token.ENTER_VALID_COMMAND: "Lütfen geçerli bir komut girin.",
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: "Öyle görünüyor ki girdiğin örnekte günün MWE'si (*%s*) bulunmamakta, lütfen tekrar gir.",
    Token.PLEASE_SELECT_SUBMISSION_CATEGORY: "Lütfen gönderinizin kategorisini seçin.",
    Token.LITERAL: "Gerçek",
    Token.FIGURATIVE: "Mecazi",
    Token.CANCEL: "İptal",
    Token.OPERATION_CANCELLED: "İşlem iptal edildi.",
    Token.HELP: "Yardım",
    Token.HELP_MESSAGE: """\
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
""",
    Token.DOES_WORDS_FORM_SPECIAL_MEANING: "*%s* kelimeleri bu örnekte özel bir anlam ifade ediyor mu?",
    Token.FORMS_SPECIAL_MEANING: "Eve, ediyor",
    Token.DOES_NOT_FORM_SPECIAL_MEANING: "Hayır",
    Token.AND: "ve"
}


def get_language_token(language: Language, token: Token) -> str:
    if language == Language.ENGLISH:
        return lang_en[token]
    elif language == Language.TURKISH:
        return lang_tr[token]


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
