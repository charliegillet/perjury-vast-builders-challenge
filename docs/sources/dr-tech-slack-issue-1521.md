[Skip to content](https://github.com/slackapi/python-slack-sdk/issues/1521#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/slackapi/python-slack-sdk/issues/1521) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/slackapi/python-slack-sdk/issues/1521) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/slackapi/python-slack-sdk/issues/1521) to refresh your session.Dismiss alert

{{ message }}

[slackapi](https://github.com/slackapi)/ **[python-slack-sdk](https://github.com/slackapi/python-slack-sdk)** Public

- [Notifications](https://github.com/login?return_to=%2Fslackapi%2Fpython-slack-sdk) You must be signed in to change notification settings
- [Fork\\
860](https://github.com/login?return_to=%2Fslackapi%2Fpython-slack-sdk)
- [Star\\
4k](https://github.com/login?return_to=%2Fslackapi%2Fpython-slack-sdk)


# Sending a message with file after uploading the file gives file not found error\#1521

[New issue](https://github.com/login?return_to=https://github.com/slackapi/python-slack-sdk/issues/1521)

Copy link

[New issue](https://github.com/login?return_to=https://github.com/slackapi/python-slack-sdk/issues/1521)

Copy link

Closed

Closed

[Sending a message with file after uploading the file gives file not found error](https://github.com/slackapi/python-slack-sdk/issues/1521#top)#1521

Copy link

Assignees

[![hello-ashleyintech](https://avatars.githubusercontent.com/u/12901850?s=64&u=e234f0035bad509f50c38af3e08edfe792d22e76&v=4)](https://github.com/hello-ashleyintech)

Labels

[Version: 3x](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22Version%3A%203x%22) [questionM-T: User needs support to use the project](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22question%22) M-T: User needs support to use the project [web-client](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22web-client%22)

## Description

[![@nursimaaigoritma](https://avatars.githubusercontent.com/u/106086311?v=4&size=48)](https://github.com/nursimaaigoritma)

[nursimaaigoritma](https://github.com/nursimaaigoritma)

opened [on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issue-2381215238)

Issue body actions

Hello,

I upload a file to Slack, and then send a message to a channel referencing that file. However, if I call them immediately after each other, sending message fails saying it could not find the file. If I wait for about 1 sec between these two operations then it works, I can see the image in the sent message in Slack.

### Reproducible in:

```
slack_sdk==3.27.1
Python 3.10.13
ProductName:            macOS
ProductVersion:         14.1.1
BuildVersion:           23B81
Darwin Kernel Version 23.1.0: Mon Oct  9 21:27:24 PDT 2023; root:xnu-10002.41.9~6/RELEASE_ARM64_T6000
```

#### The Slack SDK version

slack\_sdk==3.27.1

#### Python runtime version

Python 3.10.13

#### OS info

ProductName: macOS

ProductVersion: 14.1.1

BuildVersion: 23B81

Darwin Kernel Version 23.1.0: Mon Oct 9 21:27:24 PDT 2023; root:xnu-10002.41.9~6/RELEASE\_ARM64\_T6000

#### Steps to reproduce:

```
from slack_sdk import WebClient
import ssl
import certifi
import datetime

token = ""
channel_id = ""
img_path = ""

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = WebClient(token, ssl=ssl_context)

fd = open(img_path, 'rb')
slack_response = client.files_upload_v2(
    file=fd.read(),
    alt_txt="screenshot"
)
fd.close()

print(slack_response)

message = [\
            {\
                "type": "section",\
                "text": {\
                    "type": "mrkdwn",\
                    "text": "*Bug Report* :ladybug:"\
                }\
            },\
            {\
                "type": "section",\
                "fields": [\
                    {\
                        "type": "mrkdwn",\
                        "text": "*Company:*\nCompany"\
                    },\
                    {\
                        "type": "mrkdwn",\
                        "text": "*User Name:*\nUser name"\
                    },\
                    {\
                        "type": "mrkdwn",\
                        "text": "*Browser Type:*\nBrowser Type"\
                    },\
                    {\
                        "type": "mrkdwn",\
                        "text": f"*Timestamp:*\n{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"\
                    },\
                    {\
                        "type": "mrkdwn",\
                        "text": "*Title:*\nTitle"\
                    },\
                    {\
                        "type": "mrkdwn",\
                        "text": "*Description:*\nDescription"\
                    },\
                    {\
                        "type": "mrkdwn",\
                        "text": "*Error Message:*\nError Message"\
                    }\
                ]\
            },\
           {\
                "type": "image",\
                "alt_text": "screenshot",\
                "slack_file": {\
                    "id": slack_response["file"]["id"]\
                }\
            }\
        ]

client.chat_postMessage(
    channel=channel_id,
    blocks= message,
)
```

The output is

```
{'ok': True, 'files': [{'id': 'F07AZJY97DE', 'created': 1719608394, ...}\
\
Traceback (most recent call last):\
  File "...", line 73, in <module>\
    client.chat_postMessage(\
  File "myenv/lib/python3.10/site-packages/slack_sdk/web/client.py", line 2564, in chat_postMessage\
    return self.api_call("chat.postMessage", json=kwargs)\
  File "myenv/lib/python3.10/site-packages/slack_sdk/web/base_client.py", line 155, in api_call\
    return self._sync_send(api_url=api_url, req_args=req_args)\
  File "myenv/lib/python3.10/site-packages/slack_sdk/web/base_client.py", line 186, in _sync_send\
    return self._urllib_api_call(\
  File "myenv/lib/python3.10/site-packages/slack_sdk/web/base_client.py", line 317, in _urllib_api_call\
    ).validate()\
  File "myenv/lib/python3.10/site-packages/slack_sdk/web/slack_response.py", line 199, in validate\
    raise e.SlackApiError(message=msg, response=self)\
slack_sdk.errors.SlackApiError: The request to the Slack API failed. (url: https://www.slack.com/api/chat.postMessage)\
The server responded with: {'ok': False, 'error': 'invalid_blocks', 'errors': ['invalid slack file [json-pointer:/blocks/2/slack_file.id/slack_file]'], 'response_metadata': {'messages': ['[ERROR] invalid slack file [json-pointer:/blocks/2/slack_file.id/slack_file]']}}\
```\
\
If I add `time.sleep(1)` just before sending message it works fine. It sends the message with attached file. Sometimes up to 0.5 sec also works.\
\
### Expected result:\
\
I expect file upload to be observable with less latency.\
\
### Actual result:\
\
```\
SlackApiError("The request to the Slack API failed. (url: https://www.slack.com/api/chat.postMessage)\nThe server responded with: {'ok': False, 'error': 'invalid_blocks', 'errors': ['invalid slack file [json-pointer:/blocks/2/slack_file.id/slack_file]'], 'response_metadata': {'messages': ['[ERROR] invalid slack file [json-pointer:/blocks/2/slack_file.id/slack_file]']}}")\
```\
\
## Activity\
\
[![](https://avatars.githubusercontent.com/u/106086311?s=64&v=4)nursimaaigoritma](https://github.com/nursimaaigoritma)\
\
added\
\
[untriaged](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22untriaged%22)\
\
[on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#event-13336591040)\
\
[![](https://avatars.githubusercontent.com/u/12901850?s=64&u=e234f0035bad509f50c38af3e08edfe792d22e76&v=4)hello-ashleyintech](https://github.com/hello-ashleyintech)\
\
self-assigned this\
\
[on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#event-13336692927)\
\
[![](https://avatars.githubusercontent.com/u/12901850?s=64&u=e234f0035bad509f50c38af3e08edfe792d22e76&v=4)hello-ashleyintech](https://github.com/hello-ashleyintech)\
\
added\
\
[needs infoAn issue that is claimed to be a bug and hasn't been reproduced, or otherwise needs more info](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22needs%20info%22) An issue that is claimed to be a bug and hasn't been reproduced, or otherwise needs more info\
\
and removed\
\
[untriaged](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22untriaged%22)\
\
[on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#event-13336693885)\
\
### hello-ashleyintech commented on Jun 28, 2024on Jun 28, 2024\
\
[![@hello-ashleyintech](https://avatars.githubusercontent.com/u/12901850?u=e234f0035bad509f50c38af3e08edfe792d22e76&v=4&size=48)](https://github.com/hello-ashleyintech)\
\
[hello-ashleyintech](https://github.com/hello-ashleyintech)\
\
[on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issuecomment-2197691018)\
\
Contributor\
\
More actions\
\
Thanks for submitting this issue, [@nursimaaigoritma](https://github.com/nursimaaigoritma)! 🙌\
\
Looking over it initially, it does appear to be a latency issue as you identified, but is a bit confusing since it does seem that the file upload API call has fully executed, which indicates a file was uploaded successfully.\
\
Before examining that side of this, I did want to see if using the `url` param instead of `id` within your `slack_file` Block made a difference. You could do something like this:\
\
```\
file_url = slack_response.get("file").get("permalink")\
\
...\
# within your message block kit, replace the image block using `slack_files` with this:\
 {\
        "type": "image",\
        "alt_text": "screenshot",\
        "slack_file": {\
                "id": file_url\
            }\
}\
...\
```\
\
Just wanted to see if using the `permalink` of the file made a difference or not with file retrieval in this case vs. the ID! You can learn more in [this guide](https://api.slack.com/tutorials/tracks/uploading-files-python).\
\
### nursimaaigoritma commented on Jun 28, 2024on Jun 28, 2024\
\
[![@nursimaaigoritma](https://avatars.githubusercontent.com/u/106086311?v=4&size=48)](https://github.com/nursimaaigoritma)\
\
[nursimaaigoritma](https://github.com/nursimaaigoritma)\
\
[on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issuecomment-2197698813)\
\
Author\
\
More actions\
\
It gives another error (again while sending the message):\
\
```\
The server responded with: {'ok': False, 'error': 'invalid_blocks', 'errors': ['input must match regex pattern: ^[F][A-Z0-9]{8,}$ [json-pointer:/blocks/2/slack_file/id]'], 'response_metadata': {'messages': ['[ERROR] input must match regex pattern: ^[F][A-Z0-9]{8,}$ [json-pointer:/blocks/2/slack_file/id]']}}\
```\
\
Url was like this\
\
```\
https://our-workspace.slack.com/files/xxxxxxxxxxx/xxxxxxxxxxx/uploaded_file\
```\
\
### seratch commented on Jun 28, 2024on Jun 28, 2024\
\
[![@seratch](https://avatars.githubusercontent.com/u/19658?u=f4b4e7ec8ee32f3043d4d57aca50514113ed2328&v=4&size=48)](https://github.com/seratch)\
\
[seratch](https://github.com/seratch)\
\
[on Jun 28, 2024on Jun 28, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issuecomment-2197783409)\
\
Contributor\
\
More actions\
\
[@nursimaaigoritma](https://github.com/nursimaaigoritma) files.upload v2 has a slight delay in completing the file upload process. Therefore, for this use case, your app needs to poll the `files.info` API endpoint with the uploaded file IDs until the shares properties are populated (indicating that the files are successfully uploaded and shared). Please refer to [#1329 (comment)](https://github.com/slackapi/python-slack-sdk/issues/1329#issuecomment-1430589611) for more details.\
\
If you try to embed the file permalink in a block before the process is completed, displaying the block can result in the error you've encountered. I understand this could be frustrating but I hope this clarifies.\
\
### nursimaaigoritma commented on Jun 29, 2024on Jun 29, 2024\
\
[![@nursimaaigoritma](https://avatars.githubusercontent.com/u/106086311?v=4&size=48)](https://github.com/nursimaaigoritma)\
\
[nursimaaigoritma](https://github.com/nursimaaigoritma)\
\
[on Jun 29, 2024on Jun 29, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issuecomment-2198282361)\
\
Last edited by nursimaaigoritma\
\
Author\
\
More actions\
\
Yes this absolutely clarifies. Thank you for the response. Would you consider adding it to documentation (or I may have missed it)? As I understand, making files\_upload\_v2 asynchronous was a deliberate choice and polling is the only way.\
\
### nursimaaigoritma commented on Jul 1, 2024on Jul 1, 2024\
\
[![@nursimaaigoritma](https://avatars.githubusercontent.com/u/106086311?v=4&size=48)](https://github.com/nursimaaigoritma)\
\
[nursimaaigoritma](https://github.com/nursimaaigoritma)\
\
[on Jul 1, 2024on Jul 1, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issuecomment-2200069235)\
\
Last edited by nursimaaigoritma\
\
Author\
\
More actions\
\
Can I assume file upload is completed if client.files\_info(file=file\_id) returns "ok": True?\
\
I try this\
\
```\
# uploading file is same\
# ...\
\
# check if completed\
import polling\
polling.poll(\
    lambda: client.files_info(file=file_id)["ok"],\
    step=0.5,\
    timeout=10\
)\
\
# At this point, I assume file upload is complete and I can use the id in a message\
client.chat_postMessage(\
    channel=channel_id,\
    blocks= message,\
)\
```\
\
But the problem persists. Should I check something else in the "files\_info" response?\
\
### seratch commented on Jul 3, 2024on Jul 3, 2024\
\
[![@seratch](https://avatars.githubusercontent.com/u/19658?u=f4b4e7ec8ee32f3043d4d57aca50514113ed2328&v=4&size=48)](https://github.com/seratch)\
\
[seratch](https://github.com/seratch)\
\
[on Jul 3, 2024on Jul 3, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#issuecomment-2205188813)\
\
Contributor\
\
More actions\
\
> Should I check something else in the "files\_info" response?\
\
Yes, you need to check the updates on the file metadata. Specifically, mime\_type, shares, and a few others will be filled once the upload process completes.\
\
👍React with 👍1Reacted by nursimaaigoritma\
\
[![](https://avatars.githubusercontent.com/u/19658?s=64&u=f4b4e7ec8ee32f3043d4d57aca50514113ed2328&v=4)seratch](https://github.com/seratch)\
\
added\
\
[questionM-T: User needs support to use the project](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22question%22) M-T: User needs support to use the project\
\
[web-client](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22web-client%22)\
\
[Version: 3x](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22Version%3A%203x%22)\
\
and removed\
\
[needs infoAn issue that is claimed to be a bug and hasn't been reproduced, or otherwise needs more info](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22needs%20info%22) An issue that is claimed to be a bug and hasn't been reproduced, or otherwise needs more info\
\
[on Jul 3, 2024on Jul 3, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#event-13375301857)\
\
[![](https://avatars.githubusercontent.com/u/19658?s=64&u=f4b4e7ec8ee32f3043d4d57aca50514113ed2328&v=4)seratch](https://github.com/seratch)\
\
closed this as [completed](https://github.com/slackapi/python-slack-sdk/issues?q=is%3Aissue%20state%3Aclosed%20archived%3Afalse%20reason%3Acompleted) [on Jul 12, 2024on Jul 12, 2024](https://github.com/slackapi/python-slack-sdk/issues/1521#event-13482345844)\
\
[Sign up for free](https://github.com/signup?return_to=https://github.com/slackapi/python-slack-sdk/issues/1521)**to join this conversation on GitHub.** Already have an account? [Sign in to comment](https://github.com/login?return_to=https://github.com/slackapi/python-slack-sdk/issues/1521)\
\
## Metadata\
\
## Metadata\
\
### Assignees\
\
- [![@hello-ashleyintech](https://avatars.githubusercontent.com/u/12901850?s=64&u=e234f0035bad509f50c38af3e08edfe792d22e76&v=4)\\
hello-ashleyintech](https://github.com/hello-ashleyintech)\
\
### Labels\
\
[Version: 3x](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22Version%3A%203x%22) [questionM-T: User needs support to use the project](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22question%22) M-T: User needs support to use the project [web-client](https://github.com/slackapi/python-slack-sdk/issues?q=state%3Aopen%20label%3A%22web-client%22)\
\
### Type\
\
No type\
\
### Projects\
\
No projects\
\
### Milestone\
\
No milestone\
\
### Relationships\
\
None yet\
\
### Development\
\
No branches or pull requests\
\
### Participants\
\
[![@seratch](https://avatars.githubusercontent.com/u/19658?s=64&u=f4b4e7ec8ee32f3043d4d57aca50514113ed2328&v=4)](https://github.com/seratch)[![@hello-ashleyintech](https://avatars.githubusercontent.com/u/12901850?s=64&u=e234f0035bad509f50c38af3e08edfe792d22e76&v=4)](https://github.com/hello-ashleyintech)[![@nursimaaigoritma](https://avatars.githubusercontent.com/u/106086311?s=64&v=4)](https://github.com/nursimaaigoritma)\
\
## Issue actions\
\
- ![](https://github.githubassets.com/assets/github-copilot-app-light-15ad5534265eeacd.svg)Open in GitHub Copilot app\
\
You can’t perform that action at this time.