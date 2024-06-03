"""
The `Model` class is an interface between the ML model that you're packaging and the model
server that you're running it on.

The main methods to implement here are:
* `load`: runs exactly once when the model server is spun up or patched and loads the
   model onto the model server. Include any logic for initializing your model, such
   as downloading model weights and loading the model into memory.
* `predict`: runs every time the model server is called. Include any logic for model
  inference and return the model output.

See https://truss.baseten.co/quickstart for more.
"""

from sentence_transformers.cross_encoder import CrossEncoder


class Model:
    def __init__(self, **kwargs):
        # Uncomment the following to get access
        # to various parts of the Truss config.

        # self._data_dir = kwargs["data_dir"]
        # self._config = kwargs["config"]
        # self._secrets = kwargs["secrets"]
        self._model = None

    def load(self):
        # Load model here and assign to self._model.
        self._model = CrossEncoder("cross-encoder/stsb-distilroberta-base")

    def predict(self, model_input):
        # TODO: validate pieces of model input
        limit = model_input.get('limit', 5)
        offset = model_input.get('offset', 0)

        # TODO: this is not the right way to represent the "database"
        # using this as a way to validate the model usage
        corpus = [
            "A man is eating food.",
            "A man is eating a piece of bread.",
            "The girl is carrying a baby.",
            "A man is riding a horse.",
            "A woman is playing violin.",
            "Two men pushed carts through the woods.",
            "A man is riding a white horse on an enclosed ground.",
            "A monkey is playing drums.",
            "A cheetah is running behind its prey.",
        ]
        result = []
        ranks =  self._model.rank(model_input['query'], corpus)
        for rank in ranks:
            result.append(corpus[rank['corpus_id']])
        return result[offset:(limit+offset)]
