> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.coreweave.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.coreweave.com/products/inference/serverless/api-reference#content-area)

This reference describes the Serverless Inference REST API, which lets you call foundation models programmatically from your own applications. Use it to integrate hosted inference into services, scripts, or notebooks without managing model infrastructure.

This API calls models hosted by Serverless Inference. To manage Dedicated Inference gateways, deployments, and capacity claims, see the [Dedicated Inference API reference](https://docs.coreweave.com/products/inference/reference/api-overview). To compare Serverless Inference, Dedicated Inference, and Inference on CKS, see [About CoreWeave Inference](https://docs.coreweave.com/products/inference#choose-a-deployment-option).

## [​](https://docs.coreweave.com/products/inference/serverless/api-reference\#base-url)  Base URL

Access the Serverless Inference service at:

```
https://api.inference.wandb.ai/v1
```

## [​](https://docs.coreweave.com/products/inference/serverless/api-reference\#prerequisites)  Prerequisites

To call the Serverless Inference API, you need:

- A CoreWeave Forge account with Serverless Inference credits.
- A valid CoreWeave Forge API key.
- Install the required libraries:


























```
pip install openai
```


If you belong to more than one team, or want to attribute your usage to a project, you’ll also need team and project IDs. In code samples, these appear as `[YOUR-TEAM]/[YOUR-PROJECT]`. If you don’t specify these, Serverless Inference uses your default entity and the project name `inference`.

## [​](https://docs.coreweave.com/products/inference/serverless/api-reference\#available-methods)  Available methods

The Serverless Inference API provides OpenAI-compatible endpoints for interacting with foundation models. The following methods are available:

- **[Chat Completions](https://docs.coreweave.com/products/inference/serverless/api-reference/chat-completions)**: Create chat completions using foundation models.
- **[List Models](https://docs.coreweave.com/products/inference/serverless/api-reference/list-models)**: Get all available models and their IDs.

## [​](https://docs.coreweave.com/products/inference/serverless/api-reference\#authentication)  Authentication

All API requests require authentication using your CoreWeave Forge API key. Create an API key at [forge.coreweave.com/settings](https://forge.coreweave.com/settings).Include your API key in the request headers:

- For the OpenAI SDK, set the `api_key` parameter.
- For direct API calls, use `Authorization: Bearer [YOUR-API-KEY]`.

## [​](https://docs.coreweave.com/products/inference/serverless/api-reference\#error-handling)  Error handling

For a complete list of error codes and how to resolve them, see [API errors](https://docs.coreweave.com/support/inference).

## [​](https://docs.coreweave.com/products/inference/serverless/api-reference\#next-steps)  Next steps

After you have your API key, continue with one of the following:

- Try the [usage examples](https://docs.coreweave.com/products/inference/serverless/examples) to see how the API works.
- Explore models in the [Serverless Inference UI](https://docs.coreweave.com/products/inference/serverless/ui-guide).
- Check [usage limits](https://docs.coreweave.com/products/inference/serverless/usage-limits) for your account.

Last modified onSeptember 29, 2026

Was this page helpful?

YesNo

![Project Logo](<Base64-Image-Removed>)

Ask AI

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**