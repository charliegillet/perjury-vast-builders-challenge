

## FILE: dataengine-pipelines/DEVELOPMENT.md
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/DEVELOPMENT.md

```
# Development Guide

## Prerequisites

Before you get started, make sure you have the following installed:

- Python 3.11+
- Docker (required for building functions)
- `vastde` CLI — see install steps below

## Install the CLI

Download the latest binary for your platform from the [DataEngine CLI releases page](https://github.com/vast-data/dataengine-cli/releases), then:

```bash
# macOS / Linux
chmod +x vastde
mv vastde /usr/local/bin/vastde

# Verify
vastde --version
```

Then initialise your credentials:

```bash
vastde config init
```

This creates `~/.vast/config.toml` with your VMS endpoint and credentials. Never commit this file.

## Scaffold a new function

```bash
vastde functions init python-pip <lang>-<trigger>-<use-case>
```

This generates:

```
<lang>-<trigger>-<use-case>/
├── main.py          # Handler entry point (init and handler)
├── requirements.txt # Python dependencies
├── Aptfile          # System packages
├── customDeps       # Custom/private shared libraries
└── README.md        # Generated development guide
```

## Build

```bash
vastde functions build <function-name>
```

Docker must be running. The build will:
- Install system packages from `Aptfile`
- Install Python dependencies from `requirements.txt`
- Install custom dependencies from `customDeps`
- Create a container image ready for deployment

## Test locally

```bash
# Basic local run
vastde functions localrun <function-name>

# Run with custom port
vastde functions localrun <function-name> --port 9090

# Run with config
vastde functions localrun <function-name> -c config.yaml
```

Invoke your function with an auto-generated event:

```bash
vastde functions invoke --generate-event --url http://localhost:8080/  # change port if specified via --port
```

Alternatively, create a `cloudevent.yaml` in your function folder to send a custom event specific to your function, then invoke with:

```bash
vastde functions invoke <function-name> -f cloudevent.yaml
```

## Configuration

Create a `config.yaml` to pass environment variables and secrets to your function:

```yaml
envs:
  MY_VARIABLE: "hello-world"

secrets:
  username: "myuser"
  password: "mypassword"
```

Never commit real credentials. `config.yaml` is in `.gitignore` — use placeholder values and document what each variable does in your function's `README.md`.

## Deploy

Deploy via the DataEngine UI or CLI. See the per-function `README.md` for function-specific steps.

## Logs

```bash
vastde logs tail <pipeline> --function <lang>-<trigger>-<use-case>
```

## Run unit tests (optional)

```bash
pytest tests/
```

```


## FILE: dataengine-pipelines/python-cron-hello-world/README.md
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/python-cron-hello-world/README.md

