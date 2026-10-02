> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.coreweave.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.coreweave.com/products/wandb/weave/guides/integrations/google#content-area)

[GitHub source](https://github.com/wandb/examples/blob/master/weave/docs/quickstart_google.ipynb)

You can experiment with Google AI models on Weave without any setup using the [LLM Playground](https://docs.coreweave.com/products/wandb/weave/guides/tools/playground).

This page describes how to use W&B Weave with the Google Vertex AI API and the Google Gemini API so you can evaluate, monitor, and iterate on your Google GenAI applications.Weave automatically captures traces for the:

- [Google GenAI SDK](https://github.com/googleapis/python-genai), which is accessible through Python SDK, Node.js SDK, Go SDK, and REST.
- [Google Vertex AI API](https://cloud.google.com/vertex-ai/docs), which provides access to Google’s Gemini models and [partner models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models).

Weave also supports the deprecated [Google AI Python SDK for the Gemini API](https://github.com/google-gemini/deprecated-generative-ai-python). This support is deprecated as well and is scheduled for removal in a future version.

## [​](https://docs.coreweave.com/products/wandb/weave/guides/integrations/google\#get-started)  Get started

The following examples show how to enable tracing for each supported SDK. In both cases, calling `weave.init` is the only Weave-specific step required. Your existing Google GenAI or Vertex AI code stays the same.Weave automatically captures traces for the [Google GenAI SDK](https://github.com/googleapis/python-genai). To start tracking, call `weave.init(project_name="[YOUR-WANDB-PROJECT-NAME]")` and use the library as normal.

```
import os
from google import genai
import weave

weave.init(project_name="google-genai")

google_client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_KEY"))
response = google_client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What's the capital of France?",
)
```

[![dspy_trace.png](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/google-genai-trace.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=ff14b5daa921aab6e32038eaa67f6a47)](https://forge.coreweave.com/wandb/geekyrakshit/google-genai/weave/traces)Weave also automatically captures traces for [Vertex APIs](https://github.com/googleapis/python-aiplatform/tree/main/vertexai/generative_models). To start tracking, call `weave.init(project_name="[YOUR-WANDB-PROJECT-NAME]")` and use the library as normal.

```
import vertexai
import weave
from vertexai.generative_models import GenerativeModel

weave.init(project_name="vertex-ai-test")
vertexai.init(project="[YOUR-VERTEX-AI-PROJECT-NAME]", location="[YOUR-VERTEX-AI-PROJECT-LOCATION]")
model = GenerativeModel("gemini-1.5-flash-002")
response = model.generate_content(
    "What's a good name for a flower shop specialising in selling dried flower bouquets?"
)
```

## [​](https://docs.coreweave.com/products/wandb/weave/guides/integrations/google\#track-your-own-ops)  Track your own ops

Wrap a function with `@weave.op` to start capturing inputs, outputs, and app logic so you can debug how data flows through your app. You can deeply nest ops and build a tree of functions that you want to track. This also starts automatically versioning code as you experiment to capture ad-hoc details that haven’t been committed to git.Create a function decorated with [`@weave.op`](https://docs.coreweave.com/products/wandb/weave/guides/tracking/ops).In the following example, the function `recommend_places_to_visit` is wrapped with `@weave.op` and recommends places to visit in a city.

```
import os
from google import genai
import weave

weave.init(project_name="google-genai")
google_client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_KEY"))

@weave.op()
def recommend_places_to_visit(city: str, model: str = "gemini-1.5-flash"):
    response = google_client.models.generate_content(
        model=model,
        contents="You are a helpful assistant meant to suggest all budget-friendly places to visit in a city",
    )
    return response.text

recommend_places_to_visit("New York")
recommend_places_to_visit("Paris")
recommend_places_to_visit("Kolkata")
```

[![dspy_trace.png](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/google-genai-ops.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=cbc4a918b14a6994fcb1c2917ceb8a0a)](https://forge.coreweave.com/wandb/geekyrakshit/google-genai/weave/traces)

## [​](https://docs.coreweave.com/products/wandb/weave/guides/integrations/google\#create-a-model-for-easier-experimentation)  Create a `Model` for easier experimentation

Organizing experimentation is difficult when there are many moving pieces. By using the [`Model`](https://docs.coreweave.com/products/wandb/weave/guides/core-types/models) class, you can capture and organize the experimental details of your app like your system prompt or the model you’re using. This helps organize and compare different iterations of your app.In addition to versioning code and capturing inputs/outputs, [`Model`](https://docs.coreweave.com/products/wandb/weave/guides/core-types/models) s capture structured parameters that control your application’s behavior, helping you find what parameters worked best. You can also use Weave Models with `serve`, and [`Evaluation`](https://docs.coreweave.com/products/wandb/weave/guides/core-types/evaluations) s.In the following example, you can experiment with `CityVisitRecommender`. Every time you change one of these, you’ll get a new _version_ of `CityVisitRecommender`. This gives you a versioned record of each configuration you try, which you can later compare or evaluate.

```
import os
from google import genai
import weave

weave.init(project_name="google-genai")
google_client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_KEY"))

class CityVisitRecommender(weave.Model):
    model: str

    @weave.op()
    def predict(self, city: str) -> str:
        response = google_client.models.generate_content(
            model=self.model,
            contents="You are a helpful assistant meant to suggest all budget-friendly places to visit in a city",
        )
        return response.text

city_recommender = CityVisitRecommender(model="gemini-1.5-flash")
print(city_recommender.predict("New York"))
print(city_recommender.predict("San Francisco"))
print(city_recommender.predict("Los Angeles"))
```

Last modified onSeptember 29, 2026

Was this page helpful?

YesNo

![Project Logo](<Base64-Image-Removed>)

Ask AI

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**