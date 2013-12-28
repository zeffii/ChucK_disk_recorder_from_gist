def write_full_json(state, wavname, ext, percent):

    json_to_write = """\
{{
    "finished": {0},
    "link": "http://www.thegibson.net/~zeffii/output/{1}.{2}",
    "link_name": "{1}.{2}",
    "encoder": "{2}",
    "percent": {3}
}}"""

    content = json_to_write.format(state, wavname, ext, percent)
    with open("/home/zeffii/public_html/static/status.json", "w") as ofile:
        ofile.write(content)