```
## Overview

A hello world function triggered on a cron schedule. Logs a greeting on initialization and the trigger event on each invocation.

| Field | Value |
|---|---|
| **Trigger** | Cron |
| **Runtime** | Python 3.12.12 |
| **Status** | Complete |

## Prerequisites

- Access to a VAST DataEngine tenant and container registry (below as `<registry-host>`)
- `vastde` CLI installed and configured, see [DEVELOPMENT.md](../DEVELOPMENT.md)
  - run `vastde --version` to check installation
  - run `vastde functions list` to check that you have DataEngine access

## Project Structure
    |- main.py               # Your function handlers (init and handler)
    |- requirements.txt      # Python dependencies
    |- Aptfile               # System packages
    |- customDeps            # custom dependencies such as private common libraries
    |- config.example.yaml   # Environment variable template, copy to config.yaml and fill in values
    |- pipeline-config.yaml  # Pipeline definition (trigger → function wiring)
    |- README.md             # This file

## Configuration

Copy `config.example.yaml` to `config.yaml` and fill in your values:

```bash
cp config.example.yaml config.yaml
```

### Environment Variables

| Variable | Type | Description |
|---|---|---|
| `GREETING` | env | Message logged on each invocation |

Never commit `config.yaml`. It is already included in `.gitignore`.

## Run Function on DataEngine

Follow these steps to deploy and run the function on DataEngine. For detailed instructions, refer to the [DataEngine Documentation](https://kb.vastdata.com/documentation/docs/version-54-3).

Instructions are given using the `vastde` CLI and DataEngine UI.

> **Note:** Commands use `$USER` as a prefix for resource names (e.g. `$USER-hello-world`). This avoids naming collisions when multiple users are deploying to a shared tenant.

### 1. Build Function

Build the function image, then register it as a function in DataEngine:

```bash
cd python-cron-hello-world
vastde functions build $USER-hello-world
```

```bash
# vastde functions build output
Detected language: python
Validating Python version 3.12.*...
Python version 3.12.* resolved to 3.12.12
Building $USER-hello-world:latest
App Path: .../python-cron-hello-world
Handlers File: main.py
Build log: .../python-cron-hello-world/build.log
2026/03/18 14:22:18 [Started] Python Builder: $USER-hello-world:latest
2026/03/18 14:22:34 [Completed] Python Builder: $USER-hello-world:latest
Build completed: $USER-hello-world:latest
Build log saved to: .../python-cron-hello-world/build.log
```

Push the image to your container registry configured on your DataEngine tenant (search for `Container Registries` in VMS):

```bash
docker tag $USER-hello-world:latest <registry-host>/<registry-user>/$USER-hello-world:<version>
docker push <registry-host>/<registry-user>/$USER-hello-world:<version>
```

Create the function on DataEngine:
```bash
vastde functions create \
 --name $USER-hello-world \
 --container-registry <registry-name-on-vms> \
 --artifact-source <registry-user>/$USER-hello-world  \
 --image-tag <version>
```

```bash
# vastde functions create output
Function created: $USER-hello-world
Name: $USER-hello-world
Tags: []
GUID: <guid>
Owner: [id: <id>, id-type: vid]
Created At: 2026-03-18T18:50:47Z
Updated At: 2026-03-18T18:50:47Z
VRN: vast:dataengine:functions:$USER-hello-world
Last Revision: 1
```

### 2. Set up Trigger

To create the trigger, navigate to the DataEngine UI and click on `Triggers` + `Create Trigger`:

![alt text](set-up-trigger.png)

Fill in the following fields:

| Field | Example value | Notes |
|---|---|---|
| **Name** | `$USER-schedule-5m-trigger` | Must match the trigger name in `pipeline-config.yaml`. The pipeline create step will fail if the trigger does not exist or the name does not match |
| **Type** | `Schedule` | |
| **Cron Expression** | `0 0/5 * ? * * *` | Runs every 5 minutes |
| **Description** | `Schedule trigger - every 5 minutes` | Optional |

Afterwards, you can view the trigger via CLI:

```bash
vastde triggers list
```

```bash
# vastde triggers list output
Trigger Name               Status        Type        Description      GUID                        Updated at
------------------------------------------------------------------------------------------------------------------
schedule-20m-trigger       Ready         0xc0004...  Schedule tri...  6a9f2b3a-605d-4593-a90e...  2026-03-29 21:22
schedule-5m-trigger        Ready         0xc0006...                   4d32fd72-7961-4b00-940b...  2026-03-29 21:23
```

### 3. Deploy Pipeline

Create a pipeline connecting the trigger to the function using `pipeline-config.yaml`. 

> Before running, update the resource names in `pipeline-config.yaml` to include your `$USER` prefix:

```bash
vastde pipelines create --config pipeline-config.yaml
```

```bash
# vastde pipelines create output
Pipeline created: $USER-cron-hello-world-pipeline
Name: $USER-cron-hello-world-pipeline
Description: A sample pipeline to print hello world on a schedule
Tags: [cron]
GUID: df31058f-9e34-48f0-97ea-7222138e5bff
Owner: [id: 477, id-type: vid]
Created At: 2026-03-29T21:51:00Z
Updated At: 2026-03-29T21:51:00Z
VRN: vast:dataengine:pipelines:$USER-cron-hello-world-pipeline
```

You can deploy the pipeline via UI or CLI:

```bash
vastde pipelines deploy $USER-cron-hello-world-pipeline
```

```bash
# vastde pipelines deploy output
Pipeline deployed successfully
```

After the pipeline is deployed, tail the logs to verify the function is being invoked:

```bash
vastde logs tail $USER-cron-hello-world-pipeline --function $USER-hello-world --since 1h
```

```bash
# vastde logs tail output
2026-03-30 11:25:01.22 [$USER-hello-world] [INFO]  [user] Handler {'attributes': {'source': 'vastdata.com:schedule-5m-trigger.4d32fd72-7961-4b00-940b-e16383ee8a3f', 'id': '2d8ffd24-c69e-4ff6-8c29-6f4523991cbe', 'type': 'vastdata.com:Schedule.TimerElapsed', 'specversion': '1.0', 'time': '2026-03-30T15:25:00.837000+00:00', 'subject': 'engine-broker.main', 'datacontenttype': 'application/json', 'dataschema': None, 'cronschedule': '0 0/5 * ? * * *', 'knativekafkaoffset': '85992', 'knativekafkapartition': '0', 'partitionkey': '2d8ffd24-c69e-4ff6-8c29-6f4523991cbe', 'timerelapsedtimestamp': '2026-03-30T15:25:00.008211Z'}, 'data': {'message': 'Activating trigger by cron'}}
```

## Local Development

### Build

```bash
vastde functions build $USER-hello-world
```

### Run locally

```bash
vastde functions localrun $USER-hello-world -c config.yaml
```

### Invoke

```bash
vastde functions invoke --generate-event --url http://localhost:8080/
```

## Resources

- [DEVELOPMENT.md](../DEVELOPMENT.md): local setup and CLI workflow
- [CONTRIBUTING.md](../CONTRIBUTING.md): how to contribute
- [DataEngine Docs](https://kb.vastdata.com/documentation/docs/version-54-3)
- [DataEngine CLI](https://github.com/vast-data/dataengine-cli)
- [VAST Community](https://community.vastdata.com/)
- [VAST Developers](https://www.vastdata.com/developers)
```


