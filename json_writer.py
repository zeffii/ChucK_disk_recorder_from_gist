def write_full_json(state, wavname, ext):

    json_to_write = """\
{{
    "finished": {0},
    "link": "http://www.thegibson.net/~zeffii/output/{1}.{2}",
    "link_name": "{1}.{2}",
    "encoder": "{2}"
}}"""

    content = json_to_write.format(state, wavname, ext)
    with open("static/status.json", "w") as ofile:
        ofile.write(content)

# write_full_json(1, "demo_song2", "wav")