

## FILE: dataengine-cli/docs/references/commands/vastde_triggers_create.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_triggers_create.md

```
---
title: vastde triggers create
description: Create a VAST DataEngine trigger
---

# vastde triggers create

Create a VAST DataEngine trigger

## Synopsis

Create a VAST DataEngine trigger

## Usage

```
vastde triggers create [command] [options]
```

## Examples

```bash
  # Create Element trigger for object created events
  vastde triggers create \
    --name image-processor-trigger \
    --type Element \
    --event "ObjectCreated:*" \
    --source-bucket my-bucket

  # Create trigger from YAML configuration file
  vastde triggers create --from-file trigger-config.yaml

  # Create Element trigger with name prefix filter
  vastde triggers create \
    --name csv-processor-trigger \
    --type Element \
    --event "ObjectCreated:*" \
    --source-bucket data-bucket \
    --name-prefix "csv/"

  # Create trigger with multiple events (using repeated flag)
  vastde triggers create \
    --name multi-event-trigger \
    --type Element \
    --event "ObjectCreated:*" \
    --event "ObjectRemoved:*" \
    --source-bucket my-bucket

  # Create Schedule trigger for scheduled execution
  vastde triggers create \
    --name daily-report-trigger \
    --type Schedule \
    --cron-schedule "0 2 * * *"

  # Create trigger with custom extensions
  vastde triggers create \
    --name advanced-trigger \
    --type Element \
    --event "ObjectCreated:*" \
    --source-bucket my-bucket \
    --custom-extension "key1=value1" \
    --custom-extension "key2=value2"

  # Dry-run to preview the API request
  vastde triggers create \
    --name test-trigger \
    --type Element \
    --event "ObjectCreated:*" \
    --source-bucket test-bucket \
    --dry-run
```

## Subcommands

- [element](vastde_triggers_create_element.md) - Create a new element trigger
- [schedule](vastde_triggers_create_schedule.md) - Create a new schedule trigger

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--broker-name` | string | Broker name for an external event broker or bucket (view) name for a VAST event broker on the VAST Cluster. If omitted, the DataEngine default broker is used. |  |
| `--broker-type` | string | Broker type (`external` or `internal` for a VAST event broker) |  |
| `--broker-url` | string | URL to the broker (for external brokers) |  |
| `--cron-schedule` | string | Cron schedule for schedule triggers (required for --type schedule) |  |
| `--custom-extension` | stringArray | Custom extension as key=value or @file (repeatable, only flat key-value pairs allowed) |  |
| `--description` | string | A description of the resource. (optional) |  |
| `--event` | stringSlice | List of events for element triggers (can be repeated). Allowed: ObjectCreated:*, ObjectRemoved:*, ObjectTagging:Put, ObjectTagging:Delete |  |
| `-f`, `--from-file` | string | Path to trigger config file (yaml|json) |  |
| `-n`, `--name` | string | A name for the resource |  |
| `--name-prefix` | string | Name filter prefix for element triggers |  |
| `--name-suffix` | string | Name filter suffix for element triggers |  |
| `--source-bucket` | string | The source bucket name (required for element triggers). Use 'vastde buckets list' to see available buckets |  |
| `--tag-prefix` | string | Tag filter prefix for element triggers |  |
| `--tag-suffix` | string | Tag filter suffix for element triggers |  |
| `--tags` | stringSlice | Custom tags to apply. (optional) |  |
| `--topic` | string | Target topic for trigger events |  |
| `-t`, `--type` | string | The trigger type (Element,Schedule) |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde triggers](vastde_triggers.md) - Manage VAST DataEngine triggers


```


## FILE: dataengine-cli/docs/references/commands/vastde_triggers_create_schedule.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_triggers_create_schedule.md

```
---
title: vastde triggers create schedule
description: Create a new schedule trigger
---

# vastde triggers create schedule

Create a new schedule trigger

## Synopsis

Create a new schedule trigger

## Usage

```
vastde triggers create schedule [options]
```

## Examples

