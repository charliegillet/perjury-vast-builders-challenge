> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.wandb.ai/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.wandb.ai/inference#content-area)

Notice: The Weights & Biases domain [will change on September 30](https://wandb.ai/site/domain-update-faqs/). This includes all websites and services that use a W&B domain. No action is needed today.

[Weights & Biases Documentation home page![light logo](https://mintcdn.com/wb-21fd5541/C7PMWo9Jl9GZ2Zki/icons/Endorsed_primary_blackwhite.svg?fit=max&auto=format&n=C7PMWo9Jl9GZ2Zki&q=85&s=a9d999235518399090dd8ddd0a9e1e4a)![dark logo](https://mintcdn.com/wb-21fd5541/C7PMWo9Jl9GZ2Zki/icons/Endorsed_primary_goldwhite.svg?fit=max&auto=format&n=C7PMWo9Jl9GZ2Zki&q=85&s=f4eaf37e934c12e5fd3e806fe2984c2e)](https://docs.wandb.ai/)

English

Search...

Ctrl K

- [Log in](https://app.wandb.ai/login?_gl=1*8ninq0*_ga*MTE3ODEwNDkyLjE3MzQwMjk0NjA.*_ga_JH1SJHJQXJ*MTczNDA2Mzc4OS4yLjEuMTczNDA2MzkxMC42MC4wLjA.*_ga_GMYDGNGKDT*MTczNDA2Mzc4OS4zLjEuMTczNDA2Mzg2Ny4wLjAuMA..*_gcl_au*MTc0Mjk3ODgzMi4xNzM0MDI5NDYw)
- [Sign Up](https://app.wandb.ai/login?signup=true&_gl=1*y15ckv*_ga*MTE3ODEwNDkyLjE3MzQwMjk0NjA.*_ga_JH1SJHJQXJ*MTczNDA2Mzc4OS4yLjEuMTczNDA2Mzk3MC42MC4wLjA.*_ga_GMYDGNGKDT*MTczNDA2Mzc4OS4zLjEuMTczNDA2Mzg2Ny4wLjAuMA..*_gcl_au*MTc0Mjk3ODgzMi4xNzM0MDI5NDYw)
- [Sign Up](https://app.wandb.ai/login?signup=true&_gl=1*y15ckv*_ga*MTE3ODEwNDkyLjE3MzQwMjk0NjA.*_ga_JH1SJHJQXJ*MTczNDA2Mzc4OS4yLjEuMTczNDA2Mzk3MC42MC4wLjA.*_ga_GMYDGNGKDT*MTczNDA2Mzc4OS4zLjEuMTczNDA2Mzg2Ny4wLjAuMA..*_gcl_au*MTc0Mjk3ODgzMi4xNzM0MDI5NDYw)

Search...

Navigation

Serverless Inference

Products

[Get Started](https://docs.wandb.ai/get-started) [Reference](https://docs.wandb.ai/reference) [Release Notes](https://docs.wandb.ai/release-notes)
Support

- [Serverless Inference](https://docs.wandb.ai/inference)

- [Prerequisites](https://docs.wandb.ai/inference/prerequisites)

- [Available models](https://docs.wandb.ai/inference/models)

- [Model lifecycle](https://docs.wandb.ai/inference/lifecycle)

- [Use Serverless LoRA Inference](https://docs.wandb.ai/inference/lora)

### Response Settings

- [Enable JSON mode](https://docs.wandb.ai/inference/response-settings/json-mode)
- [View reasoning information](https://docs.wandb.ai/inference/response-settings/reasoning)
- [Enable streaming responses](https://docs.wandb.ai/inference/response-settings/streaming)
- [Prefix caching](https://docs.wandb.ai/inference/response-settings/prefix-caching)
- [Enable structured output](https://docs.wandb.ai/inference/response-settings/structured-output)
- [Call tools](https://docs.wandb.ai/inference/response-settings/tool-calling)

- [Usage information and limits](https://docs.wandb.ai/inference/usage-limits)

### Tutorials

- [Cline with Serverless Inference](https://docs.wandb.ai/inference/tutorials/integration-cline)
- [Creating a fine-tuned LoRA](https://docs.wandb.ai/inference/tutorials/creating-lora)

### API Reference

- [API Reference](https://docs.wandb.ai/inference/api-reference)

- [Usage examples](https://docs.wandb.ai/inference/examples)

- [UI guide](https://docs.wandb.ai/inference/ui-guide)

- [Support: Inference](https://docs.wandb.ai/support/inference)

# Serverless Inference

Install W&B MCP

Access open-source foundation models through W&B Weave and an OpenAI-compatible API

Install W&B MCP

Serverless Inference gives you access to leading open-source foundation models through W&B Weave and an OpenAI-compatible API.

- Using Inference you can build AI applications and agents without signing up for a hosting provider or self-hosting a model.
- Using Weave, you can trace, evaluate, monitor, and improve your Serverless Inference-powered applications.

## [​](https://docs.wandb.ai/inference\#try-out-inference-in-the-ui)  Try out Inference in the UI

Navigate to [https://wandb.ai/inference](https://wandb.ai/inference) to explore available models and try them out in the Weave Playground.For more information on the web interface, see the [UI Guide](https://docs.wandb.ai/inference/ui-guide).

## [​](https://docs.wandb.ai/inference\#use-inference-through-the-api)  Use Inference through the API

This Python example uses Inference to send a chat completion request to an LLM.

```
import openai

client = openai.OpenAI(
    # The custom base URL points to Serverless Inference
    base_url='https://api.inference.wandb.ai/v1',

    # Create an API key at https://wandb.ai/settings
    api_key="<your-api-key>",

    # Optional: Team and project for usage tracking
    project="<your-team>/<your-project>",
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[\
        {"role": "system", "content": "You are a helpful assistant."},\
        {"role": "user", "content": "Tell me a joke."}\
    ],
)

print(response.choices[0].message.content)
```

## [​](https://docs.wandb.ai/inference\#next-steps)  Next steps

1. Set up your account using the [prerequisites](https://docs.wandb.ai/inference/prerequisites).
2. Review the [available models](https://docs.wandb.ai/inference/models) and [usage information and limits](https://docs.wandb.ai/inference/usage-limits).
3. Use the service through the [API](https://docs.wandb.ai/inference/api-reference) or [UI](https://docs.wandb.ai/inference/ui-guide).
4. Try out supported models in the [W&B Weave Playground](https://docs.wandb.ai/weave/guides/tools/playground).
5. Try the [usage examples](https://docs.wandb.ai/inference/examples).

For information about pricing, usage limits, and credits, see [Usage Information and Limits](https://docs.wandb.ai/inference/usage-limits).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/wandb/docs/edit/main/inference.mdx) [Raise issue](https://github.com/wandb/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/inference)

[Prerequisites\\
\\
Next](https://docs.wandb.ai/inference/prerequisites)

[discord](https://discord.com/invite/RgB8CPk2ce) [github](https://github.com/wandb/docs) [linkedin](https://www.linkedin.com/company/wandb) [x](https://x.com/weights_biases?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) [youtube](https://www.youtube.com/c/WeightsBiases)

Cookie settings

![](https://a.usbrowserspeed.com/ncs?pid=c59fd74cbd71a58d3d354f836099a3cf5a29e8461d70dad1ea560c3559765bfc&puid=usergems-ZCKXTHyLNZTV90gD-eadfe211a1404d82b1483bdbd3a0e204-eadfe211_a140_4d82_b148_3bdbd3a0e204-%252Finference)

![Project Logo](https://site.wandb.ai/wp-content/uploads/2024/05/pictorial-mark-black-1.svg)

Ask AI

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**