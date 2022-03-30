import csv
from pathlib import Path
with open("tags.csv", "r", newline="") as file:
        reader                  = csv.reader(file, delimiter=",")
        for row in reader       : 
            meta_dic            = '<meta name="description" content="'+row[3]+'">'
            title               = '<title>'+row[2]+'</title>'
            page_url            = row[1]
            file_name           = page_url.replace("https://www.infocomstudios.com/", "")
            path_to_file        = file_name
            path                = Path(path_to_file)
            if path.is_file()   : 
                command         = "sed -i -e '\@</title>@i\<meta_dic>' "+file_name
                exe_cmd_meta    = command.replace("<meta_dic>", meta_dic)
                title_command   = "sed -i 's|<title>.*</title>|<title> "+row[2]+" </title>|g' "+file_name
                print("[+] "+file_name)
                print("\n")
                print(exe_cmd_meta)
                print(title_command)
                print("\n\n")
            