```bash
  # Create a schedule trigger that runs every hour
  vastde triggers create schedule \
    --name hourly-job \
    --cron-schedule "0 * * * *"

  # Create a schedule trigger from YAML configuration file
  vastde triggers create schedule --from-file trigger-config.yaml

  # Create a schedule trigger that runs daily at midnight
  vastde triggers create schedule \
    --name daily-cleanup \
    --cron-schedule "0 0 * * *" \
    --description "Daily cleanup job"

  # Create a schedule trigger with broker configuration
  vastde triggers create schedule \
    --name kafka-scheduled-job \
    --cron-schedule "0 2 * * *" \
    --topic-name my-topic \
    --broker-type Internal \
    --broker-name my-broker

  # Create a schedule trigger with custom tags
  vastde triggers create schedule \
    --name tagged-job \
    --cron-schedule "0 6 * * *" \
    --tags "env:prod,team:data"
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-m`, `--broker-name` | string | The broker name for the trigger |  |
| `-b`, `--broker-type` | string | The broker type for the trigger |  |
| `-u`, `--broker-url` | string | The broker URL for the trigger |  |
| `--cron-schedule` | string | The cron schedule for the trigger |  |
| `--custom-extension` | stringArray | Custom extension as key=value or @file (repeatable, only flat key-value pairs allowed) |  |
| `--description` | string | A description of the resource. (optional) |  |
| `-f`, `--from-file` | string | Path to trigger config file (yaml|json) |  |
| `-n`, `--name` | string | A name for the resource |  |
| `--tags` | stringSlice | Custom tags to apply. (optional, comma-separated or repeated) |  |
| `-t`, `--topic-name` | string | The topic name for the trigger |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde triggers create](vastde_triggers_create.md) - Create a VAST DataEngine trigger


```


## FILE: dataengine-cli/docs/references/commands/vastde_triggers_create_element.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_triggers_create_element.md

```
---
title: vastde triggers create element
description: Create a new element trigger
---

# vastde triggers create element

Create a new element trigger

## Synopsis

Create a new VAST DataEngine element trigger

## Usage

```
vastde triggers create element [options]
```

## Examples

```bash
  # Create Element trigger for object created events
  vastde triggers create element \
    --name image-processor-trigger \
    --event "ObjectCreated:*" \
    --source-bucket my-bucket

  # Create Element trigger from YAML configuration file
  vastde triggers create element --from-file trigger-config.yaml

  # Create Element trigger with name prefix filter
  vastde triggers create element \
    --name csv-processor-trigger \
    --event "ObjectCreated:*" \
    --source-bucket data-bucket \
    --name-prefix "csv/"

  # Create Element trigger with multiple events (using repeated flag)
  vastde triggers create element \
    --name multi-event-trigger \
    --event "ObjectCreated:*" \
    --event "ObjectRemoved:*" \
    --source-bucket my-bucket

  # Create Element trigger with broker configuration
  vastde triggers create element \
    --name kafka-trigger \
    --event "ObjectCreated:*" \
    --source-bucket my-bucket \
    --topic-name my-topic \
    --broker-type kafka \
    --broker-name my-broker

  # Create Element trigger with tag filters
  vastde triggers create element \
    --name tagged-trigger \
    --event "ObjectTagging:Put" \
    --source-bucket my-bucket \
    --tag-prefix "env:prod"
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-m`, `--broker-name` | string | The broker name for the trigger |  |
| `-b`, `--broker-type` | string | The broker type for the trigger |  |
| `-u`, `--broker-url` | string | The broker URL for the trigger |  |
| `--custom-extension` | stringArray | Custom extension as key=value or @file (repeatable, only flat key-value pairs allowed) |  |
| `--description` | string | A description of the resource. (optional) |  |
| `--event` | stringSlice | List of events (can be repeated). Allowed: ObjectCreated:*, ObjectRemoved:*, ObjectTagging:Put, ObjectTagging:Delete |  |
| `-f`, `--from-file` | string | Path to trigger config file (yaml|json) |  |
| `-n`, `--name` | string | A name for the resource |  |
| `--name-prefix` | string | Name filter prefix for element triggers |  |
| `--name-suffix` | string | Name filter suffix for element triggers |  |
| `-s`, `--source-bucket` | string | The source bucket name for the trigger |  |
| `--source-types` | stringSlice | The source types for the trigger (comma-separated or repeated) |  |
| `--tag-prefix` | string | Tag filter prefix for element triggers |  |
| `--tag-suffix` | string | Tag filter suffix for element triggers |  |
| `--tags` | stringSlice | Custom tags to apply. (optional, comma-separated or repeated) |  |
| `-t`, `--topic-name` | string | The topic name for the trigger |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde triggers create](vastde_triggers_create.md) - Create a VAST DataEngine trigger


```


## FILE: dataengine-cli/docs/references/commands/vastde_functions_build.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_functions_build.md

```
---
title: vastde functions build
description: Build a VAST DataEngine function locally
---

# vastde functions build

Build a VAST DataEngine function locally

## Synopsis

Build a DataEngine function container image locally using Docker.

This command packages your function code into a container image using the VAST DataEngine
builder. The build process:

