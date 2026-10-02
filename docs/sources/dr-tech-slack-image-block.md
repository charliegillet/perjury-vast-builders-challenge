reference

[Skip to main content](https://docs.slack.dev/reference/block-kit/blocks/image-block/#__docusaurus_skipToContent_fallback)

Copy as markdown

On this page

### Displays an image.

## Facts

**Available in Surfaces**

[`Modals`](https://docs.slack.dev/surfaces/modals)

[`Messages`](https://docs.slack.dev/messaging)

[`Home tabs`](https://docs.slack.dev/surfaces/app-home)

## Fields [​](https://docs.slack.dev/reference/block-kit/blocks/image-block/\#fields "Direct link to Fields")

| Field | Type | Description | Required? |
| --- | --- | --- | --- |
| `type` | String | The type of block. For an image block, `type` is always `image`. | Required |
| `alt_text` | String | A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters. | Required |
| `image_url` | String | The URL for a publicly hosted image. You must provide either an `image_url` or `slack_file`. Maximum length for this field is 3000 characters. | Optional |
| `slack_file` | Object | A [Slack image file object](https://docs.slack.dev/reference/block-kit/composition-objects/slack-file-object) that defines the source of the image. | Optional |
| `title` | Object | An optional title for the image in the form of a [text object](https://docs.slack.dev/reference/block-kit/composition-objects/text-object) that can only be of `type: plain_text`. Maximum length for the `text` in this field is 2000 characters. | Optional |
| `block_id` | String | A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`. | Optional |

## Usage info [​](https://docs.slack.dev/reference/block-kit/blocks/image-block/\#usage-info "Direct link to Usage info")

An image block, designed to make those cat photos really pop. Supported file types include `png`, `jpg`, `jpeg`, and `gif`.

## Examples [​](https://docs.slack.dev/reference/block-kit/blocks/image-block/\#example "Direct link to Examples")

The following three examples show different ways to get the following result:

![An example of an image block](https://docs.slack.dev/assets/images/bk_image_example-b5993c61154165d8f3fe45b9d50d3c46.png)

**Example 1**: An image block using `image_url`:

- JSON
- Python Slack SDK
- Node Slack SDK
- Java Slack SDK

```json
{

    "blocks": [\
\
        {\
\
            "type": "image",\
\
            "title": {\
\
                "type": "plain_text",\
\
                "text": "Please enjoy this photo of a kitten"\
\
            },\
\
            "block_id": "image4",\
\
            "image_url": "http://placekitten.com/500/500",\
\
            "alt_text": "An incredibly cute kitten."\
\
        }\
\
    ]

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22image%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Please%20enjoy%20this%20photo%20of%20a%20kitten%22%7D,%22block_id%22:%22image4%22,%22image_url%22:%22https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg%22,%22alt_text%22:%22An%20incredibly%20cute%20kitten.%22%7D%5D%7D)

block-kit/src/blocks/image.py

```py
def example01() -> ImageBlock:

    """

    Displays an image.

    https://docs.slack.dev/reference/block-kit/blocks/image-block/

    An image block using image_url.

    """

    block = ImageBlock(

        title=PlainTextObject(text="Please enjoy this photo of a kitten"),

        block_id="image4",

        image_url="http://placekitten.com/500/500",

        alt_text="An incredibly cute kitten.",

    )

    return block
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/image.py#L5-L18)

block-kit/src/blocks/image.js

```js
export function example01() {

  /**

   * @type {import('@slack/types').ImageBlock}

   */

  const block = {

    type: "image",

    title: {

      type: "plain_text",

      text: "Please enjoy this photo of a kitten",

    },

    block_id: "image4",

    image_url: "http://placekitten.com/500/500",

    alt_text: "An incredibly cute kitten.",

  };

  return block;

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/image.js#L12-L27)

block-kit/src/main/java/blocks/Image.java

```java
public static ImageBlock example01() {

    ImageBlock block = Blocks.image(i -> i.title(BlockCompositions.plainText("Please enjoy this photo of a kitten"))

            .blockId("image4")

            .imageUrl("http://placekitten.com/500/500")

            .altText("An incredibly cute kitten."));

    return block;

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Image.java#L16-L22)

* * *

**Example 2**: An image block using `slack_file` with a `url`:

- JSON
- Python Slack SDK
- Node Slack SDK
- Java Slack SDK

```json
{

    "blocks": [\
\
        {\
\
            "type": "image",\
\
            "title": {\
\
                "type": "plain_text",\
\
                "text": "Please enjoy this photo of a kitten"\
\
            },\
\
            "block_id": "image4",\
\
            "slack_file": {\
\
                "url": "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"\
\
            },\
\
            "alt_text": "An incredibly cute kitten."\
\
        }\
\
    ]

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22image%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Please%20enjoy%20this%20photo%20of%20a%20kitten%22%7D,%22block_id%22:%22image4%22,%22slack_file%22:%7B%22url%22:%22https://files.slack.com/files-pri/T0123456-F0123456/xyz.png%22%7D,%22alt_text%22:%22An%20incredibly%20cute%20kitten.%22%7D%5D%7D)

block-kit/src/blocks/image.py

```py
def example02() -> ImageBlock:

    """

    An image block using slack_file with a url.

    """

    block = ImageBlock(

        title=PlainTextObject(text="Please enjoy this photo of a kitten"),

        block_id="image4",

        slack_file=SlackFile(

            url="https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"

        ),

        alt_text="An incredibly cute kitten.",

    )

    return block
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/image.py#L21-L33)

block-kit/src/blocks/image.js

```js
export function example02() {

  /**

   * @type {import('@slack/types').ImageBlock}

   */

  const block = {

    type: "image",

    title: {

      type: "plain_text",

      text: "Please enjoy this photo of a kitten",

    },

    block_id: "image4",

    slack_file: {

      url: "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png",

    },

    alt_text: "An incredibly cute kitten.",

  };

  return block;

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/image.js#L34-L51)

block-kit/src/main/java/blocks/Image.java

```java
public static ImageBlock example02() {

    ImageBlock block = Blocks.image(i -> i.title(BlockCompositions.plainText("Please enjoy this photo of a kitten"))

            .blockId("image4")

            .slackFile(SlackFileObject.builder()

                    .url("https://files.slack.com/files-pri/T0123456-F0123456/xyz.png")

                    .build())

            .altText("An incredibly cute kitten."));

    return block;

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Image.java#L27-L35)

* * *

**Example 3**: An image block using `slack_file` with a `id`:

- JSON
- Python Slack SDK
- Node Slack SDK
- Java Slack SDK

```json
{

    "blocks": [\
\
        {\
\
            "type": "image",\
\
            "title": {\
\
                "type": "plain_text",\
\
                "text": "Please enjoy this photo of a kitten"\
\
            },\
\
            "block_id": "image4",\
\
            "slack_file": {\
\
                "id": "F0123456"\
\
            },\
\
            "alt_text": "An incredibly cute kitten."\
\
        }\
\
    ]

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22image%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Please%20enjoy%20this%20photo%20of%20a%20kitten%22%7D,%22block_id%22:%22image4%22,%22slack_file%22:%7B%22id%22:%22F0123456%22%7D,%22alt_text%22:%22An%20incredibly%20cute%20kitten.%22%7D%5D%7D)

block-kit/src/blocks/image.py

```py
def example03() -> ImageBlock:

    """

    An image block using slack_file with an id.

    """

    block = ImageBlock(

        title=PlainTextObject(text="Please enjoy this photo of a kitten"),

        block_id="image4",

        slack_file=SlackFile(id="F0123456"),

        alt_text="An incredibly cute kitten.",

    )

    return block
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/image.py#L36-L46)

block-kit/src/blocks/image.js

```js
export function example03() {

  /**

   * @type {import('@slack/types').ImageBlock}

   */

  const block = {

    type: "image",

    title: {

      type: "plain_text",

      text: "Please enjoy this photo of a kitten",

    },

    block_id: "image4",

    slack_file: {

      id: "F0123456",

    },

    alt_text: "An incredibly cute kitten.",

  };

  return block;

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/image.js#L58-L75)

block-kit/src/main/java/blocks/Image.java

```java
public static ImageBlock example03() {

    ImageBlock block = Blocks.image(i -> i.title(BlockCompositions.plainText("Please enjoy this photo of a kitten"))

            .blockId("image4")

            .slackFile(SlackFileObject.builder().id("F0123456").build())

            .altText("An incredibly cute kitten."));

    return block;

}
```

![](https://docs.slack.dev/img/devhub-icons/copy.svg)

[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Image.java#L40-L46)

Copy as markdown

- [Fields](https://docs.slack.dev/reference/block-kit/blocks/image-block/#fields)
- [Usage info](https://docs.slack.dev/reference/block-kit/blocks/image-block/#usage-info)
- [Examples](https://docs.slack.dev/reference/block-kit/blocks/image-block/#example)

 [Search](https://docs.slack.dev/search)