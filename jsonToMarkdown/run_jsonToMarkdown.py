# run_jsonToMarkdown
# David Lawrence
# 2018
# requires Python 2.7

import jsonToMarkdown
jsonToMarkdown.parseJsonFile('../input/example-long-consignments-response.json', '../output/parser-results.txt', '../output/markdown-from-json.md')


jsonToMarkdown.removeDuplicateLinesRetainOrder('../output/markdown-from-json.md', '../output/markdown-from-json_normalized.md')



