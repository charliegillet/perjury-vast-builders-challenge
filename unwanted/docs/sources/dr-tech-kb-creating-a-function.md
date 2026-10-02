> ## Documentation Index
>
> Fetch the complete documentation index at: [https://kb.vastdata.com/llms.txt](https://kb.vastdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

# Creating a DataEngine Function

- Updated on Feb 12, 2026
- Published on Jan 25, 2026

- 4 minute(s) read
- Focus
- Listen

Follow

Copy pageCopy as Markdown for LLMsView as MarkdownView the page as plain text

Open in ChatGPTAsk ChatGPT about this pageOpen in ClaudeAsk Claude about this page

Article summary[Prev](https://kb.vastdata.com/documentation/docs/creating-a-trigger "Creating a Trigger")[Next](https://kb.vastdata.com/documentation/docs/building-and-deploying-a-pipeline-on-vast-dataengine "Building and Deploying a Pipeline on VAST DataEngine")

## Overview

Any function that you want to be able to call and deploy within a DataEngine pipeline must first be packaged as an image and stored on one of the container registries that is connected to the DataEngine instance that you are working with.

VAST provides a capability, through the DataEngine CLI, to package your function code as an image ready to store on a container registry. You then push that image to your container registry. You need to obtain the image tag from the container registry for the specific image.

For each image stored on the container registry, you can create a _function_ resource within DataEngine. A function, in DataEngine terms, is a resource that points to an image of a function stored on a container registry. A function can be built into a DataEngine _pipeline_ and deployed as part of that pipeline. Within a pipeline, a function can be invoked by a trigger or by another function. Each function deployment within a pipeline has a configuration that determines the execution environment provided to the function in that instance.

When you want to update the code for a given function, you can update the code, store the updated image on the container registry and create a new revision of the same function with a different image tag. When you deploy a function in a pipeline, you can choose to deploy a specific revision or the current (latest) revision. When you edit a pipeline, you can switch a function to a different revision.

## Workflow

1. [Prepare the Function Image in the Container Registry](https://kb.vastdata.com/documentation/docs/creating-a-dataengine-function#prepare-the-function-image-in-the-container-registry "Prepare the Function Image in the Container Registry")

2. [Create the Function Resource](https://kb.vastdata.com/documentation/docs/creating-a-dataengine-function#create-the-function-resource "Create the Function Resource")


## Prepare the Function Image in the Container Registry

1. Install the [VAST DataEngine CLI](https://kb.vastdata.com/documentation/docs/installing-the-vast-dataengine-cli "Installing the VAST DataEngine CLI").

2. Run the `vastde functions init` command to create a scaffold for your function.

For example:

Plain text

```plaintext
    vastde functions init python-pip my_first_function -t ~/functions/
```





Plain text



Copy





The output is a directory structure need for implementing your function.

For example:

Plain text

```plaintext
~/functions/my-first_function/
├── Aptfile          # OS dependencies
├── README.md        # Project documentation
├── customDeps       # custom python libraries
├── main.py          # Handler functions
└── requirements.txt # Python dependencies

0 directories, 5 files
```





Plain text



Copy





The files in the directory structure are created empty.

3. Write your code in the files provided to implement the function. See the _VAST DataEngine Runtime SDK Guide_.

The following is sample `main.py` content:

Plain text

```plaintext
from sharedlib.module import lib

def init(ctx):
       lib.shared_func()

def handler(ctx, event):
       return "Hello World"
```





Plain text



Copy

4. Run the `vastde functions build` command to package the function as an image and to tag the image. For example:

Plain text

```plaintext
FUNC_NAME="function"
FUNC_PATH="example/path/to/function"
vastde functions build $FUNC_NAME -target $FUNC_PATH --image-tag my-function
```





Plain text



Copy

5. Test the function locally:



1. Run the now built function as a local container: `vastde functions localrun`

2. Send a cloud event to the locally running function for testing and invocation: `vastde functions invoke`

3. Iterate on code and rebuild as needed.


6. Tag the local image with a tag of your choice:

Plain text

```plaintext
docker tag ${FUNC_NAME}:latest CONTAINER_REGISTRY/ARTIFACT_SOURCE:TAG
```





Plain text



Copy





Substitute the following:



   - `CONTAINER_REGISTRY`. The URL of a container registry to which you have privileges to push images. The container registry must also have a connection configured on the tenant for DataEngine.  This connection is configured on the VAST Cluster tenant by an administrator.

   - `ARTIFACT_SOURCE`. A path on the container registry where you intend to push the image.

   - `TAG`. The text that you want to tag the image with (such as the name of the function).


7. Push the image to the container registry:

Plain text

```plaintext
docker push CONTAINER_REGISTRY/ARTIFACT_SOURCE:${FUNC_NAME}
```





Plain text



Copy


## Create the Function Resource

1. From the left navigation menu, select Manage Elements (![ManageElementsMenuIcon.png](https://cdn.document360.io/726fb2d3-253d-48b7-a67b-bcf45100fafc/Images/Documentation/img-b3d2ad07e044da6d7a37d19d29da0a16.png?sv=2026-02-06&spr=https&st=2026-10-02T00%3A05%3A21Z&se=2026-10-02T00%3A19%3A21Z&sr=c&sp=r&sig=oHtc1vBfD84tlSiG5qrIeer18Y%2BMA8eth2mvNIWZBus%3D)) and then Functions.

2. Click Create New Function.

3. Complete the fields:



|     |     |
| --- | --- |
| Function Name | Enter a name for the function. |
| Description | Enter a description for the function. |
| Revision Alias | Enter an alias for the initial revision of the function. |
| Revision No. | This field is a display field. It displays the revision number, which is initially 1. The number increments on every edit of the function. |
| Revision Description | Enter a description for the revision. |
| Container Registry | From the dropdown, select the container registry where the image of the function is stored. |
| Artifact Source | Enter the path to the container image. |
| Image Tag | Enter the image tag attached to the relevant version of the container image. |
| Full image path | This is the full path to the image. It is formed automatically from the container registry, artifact source and image tag values that you supply. |

4. Click Create Function.

The function is created and is listed in the Functions page.


Was this article helpful? (Provide Feedback)

Yes  No

Previous article

Creating a Trigger

Next article

Building and Deploying a Pipeline on VAST DataEngine

Related articles

- [Creating a DataEngine Function](https://kb.vastdata.com/documentation/docs/creating-a-dataengine-function-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine User Guide

- [Getting Started](https://kb.vastdata.com/documentation/docs/getting-started-dataengine-runtime-sdk-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine Runtime SDK Developer’s Guide

- [Overview of VAST DataEngine](https://kb.vastdata.com/documentation/docs/overview-of-vast-dataengine-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine User Guide