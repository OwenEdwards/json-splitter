import sys
import os
import json
import math
import tkinter as tk
import tkinter.ttk as ttk

if sys.version_info[0] < 3:
    print('This script requires Python 3 or higher')
    exit()


def json_splitter(file_name, mb_per_file):
    try:
        f = open(file_name)
        file_size = os.path.getsize(file_name)
        data = json.load(f)
        
        if isinstance(data, list):
            data_len = len(data)
            resultsContents.set("Valid JSON file found")
        else:
            return("Error: JSON is not an Array of Objects")

    except:
        return('Error loading JSON file ...')

    instanceID_to_note_val = instanceID_to_note.instate(['selected'])

    # check that file is larger than max size
    #if file_size < mb_per_file * 1000000:
    #    return('File smaller than split size, exiting')
    # determine number of files necessary
    num_files = math.ceil(file_size/(mb_per_file*1000000))
    if(instanceID_to_note_val):
        resultsContents.set('File will be split into ' + str(num_files) + ' equal parts, with the InstanceID added to the Note')
    else:
        resultsContents.set('File will be split into ' + str(num_files) + ' equal parts')

    # initialize 2D array
    split_data = [[] for i in range(0,num_files)]
    # determine indices of cutoffs in array
    starts = [math.floor(i * data_len/num_files) for i in range(0,num_files)]
    starts.append(data_len)
    # loop through 2D array
    for i in range(0,num_files):
        # loop through each range in array
        for n in range(starts[i],starts[i+1]):
            if(instanceID_to_note_val):
                if (data[n]["instanceId"]):
                    data[n]["note"] = data[n]["note"] + "\r\n\r\n[InstanceID: " + str(data[n]["instanceId"]) + "]\r\n"

            split_data[i].append(data[n])
        
        # create file when section is complete
        name = os.path.basename(file_name).split('.')[0] + '_' + str(i+1) + '.json'
        with open(name, 'w') as outfile:
            json.dump(split_data[i], outfile)
            
        resultsContents.set("Part " + str(i+1) + " ... completed")

    return('Success! Split completed, ' + str(num_files) + ' files created' )


def split_json_file():
    """Handle inputs and pass to the actual splitter
    """
    resultsContents.set('Processing ...')
    fname = ent_filename.get()
    fsize = abs(float(ent_filesize.get()))
    result = json_splitter(fname, fsize)
    resultsContents.set(result)

def clear_results(*args):
    resultsContents.set("")

# Set up the window
window = tk.Tk()
window.title("AMP to Platform JSON Splitter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = ttk.Frame(master=window)
lbl_filename = ttk.Label(master=frm_entry, text="Filename:")
track_filename = tk.StringVar()
ent_filename = ttk.Entry(master=frm_entry, width=100, textvariable=track_filename)
lbl_filesize = ttk.Label(master=frm_entry, text="Maximum file size (MB):")
track_filesize = tk.StringVar()
ent_filesize = ttk.Entry(master=frm_entry, width=4, textvariable=track_filesize)
track_instanceID_to_note = tk.StringVar()
instanceID_to_note = ttk.Checkbutton(master=frm_entry, text='Add Instance ID to Note', variable=track_instanceID_to_note)

# Set the default maximum file size to 150 MB
ent_filesize.insert(0, "150")

# Don't know how to set the default value of instanceID_to_note to False!

# Layout the filename Label and Entry in frm_entry
# using the .grid() geometry manager
lbl_filename.grid(row=0, column=0, sticky="e")
ent_filename.grid(row=0, column=1, sticky="w", padx=20)
lbl_filesize.grid(row=0, column=2, sticky="e")
ent_filesize.grid(row=0, column=3, sticky="w", padx=20)
instanceID_to_note.grid(row=0, column=4, sticky="e", padx=20)

# Create the conversion Button and result display Label
frm_result = ttk.Frame(master=window)
btn_convert = ttk.Button(
    master=frm_result,
    text="Split \N{RIGHTWARDS BLACK ARROW}",
    command=split_json_file
)
resultsContents = tk.StringVar()
lbl_result = ttk.Label(master=frm_result, text="", textvariable=resultsContents)

btn_convert.grid(row=0, column=0, sticky="w", pady=10, padx=10)
lbl_result.grid(row=0, column=1, sticky="w", padx=10)

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
frm_result.grid(row=1, column=0, pady=10)

# Any change of inputs clears the results
track_filename.trace_add("write", clear_results)
track_filesize.trace_add("write", clear_results)
track_instanceID_to_note.trace_add("write", clear_results)

# Run the application
window.mainloop()