1. Detects the programming language (Python, Go, Node.js) from project files
2. Validates the handler file based on language requirements
3. Validates the runtime version (e.g., Python version)
4. Packages dependencies (requirements.txt, go.mod, package.json)
5. Creates a container image with the function runtime
6. Tags the image with the specified tag

Language Detection:
The CLI automatically detects your function's language:
- Python: detected by presence of requirements.txt
- Go: detected by presence of go.mod (coming soon)
- Node.js: detected by presence of package.json (coming soon)

Prerequisites:
- Docker must be installed and running
- Builder image URL must be configured (use 'builders set')
- Function code must have valid handler file for the detected language

Python Functions:
- Handler file must contain init(ctx) and handler(ctx, event) functions
- Use --version to specify exact version (e.g., 3.12.11) or pattern (e.g., 3.12.*)
- Available versions are validated against the configured builder image

Build Output:
The build process creates a build.log file in the target directory with detailed build output.
This log is useful for debugging build failures or understanding the build process.

Cache Behavior:
The build process automatically caches runtime installations and dependencies for faster builds.
For Python functions, when you change the Python version, the cache is automatically cleared.
You can manually clear the cache using --clear-cache if you encounter issues.

After building, you can:
- Test locally using 'functions localrun'
- Push to a container registry (if --push was not set)
- Deploy to DataEngine using 'functions create'

## Usage

```
vastde functions build <name> [options]
```

## Examples

```bash
  # Build function with default settings (uses current directory)
  vastde functions build my-function

  # Build function from specific directory
  vastde functions build my-function --target ./my-function-code

  # Build with custom handler file name
  vastde functions build my-function \
    --target ./src \
    --handlers handler.py

  # Build with specific image tag
  vastde functions build image-processor --image-tag v1.2.3

  # Build with always pull policy for builder image
  vastde functions build my-function --pull-policy always

  # Build Python function with specific version
  vastde functions build my-function --version 3.11.*

  # Build and verify output in build.log
  vastde functions build data-transformer --target ./transformer

  # Build for production with specific tag and Python version
  vastde functions build ml-model \
    --target ./ml-service \
    --image-tag production-v2.0.0 \
    --version 3.12.*

	# Build and push the image to the container registry
  vastde functions build my-registry/my-function --image-tag v1.0.0 --push
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--clear-cache` | bool | Clear build cache (automatically done when version changes) |  |
| `-H`, `--handlers` | string | Handler file name | `main.py` |
| `-T`, `--image-tag` | string | Image tag to apply | `latest` |
| `-P`, `--pull-policy` | string | Builder image pull policy (never|always|ifnotpresent) | `ifnotpresent` |
| `--push` | bool | Push the built image to the container registry |  |
| `--save-build-log` | bool | Build with build log (default is false) |  |
| `-t`, `--target` | string | Function target folder (default is current directory) |  |
| `-V`, `--version` | string | Language version (e.g., Python: 3.12.*, 3.11.*; Go: 1.21) | `3.12.*` |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde functions](vastde_functions.md) - Manage VAST DataEngine functions


```


## FILE: dataengine-cli/docs/references/commands/vastde_functions_create.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_functions_create.md

```
---
title: vastde functions create
description: Create a VAST DataEngine function
---

# vastde functions create

Create a VAST DataEngine function

## Synopsis

Create a new function in VAST DataEngine from a container image.

This command registers a function with DataEngine, making it available for invocation by triggers
and pipelines. Creating a function requires:

1. Function name (--name): Unique identifier for the function
2. Container registry (--container-registry): Registry containing the function image
3. Artifact source (--artifact-source): Image name in the registry
4. Image tag (--image-tag): Specific version of the image to use

The function image must be built and pushed to the container registry before creating the function.
Use 'functions build' to create the image locally, then push it to your registry.

Optional configuration:
- --description: Human-readable description
- --tags: Custom labels for organization
- --architecture: Target architecture (e.g., amd64, arm64)
- --publish: Immediately publish the function for use
- --revision-alias: Friendly name for this revision
- --revision-description: Description of this revision

Functions can also be configured from a YAML file using --from-file, which supports all the
same options as command-line flags. Command-line flags take precedence over file values.

After creation, the function can be:
- Invoked directly using 'functions invoke'
- Triggered by events using 'triggers create'
- Integrated into pipelines using 'pipelines create'

## Usage

```
vastde functions create [options]
```

## Examples

