import sys, ntpath
import os.path


# replacement dictionary (replace which element with what)

replace_dict = {}

#

# initialize this variable so I can check its content with print for debugging
#can be deleted later of course, this is only for debugging.

element_content = ""

#

# open both files, read content then close

template_file = open("template.html", "r", encoding="UTF-8")
template = template_file.read()
template_file.close()

content_file = open(sys.argv[1], "r" , encoding="UTF-8")
content = content_file.readlines()
content_file.close()

# loop throught content, look for |ELEMENT|*NAME*|BLOCK| type of HTML comment
# And if finds such, the one between |ELEMENT| and |BLOCK| will always be the name
# To be replaced later in the template file.

for i in content:
    if ("|ELEMENT|" in i):
        temp_list = i.split("|")
        element_name = temp_list[2]
        element_content = ""
        replace_dict.update({element_name : element_content}) # add empty value to the key, later update it...
        continue
    element_content += i
    replace_dict.update({element_name : element_content})




# ========================================
# Create output
# ========================================
for key in replace_dict:
    template = template.replace("{{ %s }}" % (key), replace_dict[key])


output_html = open(os.path.join(os.path.pardir,ntpath.basename(sys.argv[1])), "w+",encoding="UTF-8")
output_html.write(template)
output_html.close()