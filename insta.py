import instaloader
import tkinter as tk

def fetch_account_details():
    username = username_entry.get()
    
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        details_label.config(text=f"Username: {profile.username}\n"
                                  f"Full Name: {profile.full_name}\n"
                                  f"Posts: {profile.mediacount}\n"
                                  
                                  f"Followers: {profile.followers}\n"
                                  f"Following: {profile.followees}\n"
                                  f"Bio: {profile.biography}\n"
                                  f"Links: {profile.external_url}\n"
                                  f"profile: {instaloader.Instaloader().download_profile(username,profile_pic_only=True)}"
                                  )

    except instaloader.exceptions.ProfileNotExistsException:
        details_label.config(text=f"The profile '{username}' does not exist.")
    except instaloader.exceptions.ConnectionException as e:
        details_label.config(text=f"Connection error: {e}")
    except instaloader.exceptions.QueryReturnedBadRequestException as e:
        details_label.config(text=f"Bad request error: {e}")
    except Exception as e:
        details_label.config(text=f"An error occurred: {e}")

# Create Instaloader instance
loader = instaloader.Instaloader()

# Create GUI window
root = tk.Tk()
root.title("Instagram Account Details")

# Username entry
username_label = tk.Label(root, text="Enter Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

# Fetch button
fetch_button = tk.Button(root, text="Fetch Details", command=fetch_account_details)
fetch_button.pack()

# Label to display details
details_label = tk.Label(root, text="", wraplength=300)
details_label.pack()

# Run the main loop
root.mainloop()