```bash
  # Create a function with minimal required flags
  vastde functions create --name image-processor \
    --container-registry my-ecr-registry \
    --artifact-source vastdata/image-processor \
    --image-tag v1.0.0

  # Create function with description and tags for organization
  vastde functions create --name data-transformer \
    --container-registry my-ecr-registry \
    --artifact-source vastdata/transformer \
    --image-tag v2.1.0 \
    --description "Transforms JSON data to Parquet format" \
    --tags "production,etl,data-processing"

  # Create and immediately publish the function
  vastde functions create --name event-handler \
    --container-registry my-ecr-registry \
    --artifact-source vastdata/events \
    --image-tag latest \
    --publish

  # Create function with revision metadata
  vastde functions create --name ml-inference \
    --container-registry my-ecr-registry \
    --artifact-source vastdata/ml-model \
    --image-tag v1.5.2 \
    --revision-alias "stable" \
    --revision-description "Stable release with bug fixes"

  # Create function from YAML configuration file
  vastde functions create --from-file function-config.yaml

  # Create function with JSON output for automation scripts
  vastde functions create --name api-gateway \
    --container-registry my-ecr-registry \
    --artifact-source vastdata/gateway \
    --image-tag v3.0.0 \
    --output json

  # Dry-run to preview the API request without creating
  vastde functions create --name test-function \
    --container-registry my-ecr-registry \
    --artifact-source vastdata/test \
    --image-tag dev \
    --dry-run
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--architecture` | string | Architecture |  |
| `--artifact-source` | string | Artifact source (URL) |  |
| `--artifact-type` | string | Artifact type (supported: image) |  |
| `--container-registry` | string | Container registry name or VRN |  |
| `--default-revision-number` | int32 | Default revision number | `0` |
| `--description` | string | A description of the resource. (optional) |  |
| `-f`, `--from-file` | string | Path to function config file (yaml|json) |  |
| `--image-tag` | string | Image tag |  |
| `-n`, `--name` | string | A name for the resource |  |
| `--publish` | bool | Publish the function |  |
| `--revision-alias` | string | Revision alias |  |
| `--revision-description` | string | Revision description |  |
| `--tags` | stringSlice | Custom tags to apply. (optional) |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde functions](vastde_functions.md) - Manage VAST DataEngine functions


```


## FILE: dataengine-cli/docs/references/commands/vastde_functions_update.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_functions_update.md

```
---
title: vastde functions update
description: Update a VAST DataEngine function
---

# vastde functions update

Update a VAST DataEngine function

## Synopsis

Update configuration of an existing function.

This command modifies properties of a function identified by its GUID or name. You can update:

- Description (--description)
- Tags (--tags)
- Container image and registry (--artifact-source, --container-registry, --image-tag)
- Architecture (--architecture)
- Published status (--publish)
- Revision configuration (--revision-alias, --revision-description, --default-revision-number)
- Custom configuration (via YAML file)

Updates can be specified via command-line flags or a YAML configuration file (--from-file).
When using a file, command-line flags take precedence over file values.

Important notes:
- Function name cannot be changed after creation
- Updates create a new revision of the function
- The update operation uses a GET-modify-PUT pattern to preserve existing settings
- Only explicitly specified properties are modified

The update workflow:
1. Fetches current function configuration
2. Fetches latest revision details
3. Applies your specified changes
4. Creates a new revision with the updates
5. Optionally publishes the new revision

Use --publish to immediately make the updated function available for use. Without this flag,
the update creates a new revision but doesn't make it the default.

Common update scenarios:
- Deploy new image version: --image-tag v2.0 --publish
- Change description: --description "Updated description"
- Add tags: --tags environment:production,version:v2

## Usage

```
vastde functions update <GUID>|<name> [options]
```

## Examples

```bash
  # Update function description
  vastde functions update image-processor \
    --description "Enhanced image processing with ML capabilities"

  # Update function to use a new image tag
  vastde functions update image-processor \
    --image-tag v2.0.0

  # Update image tag and publish the new revision
  vastde functions update image-processor \
    --image-tag v2.1.0 \
    --publish

  # Update multiple properties at once
  vastde functions update data-transformer \
    --description "Production-ready data transformer" \
    --tags "production,etl,critical" \
    --image-tag v3.0.0 \
    --publish

  # Update using function GUID instead of name
  vastde functions update a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
    --image-tag v1.5.1 \
    --publish

  # Update with revision metadata
  vastde functions update ml-inference \
    --image-tag v2.0.0 \
    --revision-alias "stable-v2" \
    --revision-description "Major version upgrade with new features"

  # Update from YAML configuration file
  vastde functions update event-handler --from-file updated-config.yaml

  # Dry-run to preview changes without applying
  vastde functions update api-gateway \
    --image-tag v4.0.0 \
    --dry-run

  # Update and output result as JSON for automation
  vastde functions update processor \
    --image-tag v1.2.3 \
    --publish \
    --output json
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--architecture` | string | Architecture |  |
| `--artifact-source` | string | Artifact source (URL) |  |
| `--artifact-type` | string | Artifact type (supported: image) |  |
| `--container-registry` | string | Container registry name or VRN |  |
| `--default-revision-number` | int32 | Default revision number | `0` |
| `--description` | string | A description of the resource. (optional) |  |
| `-f`, `--from-file` | string | Path to function config file (yaml|json) |  |
| `--image-tag` | string | Image tag |  |
| `--publish` | bool | Publish the function |  |
| `--revision-alias` | string | Revision alias |  |
| `--revision-description` | string | Revision description |  |
| `--tags` | stringSlice | Custom tags to apply. (optional) |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde functions](vastde_functions.md) - Manage VAST DataEngine functions


