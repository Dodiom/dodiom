# import stanza
# from stanza.utils.conll import CoNLL
# from conllu import parse
# from stanza.models.common.doc import Word, Document, Sentence
# from parseme.cupt import MWE
# import parseme.cupt as cupt
#
# nlp_en = stanza.Pipeline('en')
# # nlp_tr = stanza.Pipeline('tr')
#
# doc = nlp_en("Worse yet, what is going on will not let us alone.")
#
# dicts = doc.to_dict()
# conll = CoNLL.convert_dict(dicts)
# for sentence in conll:
#     for token in sentence:
#         token.append("_")
# conll_str = "# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC PARSEME:MWE\n"
# conll_str += "# text = Worse yet, what is going on will not let us alone.\n"
# conll_str += CoNLL.conll_as_string(conll)
#
# sentences = parse(conll_str)
# zero_serialized = sentences[0].serialize()
# sentence = sentences[0]
#
# cupt.add_mwe(sentence, mwe_id=1, mwe=MWE('VPC.full', {6, 7}))
#
# sentence_serialized = sentence.serialize()
#
#
# print(sentence_serialized)