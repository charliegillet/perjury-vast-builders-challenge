> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.coreweave.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.coreweave.com/products/inference/serverless/usage-limits#content-area)

This page describes the pricing, usage limits, and account restrictions that apply to Serverless Inference. Use this information to plan your usage and avoid unexpected charges or interruptions. Review it before you send production traffic, especially if you manage billing or operate at higher concurrency.

If you have questions about pricing, limits, or your account that this page doesn’t answer, contact [Support](mailto:forge-support@coreweave.com) to discuss your requirements.

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#view-billing-and-usage-information)  View billing and usage information

Organization admins can track credit balance and usage history from the Forge console:

1. In the top right corner, click your **user profile icon**.
2. Select **Billing**.
3. Select the **Usage & Alerts** tab.
4. Choose **Inference** from the sidebar menu.
5. From here you can:
   - See your usage over time.
   - Configure spend alerts.

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#pricing)  Pricing

For detailed model pricing information, visit [Serverless Inference pricing](https://coreweave.com/forge-pricing/inference-agents).

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#purchase-more-credits)  Purchase more credits

Serverless Inference credits come with Free, Pro, and Academic plans for a limited time. Enterprise availability may vary. When credits run out:

- **Free accounts** must activate pay-as-you-go inference on the **Billing** tab, or upgrade to a paid plan to continue using Serverless Inference. [Activate pay-as-you-go or upgrade](https://forge.coreweave.com/subscriptions).
- CoreWeave bills **Pro plan users** for overages monthly, based on [model-specific pricing](https://coreweave.com/forge-pricing/inference-agents).
- **Enterprise accounts** should contact their account executive.

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#account-tiers-and-default-usage-caps)  Account tiers and default usage caps

Each account tier has a default spending cap to help manage costs and prevent unexpected charges. CoreWeave requires prepayment for paid Serverless Inference access.The following table shows the default cap for each tier and how to request a change. If you need to change your cap, contact your account executive or [Support](mailto:forge-support@coreweave.com) to adjust your limit.

| Account tier | Default cap | How to change limit |
| --- | --- | --- |
| Free | $100/month | Upgrade to Pro or Enterprise |
| Pro | $6,000/month | Contact your account executive or support for manual review |
| Enterprise | $700,000/year | Contact your account executive or support for manual review |

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#concurrency-limits)  Concurrency limits

Concurrency limits protect service quality by capping how many requests a project or user can have in flight at once. If you exceed the concurrency limit, the API returns a `429 Concurrency limit reached for requests` response. To fix this error, reduce the number of concurrent requests.CoreWeave applies concurrency limits per Weights & Biases project and per user. For example, if you have three projects in a team, each project has its own concurrency limit quota.If your use case requires increased limits, contact [Support](mailto:forge-support@coreweave.com) to discuss your requirements.

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#geographic-restrictions)  Geographic restrictions

The Serverless Inference service is only available from supported geographic locations. For more information, see the [Terms of Service](https://docs.coreweave.com/policies/terms-of-service/terms-of-use#geographic-restrictions).

## [​](https://docs.coreweave.com/products/inference/serverless/usage-limits\#next-steps)  Next steps

See [available models](https://docs.coreweave.com/products/inference/serverless/models) and their specific pricing.

Last modified onSeptember 29, 2026

Was this page helpful?

YesNo

![Project Logo](<Base64-Image-Removed>)

Ask AI

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**