## FILE: dataengine-pipelines/python-cron-hello-world/pipeline-config.yaml
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/python-cron-hello-world/pipeline-config.yaml

```
# Sample pipeline configuration
# Before deploying, replace $USER with your username (`echo $USER`)  and <kubernetes-cluster-vrn> with your cluster VRN.
name: $USER-cron-hello-world-pipeline
description: A sample pipeline to print hello world on a schedule
tags:
  - cron
kubernetes_cluster_vrn: <kubernetes-cluster-vrn>
namespace: default
manifest:
  config:
    environment_variables:
      - name: GREETING
        value: "Hello, World!"
  triggers:
    - name: $USER-schedule-5m-trigger
      vrn: vast:dataengine:triggers:$USER-schedule-5m-trigger
  function_deployments:
    - name: $USER-hello-world
      function_vrn: vast:dataengine:functions:$USER-hello-world
      revision: 1
  links:
      - source: ["$USER-schedule-5m-trigger"]
        destination: ["$USER-hello-world"]

```


## FILE: dataengine-pipelines/python-cron-hello-world/main.py
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/python-cron-hello-world/main.py

```
import os

def init(ctx):
    # One time initialization comes here
    ctx.logger.info(f"Initialized... {os.environ.get('GREETING')}")

def handler(ctx, event):
    # Events Processing comes here
    ctx.logger.info(f"Handler {event}")
    return "Hello World"
```


## FILE: dataengine-pipelines/python-s3-hello-world/README.md
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/python-s3-hello-world/README.md

