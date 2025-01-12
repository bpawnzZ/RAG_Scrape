const fs = require('fs');
const path = require('path');

// Function to clean and process markdown content
function processMarkdown(content) {
  const lines = content.split('\n');
  const processedLines = [];
  let lastLineWasEmpty = false;

  // Helper function to check if a line is a heading
  const isHeading = (line) => /^#{1,6}\s/.test(line);

  // Helper function to check if a line is a code block delimiter
  const isCodeBlockDelimiter = (line) => line.trim() === '```';

  // Helper function to check if a line is a table row
  const isTableRow = (line) => line.includes('|');

  // Helper function to check if a line is empty
  const isEmptyLine = (line) => line.trim() === '';

  // Helper function to check if a line is redundant (e.g., duplicate heading)
  const isRedundant = (line, prevLine) => {
    if (isHeading(line) && isHeading(prevLine)) {
      return line === prevLine;
    }
    return false;
  };

  // Process each line
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const prevLine = processedLines[processedLines.length - 1] || '';

    // Skip redundant lines (e.g., duplicate headings)
    if (isRedundant(line, prevLine)) continue;

    // Skip multiple empty lines
    if (isEmptyLine(line)) {
      if (lastLineWasEmpty) continue;
      lastLineWasEmpty = true;
    } else {
      lastLineWasEmpty = false;
    }

    // Add the line to the processed lines
    processedLines.push(line);
  }

  // Join the processed lines and return the cleaned content
  return processedLines.join('\n');
}

// Function to read, process, and save the markdown file
function cleanMarkdownFile(inputFilePath, outputFilePath) {
  try {
    // Read the input markdown file
    const content = fs.readFileSync(inputFilePath, 'utf8');

    // Process the markdown content
    const cleanedContent = processMarkdown(content);

    // Save the cleaned content to the output file
    fs.writeFileSync(outputFilePath, cleanedContent, 'utf8');
    console.log(`Cleaned markdown saved to ${outputFilePath}`);
  } catch (error) {
    console.error('Error processing markdown file:', error);
  }
}

// Get file paths from command-line arguments
const inputFilePath = process.argv[2];
const outputFilePath = process.argv[3] || 'cleaned_scraped_data.md';

if (!inputFilePath) {
  console.error('Please provide an input markdown file path.');
  process.exit(1);
}

// Run the cleanup process
cleanMarkdownFile(inputFilePath, outputFilePath);
