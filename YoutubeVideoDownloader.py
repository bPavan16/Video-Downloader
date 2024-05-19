import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube

# Global variable to store available video qualities
Quality = set()


def Fetch():
    """
    Fetch function retrieves video information from the provided YouTube link
    and populates the available quality options in the OptionMenu.
    """
    VideoLink = entry1.get("1.0", "end-1c")
    YTvideo = YouTube(VideoLink)

    print(YTvideo.title)

    Quality.clear()

    for stream in YTvideo.streams:
        Quality.add(stream.resolution)

    print(Quality)

    option_menu["values"] = list(Quality)


def download():
    """
    download function downloads the selected YouTube video with the chosen quality.
    """
    VideoLink = entry1.get("1.0", "end-1c")

    YTvideo = YouTube(VideoLink)
    print(YTvideo.title)

    video = (
        YTvideo.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
        .download()
    )

    print("Downloading")


def show_values():
    """
    show_values function displays the input values in a message box.
    """
    VideoLink = entry1.get("1.0", "end-1c")
    selected_option = option_var.get()
    messagebox.showinfo(
        "Input Values",
        f"Value 1: {VideoLink}\nValue 2:\nSelected Option: {selected_option}",
    )
    download(videoLink=VideoLink)


def add_placeholder(entry, placeholder):
    """
    add_placeholder function adds a placeholder text to the entry widget.
    """
    entry.insert("1.0", placeholder)
    entry.config(foreground="grey")
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder))
    entry.bind("<FocusOut>", lambda event: set_placeholder(event, placeholder))


def clear_placeholder(event, placeholder):
    """
    clear_placeholder function clears the placeholder text when entry widget is focused.
    """
    if event.widget.get("1.0", "end-1c") == placeholder:
        event.widget.delete("1.0", tk.END)
        event.widget.config(foreground="white")


def set_placeholder(event, placeholder):
    """
    set_placeholder function sets the placeholder text when entry widget is unfocused.
    """
    if not event.widget.get("1.0", "end-1c").strip():
        event.widget.insert("1.0", placeholder)
        event.widget.config(foreground="grey")


# Create the main window
root = tk.Tk()
root.title("Youtube - Video Downloader")
root.geometry("600x350")

# Configure the style
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel", font=("Helvetica", 12), background="#2e2e2e", foreground="#f0f0f0"
)
style.configure(
    "TText", font=("Helvetica", 12), background="#3e3e3e", foreground="white"
)
style.configure(
    "TButton",
    font=("Helvetica", 12, "bold"),
    background="#444444",
    foreground="#f0f0f0",
)
style.configure(
    "TCombobox", font=("Helvetica", 12), background="#3e3e3e", foreground="white"
)

style.map(
    "TButton",
    foreground=[("pressed", "white"), ("active", "white")],
    background=[("pressed", "!disabled", "#555555"), ("active", "#666666")],
    relief=[("pressed", "sunken"), ("!pressed", "raised")],
)

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
frame.grid(row=0, column=0, sticky="")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create and place the labels and entry widgets for the input boxes
label1 = ttk.Label(frame, text="LINK : ")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry1 = tk.Text(frame, width=40, height=1, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Option Menu
option_var = tk.StringVar()
option_menu = ttk.Combobox(frame, textvariable=option_var, values=[])
option_menu.grid(row=2, column=1, padx=10, pady=10, sticky="w")
option_menu.set("Quality")
option_menu.config(foreground="black")

# Create and place the submit button
submit_button = ttk.Button(frame, text="Submit", command=Fetch)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)
download_button = ttk.Button(frame, text="Download", command=download)
download_button.grid(row=4, column=0, columnspan=2)

# Set the background color of the main window and frame
root.configure(bg="#2e2e2e")
frame.configure(style="TFrame")
style.configure("TFrame", background="#2e2e2e")

# Run the application
root.mainloop()
