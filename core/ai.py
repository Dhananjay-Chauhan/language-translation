from transformers import pipeline, BertTokenizerFast, BertForQuestionAnswering

spanish_engine = pipeline(
    "question-answering", model="PlanTL-GOB-ES/roberta-large-bne-sqac"
)
french_engine = pipeline(
    "question-answering",
    model="cmarkea/distilcamembert-base-qa",
    tokenizer="cmarkea/distilcamembert-base-qa",
)
english_engine = pipeline("question-answering")
italian_engine = pipeline(
    "question-answering",
    model=BertForQuestionAnswering.from_pretrained(
        "osiria/bert-italian-cased-question-answering"
    ),
    tokenizer=BertTokenizerFast.from_pretrained(
        "osiria/bert-italian-cased-question-answering"
    ),
)

engines = {
    "english": english_engine,
    "spanish": spanish_engine,
    "italian": italian_engine,
    "french": french_engine,
}
