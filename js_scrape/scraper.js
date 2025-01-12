const puppeteer = require('puppeteer');
const fs = require('fs');
const process = require('process');
const { URL } = require('url');

// Function to scrape and clean content from a single page
async function scrapePage(page, url) {
  await page.goto(url, { waitUntil: 'networkidle2' });

  // Extract and clean content
  const content = await page.evaluate(() => {
    // Selectors for meaningful content
    const selectors = [
      'h1', 'h2', 'h3', 'h4', 'h5', 'h6', // Headings
      'p', 'ul', 'ol', 'li', // Paragraphs and lists
      'pre', 'code', // Code blocks
      'article', 'section', // Semantic blocks
      'table', // Tables
    ];

    // Extract text from selected elements
    const elements = document.querySelectorAll(selectors.join(', '));
    let text = Array.from(elements)
      .map(element => {
        // Clean up whitespace and trim
        let content = element.innerText.replace(/\s+/g, ' ').trim();

        // Format headings
        if (element.tagName.match(/^h[1-6]$/i)) {
          const level = element.tagName.toLowerCase().replace('h', '');
          content = '#'.repeat(level) + ' ' + content;
        }

        // Format code blocks
        if (element.tagName === 'PRE' || element.tagName === 'CODE') {
          content = '```\n' + content + '\n```';
        }

        // Format tables (basic support)
        if (element.tagName === 'TABLE') {
          const rows = Array.from(element.querySelectorAll('tr'));
          content = rows
            .map(row => {
              const cells = Array.from(row.querySelectorAll('th, td'));
              return cells.map(cell => cell.innerText.trim()).join(' | ');
            })
            .join('\n');
        }

        return content;
      })
      .filter(content => content.length > 0) // Remove empty lines
      .join('\n\n'); // Separate sections with double newlines

    return text;
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

      if (content) {
        scrapedData.push(`# Page: ${currentUrl}\n\n${content}\n\n---\n`);
      }

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
  const markdownContent = data.join('\n');
  fs.writeFileSync(filename, markdownContent, 'utf8');
  console.log(`Scraped data saved to ${filename}`);
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
