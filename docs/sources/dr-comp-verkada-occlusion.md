For the complete documentation index, see [llms.txt](https://help.verkada.com/llms.txt). This page is also available as [Markdown](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts.md).

Occlusion Alerts notify users when a camera’s view is blocked or obscured, helping security teams ensure that all cameras maintain clear visibility of key areas.

- Occlusion Alerts may take up to one day to calibrate as the system learns the scene and creates a baseline reference image. Once this baseline is established, the camera will begin generating alerts when its view becomes obstructed.

- When an occlusion occurs, the camera waits about two minutes before sending the alert to minimize false positives.


- You need [Site Admin permissions](https://help.verkada.com/command/users-and-permissions/roles-and-permissions-for-command) for the site a camera is in to configure occlusion alerts.

- Cameras in LPR mode do not support occlusion alerts.


* * *

## **Configure occlusion alerts**[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#configure-occlusion-alerts)

### **Create Alert > Events**[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#create-alert-greater-than-events)

1

**On the Command homepage, left navigation, click Alerts .**

2

**At the top, click New Alert.**

3

**On Select Event, choose Camera > Occlusion Detection.**

4

**On Cameras:**

1. Choose to receive alerts from **Sites** or **Individual Cameras**.

2. Click **Done** to continue.


5

**Click Done and continue with the alert** [**notification schedule**](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts#create-alert-greater-than-cameras) **.**

### Create Alert > Notification Schedule[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#create-alert-greater-than-notification-schedule)

1

**On Notification Schedule, specify the days and times for the alerts to send notifications. Alerts generate 24/7 by default.**

![](https://help.verkada.com/~gitbook/image?url=https%3A%2F%2F1795869993-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FylYKicREo6JpuOJH4teK%252Fuploads%252Fgit-blob-b9042c786a9dd12580abefdd20f412fe59cbac5e%252F7b61969c185d482c85ec3b7f15a687d75aee8d13.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=45b70a898f2e0527268580dd64a61b97&sv=3)

2

**Click Done and continue with the alert** [**notification**](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts#create-alert-greater-than-notification) **.**

### Create Alert > Notification[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#create-alert-greater-than-notification)

1

**On Notification, add users individually or assign the alert to a group.**

2

**Select the dropdown menu next to a user or group to choose their notification method(s). Recipients can be notified via push, SMS, messaging platform alerts, or email notifications.**

![](https://help.verkada.com/~gitbook/image?url=https%3A%2F%2F1795869993-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FylYKicREo6JpuOJH4teK%252Fuploads%252FB3d7G5pdaN9CXvXFdRgb%252FScreenshot_2026-04-06_at_10_03_04%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Dc2bb4e66-d8ae-4b28-bd4e-635a4c9b4241&width=768&dpr=3&quality=100&sign=ee70d64330e59337e9ebaa00af22a023&sv=3)

Any recipient added to this alert will see it appear under the **Shared Alerts** section of their **Alerts** page.

3

**(Optional) By default, you will be an alert recipient. Select the dropdown menu and click Delete to remove yourself.**

4

**Click Done and continue with the alert's** [**optional settings**](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts#optional-settings) **, or** [**finish the alert**](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts#finish-the-alert) **.**

### Optional settings[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#optional-settings)

#### Create Alert > Operations[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#create-alert-greater-than-operations)

1

**Toggle on Route to Operations to create a ticket from the alert.**

2

**(Optional) Select Ticket Instructions to add information to the ticket and click Done.**

3

**Click Done and continue to** [**finish the alert**](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts#finish-the-alert) **.**

#### Create Alert > Device Action[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#create-alert-greater-than-device-action)

In addition to notifying individuals, you can configure your horn speaker to play when an alert is triggered. These alerts can be text-to-speech or an uploaded MP3 file.

1

**On Device Action, select the horn speaker(s) you want to play your message.**

2

**Select your notification preference (Text to Speech or Audio File).**

a. For **Text to Speech,** enter a message up to 200 characters.
b. For **Audio File,** drag and drop the file or click **choose a file** to upload your audio clip.

![](https://help.verkada.com/~gitbook/image?url=https%3A%2F%2F1795869993-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FylYKicREo6JpuOJH4teK%252Fuploads%252Fgit-blob-6eebd070cac52d81c895573628cb7b21ba245804%252Fbd7aa4597a411933461874e312ac1e72683f4dab.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8693d0f03f208ccc33b4c193630bb2e9&sv=3)

3

**Click Done and continue to** [**finish the alert**](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts#finish-the-alert) **.**

### Finish the alert[Direct link to heading](https://help.verkada.com/verkada-cameras/analytics/create-camera-event-alerts/occlusion-alerts\#finish-the-alert)

1

**In the bottom right of the configuration window, click Next.**

2

**Enter a descriptive name for the alert.**

3

**Click Done to complete the setup.**

![](https://help.verkada.com/~gitbook/image?url=https%3A%2F%2F1795869993-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FylYKicREo6JpuOJH4teK%252Fuploads%252FIZ32hKtacP5b4UOUvsXG%252FScreenshot%25202026-04-06%2520at%25209.35.06%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Dcfccfaf4-d2b9-4566-882c-fe6a23f98dcd&width=768&dpr=3&quality=100&sign=7472a93ff3000b83f6571e29c7e87eb1&sv=3)

Last updated 5 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.verkada.com/privacy/privacy-policy/).

AcceptReject