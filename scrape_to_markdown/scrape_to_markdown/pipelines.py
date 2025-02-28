import os
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MarkdownPipeline:
    def open_spider(self, spider):
        self.markdown_file = open('output.md', 'w', encoding='utf-8')
        self.image_dir = 'images'
        os.makedirs(self.image_dir, exist_ok=True)

    def close_spider(self, spider):
        self.markdown_file.close()

    def process_item(self, item, spider):
        # Update image references in markdown content
        if 'images' in item:
            for image in item['images']:
                image_url = image['url']
                image_path = os.path.join(self.image_dir, image['path'])
                # Replace base64 images with proper markdown image syntax
                item['content'] = item['content'].replace(
                    f'![](data:image/{image_url.split(".")[-1]};base64,',
                    f'![]({image_path})'
                )

        # Write to markdown file
        title = item.get('title', 'Untitled Document')
        self.markdown_file.write(f"# {title}\n\n")
        self.markdown_file.write(f"**URL:** {item['url']}\n\n")
        if 'content' in item:
            self.markdown_file.write(f"{item['content']}\n\n")
        else:
            self.markdown_file.write("No content available\n\n")
        self.markdown_file.write("---\n\n")
        return item

class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # Generate unique filename based on image URL
        image_guid = request.url.split('/')[-1]
        return f'full/{image_guid}'

    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['images'] = [{'url': x['url'], 'path': x['path']} for ok, x in results if ok]
        return item
