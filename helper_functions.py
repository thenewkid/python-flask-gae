import os
import logging

production_url = "https://game-tutorial-slideshow.appspot.com"
development_url = "http://localhost:8080"


def get_url():
    if is_development():
        return development_url
    else:
        return production_url


def is_development():
    return os.environ.get("SERVER_SOFTWARE").startswith("Development")


def create_footer_links():
    files = os.listdir("templates")
    file_objects = []
    for filename in files:
    
        if filename != "base.html":
            file_object = {}
            page_name = filename.split(".")[0]
            file_object["link"] = get_url() + "/html/" + page_name
            file_object["page_name"] = page_name

            if "_" in filename:
                filename_args = filename.split("_")
                formatted_filename = " ".join(filename_args)
                formatted_filename = formatted_filename.title()
                file_object["title"] = formatted_filename.split(".")[0]
            else:
                file_object["title"] = filename.split(".")[0].title()

            file_objects.append(file_object)

    return file_objects

