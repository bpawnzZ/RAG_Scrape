import os

class MarkdownPipeline:
    def open_spider(self, spider):
        self.markdown_file = open('output.md', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.markdown_file.close()

    def process_item(self, item, spider):
        # Write the URL, title, and content to the Markdown file
        self.markdown_file.write(f"# {item['title']}\n\n")
        self.markdown_file.write(f"**URL:** {item['url']}\n\n")
        self.markdown_file.write(f"{item['content']}\n\n")
        self.markdown_file.write("---\n\n")
        return item
