const puppeteer = require('puppeteer');
const fs = require('fs');
const process = require('process');
const { URL } = require('url');

// Function to scrape a single page
async function scrapePage(page, url) {
  await page.goto(url, { waitUntil: 'networkidle2' });

  // Extract content (customize as needed)
  const content = await page.evaluate(() => {
    const body = document.querySelector('body');
    return body ? body.innerText : 'No content found';
  });

  return content;
}

// Function to crawl and scrape the website
async function crawlAndScrape(baseUrl, maxPages = 300) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  const visited = new Set();
  const queue = [baseUrl];
  const scrapedData = [];

  try {
    while (queue.length > 0 && visited.size < maxPages) {
      const currentUrl = queue.shift();

      if (visited.has(currentUrl)) continue;
      visited.add(currentUrl);

      console.log(`Scraping: ${currentUrl}`);
      const content = await scrapePage(page, currentUrl);
      scrapedData.push(`# ${currentUrl}\n\n${content}\n\n---\n`);

      // Find all links on the page
      const links = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('a'))
          .map(link => link.href)
          .filter(href => href); // Filter out empty hrefs
      });

      // Add new links to the queue (only for the same domain/subdomain)
      for (const link of links) {
        const parsedLink = new URL(link);
        const parsedBaseUrl = new URL(baseUrl);

        if (
          parsedLink.hostname === parsedBaseUrl.hostname && // Same domain/subdomain
          !visited.has(link) && // Not already visited
          !queue.includes(link) // Not already in the queue
        ) {
          queue.push(link);
        }
      }
    }
  } catch (error) {
    console.error('Error during crawling or scraping:', error);
  } finally {
    await browser.close();
  }

  return scrapedData;
}

// Function to save scraped data to a .md file
function saveToMarkdown(data, filename = 'scraped_data.md') {
  const outputDir = '/home/insomnia/scraped_data';
  const outputPath = `${outputDir}/${filename}`;
  
  // Create directory if it doesn't exist
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const markdownContent = data.join('\n');
  fs.writeFileSync(outputPath, markdownContent, 'utf8');
  console.log(`Scraped data saved to ${outputPath}`);
}

// Get URL from command-line arguments
const baseUrl = process.argv[2];

if (!baseUrl) {
  console.error('Please provide a base URL as an argument.');
  process.exit(1);
}

// Run the crawler and save the results
(async () => {
  const scrapedData = await crawlAndScrape(baseUrl);
  saveToMarkdown(scrapedData);
})();