```


## FILE: dataengine-cli/docs/references/commands/vastde_functions_localrun.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_functions_localrun.md

```
---
title: vastde functions localrun
description: Run a built VAST DataEngine function as a local container
---

# vastde functions localrun

Run a built VAST DataEngine function as a local container

## Synopsis

Run a built function container locally using Docker for testing and development.

This command starts a function container on your local machine, allowing you to test function
behavior before deploying to DataEngine. The function runs in Docker and exposes an HTTP endpoint
for receiving CloudEvents.

Prerequisites:
- Docker must be installed and running
- Function image must be built using 'functions build'

Runtime configuration:
- --port: Local port to expose (default: 8080)
- --config: Path to config.yaml with environment variables and secrets
- --loglevel: Function log level (DEBUG|INFO|WARNING|ERROR|CRITICAL)
- --image-tag: Image tag to run (default: latest)
- --detach: Run in background mode

The config.yaml file can define:
- envs: Environment variables passed to the function
- secrets: Secret data mounted as files in /secrets directory

After starting the function, use 'functions invoke' to send test events:
  vastde functions invoke --generate-event --url http://localhost:8080/

In foreground mode, logs appear in real-time. Press Ctrl+C to stop the function.
In detached mode (--detach), the container runs in the background.

Local testing workflow:
1. Build function: vastde functions build my-function
2. Run locally: vastde functions localrun my-function
3. Test: vastde functions invoke --generate-event
4. Iterate on code and rebuild as needed

## Usage

```
vastde functions localrun [name] [options]
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-c`, `--config` | string | Path to config.yaml file |  |
| `-d`, `--detach` | bool | Run the container in detached mode |  |
| `-T`, `--image-tag` | string | Image tag to run | `latest` |
| `-l`, `--loglevel` | string | Function log level (defaults to INFO) | `INFO` |
| `-p`, `--port` | int | Local port to bind to the function container | `8080` |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde functions](vastde_functions.md) - Manage VAST DataEngine functions


```


## FILE: dataengine-cli/docs/references/commands/vastde_functions_invoke.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_functions_invoke.md

```
---
title: vastde functions invoke
description: Send a cloudEvent to a local VAST DataEngine function
---

# vastde functions invoke

Send a cloudEvent to a local VAST DataEngine function

## Synopsis

Send a CloudEvent to a locally running or remote function for testing and invocation.

This command sends a CloudEvent to a function endpoint, triggering its execution. You can either:

1. Generate a test event automatically (--generate-event):
   Creates a default CloudEvent with standard VAST DataEngine format

2. Provide a custom event from a YAML file (--event):
   Load event data from a YAML file defining all CloudEvent fields

The CloudEvent format follows the CloudEvents specification and includes:
- id: Unique event identifier
- source: Event source URI
- type: Event type (e.g., vastdata.com:Element.ObjectCreated)
- data: Event payload (arbitrary JSON object)
- Additional metadata fields (time, subject, etc.)

Use --url to specify the function endpoint (defaults to http://localhost:8080/).
This is primarily used with 'functions localrun' for local testing, but can also invoke
remote function endpoints.

The command displays the function response and HTTP status code, making it easy to verify
function behavior during development and testing.

## Usage

```
vastde functions invoke [options]
```

## Examples

```bash
  # Generate and send a default test CloudEvent to local function
  vastde functions invoke --generate-event

  # Generate a CloudEvent with custom event type
  vastde functions invoke --generate-event \
    --event-type vastdata.com:Element.ObjectDeleted

  # Send a CloudEvent from YAML file to local function
  vastde functions invoke --event my-event.yaml

  # Invoke function at custom URL (e.g., different port or remote endpoint)
  vastde functions invoke --generate-event \
    --url http://localhost:9000/

  # Invoke remote deployed function endpoint
  vastde functions invoke --event test-event.yaml \
    --url https://my-function.example.com/invoke

  # Test function with realistic object created event
  vastde functions invoke --generate-event \
    --event-type vastdata.com:Element.ObjectCreated \
    --url http://localhost:8080/
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-e`, `--event` | string | Path to the CloudEvent YAML file |  |
| `-t`, `--event-type` | string | Type for generated CloudEvent | `vastdata.com:Element.ObjectCreated` |
| `-g`, `--generate-event` | bool | Generate a default CloudEvent automatically |  |
| `-u`, `--url` | string | URL of the locally running function | `http://localhost:8080/` |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde functions](vastde_functions.md) - Manage VAST DataEngine functions