```
## Overview

A hello world function triggered on a S3 created event. Logs a greeting on initialization and the trigger event on each invocation.

| Field | Value |
|---|---|
| **Trigger** | S3 Create Event  |
| **Runtime** | Python 3.12.12 |
| **Status** | Complete |

## Prerequisites

- Access to a VAST DataEngine tenant and container registry (below as `<registry-host>`)
- `vastde` CLI installed and configured, see [DEVELOPMENT.md](../DEVELOPMENT.md)
  - run `vastde --version` to check installation
  - run `vastde functions list` to check that you have DataEngine access

## Project Structure
    |- main.py               # Your function handlers (init and handler)
    |- requirements.txt      # Python dependencies
    |- Aptfile               # System packages
    |- customDeps            # custom dependencies such as private common libraries
    |- config.example.yaml   # Environment variable template, copy to config.yaml and fill in values
    |- pipeline-config.yaml  # Pipeline definition (trigger → function wiring)
    |- README.md             # This file
    |- test.md               # Example file to upload via Virtual Machine (instructions below)

## (Optional) Configuration

Copy `config.example.yaml` to `config.yaml` and fill in your values:

```bash
cp config.example.yaml config.yaml
```

### (Optional) Environment Variables

Never commit `config.yaml`. It is already included in `.gitignore`.

## Run Function on DataEngine

Follow these steps to deploy and run the function on DataEngine. For detailed instructions, refer to the [DataEngine Documentation](https://kb.vastdata.com/documentation/docs/version-54-3).

Instructions are given using the `vastde` CLI and DataEngine UI.

> **Note:** Commands use `$USER` (`echo $USER` value) as a prefix for resource names (e.g. `$USER-s3-hello-world`). This avoids naming collisions when multiple users are deploying to a shared tenant. Also, consider using `${USER//./-}` instead of $USER to swap `.` with `-` for readability.

### 1. Build Function

Build the function image, then register it as a function in DataEngine:

```bash
cd python-s3-hello-world
vastde functions build $USER-s3-hello-world
```

```bash
# vastde functions build output
Detected language: python
Validating Python version 3.12.*...
Python version 3.12.* resolved to 3.12.12
Building $USER-s3-hello-world:latest
App Path: .../python-s3-hello-world
Handlers File: main.py
Build log: .../python-s3-hello-world/build.log
2026/03/18 14:22:18 [Started] Python Builder: $USER-s3-hello-world:latest
2026/03/18 14:22:34 [Completed] Python Builder: $USER-s3-hello-world:latest
Build completed: $USER-s3-hello-world:latest
Build log saved to: .../python-s3-hello-world/build.log
```

Push the image to your container registry configured on your DataEngine tenant (search for `Container Registries` in VMS):

```bash
docker tag $USER-s3-hello-world:latest <registry-host>/<registry-user>/$USER-s3-hello-world:<version>
docker push <registry-host>/<registry-user>/$USER-s3-hello-world:<version>
```

Create the function on DataEngine:
```bash
vastde functions create \
 --name $USER-s3-hello-world \
 --container-registry <registry-name-on-vms> \
 --artifact-source <registry-user>/$USER-s3-hello-world  \
 --image-tag <version>
```

```bash
# vastde functions create output
Function created: $USER-s3-hello-world
Name: $USER-s3-hello-world
Tags: []
GUID: <guid>
Owner: [id: <id>, id-type: vid]
Created At: 2026-03-18T18:50:47Z
Updated At: 2026-03-18T18:50:47Z
VRN: vast:dataengine:functions:$USER-s3-hello-world
Last Revision: 1
```

List the available functions: `vastde functions list`:

```bash
# vastde functions list output
Function Name              Description                          Guid                                    Updated at         
---------------------------------------------------------------------------------------------------------------------------
$USER-s3-hello-world                                           ca87e704-2501-4bc2-8ebe-aeba3ca7ed3f    2026-04-08 15:03 
```

### 2. Set up Trigger

To create the trigger, navigate to the DataEngine UI and click on `Triggers` + `Create Trigger`:

![alt text](set-up-trigger.png)

Fill in the following fields:

| Field | Example value | Notes |
|---|---|---|
| **Name** | `$USER-s3-trigger` | Replace $USER with `echo $USER` value. Must match the trigger name in `pipeline-config.yaml`. The pipeline create step will fail if the trigger does not exist or the name does not match |
| **Trigger Type** | `Element` | |
| **Source View** | `select s3 bucket` | We will use `s3cmd` to upload to the s3 bucket |
| **Element Type** | `Element Created` | |
| **Description** | `s3 element created event` | Optional |
<!-- | **Cron Expression** | `0 0/5 * ? * * *` | Runs every 5 minutes | -->

> **Note:** For `Source View`, ensure you have access to the S3 bucket for adding files to trigger pipeline.

Afterwards, you can view the trigger via CLI:

```bash
vastde triggers list
```

```bash
# vastde triggers list output
Trigger Name               Status        Type        Description      GUID                        Updated at
------------------------------------------------------------------------------------------------------------------
$USER-s3-trigger       Ready         0xc0006...                   4d32fd72-7961-4b00-940b...  2026-03-29 21:23
schedule-20m-trigger       Ready         0xc0004...  Schedule tri...  6a9f2b3a-605d-4593-a90e...  2026-03-29 21:22
```

### 3. Deploy Pipeline

Create a pipeline connecting the trigger to the function using `pipeline-config.yaml`. 

> Before running, ensure the resource names in `pipeline-config.yaml` are updated (i.e. replace `$USER`):

```bash
vastde pipelines create --config pipeline-config.yaml
```

```bash
# vastde pipelines create output
Pipeline created: $USER-s3-hello-world-pipeline
Name: $USER-s3-hello-world-pipeline
Description: A sample pipeline to print hello world on a s3 element created event
Tags: [element-created]
GUID: df31058f-9e34-48f0-97ea-7222138e5bff
Owner: [id: 477, id-type: vid]
Created At: 2026-03-29T21:51:00Z
Updated At: 2026-03-29T21:51:00Z
VRN: vast:dataengine:pipelines:$USER-s3-hello-world-pipeline
```

You can deploy the pipeline via UI or CLI:

```bash
vastde pipelines deploy $USER-s3-hello-world-pipeline
```

```bash
# vastde pipelines deploy output
Pipeline deployed successfully
```

After the pipeline is deployed, tail the logs to verify the function is being invoked:

```bash
vastde logs tail $USER-s3-hello-world-pipeline --function $USER-s3-hello-world --since 1h
```


```bash
# vastde logs tail output
2026-04-08 11:27:58.01 [$USER-s3-hell...] [INFO]  [user] Initialized... Hello, World!```
```

### 4. Test Pipeline with S3 file upload
 
Confirm network access to the S3 bucket via `ping <S3 Endpoint>`.

Run the following command to upload the example file to your S3 bucket to trigger the pipeline.

```bash
s3cmd put ./test.md s3://<your-bucket>/test.md
upload: './test.md' -> 's3://<your-bucket>/test.md'  [1 of 1]
 15 of 15   100% in    0s  1548.79 B/s  done
```

Check the pipeline output again:

```bash
vastde logs tail $USER-s3-hello-world-pipeline --function $USER-s3-hello-world --since 1h
```

```bash
#vastde logs tail output
2026-04-08 15:27:58.01 [$USER-s3-hell...] [INFO]  [user] Initialized... Hello, World!
2026-04-08 15:41:29.67 [$USER-s3-hell...] [INFO]  [user] Handler {'attributes': {'source': 'vastdata.com:$USER-s3-trigger.b45a6820-410c-457a-ac1b-035a102b5d05', 'id': '1004356627333135', 'type': 'vastdata.com:Element.ElementCreated', 'specversion': '1.0', 'time': '2026-04-08T15:41:29.591955+00:00', 'subject': 'vast-broker-engine-broker.main', 'datacontenttype': 'application/json', 'dataschema': None, 'elementhandle': '8025198034623744117', 'elementpath': 's3-bucket-name/test.md', 'elementsourcetype': 'vast:s3', 'knativekafkaoffset': '135498', 'knativekafkapartition': '0'}, 'data': {'Records': [{'eventVersion': '2.2', 'eventSource': 'vast:s3', 'awsRegion': 'selab-var-201', 'eventTime': '2026-04-08T15:41:29.591955Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'principleId'}, 'requestParameters': {'sourceIPAddress': '172.200.11.10'}, 'responseElements': {'x-amz-request-id': '0x391710286a372', 'x-amz-id-2': '0x391710286a372'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '$USER-s3-trigger.b45a6820-410c-457a-ac1b-035a102b5d05', 'bucket': {'name': 's3-bucket-name', 'ownerIdentity': {'principalId': 'principleId'}, 'arn': 'arn:aws:s3:::s3-bucket-name'}, 'object': {'key': 'test.md', 'size': 15, 'eTag': '1d6155b60405bab055527913efd734a7', 'sequencer': '009f00000000000f42fd'}}}]}}
```

## Local Development

### Build

```bash
vastde functions build $USER-s3-hello-world
```

### Run locally

```bash
vastde functions localrun $USER-s3-hello-world -c config.yaml
```

### Invoke

```bash
vastde functions invoke --generate-event --url http://localhost:8080/
```

## Resources

- [DEVELOPMENT.md](../DEVELOPMENT.md): local setup and CLI workflow
- [CONTRIBUTING.md](../CONTRIBUTING.md): how to contribute
- [DataEngine Docs](https://kb.vastdata.com/documentation/docs/version-54-3)
- [DataEngine CLI](https://github.com/vast-data/dataengine-cli)
- [VAST Community](https://community.vastdata.com/)
- [VAST Developers](https://www.vastdata.com/developers)
```


## FILE: dataengine-pipelines/python-s3-llm-summary/main.py
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/python-s3-llm-summary/main.py

```
import os
import urllib.parse
import boto3
from openai import OpenAI

EXPECTED_ENVS = [
    'S3_MOCK', 'S3_ENDPOINT_URL', 'S3_REGION',
    'LLM_MOCK', 'LLM_ENDPOINT', 'MODEL_NAME', 'MAX_TOKENS',
]

def init(ctx):
    ctx.logger.info("🚀 Init")
    for key in EXPECTED_ENVS:
        val = os.environ.get(key)
        ctx.logger.info(f"ℹ️ {key}={val if val is not None else 'NOT SET'}")

    # Load secrets
    secrets = ctx.secrets.get("secrets", {})
    s3_access_key = secrets.get("S3_ACCESS_KEY", "")
    s3_secret_key = secrets.get("S3_SECRET_KEY", "")
    llm_api_key   = secrets.get("LLM_API_KEY", "")
    ctx.logger.info(f"ℹ️ S3_ACCESS_KEY={'set' if s3_access_key else 'NOT SET'}")
    ctx.logger.info(f"ℹ️ S3_SECRET_KEY={'set' if s3_secret_key else 'NOT SET'}")
    ctx.logger.info(f"ℹ️ LLM_API_KEY={'set' if secrets.get('LLM_API_KEY') else 'NOT SET'}")

    # S3 client
    s3_mock = os.environ.get('S3_MOCK', 'false').lower() == 'true'
    ctx.logger.info(f"ℹ️ S3_MOCK={s3_mock}")
    ctx.s3_mock = s3_mock

    if not s3_mock:
        s3_endpoint = os.environ.get('S3_ENDPOINT_URL')
        s3_region = os.environ.get('S3_REGION')
        ctx.logger.info(f"ℹ️ S3_ENDPOINT_URL={s3_endpoint}")
        ctx.logger.info(f"ℹ️ S3_REGION={s3_region}")
        if not s3_access_key or not s3_secret_key:
            ctx.logger.error("⚠️ S3_ACCESS_KEY or S3_SECRET_KEY missing from secrets")
            raise ValueError("Missing required S3 secrets")
        if not s3_endpoint:
            ctx.logger.error("⚠️ S3_ENDPOINT_URL missing")
            raise ValueError("Missing S3_ENDPOINT_URL")
        ctx.s3_client = boto3.client(
            's3',
            use_ssl=False,
            endpoint_url=s3_endpoint,
            aws_access_key_id=s3_access_key,
            aws_secret_access_key=s3_secret_key,
            region_name=s3_region,
            config=boto3.session.Config(
                signature_version='s3v4',
                s3={'addressing_style': 'path'}
            )
        )
        ctx.logger.info("✅ S3 client initialized")
    else:
        ctx.s3_client = None
        ctx.logger.info("ℹ️ S3_MOCK=true, skipping S3 client init")

    # LLM client
    llm_mock = os.environ.get('LLM_MOCK', 'true').lower() == 'true'
    ctx.logger.info(f"ℹ️ LLM_MOCK={llm_mock}")

    if not llm_mock:
        endpoint = os.environ.get('LLM_ENDPOINT', '')
        if not endpoint:
            ctx.logger.error("⚠️ LLM_ENDPOINT missing")
            raise ValueError("Missing LLM_ENDPOINT")
        ctx.llm_client = OpenAI(base_url=endpoint, api_key=llm_api_key)
        ctx.logger.info(f"✅ LLM client initialized → {endpoint}")
    else:
        ctx.llm_client = None
        ctx.logger.info("ℹ️ LLM_MOCK=true, skipping LLM client init")

def handler(ctx, event):
    ctx.logger.info("ℹ️ Handler invoked")
    ctx.logger.info(f"ℹ️ event.data={event.data}")

    # Parse S3 event
    records = event.data.get('Records') or event.data.get('data', {}).get('Records', [])
    if not records:
        ctx.logger.warning("⚠️ No Records found in event")
        return "Error: No Records found in event data"

    s3_bucket = records[0]['s3']['bucket']['name']
    s3_key = urllib.parse.unquote(records[0]['s3']['object']['key'])
    ctx.logger.info(f"📦 Bucket: {s3_bucket}")
    ctx.logger.info(f"📄 Key: {s3_key}")

    # Fetch file from S3
    if ctx.s3_mock:
        sample_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        content = open(sample_path).read()
        ctx.logger.info("ℹ️ S3_MOCK=true — using sample.txt as placeholder content")
    else:
        ctx.logger.info("⬇️ Fetching file from S3...")
        try:
            response = ctx.s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
            content = response['Body'].read().decode('utf-8')
            ctx.logger.info(f"✅ File fetched — size: {response['ContentLength']} bytes, type: {response['ContentType']}")
        except Exception as e:
            ctx.logger.error(f"⚠️ Error fetching file: {e}")
            return f"Error fetching file: {e}"

    ctx.logger.info("🤖 Calling LLM for summary...")
    summary = llm_summary(ctx, content)
    ctx.logger.info(f"✅ Summary: {summary}")

    return {"bucket": s3_bucket, "key": s3_key, "summary": summary}

def llm_summary(ctx, content):
    if ctx.llm_client is None:
        ctx.logger.info("ℹ️ LLM_MOCK=true — returning placeholder summary")
        return "[mock] This is a placeholder summary for local testing without an LLM."

    model = os.environ.get("MODEL_NAME", "gpt-4o-mini")
    max_tokens = int(os.environ.get("MAX_TOKENS", "512"))
    ctx.logger.info(f"ℹ️ Model: {model}, MaxTokens: {max_tokens}")

    query = f"Summarize in 1-2 sentences:\n{content}"
    try:
        completion = ctx.llm_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}],
            max_tokens=max_tokens,
            stream=True,
        )
        out = "".join(
            chunk.choices[0].delta.content
            for chunk in completion
            if chunk.choices[0].delta.content
        )
        return out.split("</think>")[-1].strip()
    except Exception as e:
        ctx.logger.error(f"⚠️ LLM call failed: {e}")
        return f"Error: LLM call failed — {e}"

```


## FILE: dataengine-pipelines/python-s3-llm-summary/pipeline-config.yaml
Source: https://github.com/vast-data/dataengine-pipelines/blob/main/python-s3-llm-summary/pipeline-config.yaml

```
# Sample pipeline configuration
# Before deploying, replace $USER with your username (`echo $USER`) and <kubernetes-cluster-vrn> with your cluster VRN.
name: $USER-s3-llm-summary-pipeline
description: A sample pipeline to summarize body of text on a s3 element created event
tags:
  - element-created
kubernetes_cluster_vrn: <kubernetes-cluster-vrn>
namespace: default
manifest:
  config:
    environment_variables:
      - name: GREETING
        value: "Hello, World!"
  triggers:
    - name: $USER-s3-llm-summary-trigger
      vrn: vast:dataengine:triggers:$USER-s3-llm-summary-trigger
  function_deployments:
    - name: $USER-s3-llm-summary
      function_vrn: vast:dataengine:functions:$USER-s3-llm-summary
      revision: 1
  links:
    - source: ["$USER-s3-llm-summary-trigger"]
      destination: ["$USER-s3-llm-summary"]

```
