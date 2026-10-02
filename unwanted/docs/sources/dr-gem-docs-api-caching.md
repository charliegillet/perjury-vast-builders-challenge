[Skip to main content](https://ai.google.dev/api/caching#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/api/caching)
- [Deutsch](https://ai.google.dev/api/caching?hl=de)
- [Español – América Latina](https://ai.google.dev/api/caching?hl=es-419)
- [Français](https://ai.google.dev/api/caching?hl=fr)
- [Indonesia](https://ai.google.dev/api/caching?hl=id)
- [Italiano](https://ai.google.dev/api/caching?hl=it)
- [Polski](https://ai.google.dev/api/caching?hl=pl)
- [Português – Brasil](https://ai.google.dev/api/caching?hl=pt-br)
- [Shqip](https://ai.google.dev/api/caching?hl=sq)
- [Tiếng Việt](https://ai.google.dev/api/caching?hl=vi)
- [Türkçe](https://ai.google.dev/api/caching?hl=tr)
- [Русский](https://ai.google.dev/api/caching?hl=ru)
- [עברית](https://ai.google.dev/api/caching?hl=he)
- [العربيّة](https://ai.google.dev/api/caching?hl=ar)
- [فارسی](https://ai.google.dev/api/caching?hl=fa)
- [हिंदी](https://ai.google.dev/api/caching?hl=hi)
- [বাংলা](https://ai.google.dev/api/caching?hl=bn)
- [ภาษาไทย](https://ai.google.dev/api/caching?hl=th)
- [中文 – 简体](https://ai.google.dev/api/caching?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/api/caching?hl=zh-tw)
- [日本語](https://ai.google.dev/api/caching?hl=ja)
- [한국어](https://ai.google.dev/api/caching?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)Sign in

- On this page
- [Method: cachedContents.create](https://ai.google.dev/api/caching#method:-cachedcontents.create)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint)
  - [Request body](https://ai.google.dev/api/caching#request-body)
  - [Example request](https://ai.google.dev/api/caching#example-request)
  - [Response body](https://ai.google.dev/api/caching#response-body)
- [Method: cachedContents.list](https://ai.google.dev/api/caching#method:-cachedcontents.list)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_1)
  - [Query parameters](https://ai.google.dev/api/caching#query-parameters)
  - [Request body](https://ai.google.dev/api/caching#request-body_1)
  - [Response body](https://ai.google.dev/api/caching#response-body_1)
- [Method: cachedContents.get](https://ai.google.dev/api/caching#method:-cachedcontents.get)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_2)
  - [Path parameters](https://ai.google.dev/api/caching#path-parameters)
  - [Request body](https://ai.google.dev/api/caching#request-body_2)
  - [Example request](https://ai.google.dev/api/caching#example-request_1)
  - [Response body](https://ai.google.dev/api/caching#response-body_2)
- [Method: cachedContents.patch](https://ai.google.dev/api/caching#method:-cachedcontents.patch)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_3)
  - [Path parameters](https://ai.google.dev/api/caching#path-parameters_1)
  - [Query parameters](https://ai.google.dev/api/caching#query-parameters_1)
  - [Request body](https://ai.google.dev/api/caching#request-body_3)
  - [Example request](https://ai.google.dev/api/caching#example-request_2)
  - [Response body](https://ai.google.dev/api/caching#response-body_3)
- [Method: cachedContents.delete](https://ai.google.dev/api/caching#method:-cachedcontents.delete)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_4)
  - [Path parameters](https://ai.google.dev/api/caching#path-parameters_2)
  - [Request body](https://ai.google.dev/api/caching#request-body_4)
  - [Example request](https://ai.google.dev/api/caching#example-request_3)
  - [Response body](https://ai.google.dev/api/caching#response-body_4)
- [REST Resource: cachedContents](https://ai.google.dev/api/caching#rest-resource:-cachedcontents)
- [Resource: CachedContent](https://ai.google.dev/api/caching#CachedContent)
- [ToolConfig](https://ai.google.dev/api/caching#ToolConfig)
- [FunctionCallingConfig](https://ai.google.dev/api/caching#FunctionCallingConfig)
- [Mode](https://ai.google.dev/api/caching#Mode)
- [RetrievalConfig](https://ai.google.dev/api/caching#RetrievalConfig)
- [LatLng](https://ai.google.dev/api/caching#LatLng)
- [UsageMetadata](https://ai.google.dev/api/caching#UsageMetadata)

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [API reference](https://ai.google.dev/api)



 Send feedback



# Caching

- On this page
- [Method: cachedContents.create](https://ai.google.dev/api/caching#method:-cachedcontents.create)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint)
  - [Request body](https://ai.google.dev/api/caching#request-body)
  - [Example request](https://ai.google.dev/api/caching#example-request)
  - [Response body](https://ai.google.dev/api/caching#response-body)
- [Method: cachedContents.list](https://ai.google.dev/api/caching#method:-cachedcontents.list)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_1)
  - [Query parameters](https://ai.google.dev/api/caching#query-parameters)
  - [Request body](https://ai.google.dev/api/caching#request-body_1)
  - [Response body](https://ai.google.dev/api/caching#response-body_1)
- [Method: cachedContents.get](https://ai.google.dev/api/caching#method:-cachedcontents.get)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_2)
  - [Path parameters](https://ai.google.dev/api/caching#path-parameters)
  - [Request body](https://ai.google.dev/api/caching#request-body_2)
  - [Example request](https://ai.google.dev/api/caching#example-request_1)
  - [Response body](https://ai.google.dev/api/caching#response-body_2)
- [Method: cachedContents.patch](https://ai.google.dev/api/caching#method:-cachedcontents.patch)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_3)
  - [Path parameters](https://ai.google.dev/api/caching#path-parameters_1)
  - [Query parameters](https://ai.google.dev/api/caching#query-parameters_1)
  - [Request body](https://ai.google.dev/api/caching#request-body_3)
  - [Example request](https://ai.google.dev/api/caching#example-request_2)
  - [Response body](https://ai.google.dev/api/caching#response-body_3)
- [Method: cachedContents.delete](https://ai.google.dev/api/caching#method:-cachedcontents.delete)
  - [Endpoint](https://ai.google.dev/api/caching#endpoint_4)
  - [Path parameters](https://ai.google.dev/api/caching#path-parameters_2)
  - [Request body](https://ai.google.dev/api/caching#request-body_4)
  - [Example request](https://ai.google.dev/api/caching#example-request_3)
  - [Response body](https://ai.google.dev/api/caching#response-body_4)
- [REST Resource: cachedContents](https://ai.google.dev/api/caching#rest-resource:-cachedcontents)
- [Resource: CachedContent](https://ai.google.dev/api/caching#CachedContent)
- [ToolConfig](https://ai.google.dev/api/caching#ToolConfig)
- [FunctionCallingConfig](https://ai.google.dev/api/caching#FunctionCallingConfig)
- [Mode](https://ai.google.dev/api/caching#Mode)
- [RetrievalConfig](https://ai.google.dev/api/caching#RetrievalConfig)
- [LatLng](https://ai.google.dev/api/caching#LatLng)
- [UsageMetadata](https://ai.google.dev/api/caching#UsageMetadata)

Context caching allows you to save and reuse precomputed input tokens that you wish to use repeatedly, for example when asking different questions about the same media file. This can lead to cost and speed savings, depending on the usage. For a detailed introduction, see the [Context caching](https://ai.google.dev/gemini-api/docs/caching) guide.

## Method: cachedContents.create

- [Endpoint](https://ai.google.dev/api/caching#body.HTTP_TEMPLATE)
- [Request body](https://ai.google.dev/api/caching#body.request_body)
- [Response body](https://ai.google.dev/api/caching#body.response_body)
- [Authorization scopes](https://ai.google.dev/api/caching#body.aspect)
- [Example request](https://ai.google.dev/api/caching#body.codeSnippets)
  - [Basic](https://ai.google.dev/api/caching#body.codeSnippets.group)
  - [From name](https://ai.google.dev/api/caching#body.codeSnippets.group_1)
  - [From chat](https://ai.google.dev/api/caching#body.codeSnippets.group_2)

Creates CachedContent resource.

### Endpoint

post
`https://generativelanguage.googleapis.com/v1beta/cachedContents`

### Request body

The request body contains an instance of `CachedContent`.

Fields

`contents[]``object (Content)`

Optional. Input only. Immutable. The content to cache.

`tools[]``object (Tool)`

Optional. Input only. Immutable. A list of `Tools` the model may use to generate the next response

`expiration``Union type`

Specifies when this resource will expire. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`expireTime``string (Timestamp format)`

Timestamp in UTC of when this resource is considered expired. This is _always_ provided on output, regardless of what was sent on input.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.

`ttl``string (Duration format)`

Input only. New TTL for this resource, input only.

A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.

End of mutually exclusive fields.

`displayName``string`

Optional. Immutable. The user-generated meaningful display name of the cached content. Maximum 128 Unicode characters.

`model``string`

Required. Immutable. The name of the `Model` to use for cached content Format: `models/{model}`

`systemInstruction``object (Content)`

Optional. Input only. Immutable. Developer set system instruction. Currently text only.

`toolConfig``object (ToolConfig)`

Optional. Input only. Immutable. Tool config. This config is shared for all tools.

### Example request

[Basic](https://ai.google.dev/api/caching#basic)[From name](https://ai.google.dev/api/caching#from-name)[From chat](https://ai.google.dev/api/caching#from-chat)More

[Python](https://ai.google.dev/api/caching#python)[Node.js](https://ai.google.dev/api/caching#node.js)[Go](https://ai.google.dev/api/caching#go)[Shell](https://ai.google.dev/api/caching#shell)More

```
from google import genai
from google.genai import types

client = genai.Client()
document = client.files.upload(file=media / "a11.txt")
model_name = "gemini-3.8-flash"

cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
        contents=[document],
        system_instruction="You are an expert analyzing transcripts.",
    ),
)
print(cache)

response = client.models.generate_content(
    model=model_name,
    contents="Please summarize this transcript",
    config=types.GenerateContentConfig(cached_content=cache.name),
)
print(response.text)cache.py
```

```
// Make sure to include the following import:
// import {GoogleGenAI} from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

const contents = [\
  createUserContent(createPartFromUri(document.uri, document.mimeType)),\
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
console.log("Cache created:", cache);

const response = await ai.models.generateContent({
  model: modelName,
  contents: "Please summarize this transcript",
  config: { cachedContent: cache.name },
});
console.log("Response text:", response.text);cache.js
```

```
ctx := context.Background()
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:  os.Getenv("GEMINI_API_KEY"),
	Backend: genai.BackendGeminiAPI,
})
if err != nil {
	log.Fatal(err)
}

modelName := "gemini-3.8-flash"
document, err := client.Files.UploadFromPath(
	ctx,
	filepath.Join(getMedia(), "a11.txt"),
	&genai.UploadFileConfig{
		MIMEType : "text/plain",
	},
)
if err != nil {
	log.Fatal(err)
}
parts := []*genai.Part{
	genai.NewPartFromURI(document.URI, document.MIMEType),
}
contents := []*genai.Content{
	genai.NewContentFromParts(parts, genai.RoleUser),
}
cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
	Contents: contents,
	SystemInstruction: genai.NewContentFromText(
		"You are an expert analyzing transcripts.", genai.RoleUser,
	),
})
if err != nil {
	log.Fatal(err)
}
fmt.Println("Cache created:")
fmt.Println(cache)

// Use the cache for generating content.
response, err := client.Models.GenerateContent(
	ctx,
	modelName,
	genai.Text("Please summarize this transcript"),
	&genai.GenerateContentConfig{
		CachedContent: cache.Name,
	},
)
if err != nil {
	log.Fatal(err)
}
printResponse(response)cache.go
```

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-1.5-flash-001",
  "contents":[\
    {\
      "parts":[\
        {\
          "inline_data": {\
            "mime_type":"text/plain",\
            "data": "'$(base64 $B64FLAGS a11.txt)'"\
          }\
        }\
      ],\
    "role": "user"\
    }\
  ],
  "systemInstruction": {
    "parts": [\
      {\
        "text": "You are an expert at analyzing transcripts."\
      }\
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -d @request.json \
 > cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-001:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [\
        {\
          "parts":[{\
            "text": "Please summarize this transcript"\
          }],\
          "role": "user"\
        },\
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'cache.sh
```

[Python](https://ai.google.dev/api/caching#python)[Node.js](https://ai.google.dev/api/caching#node.js)[Go](https://ai.google.dev/api/caching#go)More

```
from google import genai
from google.genai import types

client = genai.Client()
document = client.files.upload(file=media / "a11.txt")
model_name = "gemini-3.8-flash"

cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
        contents=[document],
        system_instruction="You are an expert analyzing transcripts.",
    ),
)
cache_name = cache.name  # Save the name for later

# Later retrieve the cache
cache = client.caches.get(name=cache_name)
response = client.models.generate_content(
    model=model_name,
    contents="Find a lighthearted moment from this transcript",
    config=types.GenerateContentConfig(cached_content=cache.name),
)
print(response.text)cache.py
```

```
// Make sure to include the following import:
// import {GoogleGenAI} from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

const contents = [\
  createUserContent(createPartFromUri(document.uri, document.mimeType)),\
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
const cacheName = cache.name; // Save the name for later

// Later retrieve the cache
const retrievedCache = await ai.caches.get({ name: cacheName });
const response = await ai.models.generateContent({
  model: modelName,
  contents: "Find a lighthearted moment from this transcript",
  config: { cachedContent: retrievedCache.name },
});
console.log("Response text:", response.text);cache.js
```

```
ctx := context.Background()
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:  os.Getenv("GEMINI_API_KEY"),
	Backend: genai.BackendGeminiAPI,
})
if err != nil {
	log.Fatal(err)
}

modelName := "gemini-3.8-flash"
document, err := client.Files.UploadFromPath(
	ctx,
	filepath.Join(getMedia(), "a11.txt"),
	&genai.UploadFileConfig{
		MIMEType : "text/plain",
	},
)
if err != nil {
	log.Fatal(err)
}
parts := []*genai.Part{
	genai.NewPartFromURI(document.URI, document.MIMEType),
}
contents := []*genai.Content{
	genai.NewContentFromParts(parts, genai.RoleUser),
}
cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
	Contents:          contents,
	SystemInstruction: genai.NewContentFromText(
		"You are an expert analyzing transcripts.", genai.RoleUser,
	),
})
if err != nil {
	log.Fatal(err)
}
cacheName := cache.Name

// Later retrieve the cache.
cache, err = client.Caches.Get(ctx, cacheName, &genai.GetCachedContentConfig{})
if err != nil {
	log.Fatal(err)
}

response, err := client.Models.GenerateContent(
	ctx,
	modelName,
	genai.Text("Find a lighthearted moment from this transcript"),
	&genai.GenerateContentConfig{
		CachedContent: cache.Name,
	},
)
if err != nil {
	log.Fatal(err)
}
fmt.Println("Response from cache (create from name):")
printResponse(response)cache.go
```

[Python](https://ai.google.dev/api/caching#python)[Node.js](https://ai.google.dev/api/caching#node.js)[Go](https://ai.google.dev/api/caching#go)More

```
from google import genai
from google.genai import types

client = genai.Client()
model_name = "gemini-3.8-flash"
system_instruction = "You are an expert analyzing transcripts."

# Create a chat session with the given system instruction.
chat = client.chats.create(
    model=model_name,
    config=types.GenerateContentConfig(system_instruction=system_instruction),
)
document = client.files.upload(file=media / "a11.txt")

response = chat.send_message(
    message=["Hi, could you summarize this transcript?", document]
)
print("\n\nmodel:  ", response.text)
response = chat.send_message(
    message=["Okay, could you tell me more about the trans-lunar injection"]
)
print("\n\nmodel:  ", response.text)

# To cache the conversation so far, pass the chat history as the list of contents.
cache = client.caches.create(
    model=model_name,
    config={
        "contents": chat.get_history(),
        "system_instruction": system_instruction,
    },
)
# Continue the conversation using the cached content.
chat = client.chats.create(
    model=model_name,
    config=types.GenerateContentConfig(cached_content=cache.name),
)
response = chat.send_message(
    message="I didn't understand that last part, could you explain it in simpler language?"
)
print("\n\nmodel:  ", response.text)cache.py
```

```
// Make sure to include the following import:
// import {GoogleGenAI} from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const modelName = "gemini-3.8-flash";
const systemInstruction = "You are an expert analyzing transcripts.";

// Create a chat session with the system instruction.
const chat = ai.chats.create({
  model: modelName,
  config: { systemInstruction: systemInstruction },
});
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);

let response = await chat.sendMessage({
  message: createUserContent([\
    "Hi, could you summarize this transcript?",\
    createPartFromUri(document.uri, document.mimeType),\
  ]),
});
console.log("\n\nmodel:", response.text);

response = await chat.sendMessage({
  message: "Okay, could you tell me more about the trans-lunar injection",
});
console.log("\n\nmodel:", response.text);

// To cache the conversation so far, pass the chat history as the list of contents.
const chatHistory = chat.getHistory();
const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: chatHistory,
    systemInstruction: systemInstruction,
  },
});

// Continue the conversation using the cached content.
const chatWithCache = ai.chats.create({
  model: modelName,
  config: { cachedContent: cache.name },
});
response = await chatWithCache.sendMessage({
  message:
    "I didn't understand that last part, could you explain it in simpler language?",
});
console.log("\n\nmodel:", response.text);cache.js
```

```
ctx := context.Background()
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:  os.Getenv("GEMINI_API_KEY"),
	Backend: genai.BackendGeminiAPI,
})
if err != nil {
	log.Fatal(err)
}

modelName := "gemini-3.8-flash"
systemInstruction := "You are an expert analyzing transcripts."

// Create initial chat with a system instruction.
chat, err := client.Chats.Create(ctx, modelName, &genai.GenerateContentConfig{
	SystemInstruction: genai.NewContentFromText(systemInstruction, genai.RoleUser),
}, nil)
if err != nil {
	log.Fatal(err)
}

document, err := client.Files.UploadFromPath(
	ctx,
	filepath.Join(getMedia(), "a11.txt"),
	&genai.UploadFileConfig{
		MIMEType : "text/plain",
	},
)
if err != nil {
	log.Fatal(err)
}

// Send first message with the transcript.
parts := make([]genai.Part, 2)
parts[0] = genai.Part{Text: "Hi, could you summarize this transcript?"}
parts[1] = genai.Part{
	FileData: &genai.FileData{
		FileURI :      document.URI,
		MIMEType: document.MIMEType,
	},
}

// Send chat message.
resp, err := chat.SendMessage(ctx, parts...)
if err != nil {
	log.Fatal(err)
}
fmt.Println("\n\nmodel: ", resp.Text())

resp, err = chat.SendMessage(
	ctx,
	genai.Part{
		Text: "Okay, could you tell me more about the trans-lunar injection",
	},
)
if err != nil {
	log.Fatal(err)
}
fmt.Println("\n\nmodel: ", resp.Text())

// To cache the conversation so far, pass the chat history as the list of contents.
cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
	Contents:          chat.History(false),
	SystemInstruction: genai.NewContentFromText(systemInstruction, genai.RoleUser),
})
if err != nil {
	log.Fatal(err)
}

// Continue the conversation using the cached history.
chat, err = client.Chats.Create(ctx, modelName, &genai.GenerateContentConfig{
	CachedContent: cache.Name,
}, nil)
if err != nil {
	log.Fatal(err)
}

resp, err = chat.SendMessage(
	ctx,
	genai.Part{
		Text: "I didn't understand that last part, could you explain it in simpler language?",
	},
)
if err != nil {
	log.Fatal(err)
}
fmt.Println("\n\nmodel: ", resp.Text())cache.go
```

### Response body

If successful, the response body contains a newly created instance of `CachedContent`.

## Method: cachedContents.list

- [Endpoint](https://ai.google.dev/api/caching#body.HTTP_TEMPLATE)
- [Query parameters](https://ai.google.dev/api/caching#body.QUERY_PARAMETERS)
- [Request body](https://ai.google.dev/api/caching#body.request_body)
- [Response body](https://ai.google.dev/api/caching#body.response_body)
  - [JSON representation](https://ai.google.dev/api/caching#body.ListCachedContentsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://ai.google.dev/api/caching#body.aspect)

Lists CachedContents.

### Endpoint

get
`https://generativelanguage.googleapis.com/v1beta/cachedContents`

### Query parameters

`pageSize``integer`

Optional. The maximum number of cached contents to return. The service may return fewer than this value. If unspecified, some default (under maximum) number of items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

`pageToken``string`

Optional. A page token, received from a previous `cachedContents.list` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `cachedContents.list` must match the call that provided the page token.

### Request body

The request body must be empty.

### Response body

Response with CachedContents list.

If successful, the response body contains data with the following structure:

Fields

`cachedContents[]``object (CachedContent)`

List of cached contents.

`nextPageToken``string`

A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.

| JSON representation |
| --- |
| ```<br>{<br>  "cachedContents": [<br>    {<br>      object (CachedContent)<br>    }<br>  ],<br>  "nextPageToken": string<br>}<br>``` |

## Method: cachedContents.get

- [Endpoint](https://ai.google.dev/api/caching#body.HTTP_TEMPLATE)
- [Path parameters](https://ai.google.dev/api/caching#body.PATH_PARAMETERS)
- [Request body](https://ai.google.dev/api/caching#body.request_body)
- [Response body](https://ai.google.dev/api/caching#body.response_body)
- [Authorization scopes](https://ai.google.dev/api/caching#body.aspect)
- [Example request](https://ai.google.dev/api/caching#body.codeSnippets)
  - [Basic](https://ai.google.dev/api/caching#body.codeSnippets.group)

Reads CachedContent resource.

### Endpoint

get
`https://generativelanguage.googleapis.com/v1beta/{name=cachedContents/*}`

### Path parameters

`name``string`

Required. The resource name referring to the content cache entry. Format: `cachedContents/{id}` It takes the form `cachedContents/{cachedcontent}`.

### Request body

The request body must be empty.

### Example request

[Python](https://ai.google.dev/api/caching#python)[Node.js](https://ai.google.dev/api/caching#node.js)[Go](https://ai.google.dev/api/caching#go)[Shell](https://ai.google.dev/api/caching#shell)More

```
from google import genai

client = genai.Client()
document = client.files.upload(file=media / "a11.txt")
model_name = "gemini-3.8-flash"

cache = client.caches.create(
    model=model_name,
    config={
        "contents": [document],
        "system_instruction": "You are an expert analyzing transcripts.",
    },
)
print(client.caches.get(name=cache.name))cache.py
```

```
// Make sure to include the following import:
// import {GoogleGenAI} from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

const contents = [\
  createUserContent(createPartFromUri(document.uri, document.mimeType)),\
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
const retrievedCache = await ai.caches.get({ name: cache.name });
console.log("Retrieved Cache:", retrievedCache);cache.js
```

```
ctx := context.Background()
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:  os.Getenv("GEMINI_API_KEY"),
	Backend: genai.BackendGeminiAPI,
})
if err != nil {
	log.Fatal(err)
}

modelName := "gemini-3.8-flash"
document, err := client.Files.UploadFromPath(
	ctx,
	filepath.Join(getMedia(), "a11.txt"),
	&genai.UploadFileConfig{
		MIMEType : "text/plain",
	},
)
if err != nil {
	log.Fatal(err)
}
parts := []*genai.Part{
	genai.NewPartFromURI(document.URI, document.MIMEType),
}
contents := []*genai.Content{
	genai.NewContentFromParts(parts, genai.RoleUser),
}

cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
	Contents:          contents,
	SystemInstruction: genai.NewContentFromText(
		"You are an expert analyzing transcripts.", genai.RoleUser,
	),
})
if err != nil {
	log.Fatal(err)
}

cache, err = client.Caches.Get(ctx, cache.Name, &genai.GetCachedContentConfig{})
if err != nil {
	log.Fatal(err)
}
fmt.Println("Retrieved cache:")
fmt.Println(cache)cache.go
```

```
curl "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"cache.sh
```

### Response body

If successful, the response body contains an instance of `CachedContent`.

## Method: cachedContents.patch

- [Endpoint](https://ai.google.dev/api/caching#body.HTTP_TEMPLATE)
- [Path parameters](https://ai.google.dev/api/caching#body.PATH_PARAMETERS)
- [Query parameters](https://ai.google.dev/api/caching#body.QUERY_PARAMETERS)
- [Request body](https://ai.google.dev/api/caching#body.request_body)
- [Response body](https://ai.google.dev/api/caching#body.response_body)
- [Authorization scopes](https://ai.google.dev/api/caching#body.aspect)
- [Example request](https://ai.google.dev/api/caching#body.codeSnippets)
  - [Basic](https://ai.google.dev/api/caching#body.codeSnippets.group)

Updates CachedContent resource (only expiration is updatable).

### Endpoint

patch
`https://generativelanguage.googleapis.com/v1beta/{cachedContent.name=cachedContents/*}`

`PATCH https://generativelanguage.googleapis.com/v1beta/{cachedContent.name=cachedContents/*}`

### Path parameters

`cachedContent.name``string`

Output only. Identifier. The resource name referring to the cached content. Format: `cachedContents/{id}` It takes the form `cachedContents/{cachedcontent}`.

### Query parameters

`updateMask``string (FieldMask format)`

The list of fields to update.

This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Request body

The request body contains an instance of `CachedContent`.

Fields

`expiration``Union type`

Specifies when this resource will expire. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`expireTime``string (Timestamp format)`

Timestamp in UTC of when this resource is considered expired. This is _always_ provided on output, regardless of what was sent on input.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.

`ttl``string (Duration format)`

Input only. New TTL for this resource, input only.

A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.

End of mutually exclusive fields.

### Example request

[Python](https://ai.google.dev/api/caching#python)[Node.js](https://ai.google.dev/api/caching#node.js)[Go](https://ai.google.dev/api/caching#go)[Shell](https://ai.google.dev/api/caching#shell)More

```
from google import genai
from google.genai import types
import datetime

client = genai.Client()
document = client.files.upload(file=media / "a11.txt")
model_name = "gemini-3.8-flash"

cache = client.caches.create(
    model=model_name,
    config={
        "contents": [document],
        "system_instruction": "You are an expert analyzing transcripts.",
    },
)

# Update the cache's time-to-live (ttl)
ttl = f"{int(datetime.timedelta(hours=2).total_seconds())}s"
client.caches.update(
    name=cache.name, config=types.UpdateCachedContentConfig(ttl=ttl)
)
print(f"After update:\n {cache}")

# Alternatively, update the expire_time directly
# Update the expire_time directly in valid RFC 3339 format (UTC with a "Z" suffix)
expire_time = (
    (
        datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(minutes=15)
    )
    .isoformat()
    .replace("+00:00", "Z")
)
client.caches.update(
    name=cache.name,
    config=types.UpdateCachedContentConfig(expire_time=expire_time),
)cache.py
```

```
// Make sure to include the following import:
// import {GoogleGenAI} from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

const contents = [\
  createUserContent(createPartFromUri(document.uri, document.mimeType)),\
];

let cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});

// Update the cache's time-to-live (ttl)
const ttl = `${2 * 3600}s`; // 2 hours in seconds
cache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", cache);

// Alternatively, update the expire_time directly (in RFC 3339 format with a "Z" suffix)
const expireTime = new Date(Date.now() + 15 * 60000)
  .toISOString()
  .replace(/\.\d{3}Z$/, "Z");
cache = await ai.caches.update({
  name: cache.name,
  config: { expireTime: expireTime },
});
console.log("After update (expire_time):", cache);cache.js
```

```
ctx := context.Background()
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:  os.Getenv("GEMINI_API_KEY"),
	Backend: genai.BackendGeminiAPI,
})
if err != nil {
	log.Fatal(err)
}

modelName := "gemini-3.8-flash"
document, err := client.Files.UploadFromPath(
	ctx,
	filepath.Join(getMedia(), "a11.txt"),
	&genai.UploadFileConfig{
		MIMEType : "text/plain",
	},
)
if err != nil {
	log.Fatal(err)
}
parts := []*genai.Part{
	genai.NewPartFromURI(document.URI, document.MIMEType),
}
contents := []*genai.Content{
	genai.NewContentFromParts(parts, genai.RoleUser),
}

cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
	Contents:          contents,
	SystemInstruction: genai.NewContentFromText(
		"You are an expert analyzing transcripts.", genai.RoleUser,
	),
})
if err != nil {
	log.Fatal(err)
}

_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
	log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)cache.go
```

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{"ttl": "600s"}'cache.sh
```

### Response body

If successful, the response body contains an instance of `CachedContent`.

## Method: cachedContents.delete

- [Endpoint](https://ai.google.dev/api/caching#body.HTTP_TEMPLATE)
- [Path parameters](https://ai.google.dev/api/caching#body.PATH_PARAMETERS)
- [Request body](https://ai.google.dev/api/caching#body.request_body)
- [Response body](https://ai.google.dev/api/caching#body.response_body)
- [Authorization scopes](https://ai.google.dev/api/caching#body.aspect)
- [Example request](https://ai.google.dev/api/caching#body.codeSnippets)
  - [Basic](https://ai.google.dev/api/caching#body.codeSnippets.group)

Deletes CachedContent resource.

### Endpoint

delete
`https://generativelanguage.googleapis.com/v1beta/{name=cachedContents/*}`

### Path parameters

`name``string`

Required. The resource name referring to the content cache entry Format: `cachedContents/{id}` It takes the form `cachedContents/{cachedcontent}`.

### Request body

The request body must be empty.

### Example request

[Python](https://ai.google.dev/api/caching#python)[Node.js](https://ai.google.dev/api/caching#node.js)[Go](https://ai.google.dev/api/caching#go)[Shell](https://ai.google.dev/api/caching#shell)More

```
from google import genai

client = genai.Client()
document = client.files.upload(file=media / "a11.txt")
model_name = "gemini-3.8-flash"

cache = client.caches.create(
    model=model_name,
    config={
        "contents": [document],
        "system_instruction": "You are an expert analyzing transcripts.",
    },
)
client.caches.delete(name=cache.name)cache.py
```

```
// Make sure to include the following import:
// import {GoogleGenAI} from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

const contents = [\
  createUserContent(createPartFromUri(document.uri, document.mimeType)),\
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
await ai.caches.delete({ name: cache.name });
console.log("Cache deleted:", cache.name);cache.js
```

```
ctx := context.Background()
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:  os.Getenv("GEMINI_API_KEY"),
	Backend: genai.BackendGeminiAPI,
})
if err != nil {
	log.Fatal(err)
}

modelName := "gemini-3.8-flash"
document, err := client.Files.UploadFromPath(
	ctx,
	filepath.Join(getMedia(), "a11.txt"),
	&genai.UploadFileConfig{
		MIMEType : "text/plain",
	},
)
if err != nil {
	log.Fatal(err)
}
parts := []*genai.Part{
	genai.NewPartFromURI(document.URI, document.MIMEType),
}
contents := []*genai.Content{
	genai.NewContentFromParts(parts, genai.RoleUser),
}

cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
	Contents:          contents,
	SystemInstruction: genai.NewContentFromText(
		"You are an expert analyzing transcripts.", genai.RoleUser,
	),
})
if err != nil {
	log.Fatal(err)
}

_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
	log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)cache.go
```

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"cache.sh
```

### Response body

If successful, the response body is an empty JSON object.

## REST Resource: cachedContents

- [Resource: CachedContent](https://ai.google.dev/api/caching#CachedContent)
  - [JSON representation](https://ai.google.dev/api/caching#CachedContent.SCHEMA_REPRESENTATION)
- [ToolConfig](https://ai.google.dev/api/caching#ToolConfig)
  - [JSON representation](https://ai.google.dev/api/caching#ToolConfig.SCHEMA_REPRESENTATION)
- [FunctionCallingConfig](https://ai.google.dev/api/caching#FunctionCallingConfig)
  - [JSON representation](https://ai.google.dev/api/caching#FunctionCallingConfig.SCHEMA_REPRESENTATION)
- [Mode](https://ai.google.dev/api/caching#Mode)
- [RetrievalConfig](https://ai.google.dev/api/caching#RetrievalConfig)
  - [JSON representation](https://ai.google.dev/api/caching#RetrievalConfig.SCHEMA_REPRESENTATION)
- [LatLng](https://ai.google.dev/api/caching#LatLng)
  - [JSON representation](https://ai.google.dev/api/caching#LatLng.SCHEMA_REPRESENTATION)
- [UsageMetadata](https://ai.google.dev/api/caching#UsageMetadata)
  - [JSON representation](https://ai.google.dev/api/caching#UsageMetadata.SCHEMA_REPRESENTATION)
- [Methods](https://ai.google.dev/api/caching#METHODS_SUMMARY)

## Resource: CachedContent

Content that has been preprocessed and can be used in subsequent request to GenerativeService.

Cached content can be only used with model it was created for.

Fields

`contents[]``object (Content)`

Optional. Input only. Immutable. The content to cache.

`tools[]``object (Tool)`

Optional. Input only. Immutable. A list of `Tools` the model may use to generate the next response

`createTime``string (Timestamp format)`

Output only. Creation time of the cache entry.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.

`updateTime``string (Timestamp format)`

Output only. When the cache entry was last updated in UTC time.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.

`usageMetadata``object (UsageMetadata)`

Output only. Metadata on the usage of the cached content.

`expiration``Union type`

Specifies when this resource will expire. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`expireTime``string (Timestamp format)`

Timestamp in UTC of when this resource is considered expired. This is _always_ provided on output, regardless of what was sent on input.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.

`ttl``string (Duration format)`

Input only. New TTL for this resource, input only.

A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.

End of mutually exclusive fields.

`name``string`

Output only. Identifier. The resource name referring to the cached content. Format: `cachedContents/{id}`

`displayName``string`

Optional. Immutable. The user-generated meaningful display name of the cached content. Maximum 128 Unicode characters.

`model``string`

Required. Immutable. The name of the `Model` to use for cached content Format: `models/{model}`

`systemInstruction``object (Content)`

Optional. Input only. Immutable. Developer set system instruction. Currently text only.

`toolConfig``object (ToolConfig)`

Optional. Input only. Immutable. Tool config. This config is shared for all tools.

| JSON representation |
| --- |
| ```<br>{<br>  "contents": [<br>    {<br>      object (Content)<br>    }<br>  ],<br>  "tools": [<br>    {<br>      object (Tool)<br>    }<br>  ],<br>  "createTime": string,<br>  "updateTime": string,<br>  "usageMetadata": {<br>    object (UsageMetadata)<br>  },<br>  // expiration<br>  "expireTime": string,<br>  "ttl": string<br>  // Union type<br>  "name": string,<br>  "displayName": string,<br>  "model": string,<br>  "systemInstruction": {<br>    object (Content)<br>  },<br>  "toolConfig": {<br>    object (ToolConfig)<br>  }<br>}<br>``` |

## ToolConfig

The Tool configuration containing parameters for specifying `Tool` use in the request.

Fields

`functionCallingConfig``object (FunctionCallingConfig)`

Optional. Function calling config.

`retrievalConfig``object (RetrievalConfig)`

Optional. Retrieval config.

`includeServerSideToolInvocations``boolean`

Optional. If true, the API response will include the server-side tool calls and responses within the `Content` message. This allows clients to observe the server's tool interactions.

| JSON representation |
| --- |
| ```<br>{<br>  "functionCallingConfig": {<br>    object (FunctionCallingConfig)<br>  },<br>  "retrievalConfig": {<br>    object (RetrievalConfig)<br>  },<br>  "includeServerSideToolInvocations": boolean<br>}<br>``` |

## FunctionCallingConfig

Configuration for specifying function calling behavior.

Fields

`mode``enum (Mode)`

Optional. Specifies the mode in which function calling should execute. If unspecified, the default value will be set to AUTO.

`allowedFunctionNames[]``string`

Optional. A set of function names that, when provided, limits the functions the model will call.

This should only be set when the Mode is ANY or VALIDATED. Function names should match \[FunctionDeclaration.name\]. When set, model will predict a function call from only allowed function names.

| JSON representation |
| --- |
| ```<br>{<br>  "mode": enum (Mode),<br>  "allowedFunctionNames": [<br>    string<br>  ]<br>}<br>``` |

## Mode

Defines the execution behavior for function calling by defining the execution mode.

| Enums |
| --- |
| `MODE_UNSPECIFIED` | Unspecified function calling mode. This value should not be used. |
| `AUTO` | Default model behavior, model decides to predict either a function call or a natural language response. |
| `ANY` | Model is constrained to always predicting a function call only. If "allowedFunctionNames" are set, the predicted function call will be limited to any one of "allowedFunctionNames", else the predicted function call will be any one of the provided "functionDeclarations". |
| `NONE` | Model will not predict any function call. Model behavior is same as when not passing any function declarations. |
| `VALIDATED` | Model decides to predict either a function call or a natural language response, but will validate function calls with constrained decoding. If "allowedFunctionNames" are set, the predicted function call will be limited to any one of "allowedFunctionNames", else the predicted function call will be any one of the provided "functionDeclarations". |

## RetrievalConfig

Retrieval config.

Fields

`latLng``object (LatLng)`

Optional. The location of the user.

`languageCode``string`

Optional. The language code of the user. Language code for content. Use language tags defined by [BCP47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).

| JSON representation |
| --- |
| ```<br>{<br>  "latLng": {<br>    object (LatLng)<br>  },<br>  "languageCode": string<br>}<br>``` |

## LatLng

An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the [WGS84 standard](https://en.wikipedia.org/wiki/World_Geodetic_System#1984_version). Values must be within normalized ranges.

Fields

`latitude``number`

The latitude in degrees. It must be in the range \[-90.0, +90.0\].

`longitude``number`

The longitude in degrees. It must be in the range \[-180.0, +180.0\].

| JSON representation |
| --- |
| ```<br>{<br>  "latitude": number,<br>  "longitude": number<br>}<br>``` |

## UsageMetadata

Metadata on the usage of the cached content.

Fields

`totalTokenCount``integer`

Total number of tokens that the cached content consumes.

| JSON representation |
| --- |
| ```<br>{<br>  "totalTokenCount": integer<br>}<br>``` |



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-11 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-11 UTC."\],\[\],\[\]\]