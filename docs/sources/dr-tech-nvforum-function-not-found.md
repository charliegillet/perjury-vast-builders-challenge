[Skip to last reply](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670/6) [Skip to top](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670/1)

[Skip to main content](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670#main-container)

# [Function not found for account](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670)

[AI & Data Science](https://forums.developer.nvidia.com/c/ai-data-science/86) [NVIDIA NIM](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/678) [Models](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/models/698)

- [cosmos](https://forums.developer.nvidia.com/tag/cosmos/1080)

[Home](https://forums.developer.nvidia.com/categories "All Categories")

You have selected **0** posts.

[select all](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670)

[cancel selecting](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670)

549
views
5
links


![](https://developer.download.nvidia.com/images/forums/profile-default-devtalk-84.png)2

![](https://sea2.discourse-cdn.com/nvidia/user_avatar/forums.developer.nvidia.com/neal.vaidya/48/256893_2.png)

![](https://developer.download.nvidia.com/images/forums/profile-default-devtalk-84.png)

![](https://sea2.discourse-cdn.com/nvidia/user_avatar/forums.developer.nvidia.com/mmaghoumi/48/382649_2.png)

[Jan 15](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670/1 "Jump to the first post")

1 / 6


Jan 15


[Feb 6](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670/6)

## post by dd.an.ivanov on Jan 15

![](https://developer.download.nvidia.com/images/forums/profile-default-devtalk-84.png)


dd.an.ivanov

[Jan 15](https://forums.developer.nvidia.com/t/function-not-found-for-account/357670 "Post date")

Good afternoon. API shows cosmos-reason2-8b as an available model, but fails with “404: Function not found for account” when I send a request to it.

$ curl -s “ [https://integrate.api.nvidia.com/v1/models](https://integrate.api.nvidia.com/v1/models)” -H “Authorization: Bearer $NVIDIA\_API\_KEY” \| jq ‘.data\[\] \| select(.id \| contains(“cosmos”))’

{

“id”: “nvidia/cosmos-reason2-8b”,

“object”: “model”,

“created”: 735790403,

“owned\_by”: “nvidia”

}

$ curl -s “ [https://integrate.api.nvidia.com/v1/chat/completions](https://integrate.api.nvidia.com/v1/chat/completions)” -H “Authorization: Bearer $NVIDIA\_API\_KEY” -H “Content-Type: application/json” -d ‘{“model”: “nvidia/cosmos-reason2-8b”, “messages”: \[ { “role”: “user”, “content”: “hi” } \], “max\_tokens”: 1024}’

{“status”:404,“title”:“Not Found”,“detail”:“Function ‘xxx-xxx-xxx-xxx-xxx’: Not found for account ‘yyy’”}

Other models work fine.

549
views
5
links


![](https://developer.download.nvidia.com/images/forums/profile-default-devtalk-84.png)2

![](https://sea2.discourse-cdn.com/nvidia/user_avatar/forums.developer.nvidia.com/neal.vaidya/48/256893_2.png)

![](https://developer.download.nvidia.com/images/forums/profile-default-devtalk-84.png)

![](https://sea2.discourse-cdn.com/nvidia/user_avatar/forums.developer.nvidia.com/mmaghoumi/48/382649_2.png)

8 days later


## post by MMaghoumi on Jan 23

## post by dd.an.ivanov on Jan 26

## post by mahes25 on Jan 29

8 days later


## post by neal.vaidya on Feb 6

14 days later


## Closed on Feb 20

Reply

### Related topics

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [API 404](https://forums.developer.nvidia.com/t/api-404/381401)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) <br>- [deepseek](https://forums.developer.nvidia.com/tag/deepseek/1158) | [0](https://forums.developer.nvidia.com/t/api-404/381401/1) | 117 | [Aug 26](https://forums.developer.nvidia.com/t/api-404/381401/1) |
| [404 Function not found for account when calling google/diffusiongemma-26b-a4b-it](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-when-calling-google-diffusiongemma-26b-a4b-it/373006)<br>[Models](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/models/698) | [1](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-when-calling-google-diffusiongemma-26b-a4b-it/373006/1) | 156 | [Jun 11](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-when-calling-google-diffusiongemma-26b-a4b-it/373006/2) |
| [Function id ‘948fe171-ce7a-4332-8bc0-5e14e90259f9’ not found for account ‘4iX-Po20Vs9O\_8U36Mro-\_HJyG2DxzxMY2YSoKjK\_PU’](https://forums.developer.nvidia.com/t/function-id-948fe171-ce7a-4332-8bc0-5e14e90259f9-not-found-for-account-4ix-po20vs9o-8u36mro-hjyg2dxzxmy2ysokjk-pu/383496)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) <br>- [nemotron](https://forums.developer.nvidia.com/tag/nemotron/1166) | [0](https://forums.developer.nvidia.com/t/function-id-948fe171-ce7a-4332-8bc0-5e14e90259f9-not-found-for-account-4ix-po20vs9o-8u36mro-hjyg2dxzxmy2ysokjk-pu/383496/1) | 22 | [Sep 16](https://forums.developer.nvidia.com/t/function-id-948fe171-ce7a-4332-8bc0-5e14e90259f9-not-found-for-account-4ix-po20vs9o-8u36mro-hjyg2dxzxmy2ysokjk-pu/383496/1) |
| [Request to enable “Public API Endpoints” for my account — moonshotai/kimi-k2.6 returns 404 Function not found](https://forums.developer.nvidia.com/t/request-to-enable-public-api-endpoints-for-my-account-moonshotai-kimi-k2-6-returns-404-function-not-found/378047)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) <br>- [jetson](https://forums.developer.nvidia.com/tag/jetson/587),<br>- [llama](https://forums.developer.nvidia.com/tag/llama/1043),<br>- [nemotron](https://forums.developer.nvidia.com/tag/nemotron/1166),<br>- [llama-31-8b-instruct](https://forums.developer.nvidia.com/tag/llama-31-8b-instruct/1032) | [0](https://forums.developer.nvidia.com/t/request-to-enable-public-api-endpoints-for-my-account-moonshotai-kimi-k2-6-returns-404-function-not-found/378047/1) | 165 | [Jul 24](https://forums.developer.nvidia.com/t/request-to-enable-public-api-endpoints-for-my-account-moonshotai-kimi-k2-6-returns-404-function-not-found/378047/1) |
| [Function not found for account - moonshotai/kimi-k2.6 and deepseek-ai/deepseek-v4-pro-0813 (404)](https://forums.developer.nvidia.com/t/function-not-found-for-account-moonshotai-kimi-k2-6-and-deepseek-ai-deepseek-v4-pro-0813-404/382736)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) <br>- [nim](https://forums.developer.nvidia.com/tag/nim/947),<br>- [nemotron](https://forums.developer.nvidia.com/tag/nemotron/1166),<br>- [deepseek](https://forums.developer.nvidia.com/tag/deepseek/1158) | [0](https://forums.developer.nvidia.com/t/function-not-found-for-account-moonshotai-kimi-k2-6-and-deepseek-ai-deepseek-v4-pro-0813-404/382736/1) | 114 | [Sep 8](https://forums.developer.nvidia.com/t/function-not-found-for-account-moonshotai-kimi-k2-6-and-deepseek-ai-deepseek-v4-pro-0813-404/382736/1) |
| [Moonshotai/kimi-k2.6 returns 404 Function not found for account, while other NIM models work](https://forums.developer.nvidia.com/t/moonshotai-kimi-k2-6-returns-404-function-not-found-for-account-while-other-nim-models-work/379257)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) <br>- [nim](https://forums.developer.nvidia.com/tag/nim/947),<br>- [openclaw](https://forums.developer.nvidia.com/tag/openclaw/1197) | [0](https://forums.developer.nvidia.com/t/moonshotai-kimi-k2-6-returns-404-function-not-found-for-account-while-other-nim-models-work/379257/1) | 104 | [Aug 5](https://forums.developer.nvidia.com/t/moonshotai-kimi-k2-6-returns-404-function-not-found-for-account-while-other-nim-models-work/379257/1) |
| [404 Function not found for account when calling aisingapore/sea-lion-7b-instruct via integrate.api.nvidia.com](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-when-calling-aisingapore-sea-lion-7b-instruct-via-integrate-api-nvidia-com/361577)<br>[Models](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/models/698) | [0](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-when-calling-aisingapore-sea-lion-7b-instruct-via-integrate-api-nvidia-com/361577/1) | 278 | [Feb 23](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-when-calling-aisingapore-sea-lion-7b-instruct-via-integrate-api-nvidia-com/361577/1) |
| [The cosmos reason 1 model do not work with the the api key when i try to use it through it api it says model not found](https://forums.developer.nvidia.com/t/the-cosmos-reason-1-model-do-not-work-with-the-the-api-key-when-i-try-to-use-it-through-it-api-it-says-model-not-found/358478)<br>[Models](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/models/698) <br>- [cosmos](https://forums.developer.nvidia.com/tag/cosmos/1080) | [1](https://forums.developer.nvidia.com/t/the-cosmos-reason-1-model-do-not-work-with-the-the-api-key-when-i-try-to-use-it-through-it-api-it-says-model-not-found/358478/1) | 104 | [Jan 28](https://forums.developer.nvidia.com/t/the-cosmos-reason-1-model-do-not-work-with-the-the-api-key-when-i-try-to-use-it-through-it-api-it-says-model-not-found/358478/4) |
| [404 “Function not found for account” on /v1/chat/completions](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-on-v1-chat-completions/381319)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) <br>- [deepseek](https://forums.developer.nvidia.com/tag/deepseek/1158) | [0](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-on-v1-chat-completions/381319/1) | 119 | [Aug 26](https://forums.developer.nvidia.com/t/404-function-not-found-for-account-on-v1-chat-completions/381319/1) |
| [404 on /v1/chat/completions — Personal account missing Public API Endpoints](https://forums.developer.nvidia.com/t/404-on-v1-chat-completions-personal-account-missing-public-api-endpoints/383883)<br>[Access/Accounts](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/access-accounts/699) | [0](https://forums.developer.nvidia.com/t/404-on-v1-chat-completions-personal-account-missing-public-api-endpoints/383883/1) | 39 | [Sep 21](https://forums.developer.nvidia.com/t/404-on-v1-chat-completions-personal-account-missing-public-api-endpoints/383883/1) |

Topic list, column headers with buttons are sortable.