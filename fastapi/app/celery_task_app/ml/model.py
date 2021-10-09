from transformers import pipeline


class QuestionAnsweringModel:
    def __init__(self):
        self.model = self._load_model()

    @staticmethod
    def _load_model():
        model = pipeline(
            "question-answering",
            model="mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es",
            tokenizer=(
                "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es",
                {"use_fast": False},
            ),
        )
        return model

    def inference(self, data):

        return self.model({data["question"], ["context"]})
