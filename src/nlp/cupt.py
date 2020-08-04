from typing import List

from conllu import parse
from parseme import cupt
from parseme.cupt import MWE
from stanza import Document
from stanza.utils.conll import CoNLL

from models import MweCategory


def doc_to_cupt(doc: Document, mwe_id: int, mwe_category: MweCategory,
                mwe_locations: List[int]) -> str:
    dicts = doc.to_dict()
    conll = CoNLL.convert_dict(dicts)
    for sentence in conll:
        for token in sentence:
            token.append("_")
    conll_str = "# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC PARSEME:MWE\n"
    conll_str += "# text = %s\n" % doc.text
    conll_str += CoNLL.conll_as_string(conll)

    sentences = parse(conll_str)
    sentence = sentences[0]
    cat_name = {
        MweCategory.VPC: "VPC",
        MweCategory.VID: "VID"
    }
    cupt.add_mwe(sentence, mwe_id=mwe_id, mwe=MWE(cat_name[mwe_category], set(mwe_locations)))

    return sentence.serialize()