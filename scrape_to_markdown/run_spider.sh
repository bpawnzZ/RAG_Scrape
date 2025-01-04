#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./run_spider.sh <URL>"
  exit 1
fi
URL=$1
scrapy crawl domain_spider -a start_url=$URL