```


## FILE: dataengine-cli/docs/references/commands/vastde_pipelines_create.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_pipelines_create.md

```
---
title: vastde pipelines create
description: Create a VAST DataEngine pipeline
---

# vastde pipelines create

Create a VAST DataEngine pipeline

## Synopsis

Create a VAST DataEngine pipeline

## Usage

```
vastde pipelines create [options]
```

## Examples

```bash
  # Create pipeline from YAML configuration file
  vastde pipelines create --config pipeline-config.yaml

  # Create pipeline from JSON file
  vastde pipelines create --config pipeline-config.json

  # Create pipeline from inline JSON string
  vastde pipelines create --config '{"name":"data-pipeline","steps":[...]}'

  # Create pipeline using @ syntax for file path
  vastde pipelines create --config @path/to/pipeline.yaml

  # Create pipeline with secrets from a file
  vastde pipelines create --config pipeline-config.yaml --secret-file secrets.yaml

  # Create pipeline with multiple secret files
  vastde pipelines create --config pipeline-config.yaml \
    --secret-file db-secrets.yaml \
    --secret-file api-secrets.yaml

  # Secret file format (secrets.yaml):
  #   name: my-database-credentials
  #   kubernetes_cluster_vrn: vast:dataengine:kubernetes-cluster:my-cluster
  #   namespace: default
  #   entries:
  #     - key: DB_HOST
  #       value: postgres.example.com
  #     - key: DB_USERNAME
  #       value: myuser
  #     - key: DB_PASSWORD
  #       value: super-secret-password

  # Create and immediately deploy the pipeline
  vastde pipelines create --config pipeline-config.yaml --deploy

  # Create pipeline with JSON output for automation
  vastde pipelines create --config pipeline-config.yaml --output json

  # Dry-run to preview the API request
  vastde pipelines create --config pipeline-config.yaml --dry-run
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--config` | string | Path to YAML/JSON config file, raw JSON string, or @path/to/file |  |
| `--deploy` | bool | Deploy the pipeline after creation |  |
| `--description` | string | A description of the resource. (optional) |  |
| `--name` | string | A name for the resource |  |
| `--secret-file` | stringSlice | Path to YAML/JSON file containing secrets to create and attach to pipeline (can be specified multiple times) |  |
| `--tags` | stringSlice | Custom tags to apply. (optional) |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde pipelines](vastde_pipelines.md) - Manage VAST DataEngine pipelines


```


## FILE: dataengine-cli/docs/references/commands/vastde_pipelines_deploy.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_pipelines_deploy.md

```
---
title: vastde pipelines deploy
description: Deploy a pipeline to kubernetes
---

# vastde pipelines deploy

Deploy a pipeline to kubernetes

## Synopsis

Deploy a pipeline to kubernetes

## Usage

```
vastde pipelines deploy <GUID>|<name>
```

## Examples

```bash
  # Deploy pipeline by name
  vastde pipelines deploy data-processing-pipeline

  # Deploy pipeline by GUID
  vastde pipelines deploy a1b2c3d4-e5f6-7890-abcd-ef1234567890

  # Dry-run deployment to preview the operation
  vastde pipelines deploy ml-inference-pipeline --dry-run
```

## Options

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde pipelines](vastde_pipelines.md) - Manage VAST DataEngine pipelines


```


## FILE: dataengine-cli/docs/references/commands/vastde_logs_tail.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_logs_tail.md

```
---
title: vastde logs tail
description: Tail logs for a VAST DataEngine pipeline
---

# vastde logs tail

Tail logs for a VAST DataEngine pipeline

## Synopsis

Stream live logs from a pipeline and its functions in real-time.

This command continuously streams new log entries as they are generated by pipeline executions.
Similar to 'tail -f' for files, it provides a live view of pipeline activity, making it ideal
for:

- Real-time monitoring during development
- Debugging active pipelines
- Observing function execution flow
- Tracking events as they occur

The command polls the telemetry system at regular intervals (default: 5 seconds) and displays
new log entries. Filtering options are the same as 'logs get':

