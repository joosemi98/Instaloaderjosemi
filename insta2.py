import instaloader

def download_instagram_photos(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Download all posts from the profile
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        loader.download_profile(username, profile_pic_only=False)
        print(f"Downloaded all photos from the profile '{username}' successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile '{username}' does not exist.")
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
    except instaloader.exceptions.QueryReturnedBadRequestException as e:
        print(f"Bad request error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    download_instagram_photos(username)
