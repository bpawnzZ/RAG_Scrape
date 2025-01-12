# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#welcome-to-firecrawl

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#how-to-use-it

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#api-key

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#crawling

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#output

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#open-source-vs-cloud

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

# Quickstart | Firecrawl

**URL:** https://docs.firecrawl.dev/introduction#contributing

## Headers
- Get Started
- Features
- Integrations
- Contributing
- Quickstart
- ​Welcome to Firecrawl
- ​How to use it?
- ​API Key
- ​Features
- ​Powerful Capabilities
- ​Crawling
- ​Installation
- ​Usage
- ​Check Crawl Job
- ​Response
- ​Scraping
- ​Response
- ​Extraction
- ​Extracting without schema (New)
- ​Extraction (v0)
- ​Interacting with the page with Actions
- ​Example
- ​Output
- ​Open Source vs Cloud
- ​Contributing

## Code Examples
### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
async crawl
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
ID
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.

```
next
```

### Context
To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
scrape_url
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

```
prompt
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
Output:

```
{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}
```

### Context
It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.

```
wait
```

## Paragraphs
- Firecrawl allows you to turn entire websites into LLM-ready markdown
- Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.
- We provide an easy to use API with our hosted version. You can find the playground and documentation here. You can also self host the backend if you’d like.
- Check out the following resources to get started:
- Self-host: To self-host refer to guide here.
- To use the API, you need to sign up on Firecrawl and get an API key.
- You can find all of Firecrawl’s capabilities and how to use them in our documentation
- Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
- If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.
- Used to check the status of a crawl job and get its result.
- The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a next URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the next parameter is absent, it indicates the end of the crawl data.
- To scrape a single URL, use the scrape_url method. It takes the URL as a parameter and returns the scraped data as a dictionary.
- SDKs will return the data object directly. cURL will return the payload exactly as shown below.
- With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
- v1 is only supported on node, python and cURL at this time.
- Output:
- You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.
- Output:
- Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
- Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.
- It is important to almost always use the wait action before/after executing other actions to give enough time for the page to load.
- Firecrawl is open source available under the AGPL-3.0 license.
- To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.
- Firecrawl Cloud is available at firecrawl.dev and offers a range of features that are not available in the open source version:
- 
- We love contributions! Please read our contributing guide before submitting a pull request.

---