- --function: Filter by specific function
- --severity: Filter by log level
- --scope: Filter by scope (user, runtime)
- --trace-id/--span-id: Filter by trace identifiers
- --interval: Polling interval (default: 5s)
- --limit: Initial number of historical logs to show (default: 100)

Press Ctrl+C to stop streaming. The tail command is particularly useful during pipeline
deployments and when testing function changes, as it provides immediate feedback on
execution behavior.

## Usage

```
vastde logs tail <pipeline name>|<pipeline GUID> [options]
```

## Examples

```bash
  # Tail logs in real-time for a pipeline
  vastde logs tail data-processing-pipeline

  # Tail logs for a specific function
  vastde logs tail my-pipeline --function image-processor

  # Tail only error logs
  vastde logs tail my-pipeline --severity ERROR

  # Tail logs with custom polling interval (10 seconds)
  vastde logs tail my-pipeline --interval 10s

  # Tail logs starting from a specific time
  vastde logs tail my-pipeline --start "2024-01-01T12:00:00Z"

  # Tail logs filtered by trace ID
  vastde logs tail my-pipeline --trace-id abc123-def456

  # Tail logs with limit on entries per poll
  vastde logs tail my-pipeline --limit 50 --interval 5s
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-e`, `--end` | string | Filter logs until this end time (e.g. '-5m', '2025-04-21T12:00:00Z') |  |
| `-f`, `--function` | string | Filter logs by function name or GUID |  |
| `-i`, `--interval` | duration | Polling interval for new logs (default 5s) | `5s` |
| `-l`, `--limit` | int32 | Maximum number of log records to return per poll | `100` |
| `--scope` | string | Filter logs by scope (user, runtime) | `user` |
| `--severity` | string | Filter logs by severity (DEBUG, INFO, WARN, ERROR, CRITICAL) |  |
| `-s`, `--since` | string | Filter logs since this time ago (e.g. '10m', '2h', '2025-04-21T10:00:00Z') | `0s` |
| `--span-id` | string | Filter logs by span ID |  |
| `--trace-id` | string | Filter logs by trace ID |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde logs](vastde_logs.md) - View VAST DataEngine logs


```


## FILE: dataengine-cli/docs/references/commands/vastde_logs_get.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_logs_get.md

```
---
title: vastde logs get
description: Show logs for a VAST DataEngine pipeline
---

# vastde logs get

Show logs for a VAST DataEngine pipeline

## Synopsis

Retrieve historical logs for a specific pipeline and its functions.

This command queries the DataEngine telemetry system to fetch execution logs for a pipeline
identified by its name or GUID. Logs provide detailed information about pipeline and function
execution, including:

- Function invocations and outputs
- Runtime errors and exceptions
- Custom log messages from function code
- System events and status messages

Filtering options:
- --function: Filter by specific function within the pipeline
- --since: Start time for log range (default: 5m ago)
- --end: End time for log range
- --severity: Filter by log level (TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL)
- --scope: Filter by scope (user, runtime)
- --trace-id/--span-id: Filter by distributed trace identifiers
- --limit: Maximum number of log entries (default: 100)
- --order-by: Sort order (asc, desc)

Time formats support relative durations (5m, 2h, 1d) or absolute timestamps.
Logs are essential for debugging pipeline issues, monitoring execution, and understanding
system behavior.

## Usage

```
vastde logs get <pipeline name>|<pipeline GUID> [options]
```

## Examples

```bash
  # Get logs for a pipeline
  vastde logs get data-processing-pipeline

  # Get logs filtered by severity level
  vastde logs get my-pipeline --severity ERROR

  # Get logs for a specific function in the pipeline
  vastde logs get my-pipeline --function image-processor

  # Get logs within a time range
  vastde logs get my-pipeline \
    --start "2024-01-01T00:00:00Z" \
    --end "2024-01-02T00:00:00Z"

  # Get logs with pagination
  vastde logs get my-pipeline --limit 100

  # Get logs filtered by trace ID for debugging
  vastde logs get my-pipeline --trace-id abc123-def456

  # Get logs as JSON for processing
  vastde logs get my-pipeline --output json

  # Get recent error logs sorted by time
  vastde logs get production-pipeline \
    --severity ERROR \
    --order-by timestamp \
    --limit 50
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-e`, `--end` | string | Filter logs until this end time (e.g. '5m', '2025-04-21T12:00:00Z') |  |
| `-f`, `--function` | string | Filter logs by function name or GUID |  |
| `-l`, `--limit` | int32 | Maximum number of log records to return | `100` |
| `--order-by` | string | Sort order for logs (asc, desc) |  |
| `--scope` | string | Filter logs by scope (user, runtime) |  |
| `--severity` | string | Filter logs by severity (TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL) |  |
| `-s`, `--since` | string | Filter logs since this time ago (e.g. '10m', '2h', '2025-04-21T10:00:00Z'). Default is 5m. | `5m` |
| `--span-id` | string | Filter logs by span ID |  |
| `--trace-id` | string | Filter logs by trace ID |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde logs](vastde_logs.md) - View VAST DataEngine logs


