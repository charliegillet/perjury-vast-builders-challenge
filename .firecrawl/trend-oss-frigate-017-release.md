[Skip to content](https://github.com/blakeblackshear/frigate/discussions/22137#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/blakeblackshear/frigate/discussions/22137) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/blakeblackshear/frigate/discussions/22137) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/blakeblackshear/frigate/discussions/22137) to refresh your session.Dismiss alert

{{ message }}

[blakeblackshear](https://github.com/blakeblackshear)/ **[frigate](https://github.com/blakeblackshear/frigate)** Public

- Sponsor







# Sponsor blakeblackshear/frigate























##### GitHub Sponsors

[Learn more about Sponsors](https://github.com/sponsors)









[![@blakeblackshear](https://avatars.githubusercontent.com/u/569905?s=80&v=4)](https://github.com/blakeblackshear)



[blakeblackshear](https://github.com/blakeblackshear)



[blakeblackshear](https://github.com/blakeblackshear)







[Sponsor](https://github.com/sponsors/blakeblackshear)











[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=80&v=4)](https://github.com/NickM-27)



[NickM-27](https://github.com/NickM-27)



[NickM-27](https://github.com/NickM-27)







[Sponsor](https://github.com/sponsors/NickM-27)











[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=80&v=4)](https://github.com/hawkeye217)



[hawkeye217](https://github.com/hawkeye217)



[hawkeye217](https://github.com/hawkeye217)







[Sponsor](https://github.com/sponsors/hawkeye217)















[Learn more about funding links in repositories](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository).




[Report abuse](https://github.com/contact/report-abuse?report=blakeblackshear%2Ffrigate+%28Repository+Funding+Links%29)

- [Notifications](https://github.com/login?return_to=%2Fblakeblackshear%2Ffrigate) You must be signed in to change notification settings
- [Fork\\
3.7k](https://github.com/login?return_to=%2Fblakeblackshear%2Ffrigate)
- [Star\\
36.3k](https://github.com/login?return_to=%2Fblakeblackshear%2Ffrigate)


# 0.17.0 Release  \#22137

[blakeblackshear](https://github.com/blakeblackshear)

started this conversation in
[General](https://github.com/blakeblackshear/frigate/discussions/categories/general)

[0.17.0 Release](https://github.com/blakeblackshear/frigate/discussions/22137#top)#22137

[![@blakeblackshear](https://avatars.githubusercontent.com/u/569905?s=40&v=4)\\
blakeblackshear](https://github.com/blakeblackshear)

on Feb 26Feb 27, 2026·
29 comments
·
83 replies


[Return to top](https://github.com/blakeblackshear/frigate/discussions/22137#top)

Discussion options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

## [![](https://avatars.githubusercontent.com/u/569905?s=64&v=4)\ blakeblackshear](https://github.com/blakeblackshear) [on Feb 26Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussion-9542608)   Maintainer

|     |
| --- |
| ## Images<br>- [ghcr.io/blakeblackshear/frigate:0.17.0](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698571246?tag=0.17.0)<br>- [ghcr.io/blakeblackshear/frigate:0.17.0-standard-arm64](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698569586?tag=0.17.0-standard-arm64)<br>- [ghcr.io/blakeblackshear/frigate:0.17.0-tensorrt](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698573647?tag=0.17.0-tensorrt)<br>- [ghcr.io/blakeblackshear/frigate:0.17.0-rk](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698579220?tag=0.17.0-rk)<br>- [ghcr.io/blakeblackshear/frigate:0.17.0-rocm](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698576270?tag=0.17.0-rocm)<br>- [ghcr.io/blakeblackshear/frigate:0.17.0-tensorrt-jp6](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698571350?tag=0.17.0-tensorrt-jp6)<br>- [ghcr.io/blakeblackshear/frigate:0.17.0-synaptics](https://github.com/blakeblackshear/frigate/pkgs/container/frigate/698578081?tag=0.17.0-synaptics)<br>## Changes since RC3<br>- None<br># Major Changes for 0.17.0<br>## Breaking Changes<br>There are several breaking changes in this release, Frigate will attempt to update the configuration automatically. In some cases manual changes may be required. It is always recommended to back up your current config and database before upgrading:<br>1. Simply copy your current config file to a new location<br>2. Stop Frigate and make a copy of the `frigate.db` file<br>- **GenAI now supports reviews and object descriptions**. As a result, the global `genai` config now only configures the provider. Other fields have moved under `objects -> genai`. See the new GenAI [documentation](https://docs.frigate.video/category/generative-ai).<br>- **Recordings retention is now fully tiered**. This means that `record -> continuous` and `record -> motion` are separate config fields. See the examples in the [documentation](https://docs.frigate.video/configuration/record).<br>- **Some of the LPR models have been updated**, and **most users should manually switch to the `small` model**, which performs well on both CPU and GPU. The `large` model is the same as 0.16's and is not as accurate as the upgraded `small` model in 0.17. Use `large` **only** if you live in a region with multi-line plates and you are having issues detecting text on them with the `small` model.<br>- **strftime\_fmt** was deprecated in 0.16, and should now be fully removed from the config in 0.17. Date/time formatting is based on the language selected in the UI.<br>- **The auto detection logic for camera resolution has changed.** Some cameras fail to correctly advertise their resolution, and in previous versions, a default value was assumed that was not always correct. You may need to explicitly define `detect` resolution `width` and `height` for cameras in your config if Frigate hangs on startup.<br>- **The `exec`, `expr`, and `echo` sources for go2rtc are now removed by default** to reduce the security risk if an attacker has access to the configuration. This can be disabled using an environment variable `GO2RTC_ALLOW_ARBITRARY_EXEC` A separate configuration for this for HA addon users will come in a later beta. See the [documentation](https://docs.frigate.video/configuration/restream#security-restricted-stream-sources).<br>- Nvidia GTX 900 series GPUs are no longer supported due to updates to ONNX Runtime<br>## New Features<br>Frigate 0.17 introduces several major new features.<br>### Classification Model Training<br>Frigate 0.17 supports classification models in two separate types: _state classification_ and _object classification_. These models are trained locally on your machine using `ImageNet` via `MobileNetV2`.<br>#### State Classification<br>State classification allows you to choose a certain region of camera(s) with multiple states, and train on images showing these states. For example, you could create a state classification model to determine if a gate is currently open or closed.<br> ![Screen Shot 2025-10-27 at 07 51 47 AM](https://private-user-images.githubusercontent.com/14866235/506038561-ccedcb18-2a65-40f3-8a94-1be180b5913f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNDg2NjIzNS81MDYwMzg1NjEtY2NlZGNiMTgtMmE2NS00MGYzLThhOTQtMWJlMTgwYjU5MTNmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc3YzUxZjNjNjE1ZWQ3ODNhOTRiMDNjYjU1ZDFiN2JmOGFjZDYyMWVkZjM5OTEzN2VkZjBmODI2OGUzNjFkODEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.Sh2_y7v8pzabgw05Ahc2gmTWgVE8rJBUKl0l8215W2E) <br>See the [documentation](https://docs.frigate.video/configuration/custom_classification/state_classification).<br>#### Object Classification<br>Object classification allows you to choose an object type, like `dog`, and classify specific dogs. For example, you can train the model to classify your dog `Fido` and add a sub label, while not labeling unknown dogs. Another example would be classifying if a person in a construction site is wearing a helmet or not.<br> ![Screen Shot 2025-10-27 at 07 50 56 AM](https://private-user-images.githubusercontent.com/14866235/506038184-999cf86a-f5a7-4772-9a80-10298a4a8b80.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNDg2NjIzNS81MDYwMzgxODQtOTk5Y2Y4NmEtZjVhNy00NzcyLTlhODAtMTAyOThhNGE4YjgwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNjMzhiNWEwOGRiZmJlZjA4NzMwZjA5NmVlYjlmOTNjODNiYzNhZjE3OGM4MjRiMTY4YWYzOWU5MDFhYjc2MWUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.3GKNef0WCmnsKLqwysotrJaIjrcc5ylBHDbtefiYINo) <br>See the [documentation](https://docs.frigate.video/configuration/custom_classification/object_classification).<br>### Custom Viewer Roles<br>Frigate 0.17 now has the ability to create additional viewer user roles to limit access to specific cameras. Users with the `admin` role can create a uniquely named role from the UI (or `auth --> roles` in the config) and assign at least one camera to it. Users assigned to the new role will have:<br>- Guarded API access<br>- Limited frontend access, following what the `viewer` role has access to (Live, Review/History, Explore, Exports), but only to the assigned cameras<br>See the [documentation](https://docs.frigate.video/configuration/authentication#user-roles).<br>### Review Item Summary with GenAI<br>Frigate 0.17 supports using GenAI to summarize review items. Unlike object descriptions which add a searchable description, review summaries have a structured output that instruct the AI provider to generate a title, description, and classify the activity as dangerous, suspicious, or normal.<br>This information is displayed in the UI automatically making it easier to see when activity requires further review and easier to understand what is happening during a particular video segment.<br>See the [documentation](https://docs.frigate.video/configuration/genai/genai_review).<br>### Semantic Search Triggers<br>Triggers utilize Semantic Search to automate actions when a tracked object matches a specified image or description. Triggers can be configured so that Frigate executes a specific actions when a tracked object's image or description matches a predefined image or text, based on a similarity threshold. Triggers are managed per camera and can be configured via the Frigate UI in the Settings page under the Triggers tab.<br>See the [documentation](https://docs.frigate.video/configuration/semantic_search#triggers).<br>## Object Detector Improvements<br>Frigate 0.17 brings performance increases for many detectors as well as support for new object detection hardware.<br>### Nvidia GPU Performance<br>Support for Nvidia GPUs has been enhanced by implementing CUDA Graphs. CUDA Graphs work to reduce the involvement of the CPU for each inference, leading to faster inference times and lower CPU usage. CUDA graphs do have some limitations based on the complexity of the model, which means that YOLO-NAS, Semantic Search, and LPR models are not accelerated with CUDA Graphs. They will still continue to run on GPU as they did before.<br>### Intel OpenVINO<br>Frigate 0.17 supports running models on Intel NPUs, for many models performance on NPU is similar to GPU but more efficient, leaving room to run more enrichment features on the GPU.<br>OpenVINO has also had many optimizations put in place to reduce memory and CPU utilization for object detection.<br>### RKNN<br>Frigate 0.17 brings several improvements to RKNN platform including:<br>- Automatic Model Conversion: automatically convert ONNX models to RKNN format. This allows Frigate+ and other models to be seamlessly configured and converted on startup.<br>- Accelerated Enrichment Support: convert and run Semantic Search and Face Recognition models using the NPU. This greatly enhances performance while maintaining high accuracy with `large` model sizes.<br>### Apple Silicon<br>Frigate 0.17 supports running object detection on Apple Silicon NPU. This is provided through the [Apple Silicon Detector](https://github.com/frigate-nvr/apple-silicon-detector) which runs on the host and connects via IPC proxy to Frigate, providing fast and efficient inferences when run within the same Apple device.<br>See the [documentation](https://docs.frigate.video/configuration/object_detectors#apple-silicon-detector).<br>### YOLOv9 on Google Coral<br>Frigate 0.17 supports running a quantized version of `YOLOv9` on Coral devices, bringing improved accuracy over the default `mobiledet` model. Note that due to hardware limitations, only a subset of the objects on the standard COCO labelmap is included. Frigate+ has also added support for YOLOv9 models on the Google Coral and includes support for all 41 Frigate+ labels.<br>See the [documentation](https://docs.frigate.video/configuration/object_detectors/#edgetpu-supported-models).<br>### New Community Supported Detectors<br>Frigate 0.17 has community support for several new object detectors:<br>- **MemryX**: MemryX MX3 M.2 module. [Documentation](https://docs.frigate.video/configuration/object_detectors#memryx-mx3)<br>- **Degirum SDK**: a proxy for inference with a variety of models. [Documentation](https://docs.frigate.video/configuration/object_detectors#degirum)<br>- **Synaptics**: Synaptics SL1680 NPU. [Documentation](https://docs.frigate.video/configuration/object_detectors#synaptics)<br>## Frontend Improvements<br>In addition to supporting the new features, the frontend has many improvements.<br>### Detail Stream<br>History view in 0.17 supports an additional view mode, _Detail_. This mode shows a card for each review item, and expanding a card reveals all tracked objects and their lifecycle events. Selecting any lifecycle event seeks the video to that exact timestamp. You can also overlay a tracked object's path on the video to help with debugging.<br>### Redesigned Tracked Object Details pane<br>The Tracked Object Details pane in Explore has been redesigned to streamline the layout and consolidate related information. The _Object Lifecycle_ tab is now the _Tracking Details_ tab, which displays video overlays of the tracked object instead of static images, giving a clearer and more intuitive view of its activity.<br>### Revamped Settings<br>Frigate 0.17 has a revamped Settings menu with a sidebar that categorizes the available options. This brings more scalability which will make it easier to support full UI configuration in a future version.<br> ![Screenshot 2025-10-12 at 6 54 14 AM](https://private-user-images.githubusercontent.com/14866235/500255599-6b0689ac-24bf-4d9d-8aae-0371eb099e58.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNDg2NjIzNS81MDAyNTU1OTktNmIwNjg5YWMtMjRiZi00ZDlkLThhYWUtMDM3MWViMDk5ZTU4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWMyYjFiYjk4MjQyZTYyZjY0YmI0MmRmZDg1ZGVmMDA4M2Y5YWY0MmZlMWYyYzVkNjIxNTg1MGQ2YTU1NTgzNWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.MecGkuQsW_JDrrTIPfqSst2NBq5AZ3C2SjimYAyT2So) <br>**NOTE: The Debug view has been moved to the single camera Live view instead of Settings.** Access the Debug view by enabling the switch under the Live view settings (cog icon) menu.<br>### Add Camera Wizard<br>Frigate 0.17 supports adding camera via the UI without manually modifying your configuration file. When installing and starting Frigate for the first time, the main dashboard will include a button to start adding cameras via the Wizard.<br>Access the Wizard from the `Cameras --> Management` page in Settings.<br>### Update Without Restarting<br>Frigate 0.17 supports saving many more features dynamically. Cameras, zones, and masks will not require a restart to take effect when saved through the UI. More will come in future versions.<br>### Configuration Safe Mode<br>If an invalid configuration is detected, Frigate will enter **safe mode** and highlight the location of the issue. While in safe mode, the frontend is limited to the configuration editor, making it easy to correct the problem directly in the UI without needing an external file editor.<br>### Other Notable Frontend Improvements<br>- **No recordings indicator on the History timeline.** When no recordings are available, the timeline now displays a blank background to make this clear at a glance.<br>- **Clickable Birdseye view.** When using the Frigate UI, you can now click a camera within Birdseye to jump directly to its individual Live view.<br>- **Object paths in Debug view.** The Debug view can now display each tracked object's path — just enable the _Paths_ toggle.<br>- **Audio debugging support.** When audio detection is enabled, the Debug view includes an Audio tab showing live dbFS and RMS values from the camera’s microphone.<br>## Other Backend Features and Improvements<br>### Audio Transcription and Analysis<br>Frigate 0.17 supports fully local audio transcription using either `sherpa-onnx` or `faster-whisper`. The single camera Live view in the Frigate UI supports live transcription of audio for streams defined with the audio role, and any `speech` events in Explore can be transcribed and/or translated through the Transcribe button in the Tracked Object Details pane.<br>See the [documentation](https://docs.frigate.video/configuration/audio_detectors#audio-transcription).<br>### Process and Efficiency Improvements<br>Frigate 0.17 uses the forkserver spawn method, this allows for better segmented memory control and better process management. Some processes are also started with lower priority, allowing the most important processes to have more CPU time when it is required.<br>### Review Item Improvements<br>Review items have been refined to behave more intuitively:<br>- **Revamped stationary object tracking.** Stationary object tracking has been enhanced to use new features to reduce incorrectly marking objects as active:<br>  - Tracking now uses a history of the object's positions to better avoid inaccurate bounding boxes making the object be considered active.<br>  - If an object is marked as having moved, Frigate will use image heuristics to compare the object from when it was known to be stationary to double-check if the object has moved from its original position.<br>- **Smarter handling of loitering objects.** Stationary behavior is now dynamic based on object type. Objects that are normally stationary for long periods (e.g., cars) will no longer keep a review item active indefinitely when stopped inside a loitering zone. Objects that are not expected to remain still (e.g., people) will continue the review item as long as they stay within the zone.<br>  <br>- **Severity-based review item cutoff.** Review items now end when a higher-severity event (such as an `alert` for arriving home) finishes. Ongoing lower-severity motion (e.g., passing cars) will no longer keep the higher-severity review item alive. In these cases, the `alert` ends and a new `detection` review item begins immediately.<br>  <br>### Enrichment Improvements<br>- LPR now includes a normalization configuration, this allows removing some commonly confused characters such as `-`, ``, etc. to ensure that plates are more consistently recognized as the same plate. [Documentation](https://docs.frigate.video/configuration/license_plate_recognition#normalization-rules)<br>- LPR now uses newer PaddleOCR models with support for Chinese characters.<br>- All enrichments can now be assigned a specific device with the `device` config option. This is useful in cases when multiple GPUs are available. [Documentation](https://docs.frigate.video/configuration/reference)<br>### Other Improvements<br>- IPv6 can be toggled via the config with `networking -> ipv6 -> enabled`. [Documentation](https://docs.frigate.video/configuration/reference)<br>- There is now config support for mapping Frigate roles to arbitrary values used in proxy headers. [Documentation](https://docs.frigate.video/configuration/authentication#role-mapping)<br>- MQTT now has a dedicated topic for camera health / status. [Documentation](https://docs.frigate.video/integrations/mqtt#frigatecamera_namerolestatus)<br>- go2rtc support for HomeKit has now been improved, including persistent configuration being saved automatically when a camera is shared with HomeKit. [Documentation](https://docs.frigate.video/guides/configuring_go2rtc#homekit-configuration)<br>- Add a toggle in the UI Settings to always overlay camera names on the Live dashboard<br>- Add browser console logging to help debug Live view issues [Documentation](https://docs.frigate.video/configuration/live/#live-player-error-messages)<br>- Add a fallback timeout value to the UI Settings pane to configure the amount of time to wait to fall back to jsmpeg after the MSE player fails<br>- Add the ability to download an instant snapshot from single camera Live view<br>- Recording playback bugfixes and efficiency improvements should cause playback to start more quickly<br>- User account passwords have a stricter password policy (minimum length and special characters) for improved security<br>- Add the ability to dynamically toggle GenAI per camera via MQTT<br>* * *<br>_This discussion was created from the release [0.17.0 Release](https://github.com/blakeblackshear/frigate/releases/tag/v0.17.0)._ |

6You must be logged in to vote

👍11🎉11❤️6🚀6

All reactions

- 👍11
- 🎉11
- ❤️6
- 🚀6

## Replies:   29 comments  ·  83 replies

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/156946243?s=64&v=4)\ pratikrath126](https://github.com/pratikrath126) [on Feb 26Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15941649)

|     |
| --- |
| Congrats on the release! Lots of great new features—classification training, custom viewer roles, and Apple Silicon support are exciting. Thanks for your hard work! \\ud83c\\udf89 |

3You must be logged in to vote

🎉1

All reactions

- 🎉1

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/206359220?s=64&v=4)\ rbestuar](https://github.com/rbestuar) [on Feb 26Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15942021)

|     |
| --- |
| Looking forward to what's to come. I appreciate all of your hard work! Thank you |

1You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/806426?s=64&v=4)\ kbuck1](https://github.com/kbuck1) [on Feb 26Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15942114)

|     |
| --- |
| Amazing improvements and great update. Thanks to everyone involved for this wonderful release. |

1You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/9057650?s=64&v=4)\ Ba-pt0u](https://github.com/Ba-pt0u) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15945022)

|     |
| --- |
| Amazing release ! I'm going to update as soon as available on HA !<br>Thinking to take a Friagte+ subscription also to support this amazing project. |

2You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/60105043?s=64&v=4)\ H1ghSyst3m](https://github.com/H1ghSyst3m) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15950635)

|     |
| --- |
| Finally!! Thx for the Amazing update! I always waited for a feature like Classification Model Training, now I can train it on only my cats :D will keep my Frigate Subcription |

2You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/37629938?s=64&v=4)\ GaryOkie](https://github.com/GaryOkie) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15950686)

|     |
| --- |
| It looks like the state classification example in the doc duplicated the gate closed image rather than show both open and closed images. But wow, what an incredible update! |

2You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/3155291?s=64&v=4)\ def1149](https://github.com/def1149) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15950772)

|     |
| --- |
| I haven't followed the 0.17 development. Are there any specifics that need addressing before updating from 0.16.4?<br>I'm using the Stand Alone Frigate server and the HA Integration.<br>I always back up the config and database between major updates. |

1You must be logged in to vote

All reactions

2 replies


[![@H1ghSyst3m](https://avatars.githubusercontent.com/u/60105043?s=60&v=4)](https://github.com/H1ghSyst3m)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [H1ghSyst3m](https://github.com/H1ghSyst3m) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15950810)

|     |
| --- |
| Then you are ready to go when config and database are backed up.<br>I myself am also HA, no problems til now |

👍1

All reactions

- 👍1

[![@def1149](https://avatars.githubusercontent.com/u/3155291?s=60&v=4)](https://github.com/def1149)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [def1149](https://github.com/def1149) [on Mar 4Mar 4, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15999835)

|     |
| --- |
| Upated from 16.4 five days ago. Not using any new features.<br>Rock solid so far |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/26333781?s=64&v=4)\ xury77](https://github.com/xury77) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15950985)

|     |
| --- |
| Can I define the crop area for state classification myself? When selecting from the GUI, I cannot define a rectangle, only a square. This makes the area unnecessarily large. |

1You must be logged in to vote

All reactions

1 reply


[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [NickM-27](https://github.com/NickM-27) [on Feb 27Feb 27, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15950997)   Collaborator Sponsor

|     |
| --- |
| It needs to be a square, it does not matter if there is parts of the area that are not related to the state |

👍2

All reactions

- 👍2

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/17104473?s=64&v=4)\ haldi4803](https://github.com/haldi4803) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15954682)

|     |
| --- |
| ![image](https://private-user-images.githubusercontent.com/17104473/556365734-b616c742-4903-4cdd-9e5c-aeca04c23b54.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNzEwNDQ3My81NTYzNjU3MzQtYjYxNmM3NDItNDkwMy00Y2RkLTllNWMtYWVjYTA0YzIzYjU0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTcyZTliYWFkODRkZWY1YTVlOTYxZjQ0N2MwMTc5YzFkZmFmMWE3Zjc2MWVjMjhkOTcwOWYyNDlkM2ZiMTFlMzkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.eeuAsgqD0Ri8T69pE0IwmDxnJ1g7gd4vCK3TyQ5LzBM) ![image](https://private-user-images.githubusercontent.com/17104473/556365902-846e038b-b54c-401c-aff6-75b1499b4dcd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNzEwNDQ3My81NTYzNjU5MDItODQ2ZTAzOGItYjU0Yy00MDFjLWFmZjYtNzViMTQ5OWI0ZGNkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIwMzZlYzZkMmMyMjQ2ZTk4MTFlYzIzNmE5MTU1NjkyZDdhZGUwZjEzYmNkNDRmNWJlYjNlMWU4YTk0YWZjNzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.NhIZuUAz7m-wt5Bo1SGMhLo53O5-D6tBaV3IrVerOTE) ![image](https://private-user-images.githubusercontent.com/17104473/556365955-83d88c08-dcdf-44b0-86f7-c9ad821991b0.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNzEwNDQ3My81NTYzNjU5NTUtODNkODhjMDgtZGNkZi00NGIwLTg2ZjctYzlhZDgyMTk5MWIwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWMyNWRhOTYyZGMxOWVkNmUyMTUzNjU1Zjg1ZjI3NzlhZjlhOWU1ZGVjNDc0YWJhMzNiYzRlODA1ZjZhYTAwZWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.keOs8w9C9zu2lH3PFrYa-0-KYyFMkgi1CmYO-TxqlXg) <br>Why do i get "alerts" for what should be "detections" ? |

1You must be logged in to vote

All reactions

5 replies


[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [hawkeye217](https://github.com/hawkeye217) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15954708)   Collaborator

|     |
| --- |
| The message under the Alerts checkboxes tells you why: _All Person and Car objects on Einfahrt will be shown as Alerts_<br>This is Frigate's default behavior. If you want to change it, you'll need to manually edit your config. See the official documentation: [https://docs.frigate.video/configuration/review/#restricting-alerts-to-specific-labels](https://docs.frigate.video/configuration/review/#restricting-alerts-to-specific-labels) |

👍1

All reactions

- 👍1

[![@haldi4803](https://avatars.githubusercontent.com/u/17104473?s=60&v=4)](https://github.com/haldi4803)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [haldi4803](https://github.com/haldi4803) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15954722)

|     |
| --- |
| Did that change recently? Because i'm sure i didn't have it before 17.0<br>made it simple by adding another Zone and alow Alerts only in this zone. |

All reactions

[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [hawkeye217](https://github.com/hawkeye217) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15954746)   Collaborator

|     |
| --- |
| No, there were no changes to Review behavior in 0.17. |

All reactions

[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [hawkeye217](https://github.com/hawkeye217) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15954758)   Collaborator

|     |
| --- |
| Also, don't forget that [presence in a zone is based on the bottom center of an object's bounding box](https://docs.frigate.video/configuration/zones/). It is completely possible that the person in your screenshot above was detected differently than you expected. The Tracked Object Details pane in Explore or the Detail pane in History will give you more info. |

🚀1

All reactions

- 🚀1

[![@haldi4803](https://avatars.githubusercontent.com/u/17104473?s=60&v=4)](https://github.com/haldi4803)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

#### [haldi4803](https://github.com/haldi4803) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15956383)

|     |
| --- |
| ![Screenshot_20260228_182940_net_waterfox_android_release_HomeActivity](https://private-user-images.githubusercontent.com/17104473/556436127-0e6b6c95-469f-4078-9c26-79631a8135a6.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xNzEwNDQ3My81NTY0MzYxMjctMGU2YjZjOTUtNDY5Zi00MDc4LTljMjYtNzk2MzFhODEzNWE2LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDAyVDAwNDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIzOTNmYTdiMjAxYjU1ZDliNDRhNTc4ZWVlNDRlYmRkZDNmMTA1ODE0MGQ5MTg3ZDg3OGM0ZDA3ZWUyNzI0NGEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRmpwZWcifQ.L3HuLFdayUi1XN2HVF4D6EI12P_eXMf9OS0BzLTKwLo)<br>That was probably the issue... Increased zone size... Maybe someone touched the PTZ camera controls a little as that was no issue before ^^ |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/33021873?s=64&v=4)\ MaxKuh](https://github.com/MaxKuh) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15955744)

|     |
| --- |
| Thank you so much for your great work!<br>I just upgraded from 16.4 to 17.0 and I am seeing several messages that are new and I don't know if that means something is not working. Can you help out here and let me know if I need to do something?<br>I am running frigate in a docker container inside an Proxmox LXC, if that is something you need to know.<br>```<br>2026-02-28 17:01:27.536205275  [2026-02-28 17:01:27] frigate.app                    INFO    : Starting Frigate (0.17.0-f0d69f7)<br>2026-02-28 17:01:27.741844808  [2026-02-28 17:01:27] peewee_migrate.logs            INFO    : Starting migrations<br>2026-02-28 17:01:27.745670143  [2026-02-28 17:01:27] peewee_migrate.logs            INFO    : There is nothing to migrate<br>2026-02-28 17:01:27.835177573  [2026-02-28 17:01:27] frigate.app                    INFO    : Recording process started: 614<br>2026-02-28 17:01:27.892451740  [2026-02-28 17:01:27] frigate.app                    INFO    : Review process started: 616<br>2026-02-28 17:01:27.902694051  [2026-02-28 17:01:27] frigate.app                    INFO    : go2rtc process pid: 117<br>2026-02-28 17:01:28.677574612  [2026-02-28 17:01:28] frigate.app                    INFO    : Embedding process started: 637<br>2026-02-28 17:01:28.817439849  [2026-02-28 17:01:28] frigate.detectors.plugins.edgetpu_tfl INFO    : Attempting to load TPU as usb<br>2026-02-28 17:01:28.944494918  [2026-02-28 17:01:28] frigate.app                    INFO    : Output process started: 691<br>2026-02-28 17:01:29.244668346  [2026-02-28 17:01:29] frigate.api.fastapi_app        INFO    : Starting FastAPI app<br>2026-02-28 17:01:29.540496998  �[1;31m2026-02-28 17:01:29.386456471 [E:onnxruntime:Default, env.cc:228 ThreadMain] pthread_setaffinity_np failed for thread: 745, index: 1, mask: {2, }, error code: 22 error msg: Invalid argument. Specify the number of threads explicitly so the affinity is not set.�[m<br>2026-02-28 17:01:31.370395069  [2026-02-28 17:01:31] frigate.camera.maintainer      INFO    : Camera processor not started for disabled camera Simon<br>2026-02-28 17:01:31.371946677  [2026-02-28 17:01:31] frigate.camera.maintainer      INFO    : Capture process not started for disabled camera Simon<br>2026-02-28 17:01:31.433221821  [2026-02-28 17:01:31] frigate.api.fastapi_app        INFO    : FastAPI started<br>2026-02-28 17:01:31.439221306  [2026-02-28 17:01:31] frigate.detectors.plugins.edgetpu_tfl INFO    : TPU found<br>2026-02-28 17:01:31.441606066  INFO: Created TensorFlow Lite XNNPACK delegate for CPU.<br>2026-02-28 17:01:31.483993853  [2026-02-28 17:01:31] frigate.camera.maintainer      INFO    : Camera processor started for Vordereingang: 771<br>2026-02-28 17:01:31.569916190  [2026-02-28 17:01:31] frigate.camera.maintainer      INFO    : Capture process started for Vordereingang: 837<br>2026-02-28 17:01:31.685782709  [2026-02-28 17:01:31] frigate.camera.maintainer      INFO    : Camera processor started for Carport: 903<br>2026-02-28 17:01:31.779913376  [2026-02-28 17:01:31] frigate.camera.maintainer      INFO    : Capture process started for Carport: 960<br>2026-02-28 17:01:34.862189576  Fatal Python error: Illegal instruction<br>2026-02-28 17:02:26.472571  2026-02-28 17:01:34.862195671<br>2026-02-28 17:01:34.862198068  Thread 0x000075fcea82b6c0 (most recent call first):<br>2026-02-28 17:01:34.863564051    File "/usr/lib/python3.11/threading.py", line 320 in wait<br>2026-02-28 17:01:34.863569967    File "/usr/lib/python3.11/queue.py", line 171 in get<br>2026-02-28 17:01:34.863572951    File "/usr/local/lib/python3.11/dist-packages/playhouse/sqliteq.py", line 162 in loop<br>2026-02-28 17:01:34.863575786    File "/usr/local/lib/python3.11/dist-packages/playhouse/sqliteq.py", line 137 in run<br>2026-02-28 17:01:34.863580710    File "/usr/local/lib/python3.11/dist-packages/playhouse/sqliteq.py", line 272 in run<br>2026-02-28 17:01:34.863620356    File "/usr/lib/python3.11/threading.py", line 975 in run<br>2026-02-28 17:01:34.863624511    File "/usr/lib/python3.11/threading.py", line 1038 in _bootstrap_inner<br>2026-02-28 17:01:34.863627004    File "/usr/lib/python3.11/threading.py", line 995 in _bootstrap<br>2026-02-28 17:02:26.472616  2026-02-28 17:01:34.863628244<br>2026-02-28 17:01:34.863630573  Current thread 0x000075fd12e91040 (most recent call first):<br>2026-02-28 17:01:34.863633160    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863682357    File "<frozen importlib._bootstrap_external>", line 1233 in create_module<br>2026-02-28 17:01:34.863685555    File "<frozen importlib._bootstrap>", line 573 in module_from_spec<br>2026-02-28 17:01:34.863715472    File "<frozen importlib._bootstrap>", line 676 in _load_unlocked<br>2026-02-28 17:01:34.863718828    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.863721492    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.863724086    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863726579    File "<frozen importlib._bootstrap>", line 1234 in _handle_fromlist<br>2026-02-28 17:01:34.863729751    File "/usr/local/lib/python3.11/dist-packages/tensorflow/python/platform/self_check.py", line 63 in preload_check<br>2026-02-28 17:01:34.863765271    File "/usr/local/lib/python3.11/dist-packages/tensorflow/python/pywrap_tensorflow.py", line 37 in <module><br>2026-02-28 17:01:34.863768658    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863771339    File "<frozen importlib._bootstrap_external>", line 940 in exec_module<br>2026-02-28 17:01:34.863773752    File "<frozen importlib._bootstrap>", line 690 in _load_unlocked<br>2026-02-28 17:01:34.863776282    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.863817826    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.863821298    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863823667    File "<frozen importlib._bootstrap>", line 1234 in _handle_fromlist<br>2026-02-28 17:01:34.863826509    File "/usr/local/lib/python3.11/dist-packages/tensorflow/__init__.py", line 40 in <module><br>2026-02-28 17:01:34.863829315    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863831770    File "<frozen importlib._bootstrap_external>", line 940 in exec_module<br>2026-02-28 17:01:34.863834119    File "<frozen importlib._bootstrap>", line 690 in _load_unlocked<br>2026-02-28 17:01:34.863836599    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.863839091    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.863842006    File "/usr/local/lib/python3.11/dist-packages/transformers/image_transforms.py", line 49 in <module><br>2026-02-28 17:01:34.863844660    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863847100    File "<frozen importlib._bootstrap_external>", line 940 in exec_module<br>2026-02-28 17:01:34.863899990    File "<frozen importlib._bootstrap>", line 690 in _load_unlocked<br>2026-02-28 17:01:34.863903388    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.863905746    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.863908836    File "/usr/local/lib/python3.11/dist-packages/transformers/image_processing_utils.py", line 21 in <module><br>2026-02-28 17:01:34.863911388    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863914166    File "<frozen importlib._bootstrap_external>", line 940 in exec_module<br>2026-02-28 17:01:34.863916521    File "<frozen importlib._bootstrap>", line 690 in _load_unlocked<br>2026-02-28 17:01:34.863918965    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.863921331    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.863924611    File "/usr/local/lib/python3.11/dist-packages/transformers/models/clip/image_processing_clip.py", line 21 in <module><br>2026-02-28 17:01:34.863977799    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863981078    File "<frozen importlib._bootstrap_external>", line 940 in exec_module<br>2026-02-28 17:01:34.863983480    File "<frozen importlib._bootstrap>", line 690 in _load_unlocked<br>2026-02-28 17:01:34.863986026    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.863988364    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.863991686    File "/usr/local/lib/python3.11/dist-packages/transformers/models/clip/feature_extraction_clip.py", line 20 in <module><br>2026-02-28 17:01:34.863994527    File "<frozen importlib._bootstrap>", line 241 in _call_with_frames_removed<br>2026-02-28 17:01:34.863996981    File "<frozen importlib._bootstrap_external>", line 940 in exec_module<br>2026-02-28 17:01:34.863999300    File "<frozen importlib._bootstrap>", line 690 in _load_unlocked<br>2026-02-28 17:01:34.864001820    File "<frozen importlib._bootstrap>", line 1149 in _find_and_load_unlocked<br>2026-02-28 17:01:34.864004148    File "<frozen importlib._bootstrap>", line 1178 in _find_and_load<br>2026-02-28 17:01:34.864006432    File "<frozen importlib._bootstrap>", line 1206 in _gcd_import<br>2026-02-28 17:01:34.864008921    File "/usr/lib/python3.11/importlib/__init__.py", line 126 in import_module<br>2026-02-28 17:01:34.864012085    File "/usr/local/lib/python3.11/dist-packages/transformers/utils/import_utils.py", line 1764 in _get_module<br>2026-02-28 17:01:34.864015151    File "/usr/local/lib/python3.11/dist-packages/transformers/utils/import_utils.py", line 1754 in __getattr__<br>2026-02-28 17:01:34.873982100    File "/usr/local/lib/python3.11/dist-packages/transformers/models/auto/auto_factory.py", line 693 in getattribute_from_module<br>2026-02-28 17:01:34.874010126    File "/usr/local/lib/python3.11/dist-packages/transformers/models/auto/auto_factory.py", line 777 in _load_attr_from_module<br>2026-02-28 17:01:34.874013867    File "/usr/local/lib/python3.11/dist-packages/transformers/models/auto/auto_factory.py", line 763 in __getitem__<br>2026-02-28 17:01:34.874017414    File "/usr/local/lib/python3.11/dist-packages/transformers/models/auto/feature_extraction_auto.py", line 381 in from_pretrained<br>2026-02-28 17:01:34.874020400    File "/opt/frigate/frigate/embeddings/onnx/jina_v1_embedding.py", line 212 in _load_model_and_utils<br>2026-02-28 17:01:34.874023071    File "/opt/frigate/frigate/embeddings/onnx/jina_v1_embedding.py", line 204 in __init__<br>2026-02-28 17:01:34.874025619    File "/opt/frigate/frigate/embeddings/embeddings.py", line 127 in __init__<br>2026-02-28 17:01:34.874028146    File "/opt/frigate/frigate/embeddings/maintainer.py", line 120 in __init__<br>2026-02-28 17:01:34.874030520    File "/opt/frigate/frigate/embeddings/__init__.py", line 49 in run<br>2026-02-28 17:01:34.874033058    File "/usr/lib/python3.11/multiprocessing/process.py", line 314 in _bootstrap<br>2026-02-28 17:01:34.874035511    File "/usr/lib/python3.11/multiprocessing/spawn.py", line 133 in _main<br>2026-02-28 17:01:34.874038261    File "/usr/lib/python3.11/multiprocessing/forkserver.py", line 313 in _serve_one<br>2026-02-28 17:01:34.874040770    File "/usr/lib/python3.11/multiprocessing/forkserver.py", line 274 in main<br>2026-02-28 17:01:34.874042617    File "<string>", line 1 in <module><br>2026-02-28 17:02:26.472700  2026-02-28 17:01:34.874043887<br>2026-02-28 17:01:34.877003621  Extension modules: numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, pysqlite3._sqlite3, zmq.backend.cython._zmq, ruamel.yaml.clib._ruamel_yaml, _ruamel_yaml, charset_normalizer.md, requests.packages.charset_normalizer.md, requests.packages.chardet.md, PIL._imaging, playhouse._sqlite_ext, psutil._psutil_linux, scipy._lib._ccallback_c, scipy.ndimage._nd_image, scipy.ndimage._rank_filter_1d, scipy.special._ufuncs_cxx, scipy.special._ellip_harm_2, scipy.special._special_ufuncs, scipy.special._gufuncs, scipy.special._ufuncs, scipy.special._specfun, scipy.special._comb, scipy.linalg._fblas, scipy.linalg._flapack, _cyutility, scipy._cyutility, scipy.linalg.cython_lapack, scipy.linalg._cythonized_array_utils, scipy.linalg._solve_toeplitz, scipy.linalg._decomp_lu_cython, scipy.linalg._matfuncs_schur_sqrtm, scipy.linalg._matfuncs_expm, scipy.linalg._linalg_pythran, scipy.linalg.cython_blas, scipy.linalg._decomp_update, scipy.sparse._sparsetools, _csparsetools, scipy.sparse._csparsetools, _ni_label, scipy.ndimage._ni_label, setproctitle._setproctitle, scipy.spatial._ckdtree, scipy._lib.messagestream, scipy.spatial._qhull, scipy.spatial._voronoi, scipy.spatial._hausdorff, scipy.spatial._distance_wrap, scipy.spatial.transform._rotation, scipy.spatial.transform._rigid_transform, scipy.sparse.linalg._dsolve._superlu, scipy.sparse.linalg._eigen.arpack._arpack, scipy.sparse.linalg._propack._spropack, scipy.sparse.linalg._propack._dpropack, scipy.sparse.linalg._propack._cpropack, scipy.sparse.linalg._propack._zpropack, scipy.optimize._group_columns, scipy.optimize._trlib._trlib, scipy.optimize._lbfgsb, _moduleTNC, scipy.optimize._moduleTNC, scipy.optimize._slsqplib, scipy.optimize._minpack, scipy.optimize._lsq.givens_elimination, scipy.optimize._zeros, scipy._lib._uarray._uarray, scipy.linalg._decomp_interpolative, scipy.optimize._bglu_dense, scipy.optimize._lsap, scipy.optimize._direct, scipy.integrate._odepack, scipy.integrate._quadpack, scipy.integrate._vode, scipy.integrate._dop, scipy.integrate._lsoda, scipy.interpolate._fitpack, scipy.interpolate._dfitpack, scipy.interpolate._dierckx, scipy.interpolate._ppoly, scipy.interpolate._interpnd, scipy.interpolate._rbfinterp_pythran, scipy.interpolate._rgi_cython, scipy.special.cython_special, scipy.stats._stats, scipy.stats._biasedurn, scipy.stats._stats_pythran, scipy.stats._levy_stable.levyst, scipy.stats._ansari_swilk_statistics, scipy.sparse.csgraph._tools, scipy.sparse.csgraph._shortest_path, scipy.sparse.csgraph._traversal, scipy.sparse.csgraph._min_spanning_tree, scipy.sparse.csgraph._flow, scipy.sparse.csgraph._matching, scipy.sparse.csgraph._reordering, scipy.stats._sobol, scipy.stats._qmc_cy, scipy.stats._rcont.rcont, scipy.stats._qmvnt_cy, _cffi_backend, multidict._multidict, yarl._quoting_c, propcache._helpers_c, aiohttp._http_writer, aiohttp._http_parser, aiohttp._websocket.mask, aiohttp._websocket.reader_c, frozenlist._frozenlist, regex._regex, lxml._elementpath, lxml.etree, lxml.builder, ciso8601, pyclipper._pyclipper, rapidfuzz._feature_detector_cpp, rapidfuzz.distance._initialize_cpp, rapidfuzz.distance.metrics_cpp, rapidfuzz.fuzz_cpp, rapidfuzz.process_cpp_impl, rapidfuzz.utils_cpp, shapely.lib, shapely._geos, shapely._geometry_helpers, yaml._yaml, markupsafe._speedups (total: 135)<br>``` |\
\
1You must be logged in to vote\
\
All reactions\
\
7 replies\
\
\
Show 2 previous replies\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15956305)   Collaborator Sponsor\
\
|     |\
| --- |\
| my understanding is that it is just regular AVX |\
\
All reactions\
\
[![@netrunnereve](https://avatars.githubusercontent.com/u/139727413?s=60&v=4)](https://github.com/netrunnereve)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [netrunnereve](https://github.com/netrunnereve) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15956805)\
\
|     |\
| --- |\
| Thanks, I just did the update on my regular AVX server and so far it's running fine with no issues. I haven't tried the new model training feature though so I'm not sure about that one. |\
\
All reactions\
\
[![@MaxKuh](https://avatars.githubusercontent.com/u/33021873?s=60&v=4)](https://github.com/MaxKuh)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
#### [MaxKuh](https://github.com/MaxKuh) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15956918)\
\
|     |\
| --- |\
| Oh, I am running Frigate on a system with Intel Celeron J4105 together with Coral TPU, so no AVX means no Frigate 17? :( |\
\
All reactions\
\
[![@gofaster](https://avatars.githubusercontent.com/u/1273372?s=60&v=4)](https://github.com/gofaster)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [gofaster](https://github.com/gofaster) [on Mar 1Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15965649)\
\
|     |\
| --- |\
| If the new state/object classification features are not used - will 0.17.0 run on a CPU without AVX? |\
\
All reactions\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 1Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15965661)   Collaborator Sponsor\
\
|     |\
| --- |\
| There are other features that require it too |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
### [![](https://avatars.githubusercontent.com/u/35746122?s=64&v=4)\ quantum77](https://github.com/quantum77) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15956384)\
\
|     |\
| --- |\
| I may be alone here, but Frigate will not support nVidia Blackwell GPUs until 0.18. For those who have a Blackwell here's the solution for now.<br>I run Debian 13.3 on an AMD Ryzen system in a KVM VM with GPU passthrough, and use Podman to build the containers (not the unsecure Docker). I split out the ORT (ONNX Runtime) container as it is a long build, and frees you to run many iterations of the Cormorant (née Frigate) build.<br>The only thing you have to install in the VM is the nVidia driver v590+, podman, and podman-compose. For nVidia driver you must install using the .run method.<br>I do both container builds as my unprived user. (not even allowed sudo {shudder} - pardon my infosec-awareness). I put my two build files in ~/src/cormorant/.<br>Architecture Overview<br>\- Based on latest CUDA devel image<br>\- Install latest TensorRT from NGC repo<br>\- Build ONNX Runtime from source (CUDA + TensorRT EP)<br>\- Build FFmpeg with CUDA/NVENC/NPP<br>\- Build Frigate Python package correctly<br>\- Strip image down in final stage<br>Final Target Stack (Latest Everything):<br>```<br>	Driver	 590+<br>	CUDA	 13.1<br>	TensorRT 10.15.1.29<br>	cuDNN	CUDA 13 compatible<br>	ONNX Runtime	built from source<br>	CUDA Arch 120 (121 not supported by RTX 50xx)<br>	Frigate	 latest from git<br>```<br>Build podman.ort wheel factory so:<br>If **no valued containers exist** (start fresh):<br>$ podman system reset<br>$ podman build --format docker -f podman.ort -t local/ort:1.24.2-cuda13.1 .<br>ORT container is a wheel factory in the truest sense — its only job is to compile ORT from source with my exact CUDA 13.1 + TensorRT flags, and **output a .whl artifact**. The cormorant containerfile then reaches into it, grabs that wheel, and installs it permanently into the Cormorant image.<br>A useful mental model:<br>podman.ort<br>└── Compiles ORT from source<br>└── Outputs: onnxruntime-1.24.2-\*.whl ← the product<br>podman.cormorant<br>└── Takes Frigate's official TRT image<br>└── Reaches into your ORT factory → grabs the wheel<br>└── pip installs it over Frigate's stock ORT<br>└── Result: one self-contained cormorant image<br>with Frigate's full native stack + my custom ORT<br>At runtime you only ever run one container — cormorant. I can provide details on running and a systemd file if any interest. The ORT factory image just sits there in your local Podman image store, never running, only consulted again if you need to rebuild. You could even podman image rm it after a successful cormorant build and nothing would break.<br>Build podman.cormorant so:<br>$ podman build --format docker -f podman.cormorant -t localhost/cormorant:latest .<br>Must build to format docker so healthcheck works.<br>Words to the wise:<br>- Set all cameras to H264H - H.265 in Firefox results in jerkiness. The 'H' means High, for better compression.<br>- In your config.yml file, set the low stream to match the settings in your camera: dimensions and fps.<br>- Ensure that your GPU is passd through and recognized: $ podman exec -it frigate nvidia-smi<br>- Start $ podman-compose -f /srv/cameras/config/compose.yml up -d<br>- Stop (graceful — respects stop\_grace\_period: 30s) $ podman-compose -f /srv/cameras/config/compose.yml down<br>- For all the world, make sure your ZFS array is fast enough:<br>  1. A striped array is fastest (but if one drive fails, all is lost)<br>  2. Add More VDEVs: Increasing the number of virtual devices (VDEVs - diskd) in your pool can improve performance by allowing more concurrent operations.<br>  3. volblocksize is crucial, and must be set on zpool creation. Hardware is 512B. ZFS volblocksize default 16kB. For high-rez video set to 128KB.<br>  4. recordsize for high-rez video (e.g., 1M) benefits large file transfers.<br>  5. Disable ZFS compression (compression=off) to save CPU resources, as ZFS cannot compress already-compressed video data.<br>  6. atime=off: Improves performance by not updating the last-accessed time for every file read.<br>Other shit you need: a Model (which holds the 'weights', ie 'wisdom' of your AI), a compose.yml and config.yml. The basic model is yolo9, but you can add tools, weapons, fire/smoke recognition, etc from Roboflow Universe.<br>Comments, criticisms, insults, welcomed.<br>[podman.ort.zip](https://github.com/user-attachments/files/25627965/podman.ort.zip)<br>[podman.cormorant.zip](https://github.com/user-attachments/files/25628013/podman.cormorant.zip) |\
\
1You must be logged in to vote\
\
All reactions\
\
29 replies\
\
\
Show 24 previous replies\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17299830)   Collaborator\
\
|     |\
| --- |\
| I see. Blackwell users haven't reported any difficult issues for us so far, and the dev builds are stabilizing nicely. We'll see what comes up during the beta period. |\
\
👍3👎1\
\
All reactions\
\
- 👍3\
- 👎1\
\
[![@quantum77](https://avatars.githubusercontent.com/u/35746122?s=60&v=4)](https://github.com/quantum77)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
#### [quantum77](https://github.com/quantum77) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17299921)\
\
|     |\
| --- |\
| I know. It's alot easier when everything else is ancient and inappropriate for outdoor security work.<br>Beta _may_ exonerate you in that case.<br>And pardon me hawkeye, you are not the one I am targeting. I am reluctant though as it may benefit NickM\_"I would suggest you read the documentation..."-27 |\
\
👎3\
\
All reactions\
\
- 👎3\
\
[![@shinyzard123](https://avatars.githubusercontent.com/u/145939322?s=60&v=4)](https://github.com/shinyzard123)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [shinyzard123](https://github.com/shinyzard123) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17300151)\
\
|     |\
| --- |\
| I'd like to offer a different perspective.<br>Nick has helped me multiple times on Reddit and has always been patient, helpful, and generous with his time. My experience with him has been nothing but positive.<br>Open-source maintainers often receive far more criticism than thanks despite volunteering countless hours to build and support projects like Frigate. So I'd just like to thank Nick and the rest of the maintainers for the work they do. Frigate is an excellent project, and the effort is appreciated. |\
\
👍2👎1❤️3\
\
All reactions\
\
- 👍2\
- 👎1\
- ❤️3\
\
[![@quantum77](https://avatars.githubusercontent.com/u/35746122?s=60&v=4)](https://github.com/quantum77)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [quantum77](https://github.com/quantum77) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17300241)\
\
|     |\
| --- |\
| My experience is different. Vote me down as much as you want, Idgad. I started here with the best of attitude and intentions and got whacked, with zero justification. I will not have it and screw NickM-27. I always just _take_ when presented with such circumstances. Like it or lump it. Do better than I have or eat the dog food.<br>I am running the newest everything on 0.17.1. It is a good project but I am running some worthy refinements. We all make our choices. |\
\
👎3\
\
All reactions\
\
- 👎3\
\
[![@blakeblackshear](https://avatars.githubusercontent.com/u/569905?s=60&v=4)](https://github.com/blakeblackshear)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [blakeblackshear](https://github.com/blakeblackshear) [on Jun 15Jun 15, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17303962)   Maintainer  Author\
\
|     |\
| --- |\
| Please take your musings elsewhere. I'm not interested in reading your posts berating Nick or any of the other maintainers. I have read every post you have made from the beginning, and I don't think you are engaging within the bounds of our Code of Conduct. |\
\
👍2\
\
All reactions\
\
- 👍2\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/8712438?s=64&v=4)\ ZhaiSoul](https://github.com/ZhaiSoul) [on Feb 28Feb 28, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15956508)\
\
|     |\
| --- |\
| Update on the feedback: I've lowered the camera frame rate to 5, but the issue still occurs. Do you have any suggestions for debugging this?<br>![Screenshot_2026-03-01-01-53-49-331_com.microsoft.emmx.jpg](https://private-user-images.githubusercontent.com/8712438/556439670-eb47d93e-745b-41a9-896e-a5ebc3ac63d2.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii84NzEyNDM4LzU1NjQzOTY3MC1lYjQ3ZDkzZS03NDViLTQxYTktODk2ZS1hNWViYzNhYzYzZDIuanBnP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAwMiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMDJUMDA0ODQ5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MWIwMDhjYzhkZTI2Mzg2YTkzNmExYzBhNThiZmIxYTY4M2YzNWMwZjM0M2EyOGE3NmI1ZjljNzFlODQxZjQ2YyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGanBlZyJ9.8C8sQqMHTuJn4qX6WtFEJ1w8fke11qSGrtHrMc1EPe0) |\
\
1You must be logged in to vote\
\
All reactions\
\
12 replies\
\
\
Show 7 previous replies\
\
[![@ZhaiSoul](https://avatars.githubusercontent.com/u/8712438?s=60&v=4)](https://github.com/ZhaiSoul)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 1Mar 1, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15963256)\
\
|     |\
| --- |\
| I referenced the multithreading design of other modules, came up with a simple modification inspired by them (vibe), and the issue hasn't occurred since! This change is really effective!<br>[Frigate-CN@ `8da392c`](https://github.com/Frigate-CN/frigate/commit/8da392ce4b6169dcfc53d65bbbd1f6623ef5c9f5) |\
\
All reactions\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 1Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15965668)   Collaborator Sponsor\
\
|     |\
| --- |\
| The idea in general seems fine, I think the main concern is that semantic triggers depend on the embeddings but I didn't take a close look at the code. |\
\
All reactions\
\
[![@ZhaiSoul](https://avatars.githubusercontent.com/u/8712438?s=60&v=4)](https://github.com/ZhaiSoul)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 1Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15966720)\
\
|     |\
| --- |\
| > The idea in general seems fine, I think the main concern is that semantic triggers depend on the embeddings but I didn't take a close look at the code.<br>I don’t think so, because I previously tried disabling semantic search, and the problem persisted. |\
\
All reactions\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 1Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15966734)   Collaborator Sponsor\
\
|     |\
| --- |\
| I think you misunderstand, I'm just saying we have to be careful about how this change affects feature order |\
\
👀1\
\
All reactions\
\
- 👀1\
\
[![@ZhaiSoul](https://avatars.githubusercontent.com/u/8712438?s=60&v=4)](https://github.com/ZhaiSoul)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15969240)\
\
|     |\
| --- |\
| Update: After testing, there has indeed been significant improvement. However, if my CPU is running high-load tasks (such as training an object classification model), I still encounter cases where targets are lost in the results. My current modification only mitigates the issue but doesn’t completely resolve it. This problem is especially noticeable on low-power devices when multiple object classifications are configured.<br>For now, I can continue using the modification I mentioned earlier, which at least greatly alleviates the issue when no model training is happening. I hope others can share their thoughts or suggestions. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/10836275?s=64&v=4)\ ElectronicBattle](https://github.com/ElectronicBattle) [on Mar 1Mar 1, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15962646)\
\
|     |\
| --- |\
| An update to my TrueNAS "app" to v0.17 went painlessly; now I've some new stuff to play with!<br>Just in case, I took the precaution of stopping the app, backing up my three database files, and then upgrading. I didn't bother doing anything to my config (I am using git to control the versions I have); anyway it all works fine. Great work by the Frigate team as always. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/127434049?s=64&v=4)\ Grzesiektaktoja](https://github.com/Grzesiektaktoja) [on Mar 1Mar 1, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15963668)\
\
|     |\
| --- |\
| There is no switch in version 17?<br>![switch](https://private-user-images.githubusercontent.com/127434049/556617482-c59eeefc-f041-4bf5-9fc0-592029a5040f.PNG?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii8xMjc0MzQwNDkvNTU2NjE3NDgyLWM1OWVlZWZjLWYwNDEtNGJmNS05ZmMwLTU5MjAyOWE1MDQwZi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAwMlQwMDQ4NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wZWZkM2RkMWM2MjUyODVhZDgwN2VjYTdlMGUxOTFjYjIwMmUzYTY0NDE1MDhiNzg1MGQ0YjE3YzhiZDljMzgyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.gcu2yoMZAmF8WfSrjCnYNqnEW5Rosaw_h1_EUJjJbnE) |\
\
1You must be logged in to vote\
\
All reactions\
\
2 replies\
\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on Mar 1Mar 1, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15963676)   Collaborator\
\
|     |\
| --- |\
| You will want to double check Frigate's connection to your MQTT broker as well as the Frigate integration version. |\
\
All reactions\
\
[![@Grzesiektaktoja](https://avatars.githubusercontent.com/u/127434049?s=60&v=4)](https://github.com/Grzesiektaktoja)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [Grzesiektaktoja](https://github.com/Grzesiektaktoja) [on Mar 1Mar 1, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15963760)\
\
|     |\
| --- |\
| it works, thanks |\
\
👍1\
\
All reactions\
\
- 👍1\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/28842285?s=64&v=4)\ pdobrien3](https://github.com/pdobrien3) [on Mar 1Mar 1, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15965189)\
\
|     |\
| --- |\
| I have been having issues since beta2 with facial recognition failing. I think I have finally isolated it to stopping motion/recording/detection while it is likely tracking a subject. I can consistently reproduce it.<br>```<br>2026-03-01 16:29:16.410440432  [2026-03-01 16:29:16] frigate.comms.dispatcher       INFO    : Turning off recordings for camera<br>2026-03-01 16:29:16.415379098  [2026-03-01 16:29:16] frigate.comms.dispatcher       INFO    : Turning off snapshots for camera<br>2026-03-01 16:29:16.417152568  [2026-03-01 16:29:16] frigate.comms.dispatcher       INFO    : Turning off detection for camera<br>2026-03-01 16:29:16.423866450  [2026-03-01 16:29:16] frigate.comms.dispatcher       INFO    : Turning off motion for camera<br>2026-03-01 16:29:16.433149246  [2026-03-01 16:29:16] frigate.comms.dispatcher       INFO    : Turning off alerts for camera<br>2026-03-01 16:29:16.441689466  [2026-03-01 16:29:16] frigate.comms.dispatcher       INFO    : Turning off detections for camera<br>2026-03-01 16:29:21.337784190  loading data from : /config/model_cache/facedet/landmarkdet.yaml<br>2026-03-01 16:29:21.345643970  Exception in thread embeddings_maintainer:<br>2026-03-01 16:29:21.345650309  Traceback (most recent call last):<br>2026-03-01 16:29:21.345654233    File "/usr/lib/python3.11/threading.py", line 1038, in _bootstrap_inner<br>2026-03-01 16:29:21.345656828      self.run()<br>2026-03-01 16:29:21.345660244    File "/opt/frigate/frigate/embeddings/maintainer.py", line 279, in run<br>2026-03-01 16:29:21.345663020      self._process_finalized()<br>2026-03-01 16:29:21.345670632    File "/opt/frigate/frigate/embeddings/maintainer.py", line 496, in _process_finalized<br>2026-03-01 16:29:21.345674455      self._embed_thumbnail(event_id, thumbnail)<br>2026-03-01 16:29:21.345678019    File "/opt/frigate/frigate/embeddings/maintainer.py", line 682, in _embed_thumbnail<br>2026-03-01 16:29:21.345703787      self.embeddings.embed_thumbnail(event_id, thumbnail)<br>2026-03-01 16:29:21.345707787    File "/opt/frigate/frigate/embeddings/embeddings.py", line 181, in embed_thumbnail<br>2026-03-01 16:29:21.345749714      embedding = self.vision_embedding([thumbnail])[0]<br>2026-03-01 16:29:21.345754177                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>2026-03-01 16:29:21.345758046    File "/opt/frigate/frigate/embeddings/onnx/base_embedding.py", line 79, in __call__<br>2026-03-01 16:29:21.345760971      processed = self._preprocess_inputs(inputs)<br>2026-03-01 16:29:21.345800600                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>2026-03-01 16:29:21.345804985    File "/opt/frigate/frigate/embeddings/onnx/jina_v1_embedding.py", line 225, in _preprocess_inputs<br>2026-03-01 16:29:21.345807566      return [<br>2026-03-01 16:29:21.345810134             ^<br>2026-03-01 16:29:21.345814090    File "/opt/frigate/frigate/embeddings/onnx/jina_v1_embedding.py", line 226, in <listcomp><br>2026-03-01 16:29:21.345817905      self.feature_extractor(images=image, return_tensors="np")<br>2026-03-01 16:29:21.345821975    File "/usr/local/lib/python3.11/dist-packages/transformers/image_processing_utils.py", line 41, in __call__<br>2026-03-01 16:29:21.345858540      return self.preprocess(images, **kwargs)<br>2026-03-01 16:29:21.345861504             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>2026-03-01 16:29:21.345865337    File "/usr/local/lib/python3.11/dist-packages/transformers/models/clip/image_processing_clip.py", line 286, in preprocess<br>2026-03-01 16:29:21.345868092      images = make_list_of_images(images)<br>2026-03-01 16:29:21.345870576               ^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>2026-03-01 16:29:21.345874069    File "/usr/local/lib/python3.11/dist-packages/transformers/image_utils.py", line 205, in make_list_of_images<br>2026-03-01 16:29:21.345876276      raise ValueError(<br>2026-03-01 16:29:21.345913869  ValueError: Invalid image type. Expected either PIL.Image.Image, numpy.ndarray, torch.Tensor, tf.Tensor or jax.ndarray, but got <class 'NoneType'>.<br>``` |\
\
1You must be logged in to vote\
\
All reactions\
\
3 replies\
\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 1Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15965674)   Collaborator Sponsor\
\
|     |\
| --- |\
| I can't reproduce this but we can catch this regardless so it doesn't crash. |\
\
All reactions\
\
[![@pdobrien3](https://avatars.githubusercontent.com/u/28842285?s=60&v=4)](https://github.com/pdobrien3)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [pdobrien3](https://github.com/pdobrien3) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15970387)\
\
|     |\
| --- |\
| Good deal. Thank you. Were there changes in beta 3 that could be causing this or is it just a coincidence on my end? |\
\
All reactions\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15971380)   Collaborator Sponsor\
\
|     |\
| --- |\
| Perhaps there was something subtle, hard to say |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/26333781?s=64&v=4)\ xury77](https://github.com/xury77) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15970397)\
\
|     |\
| --- |\
| Can I limit the custom classification to a specific camera? That is, transfer the configuration from global to camera? |\
\
2You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15971375)   Collaborator Sponsor\
\
|     |\
| --- |\
| Object classification can't be configured per camera but the updates are per camera already |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
### [![](https://avatars.githubusercontent.com/u/218326017?s=64&v=4)\ WilyWalrus](https://github.com/WilyWalrus) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15972803)\
\
|     |\
| --- |\
| Awesome new features in this release; thanks!<br>In the Classification screen, Is it possible to edit or choose which image is used for the object thumbnail? Can I rename a file in the clips directory or anything?<br>Two of my custom objects have thumbnails that are very light/washed-out images, so it's a little difficult to read the white text label over it.<br>A very minor issue; just curious. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/160263479?s=64&v=4)\ kartalsmart](https://github.com/kartalsmart) [on Mar 2Mar 2, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15974667)\
\
|     |\
| --- |\
| Thank you guys for your excellent work! |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/6403564?s=64&v=4)\ vincenttor](https://github.com/vincenttor) [on Mar 3Mar 3, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15985806)\
\
|     |\
| --- |\
| is there a possibility to record the 247 stream in SD quality, and triggers/movements in HD, this is how i used to set up the v16 but now it doesn't work its or ?HD only or SD and HD all day long is 500Gb a day. also the cpu is busy, im running face detection on 2 cams HD, movement detection, and no more 247 36-41 Watt from wall , when using v16 247 record on SD, movement HD, face detection HD, and sym search the power was about 32/36Watt idle , so less options on more power use now but i assume of the new engine its running on ? |\
\
1You must be logged in to vote\
\
All reactions\
\
3 replies\
\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on Mar 3Mar 3, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15985843)   Collaborator\
\
|     |\
| --- |\
| Frigate has never supported separating SD and HD streams for recording. The recording configuration changed in 0.17 as the [release notes](https://github.com/blakeblackshear/frigate/releases/tag/v0.17.0) indicated. You may want to review the recording docs and adjust your configuration accordingly: [https://docs.frigate.video/configuration/record/](https://docs.frigate.video/configuration/record/) |\
\
All reactions\
\
[![@vincenttor](https://avatars.githubusercontent.com/u/6403564?s=60&v=4)](https://github.com/vincenttor)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [vincenttor](https://github.com/vincenttor) [on Mar 3Mar 3, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15985932)\
\
|     |\
| --- |\
| huh, that's strange i always thought i had it on sub stream SD recording for the 247, i mean when you use the slider to scroll you can see the sub stream record over the whole day right ? i thought you could set that on hd or sd. Thank for the fast reply software futher is great ! |\
\
All reactions\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on Mar 3Mar 3, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15985954)   Collaborator\
\
|     |\
| --- |\
| The low resolution scrubbing is done with _previews_, which are taken from the stream defined by the `detect` role in your config. So that may be what you are referring to. That behavior has not changed in 0.17. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/150403?s=64&v=4)\ ramunasd](https://github.com/ramunasd) [on Mar 3Mar 3, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15989617)\
\
|     |\
| --- |\
| Very nice release 🚀 Thank you guys!<br>I just tried it on my jetson orin nano and seems object detection does not work at all. Has anyone faced the same issue? Can it be related to CUDA Graphs?<br>I'm using docker image `frigate:0.17.0-tensorrt-jp6` and frigate+ models. Here is container log:<br>```<br>2026-03-03 22:57:31.805802474  [2026-03-03 22:57:31] frigate.app                    INFO    : Starting Frigate (0.17.0-f0d69f7)<br>2026-03-03 22:57:31.972025232  2026/03/03 22:57:31 [error] 354#354: *6 connect() failed (111: Connection refused) while connecting to upstream, client: 127.0.0.1, server: , request: "GET /api/version HTTP/1.1", subrequest: "/auth", upstream: "http://127.0.0.1:5001/auth", host: "127.0.0.1:5000"<br>2026-03-03 22:57:31.972060785  2026/03/03 22:57:31 [error] 354#354: *6 auth request unexpected status: 502 while sending to client, client: 127.0.0.1, server: , request: "GET /api/version HTTP/1.1", host: "127.0.0.1:5000"<br>2026-03-03 22:57:32.199894340  [2026-03-03 22:57:32] peewee_migrate.logs            INFO    : Starting migrations<br>2026-03-03 22:57:32.201389168  [2026-03-03 22:57:32] peewee_migrate.logs            INFO    : There is nothing to migrate<br>2026-03-03 22:57:32.661545882  [2026-03-03 22:57:32] frigate.app                    INFO    : Recording process started: 846<br>2026-03-03 22:57:32.684541116  [2026-03-03 22:57:32] frigate.app                    INFO    : Review process started: 859<br>2026-03-03 22:57:32.688134117  [2026-03-03 22:57:32] frigate.app                    INFO    : go2rtc process pid: 210<br>2026-03-03 22:57:33.136262479  [2026-03-03 22:57:33] frigate.app                    INFO    : Embedding process started: 869<br>2026-03-03 22:57:33.175294855  [2026-03-03 22:57:33] frigate.detectors.plugins.onnx INFO    : ONNX: loading /config/model_cache/026f8a4a2163b37bd50057b7f341660e<br>2026-03-03 22:57:33.213813871  [2026-03-03 22:57:33] frigate.app                    INFO    : Output process started: 928<br>2026-03-03 22:57:33.240928810  [2026-03-03 22:57:33] frigate.api.fastapi_app        INFO    : Starting FastAPI app<br>2026-03-03 22:57:34.936059212  [2026-03-03 22:57:34] frigate.util.downloader        INFO    : Downloading model file from: https://github.com/NickM-27/facenet-onnx/releases/download/v1.0/arcface.onnx<br>2026-03-03 22:57:35.402966621  [2026-03-03 22:57:35] frigate.detectors.plugins.onnx INFO    : ONNX: /config/model_cache/026f8a4a2163b37bd50057b7f341660e loaded<br>2026-03-03 22:57:35.463281796  [2026-03-03 22:57:35] frigate.camera.maintainer      INFO    : Camera processor started for backyard: 1045<br>2026-03-03 22:57:35.514978415  [2026-03-03 22:57:35] frigate.api.fastapi_app        INFO    : FastAPI started<br>2026-03-03 22:57:35.538524705  [2026-03-03 22:57:35] frigate.camera.maintainer      INFO    : Capture process started for backyard: 1103<br>2026-03-03 22:57:35.624688285  [2026-03-03 22:57:35] frigate.camera.maintainer      INFO    : Camera processor started for front: 1172<br>2026-03-03 22:57:35.676902775  [2026-03-03 22:57:35] frigate.camera.maintainer      INFO    : Capture process started for front: 1231<br>2026-03-03 22:57:35.742996040  [2026-03-03 22:57:35] frigate.camera.maintainer      INFO    : Camera processor started for front_left: 1297<br>2026-03-03 22:57:35.804670999  [2026-03-03 22:57:35] frigate.camera.maintainer      INFO    : Capture process started for front_left: 1356<br>2026-03-03 22:57:46.988727542  NvMapMemAllocInternalTagged: 1075072515 error 12<br>2026-03-03 22:57:46.988735926  NvMapMemHandleAlloc: error 0<br>2026-03-03 22:57:53.231068868  [2026-03-03 22:57:53] frigate.watchdog               INFO    : Detection appears to be stuck. Restarting detection process...<br>2026-03-03 22:57:53.231696598  [2026-03-03 22:57:53] root                           INFO    : Waiting for detection process to exit gracefully...<br>2026-03-03 22:58:06.072173453  [2026-03-03 22:58:06] frigate.util.downloader        INFO    : Downloading complete: https://github.com/NickM-27/facenet-onnx/releases/download/v1.0/arcface.onnx<br>2026-03-03 22:58:20.864131586  127.0.0.1 - - [03/Mar/2026:22:58:20 +0200] "" 400 0 "-" "-" "-" request_time="0.000" upstream_response_time="-"<br>2026-03-03 22:58:23.259716847  [2026-03-03 22:58:23] root                           INFO    : Detection process didn't exit. Force killing...<br>2026-03-03 22:58:23.378005466  [2026-03-03 22:58:23] root                           INFO    : Detection process has exited...<br>2026-03-03 22:58:23.411984766  [2026-03-03 22:58:23] frigate.detectors.plugins.onnx INFO    : ONNX: loading /config/model_cache/026f8a4a2163b37bd50057b7f341660e<br>2026-03-03 22:58:25.644273786  [2026-03-03 22:58:25] frigate.detectors.plugins.onnx INFO    : ONNX: /config/model_cache/026f8a4a2163b37bd50057b7f341660e loaded<br>2026-03-03 22:59:20.911412283  127.0.0.1 - - [03/Mar/2026:22:59:20 +0200] "" 400 0 "-" "-" "-" request_time="0.000" upstream_response_time="-"<br>``` |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 4Mar 4, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-15998487)   Collaborator Sponsor\
\
|     |\
| --- |\
| I'd suggest creating a support discussion |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/8712438?s=64&v=4)\ ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 22Mar 22, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16257200)\
\
|     |\
| --- |\
| ![image](https://private-user-images.githubusercontent.com/8712438/567407133-47e20794-777d-4ad9-bffa-2ca1b794918f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA5MDI0MjksIm5iZiI6MTc5MDkwMjEyOSwicGF0aCI6Ii84NzEyNDM4LzU2NzQwNzEzMy00N2UyMDc5NC03NzdkLTRhZDktYmZmYS0yY2ExYjc5NDkxOGYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAwMiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMDJUMDA0ODQ5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YjQyNGE1MmUzODE0MWFiMmY3NWY3NjQxNjI2NzZiMWNhZDNhMTRmMmNlYWI3ZmFkYzY1MjU4ZDc3YWFjN2M1YyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.TxcgTJZJMGZIsfZOOMCLA-tD6yFZZn5M6y7RkJ0ix9E)<br>For some reason, even when the visual classifier is enabled, it still doesn't help much in certain scenarios. |\
\
1You must be logged in to vote\
\
All reactions\
\
12 replies\
\
\
Show 7 previous replies\
\
[![@ZhaiSoul](https://avatars.githubusercontent.com/u/8712438?s=60&v=4)](https://github.com/ZhaiSoul)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 26Mar 26, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16331693)\
\
|     |\
| --- |\
| > It would not make sense to break apart the object tracking pipeline to use motion classification which would require forking the norfair tracker.<br>I found an anti-interference algorithm called ByteTrack designed for multiple overlapping targets, which might be helpful for us. From what I’ve heard from industry insiders, some well-known security projects in China are already using this algorithm.<br>[https://github.com/ifzhang/ByteTrack](https://github.com/ifzhang/ByteTrack) |\
\
All reactions\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Mar 26Mar 26, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16331742)   Collaborator Sponsor\
\
|     |\
| --- |\
| Norfair is already built for handling this, the basic fact is with inaccuracies in object detection there will always be an error rate. The risk of moving to a new object tracker would have to have a major upside to deal with all the migration, potential bugs, etc. with all the features that already utilize tracking.<br>We also are not using the Re-ID feature of norfair currently as models did not exist to be fast enough last we checked<br>[https://github.com/tryolabs/norfair](https://github.com/tryolabs/norfair) |\
\
👍1\
\
All reactions\
\
- 👍1\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on Mar 26Mar 26, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16331748)   Collaborator\
\
|     |\
| --- |\
| Frigate's Norfair integration is heavily customized for our specific use case - it includes per-object-type Kalman filter tuning (separate configs for cars, license plates, PTZ persons), a custom 4D distance function that normalizes position change by box size, histogram-based visual re-identification for PTZ autotracking, and optical-flow camera motion compensation via Norfair's `MotionEstimator`. ByteTrack's main advantage is its two-stage association that recovers tracks using low-confidence detections, which shines in dense pedestrian benchmarks but provides little benefit for typical Frigate deployments with a smaller number of objects in frame. Switching would mean losing PTZ motion compensation, re-ID, and per-object Kalman tuning - or reimplementing all of it - for marginal gains in a crowded-scene edge case most users don't have. The MOT benchmark numbers that make ByteTrack look appealing don't reflect our operating conditions. |\
\
👍1\
\
All reactions\
\
- 👍1\
\
[![@ZhaiSoul](https://avatars.githubusercontent.com/u/8712438?s=60&v=4)](https://github.com/ZhaiSoul)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 29Mar 29, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16370566)\
\
|     |\
| --- |\
| > We also are not using the Re-ID feature of norfair currently as models did not exist to be fast enough last we checked<br>What are the performance benchmarks? Must it be run on the CPU? I noticed that auto-tracking appears to use ReID, and I’m wondering how demanding this is on performance in multi-object scenarios. |\
\
All reactions\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on Mar 29Mar 29, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16370591)   Collaborator\
\
|     |\
| --- |\
| Autotracking is using a very simple histogram based Re-ID as a supplement that has proven to be helpful in some limited scenarios. It certainly isn't robust enough for anything else.<br>I've done a lot of investigation into Re-ID models, and as [@NickM-27](https://github.com/NickM-27) mentioned, none of them are fast enough or robust enough to even consider implementing in Frigate. |\
\
👍1\
\
All reactions\
\
- 👍1\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/8712438?s=64&v=4)\ ZhaiSoul](https://github.com/ZhaiSoul) [on Mar 24Mar 24, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16288663)\
\
|     |\
| --- |\
| Feedback from the Chinese community indicates that most users haven’t found how to customize the camera layout. Currently, you must first create a Camera Group before being able to customize the layout. This guidance may need to be improved—for example, displaying a custom layout button on the default page but disabling it, and using tooltips or other prompts to remind users to create a Camera Group first. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/105557996?s=64&v=4)\ patienttruth](https://github.com/patienttruth) [on Apr 8Apr 8, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16484082)\
\
|     |\
| --- |\
| Can someone help me to understand the default for state classification?<br>Per the docs it seems neither motion or interval are enabled, so does it run at all?<br>```<br>classification:<br>  custom:<br>    # Required: name of the classification model<br>    model_name:<br>      # Optional: Enable running the model (default: shown below)<br>      enabled: True<br>      # Optional: Name of classification model (default: shown below)<br>      name: None<br>      # Optional: Classification score threshold to change the state (default: shown below)<br>      threshold: 0.8<br>      # Optional: Number of classification attempts to save in the recent classifications tab (default: shown below)<br>      # NOTE: Defaults to 200 for object classification and 100 for state classification if not specified<br>      save_attempts: None<br>      # Optional: State classification configuration<br>      state_config:<br>        # Required: Cameras to run classification on<br>        cameras:<br>          camera_name:<br>            # Required: Crop of image frame on this camera to run classification on<br>            crop: [0, 180, 220, 400]<br>        # Optional: If classification should be run when motion is detected in the crop (default: shown below)<br>        motion: False<br>        # Optional: Interval to run classification on in seconds (default: shown below)<br>        interval: None<br>``` |\
\
1You must be logged in to vote\
\
All reactions\
\
2 replies\
\
\
[![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=60&v=4)](https://github.com/NickM-27)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [NickM-27](https://github.com/NickM-27) [on Apr 8Apr 8, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16488821)   Collaborator Sponsor\
\
|     |\
| --- |\
| If you manually configured it then yes, but the wizard enables motion by default |\
\
All reactions\
\
[![@patienttruth](https://avatars.githubusercontent.com/u/105557996?s=60&v=4)](https://github.com/patienttruth)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [patienttruth](https://github.com/patienttruth) [on Apr 8Apr 9, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-16497404)\
\
|     |\
| --- |\
| 👌🏼 thanks. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/159130515?s=64&v=4)\ misterben88](https://github.com/misterben88) [on May 23May 23, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17030427)\
\
|     |\
| --- |\
| Hi ! with 0.17.1, when a role only has access to selected cameras, the review page (tab Motion) still shows cards for all cameras.<br>Those without permission are black with the message "No Preview Found".<br>But this is not a great user experience as they can see that there are other cameras that they don't have permission for.<br>Can this minor issue be fixed in a 0.17.2 release ?<br>Thanks ! |\
\
1You must be logged in to vote\
\
All reactions\
\
2 replies\
\
\
[![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=60&v=4)](https://github.com/hawkeye217)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [hawkeye217](https://github.com/hawkeye217) [on May 23May 23, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17032075)   Collaborator\
\
|     |\
| --- |\
| Thanks, this will be fixed in the next maintenance release. PR is here: [#23294](https://github.com/blakeblackshear/frigate/pull/23294) |\
\
🚀1\
\
All reactions\
\
- 🚀1\
\
[![@misterben88](https://avatars.githubusercontent.com/u/159130515?s=60&v=4)](https://github.com/misterben88)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [misterben88](https://github.com/misterben88) [on May 23May 23, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17032361)\
\
|     |\
| --- |\
| Thanks ! |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/3423596?s=64&v=4)\ zhamm](https://github.com/zhamm) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17300697)\
\
|     |\
| --- |\
| The problem is AV1 is only supported by a very few AXIS cameras at this<br>point, unless you mean re-encoding all video to store as AV1, which seems<br>unnecessarily burdensome on the CPU/GPU. Hell, most people don't even turn<br>on H.265 because they don't know what it is.<br>Much of the back end is/was in python last I checked, so any other language<br>refactor seems low yield. That said, if you got that kind of skill set,<br>party on. I'm still waiting to see your model and dataset... :)<br>[…](https://github.com/blakeblackshear/frigate/discussions/22137#)<br>On Sun, Jun 14, 2026 at 2:36 PM Quantum \*\*\*@\*\*\*.\*\*\*> wrote:<br>Whelp, my model is loading and running clean on Blackwell with four<br>patches -- selected YOLOv26 classes along with my custom ones, through the<br>parse path which used to be impossible.<br>0: Ambulance<br>1: Bicycle<br>2: Boat<br>3: Bus<br>4: Car<br>5: Cat<br>6: Courier<br>7: Dog<br>8: Drone<br>9: Fire<br>10: Fire Extinguisher<br>11: Fire Truck<br>12: Heavy Truck<br>13: Helicopter<br>14: Ladder<br>15: Meteor<br>16: Motorcycle<br>17: My Car<br>18: Neighbor Vehicle<br>19: Parcel<br>20: Person<br>21: Police Car<br>22: Projector<br>23: Rat<br>24: Smoke<br>25: Snake<br>26: Surveillance Camera<br>27: Truck<br>28: Weapon<br>29: Wheelchair<br>30: Wild Bird<br>31: Wildlife<br>I realize that I am only talking to myself since I am muzzled, but I pat<br>myself on the back just the same.<br>To the devs who care (one bad apple spoils the barrel), I suggest AV1 and<br>RUST for all. Maybe I'll do those at some point.<br>—<br>Reply to this email directly, view it on GitHub<br>< [#22137](https://github.com/blakeblackshear/frigate/discussions/22137)?email\_source=notifications&email\_token=AA2D23GY7YRZS3J5MQXINAT473WCJA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZSHE4TOMBUUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSWGM33PORSXEX3DNRUWG2Y#discussioncomment-17299704>,<br>or unsubscribe<br>< [https://github.com/notifications/unsubscribe-auth/AA2D23AEOTJ6MCC7646HGUL473WCJAVCNFSNUABHKJSXA33TNF2G64TZHMYTMNZWHE2DCOJUHNCGS43DOVZXG2LPNY5TSNJUGI3DAOFBOYBA](https://github.com/notifications/unsubscribe-auth/AA2D23AEOTJ6MCC7646HGUL473WCJAVCNFSNUABHKJSXA33TNF2G64TZHMYTMNZWHE2DCOJUHNCGS43DOVZXG2LPNY5TSNJUGI3DAOFBOYBA) ><br>.<br>Triage notifications, keep track of coding agent tasks and review pull<br>requests on the go with GitHub Mobile for iOS<br>< [https://github.com/notifications/mobile/ios/AA2D23FL6TJ74BGRVAKREXT473WCJA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZSHE4TOMBUUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSVGM33PORSXEX3JN5ZQ](https://github.com/notifications/mobile/ios/AA2D23FL6TJ74BGRVAKREXT473WCJA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZSHE4TOMBUUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSVGM33PORSXEX3JN5ZQ) ><br>and Android<br>< [https://github.com/notifications/mobile/android/AA2D23GXWJ5ALDZWV43UQOD473WCJA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZSHE4TOMBUUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSXGM33PORSXEX3BNZSHE33JMQ](https://github.com/notifications/mobile/android/AA2D23GXWJ5ALDZWV43UQOD473WCJA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZSHE4TOMBUUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSXGM33PORSXEX3BNZSHE33JMQ) >.<br>Download it today!<br>You are receiving this because you commented.Message ID:<br>\*\*\*@\*\*\*.\*\*\*<br>com> |\
\
2You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@quantum77](https://avatars.githubusercontent.com/u/35746122?s=60&v=4)](https://github.com/quantum77)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
#### [quantum77](https://github.com/quantum77) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17300981)\
\
|     |\
| --- |\
| I mean _reencoding_ to AV1, because it is right, not because it is facile. It appears that few here have heard of it and less have the hardware. But I see the value even if most don't understand the difference. I intend to archive for a long time.<br>Honestly, converting to RUST is an unknown to me at this point. Maybe I will try, maybe I won't.<br>But if you do not set goals... if you do not fail and keep trying... you are not DOING ANYTHING with your life and are worthless. Volunteer your fat ass to be put in the furnace to provide heat for the rest of us, giving at least some value. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/3423596?s=64&v=4)\ zhamm](https://github.com/zhamm) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17301053)\
\
|     |\
| --- |\
| I disagree with re-encoding, for a number of reasons, but that's just me.<br>The incremental savings just isn't worth it to me unless you're recording<br>continuously on low/medium activity scenes, and I'm not doing that.<br>Besides, AV2 is coming out soon, so why not shoot for that. I'm betting<br>the FFMPEG crew will pick it up pretty quick.<br>[…](https://github.com/blakeblackshear/frigate/discussions/22137#)<br>On Sun, Jun 14, 2026 at 6:19 PM Quantum \*\*\*@\*\*\*.\*\*\*> wrote:<br>I mean \*reencoding\* to AV1, because it is right, not because it is<br>facile. It appears that few here have heard of it and less have the<br>hardware. But I see the value even if most don't understand the difference.<br>I intend to archive for a long time.<br>Honestly, converting to RUST is an unknown to me at this point. Maybe I<br>will try, maybe I won't.<br>But if you do not set goals... if you do not fail and keep trying... you<br>are not DOING ANYTHING with your life and are worthless. Volunteer your fat<br>ass to be put in the furnace to provide heat for the rest of us, giving at<br>least some value.<br>—<br>Reply to this email directly, view it on GitHub<br>< [#22137](https://github.com/blakeblackshear/frigate/discussions/22137)?email\_source=notifications&email\_token=AA2D23HFIIZUJJHNPO2WPPT474QI7A5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYDSOBRUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSWGM33PORSXEX3DNRUWG2Y#discussioncomment-17300981>,<br>or unsubscribe<br>< [https://github.com/notifications/unsubscribe-auth/AA2D23DBUGFPENKVJMXCLJD474QI7AVCNFSNUABHKJSXA33TNF2G64TZHMYTMNZWHE2DCOJUHNCGS43DOVZXG2LPNY5TSNJUGI3DAOFBOYBA](https://github.com/notifications/unsubscribe-auth/AA2D23DBUGFPENKVJMXCLJD474QI7AVCNFSNUABHKJSXA33TNF2G64TZHMYTMNZWHE2DCOJUHNCGS43DOVZXG2LPNY5TSNJUGI3DAOFBOYBA) ><br>.<br>Triage notifications, keep track of coding agent tasks and review pull<br>requests on the go with GitHub Mobile for iOS<br>< [https://github.com/notifications/mobile/ios/AA2D23F7ADRLIBGEQN3RB6T474QI7A5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYDSOBRUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSVGM33PORSXEX3JN5ZQ](https://github.com/notifications/mobile/ios/AA2D23F7ADRLIBGEQN3RB6T474QI7A5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYDSOBRUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSVGM33PORSXEX3JN5ZQ) ><br>and Android<br>< [https://github.com/notifications/mobile/android/AA2D23AQZZBB2G5LX5MKQNT474QI7A5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYDSOBRUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSXGM33PORSXEX3BNZSHE33JMQ](https://github.com/notifications/mobile/android/AA2D23AQZZBB2G5LX5MKQNT474QI7A5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYDSOBRUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSXGM33PORSXEX3BNZSHE33JMQ) >.<br>Download it today!<br>You are receiving this because you commented.Message ID:<br>\*\*\*@\*\*\*.\*\*\*<br>com> |\
\
3You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
### [![](https://avatars.githubusercontent.com/u/35746122?s=64&v=4)\ quantum77](https://github.com/quantum77) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17301089)\
\
|     |\
| --- |\
| Fair enough. But to me it is not about compaction, it's about politics.<br>And evidently [AV2](https://en.wikipedia.org/wiki/AV2) dropped on 28 May and well, if there's a firmware update to the latest cards no objection. If not I'm Ok with AV1 for the time being.<br>Ahh...<br>Now I've offended all the fatties...<br>er, 'those of wide girth'...<br>uh, the 'heavy-set'...<br>Oh well. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/3423596?s=64&v=4)\ zhamm](https://github.com/zhamm) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17301208)\
\
|     |\
| --- |\
| Nah, it won't be a firmware update, most likely. It's almost always a<br>hardware upgrade (at least for encoding). The older Ampere cards don't<br>even support AV1 encoding.<br>It'll be a while before we see it in anything I suspect.<br>[…](https://github.com/blakeblackshear/frigate/discussions/22137#)<br>On Sun, Jun 14, 2026 at 6:47 PM Quantum \*\*\*@\*\*\*.\*\*\*> wrote:<br>Fair enough. But to me it is not about compaction, it's about politics.<br>And if AV2 is around the corner well, if it's a firmware update to the<br>latest cards no objection. If not I'm Ok with AV1 for the time being.<br>—<br>Reply to this email directly, view it on GitHub<br>< [#22137](https://github.com/blakeblackshear/frigate/discussions/22137)?email\_source=notifications&email\_token=AA2D23DHT6N3WZCJHH5ANBT474TQBA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYTAOBZUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSWGM33PORSXEX3DNRUWG2Y#discussioncomment-17301089>,<br>or unsubscribe<br>< [https://github.com/notifications/unsubscribe-auth/AA2D23GC3ITICBOYIJZ7TSD474TQBAVCNFSNUABHKJSXA33TNF2G64TZHMYTMNZWHE2DCOJUHNCGS43DOVZXG2LPNY5TSNJUGI3DAOFBOYBA](https://github.com/notifications/unsubscribe-auth/AA2D23GC3ITICBOYIJZ7TSD474TQBAVCNFSNUABHKJSXA33TNF2G64TZHMYTMNZWHE2DCOJUHNCGS43DOVZXG2LPNY5TSNJUGI3DAOFBOYBA) ><br>.<br>Triage notifications, keep track of coding agent tasks and review pull<br>requests on the go with GitHub Mobile for iOS<br>< [https://github.com/notifications/mobile/ios/AA2D23EB4PSZMWBCV7Y2UJT474TQBA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYTAOBZUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSVGM33PORSXEX3JN5ZQ](https://github.com/notifications/mobile/ios/AA2D23EB4PSZMWBCV7Y2UJT474TQBA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYTAOBZUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSVGM33PORSXEX3JN5ZQ) ><br>and Android<br>< [https://github.com/notifications/mobile/android/AA2D23BKTMJZYN632KZZJLD474TQBA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYTAOBZUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSXGM33PORSXEX3BNZSHE33JMQ](https://github.com/notifications/mobile/android/AA2D23BKTMJZYN632KZZJLD474TQBA5CNFSNUABIM5UWIORPF5TWS5BNNB2WEL2ENFZWG5LTONUW63SDN5WW2ZLOOQXTCNZTGAYTAOBZUZZGKYLTN5XKOY3PNVWWK3TUUVSXMZLOOSXGM33PORSXEX3BNZSHE33JMQ) >.<br>Download it today!<br>You are receiving this because you commented.Message ID:<br>\*\*\*@\*\*\*.\*\*\*<br>com> |\
\
3You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/blakeblackshear/frigate/discussions/22137).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/35746122?s=64&v=4)\ quantum77](https://github.com/quantum77) [on Jun 14Jun 14, 2026](https://github.com/blakeblackshear/frigate/discussions/22137\#discussioncomment-17301234)\
\
|     |\
| --- |\
| You're right. A firmware or driver update won't bring AV2 to the 5050. NVDEC and NVENC are fixed-function silicon — the decode/encode logic is hardwired at tape-out, not microcode you can reflash. The consensus is software-first: through 2026 browsers and streaming platforms integrate the reference code while silicon makers are expected to add hardware decoders in 2027–2028, and some analyses push realistic consumer rollout later still, partly because AV2 is roughly five times more complex to decode than AV1. So it's not a concern for me at this time. I'll be dead by the time AV2 comes out. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**.\
Already have an account?\
[Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fblakeblackshear%2Ffrigate%2Fdiscussions%2F22137)\
\
Category\
\
\
[💬\\
\\
General](https://github.com/blakeblackshear/frigate/discussions/categories/general)\
\
Labels\
\
\
None yet\
\
\
28 participants\
\
\
[![@blakeblackshear](https://avatars.githubusercontent.com/u/569905?s=48&v=4)](https://github.com/blakeblackshear) [![@ramunasd](https://avatars.githubusercontent.com/u/150403?s=48&v=4)](https://github.com/ramunasd) [![@kbuck1](https://avatars.githubusercontent.com/u/806426?s=48&v=4)](https://github.com/kbuck1) [![@gofaster](https://avatars.githubusercontent.com/u/1273372?s=48&v=4)](https://github.com/gofaster) [![@def1149](https://avatars.githubusercontent.com/u/3155291?s=48&v=4)](https://github.com/def1149) [![@zhamm](https://avatars.githubusercontent.com/u/3423596?s=48&v=4)](https://github.com/zhamm) [![@vincenttor](https://avatars.githubusercontent.com/u/6403564?s=48&v=4)](https://github.com/vincenttor) [![@ZhaiSoul](https://avatars.githubusercontent.com/u/8712438?s=48&v=4)](https://github.com/ZhaiSoul) [![@Ba-pt0u](https://avatars.githubusercontent.com/u/9057650?s=48&v=4)](https://github.com/Ba-pt0u) [![@ElectronicBattle](https://avatars.githubusercontent.com/u/10836275?s=48&v=4)](https://github.com/ElectronicBattle) [![@NickM-27](https://avatars.githubusercontent.com/u/14866235?s=48&v=4)](https://github.com/NickM-27) [![@haldi4803](https://avatars.githubusercontent.com/u/17104473?s=48&v=4)](https://github.com/haldi4803) [![@xury77](https://avatars.githubusercontent.com/u/26333781?s=48&v=4)](https://github.com/xury77) [![@pdobrien3](https://avatars.githubusercontent.com/u/28842285?s=48&v=4)](https://github.com/pdobrien3) [![@hawkeye217](https://avatars.githubusercontent.com/u/32435876?s=48&v=4)](https://github.com/hawkeye217) [![@MaxKuh](https://avatars.githubusercontent.com/u/33021873?s=48&v=4)](https://github.com/MaxKuh) [![@quantum77](https://avatars.githubusercontent.com/u/35746122?s=48&v=4)](https://github.com/quantum77) [![@GaryOkie](https://avatars.githubusercontent.com/u/37629938?s=48&v=4)](https://github.com/GaryOkie) [![@H1ghSyst3m](https://avatars.githubusercontent.com/u/60105043?s=48&v=4)](https://github.com/H1ghSyst3m) [![@patienttruth](https://avatars.githubusercontent.com/u/105557996?s=48&v=4)](https://github.com/patienttruth) [![@Grzesiektaktoja](https://avatars.githubusercontent.com/u/127434049?s=48&v=4)](https://github.com/Grzesiektaktoja) and others\
\
Heading\
\
Bold\
\
Italic\
\
Quote\
\
Code\
\
Link\
\
* * *\
\
Numbered list\
\
Unordered list\
\
Task list\
\
* * *\
\
Attach files\
\
Mention\
\
Reference\
\
# Select a reply\
\
Loading\
\
[Create a new saved reply](https://github.com/blakeblackshear/frigate/discussions/22137)\
\
👍1 reacted with thumbs up emoji👎1 reacted with thumbs down emoji😄1 reacted with laugh emoji🎉1 reacted with hooray emoji😕1 reacted with confused emoji❤️1 reacted with heart emoji🚀1 reacted with rocket emoji👀1 reacted with eyes emoji\
\
You can’t perform that action at this time.