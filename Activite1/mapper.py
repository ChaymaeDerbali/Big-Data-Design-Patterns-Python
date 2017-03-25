#! /usr/bin/python

import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 19:
        ident, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
        res = body.replace('?','.')
        res = res.replace('!','.')
        if(len(body)>2):
            if((res.count('.')<=1) and (res.find('.') == len(res)-6)):
                print "{0}\t{1}".format(ident,body)

