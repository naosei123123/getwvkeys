from msilib.schema import Directory
import os
import xml.dom.minidom
import downloadFile

directory = "download/mpd"

def get(urlMPD):
    filename = downloadFile.download(urlMPD, directory)
    
    dom_elements = xml.dom.minidom.parse(filename).getElementsByTagName("cenc:pssh")

    try:
        os.remove(filename)
    except OSError as e:
        print("")
    
    if len(dom_elements)>0:
        node = dom_elements[0]
        text_node = node.firstChild
        text_value = text_node.nodeValue
        return text_value
    else:
        return "null"