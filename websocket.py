from websockets.sync.client import connect
import tkinter as tk

with connect("ws://localhost:8888/websocket") as websocket:

    def send_message():
        global entry_box, message_display
        message = entry_box.get()
        websocket.send(message)

        message_display.config(state="normal")  # Enable editing
        message_display.insert(tk.END, f"You: {message}\n")  # Append message
        message_display.config(state="disabled")  # Disable editing again

        entry_box.delete(0, 'end')
        message = websocket.recv()
        print(f"Received: {message}")

    root = tk.Tk()
    root.title("Chatr")

    # Chatters frame
    chatters_frame = tk.Frame(root, width=200, height=400, bg="skyblue")
    chatters_frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)
    tk.Label(
        chatters_frame,
        text="Chatters",
        bg="skyblue",
    ).pack(padx=5, pady=5)

    users_tab = tk.Frame(chatters_frame, bg="lightblue")

    users_var = tk.StringVar(value="None")
    for tool in ["Sam", "BappleBoi", "Penitent"]:
        tk.Button(
            users_tab,
            text=tool,
            bg="lightblue",
        ).pack(anchor="w", padx=20, pady=5)

    users_tab.pack(padx=5, pady=5, fill=tk.Y)


    # Chat Box frame
    chatbox_frame = tk.Frame(root, width=200, height=400, bg="gray")
    chatbox_frame.pack(padx=5, pady=5, side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Message Display Area (Scrollable)
    message_display = tk.Text(chatbox_frame, bg="gray", fg="white", state="disabled", wrap="word")
    message_display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    # Input box
    messagebox_frame = tk.Frame(chatbox_frame, width=200, height=20, bg="white")
    messagebox_frame.pack(padx=5, pady=5, side=tk.BOTTOM, fill=tk.X)

    entry_box = tk.Entry(messagebox_frame, width=30)
    entry_box.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)


    send_button = tk.Button(messagebox_frame, text="Send", bg="blue", fg="white", command=send_message)
    send_button.pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()