```


## FILE: dataengine-cli/docs/references/commands/vastde_traces_list.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_traces_list.md

```
---
title: vastde traces list
description: List VAST DataEngine traces by filter
---

# vastde traces list

List VAST DataEngine traces by filter

## Synopsis

List VAST DataEngine traces by filter

## Usage

```
vastde traces list <pipeline name>|<pipeline GUID> [options]
```

## Examples

```bash
  # List traces for a pipeline
  vastde traces list data-processing-pipeline

  # List traces within a time range
  vastde traces list my-pipeline \
    --since "2024-01-01T00:00:00Z" \
    --end "2024-01-02T00:00:00Z"

  # List traces filtered by event type
  vastde traces list my-pipeline --event-type vastdata.com:Element.ObjectCreated

  # List traces filtered by status
  vastde traces list my-pipeline --status SUCCESS

  # List traces with pagination
  vastde traces list my-pipeline --limit 50

  # List traces sorted by time
  vastde traces list my-pipeline --order-by start_time

  # List traces as JSON for processing
  vastde traces list my-pipeline --output json

  # List recent traces (last 1 hour)
  vastde traces list my-pipeline --since 1h
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `-e`, `--end` | string | Filter traces until this duration ago (e.g. '5m', '2025-04-21T12:00:00Z') |  |
| `-i`, `--event-id` | string | Filter traces by event ID |  |
| `-t`, `--event-type` | string | Filter traces by event type |  |
| `-l`, `--limit` | int32 | Maximum number of traces to return | `20` |
| `--order-by` | string | Sort order for traces (asc, desc) |  |
| `-s`, `--since` | string | Filter traces since this duration ago (e.g. '10m', '2h', '2025-04-21T10:00:00Z') | `1m` |
| `--status` | string | Filter traces by status (e.g. 'UNSET', 'OK', 'ERROR') |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde traces](vastde_traces.md) - View VAST DataEngine traces


```


## FILE: dataengine-cli/docs/references/commands/vastde_traces_get.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_traces_get.md

```
---
title: vastde traces get
description: Get VAST DataEngine trace details
---

# vastde traces get

Get VAST DataEngine trace details

## Synopsis

Get VAST DataEngine trace details

## Usage

```
vastde traces get <trace-id>
```

## Examples

```bash
  # Get trace details by trace ID
  vastde traces get abc123-def456-789xyz

  # Get trace details as JSON
  vastde traces get abc123-def456-789xyz --output json

  # Get trace details as YAML
  vastde traces get abc123-def456-789xyz --output yaml
```

## Options

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde traces](vastde_traces.md) - View VAST DataEngine traces


```


## FILE: dataengine-cli/docs/references/commands/vastde_topics_list.md
Source: https://github.com/vast-data/dataengine-cli/blob/main/docs/references/commands/vastde_topics_list.md

```
---
title: vastde topics list
description: List VAST DataEngine topics
---

# vastde topics list

List VAST DataEngine topics

## Synopsis

List VAST DataEngine topics

## Usage

```
vastde topics list [options]
```

## Examples

```bash
  # List topics in a database (database name required)
  vastde topics list --database-name kafka-view1

  # List topics with pagination
  vastde topics list --database-name kafka-db --limit 10

  # List topics filtered by name
  vastde topics list --database-name kafka-db --name event-stream

  # List topics as JSON
  vastde topics list --database-name kafka-db --output json
```

## Options

### Command-specific options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--database-name` | string | Database name (required) |  |
| `-l`, `--limit` | int32 | Maximum number of items to display (0 = no limit) | `0` |
| `-n`, `--name` | string | Filter by topic name |  |

### Global options

| Flag | Type | Description | Default |
|------|------|-------------|----------|
| `--dry-run` | bool | Simulate the operation without making actual changes to the system |  |
| `-o`, `--output` | string | Output format: `json`, `yaml`, `human` | `human` |
| `--silent` | bool | Suppress UI outputs, such as spinner and success messages |  |
| `-v`, `--verbose` | int | Verbosity level (0-9): 0=standard, 1=verbose, 2=detailed, 3=extended, 4=debug, 5=trace | `0` |

## See Also

- [vastde topics](vastde_topics.md) - Manage VAST DataEngine topics


```
