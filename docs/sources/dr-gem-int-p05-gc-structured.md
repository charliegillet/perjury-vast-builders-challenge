[Skip to main content](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#main-content)

[![Gemini Generate Content API (Legacy)](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/generate-content/structured-output)
- [Deutsch](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fgenerate-content%2Fstructured-output&prompt=select_account)

- On this page
- [Structured output examples](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#structured_output_examples)
  - [Recipe Extractor](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#recipe)
  - [Content Moderation](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#feedback)
  - [Recursive Structures](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#recursive)
- [Streaming](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#streaming)
- [Structured outputs with tools](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#structured_outputs_with_tools)
- [JSON schema support](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#json_schema_support)
  - [Type-specific properties](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#type-specific_properties)
- [Model support](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#model_support)
- [Structured outputs vs. function calling](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#structured_outputs_vs_function_calling)
- [Best practices](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#best_practices)
- [Limitations](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#limitations)

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content)

Interactions API (Recommended)generateContent APILearn more

Select an optiongenerateContent API

- [Interactions API (Recommended)](https://ai.google.dev/gemini-api/docs/structured-output)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content/structured-output)
- [Learn more](https://ai.google.dev/gemini-api/docs/interactions)



 Send feedback



# Structured outputs

- On this page
- [Structured output examples](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#structured_output_examples)
  - [Recipe Extractor](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#recipe)
  - [Content Moderation](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#feedback)
  - [Recursive Structures](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#recursive)
- [Streaming](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#streaming)
- [Structured outputs with tools](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#structured_outputs_with_tools)
- [JSON schema support](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#json_schema_support)
  - [Type-specific properties](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#type-specific_properties)
- [Model support](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#model_support)
- [Structured outputs vs. function calling](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#structured_outputs_vs_function_calling)
- [Best practices](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#best_practices)
- [Limitations](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#limitations)

You can configure Gemini models to generate responses that adhere to a provided JSON
Schema. This ensures predictable, type-safe results and simplifies extracting
structured data from unstructured text.

Using structured outputs is ideal for:

- **Data extraction:** Pull specific information like names and dates from text.
- **Structured classification:** Classify text into predefined categories.
- **Agentic workflows:** Generate structured inputs for tools or APIs.

In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs
make it easy to define schemas using
[Pydantic](https://docs.pydantic.dev/latest/) (Python) and
[Zod](https://zod.dev/) (JavaScript).

## Structured output examples

### Recipe Extractor

This example demonstrates how to extract structured data from text using basic
JSON Schema types like `object`, `array`, `string`, and `integer`.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

client = genai.Client()

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Recipe.model_json_schema()}},
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

const ai = new GoogleGenAI({});

const prompt = `
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
`;

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(recipeSchema) } },
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please extract the recipe from the following text.
  The user wants to make delicious chocolate chip cookies.
  They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
  1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
  3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
  For the best part, they'll need 2 cups of semisweet chocolate chips.
  First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
  baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
  until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
  ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
  onto ungreased baking sheets and bake for 9 to 11 minutes.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "recipe_name": map[string]any{
                    "type":        "string",
                    "description": "The name of the recipe.",
                },
                "prep_time_minutes": map[string]any{
                    "type":        "integer",
                    "description": "Optional time in minutes to prepare the recipe.",
                },
                "ingredients": map[string]any{
                    "type": "array",
                    "items": map[string]any{
                        "type": "object",
                        "properties": map[string]any{
                            "name": map[string]any{
                                "type":        "string",
                                "description": "Name of the ingredient.",
                            },
                            "quantity": map[string]any{
                                "type":        "string",
                                "description": "Quantity of the ingredient, including units.",
                            },
                        },
                        "required": []string{"name", "quantity"},
                    },
                },
                "instructions": map[string]any{
                    "type":  "array",
                    "items": map[string]any{"type": "string"},
                },
            },
            "required": []string{"recipe_name", "ingredients", "instructions"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }\
        ]\
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "recipe_name": {
              "type": "string",
              "description": "The name of the recipe."
            },
            "prep_time_minutes": {
                "type": "integer",
                "description": "Optional time in minutes to prepare the recipe."
            },
            "ingredients": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "description": "Name of the ingredient."},
                  "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
          }
        }
      },
                "required": ["name", "quantity"]
              }
            },
            "instructions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["recipe_name", "ingredients", "instructions"]
        }
      }
    }'
```

**Example Response:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [\
    {\
      "name": "all-purpose flour",\
      "quantity": "2 and 1/4 cups"\
    },\
    {\
      "name": "baking soda",\
      "quantity": "1 teaspoon"\
    },\
    {\
      "name": "salt",\
      "quantity": "1 teaspoon"\
    },\
    {\
      "name": "unsalted butter (softened)",\
      "quantity": "1 cup"\
    },\
    {\
      "name": "granulated sugar",\
      "quantity": "3/4 cup"\
    },\
    {\
      "name": "packed brown sugar",\
      "quantity": "3/4 cup"\
    },\
    {\
      "name": "vanilla extract",\
      "quantity": "1 teaspoon"\
    },\
    {\
      "name": "large eggs",\
      "quantity": "2"\
    },\
    {\
      "name": "semisweet chocolate chips",\
      "quantity": "2 cups"\
    }\
  ],
  "instructions": [\
    "Preheat the oven to 375°F (190°C).",\
    "In a small bowl, whisk together the flour, baking soda, and salt.",\
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",\
    "Beat in the vanilla and eggs, one at a time.",\
    "Gradually beat in the dry ingredients until just combined.",\
    "Stir in the chocolate chips.",\
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."\
  ]
}
```

### Content Moderation

This example showcases `anyOf` for conditional schemas and `enum` for
classification, allowing the output structure to vary based on the content.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import Union, Literal

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"] = Field(description="The type of spam.")

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

client = genai.Client()

prompt = """
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": ModerationResult.model_json_schema()}},
    },
)

result = ModerationResult.model_validate_json(response.text)
print(result)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const spamDetailsSchema = z.object({
  reason: z.string().describe("The reason why the content is considered spam."),
  spam_type: z.enum(["phishing", "scam", "unsolicited promotion", "other"]).describe("The type of spam."),
});

const notSpamDetailsSchema = z.object({
  summary: z.string().describe("A brief summary of the content."),
  is_safe: z.boolean().describe("Whether the content is safe for all audiences."),
});

const moderationResultSchema = z.object({
  decision: z.union([spamDetailsSchema, notSpamDetailsSchema]),
});

const ai = new GoogleGenAI({});

const prompt = `
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
`;

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(moderationResultSchema) } },
  },
});

const result = moderationResultSchema.parse(JSON.parse(response.text));
console.log(result);
```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please moderate the following content and provide a decision.
  Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "decision": map[string]any{
                    "anyOf": []map[string]any{
                        {
                            "type":        "object",
                            "title":       "SpamDetails",
                            "description": "Details for content classified as spam.",
                            "properties": map[string]any{
                                "reason": map[string]any{
                                    "type":        "string",
                                    "description": "The reason why the content is considered spam.",
                                },
                                "spam_type": map[string]any{
                                    "type":        "string",
                                    "enum":        []string{"phishing", "scam", "unsolicited promotion", "other"},
                                    "description": "The type of spam.",
                                },
                            },
                            "required": []string{"reason", "spam_type"},
                        },
                        {
                            "type":        "object",
                            "title":       "NotSpamDetails",
                            "description": "Details for content classified as not spam.",
                            "properties": map[string]any{
                                "summary": map[string]any{
                                    "type":        "string",
                                    "description": "A brief summary of the content.",
                                },
                                "is_safe": map[string]any{
                                    "type":        "boolean",
                                    "description": "Whether the content is safe for all audiences.",
                                },
                            },
                            "required": []string{"summary", "is_safe"},
                        },
                    },
                },
            },
            "required": []string{"decision"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

````
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          { "text": "Please moderate the following content and provide a decision.\nContent: ''Congratulations! You have won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com''" }\
        ]\
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "decision": {
              "anyOf": [\
                {\
                  "type": "object",\
                  "title": "SpamDetails",\
                  "description": "Details for content classified as spam.",\
                  "properties": {\
                    "reason": { "type": "string", "description": "The reason why the content is considered spam." },\
                    "spam_type": { "type": "string", "enum": ["phishing", "scam", "unsolicited promotion", "other"], "description": "The type of spam." }\
          }\
        }\
      },\
                   "required": ["reason", "spam_type"]\
                 },\
                 {\
                   "type": "object",\
                   "title": "NotSpamDetails",\
                   "description": "Details for content classified as not spam.",\
                   "properties": {\
                     "summary": { "type": "string", "description": "A brief summary of the content." },\
                     "is_safe": { "type": "boolean", "description": "Whether the content is safe for all audiences." }\
                   },\
                   "required": ["summary", "is_safe"]\
                 }\
               ]
             }
           },
           "required": ["decision"]
         }
       }
     }'
 ```

**Example Response:**

```json
{
"decision": {
"reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
"spam_type": "scam"
}
}
````

### Recursive Structures

This example illustrates how to define a recursive schema such as an organization
chart.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class Employee(BaseModel):
    """Represents an employee in an organization."""
    name: str
    employee_id: int
    reports: List["Employee"] = Field(
        default_factory=list,
        description="A list of employees reporting to this employee."
    )

client = genai.Client()

prompt = """
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Employee.model_json_schema()}},
    },
)

employee = Employee.model_validate_json(response.text)
print(employee)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const employeeSchema = z.object({
name: z.string(),
employee_id: z.number().int(),
reports: z.lazy(() => z.array(employeeSchema)).describe("A list of employees reporting to this employee."),
});

const ai = new GoogleGenAI({});

const prompt = `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`;

const response = await ai.models.generateContent({
model: "gemini-3.8-flash",
contents: prompt,
config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(employeeSchema) } },
},
});

const employee = employeeSchema.parse(JSON.parse(response.text));
console.log(employee);
```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "name":        map[string]any{"type": "string"},
                "employee_id": map[string]any{"type": "integer"},
                "reports": map[string]any{
                    "type":        "array",
                    "description": "A list of employees reporting to this employee.",
                    "items": map[string]any{
                        "$ref": "#",
                    },
                },
            },
            "required": []string{"name", "employee_id", "reports"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          { "text": "Generate an organization chart for a small team.\nThe manager is Alice, who manages Bob and Charlie. Bob manages David." }\
        ]\
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "employee_id": { "type": "integer" },
            "reports": {
              "type": "array",
              "description": "A list of employees reporting to this employee.",
              "items": {
                "$ref": "#"
              }
          }
        }
      }
          },
          "required": ["name", "employee_id", "reports"]
        }
      }
    }'
```

**Example Response:**

```
{
"name": "Alice",
"employee_id": 101,
"reports": [\
    {\
      "name": "Bob",\
      "employee_id": 102,\
      "reports": [\
        {\
          "name": "David",\
          "employee_id": 104,\
          "reports": []\
        }\
      ]\
    },\
    {\
      "name": "Charlie",\
      "employee_id": 103,\
      "reports": []\
    }\
]
}
```

## Streaming

You can stream structured outputs, which allows you to start processing the
response as it's being generated, without having to wait for the entire output
to be complete. This can improve the perceived performance of your application.

The streamed chunks will be valid partial JSON strings, which can be
concatenated to form the final, complete JSON object.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#javascript)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Feedback.model_json_schema()}},
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});
const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

const feedbackSchema = z.object({
sentiment: z.enum(["positive", "neutral", "negative"]),
summary: z.string(),
});

const stream = await ai.models.generateContentStream({
model: "gemini-3.8-flash",
contents: prompt,
config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
},
});

for await (const chunk of stream) {
console.log(chunk.candidates[0].content.parts[0].text)
}
```

## Structured outputs with tools

Gemini 3 lets you combine Structured Outputs with built-in tools, including
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search),
[URL Context](https://ai.google.dev/gemini-api/docs/url-context),
[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution),
[File Search](https://ai.google.dev/gemini-api/docs/file-search#structured-output), and
[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling).

[Python](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#javascript)[REST](https://ai.google.dev/gemini-api/docs/generate-content/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [\
            {"google_search": {}},\
            {"url_context": {}}\
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
winner: z.string().describe("The name of the winner."),
final_match_score: z.string().describe("The final score."),
scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [\
        { googleSearch: {} },\
        { urlContext: {} }\
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
});

const match = matchSchema.parse(JSON.parse(response.text));
console.log(match);
}

run();
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{\
      "parts": [{"text": "Search for all details for the latest Euro."}]\
    }],
    "tools": [\
      {"googleSearch": {}},\
      {"urlContext": {}}\
    ],
    "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
          }
        }
      },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
}'
```

## JSON schema support

To generate a JSON object, set the `response_format` in the generation configuration. The schema must be a valid [JSON Schema](https://json-schema.org/) that describes the desired output format.

The model will then generate a response that is a syntactically valid JSON string matching the provided schema. When using structured outputs, the model will produce outputs in the same order as the keys in the schema.

Gemini's structured output mode supports a subset of the [JSON Schema](https://json-schema.org/) specification.

The following values of `type` are supported:

- **`string`**: For text.
- **`number`**: For floating-point numbers.
- **`integer`**: For whole numbers.
- **`boolean`**: For true/false values.
- **`object`**: For structured data with key-value pairs.
- **`array`**: For lists of items.
- **`null`**: To allow a property to be null, include `"null"` in the type array (e.g., `{"type": ["string", "null"]}`).

These descriptive properties help guide the model:

- **`title`**: A short description of a property.
- **`description`**: A longer and more detailed description of a property.

### Type-specific properties

**For `object` values:**

- **`properties`**: An object where each key is a property name and each value is a schema for that property.
- **`required`**: An array of strings, listing which properties are mandatory.
- **`additionalProperties`**: Controls whether properties not listed in `properties` are allowed. Can be a boolean or a schema.

**For `string` values:**

- **`enum`**: Lists a specific set of possible strings for classification tasks.
- **`format`**: Specifies a syntax for the string, such as `date-time`, `date`, `time`.

**For `number` and `integer` values:**

- **`enum`**: Lists a specific set of possible numeric values.
- **`minimum`**: The minimum inclusive value.
- **`maximum`**: The maximum inclusive value.

**For `array` values:**

- **`items`**: Defines the schema for all items in the array.
- **`prefixItems`**: Defines a list of schemas for the first N items, allowing for tuple-like structures.
- **`minItems`**: The minimum number of items in the array.
- **`maxItems`**: The maximum number of items in the array.

## Model support

The following models support structured output:

| Model | Structured Outputs |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

_\\* Note that Gemini 2.0 requires an explicit `propertyOrdering` list within the JSON input to define the preferred structure. You can find an example in this [cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb)._

## Structured outputs vs. function calling

Both structured outputs and function calling use JSON schemas, but they serve different purposes:

| Feature | Primary Use Case |
| --- | --- |
| **Structured Outputs** | **Formatting the final response to the user.** Use this when you want the model's _answer_ to be in a specific format (e.g., extracting data from a document to save to a database). |
| **Function Calling** | **Taking action during the conversation.** Use this when the model needs to _ask you_ to perform a task (e.g., "get current weather") before it can provide a final answer. |

## Best practices

- **Clear descriptions:** Use the `description` field in your schema to provide clear instructions to the model about what each property represents. This is crucial for guiding the model's output.
- **Strong typing:** Use specific types (`integer`, `string`, `enum`) whenever possible. If a parameter has a limited set of valid values, use an `enum`.
- **Prompt engineering:** Clearly state in your prompt what you want the model to do. For example, "Extract the following information from the text..." or "Classify this feedback according to the provided schema...".
- **Validation:** While structured output guarantees syntactically correct JSON, it does not guarantee the values are semantically correct. Always validate the final output in your application code before using it.
- **Error handling:** Implement robust error handling in your application to gracefully manage cases where the model's output, while schema-compliant, may not meet your business logic requirements.

## Limitations

- **Schema subset:** Not all features of the JSON Schema specification are supported. The model ignores unsupported properties.
- **Schema complexity:** The API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your schema by shortening property names, reducing nesting, or limiting the number of constraints.



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-02 UTC."\],\[\],\[\]\]