profil = {
    "my_name": "Adnan.",
    "my_dream": "AI Engineer/Software Engineer Web 4.0.",
    "like": ["Technology", "Space", "Sains",
                "In-depth discussion", "Programming", "Etc."],
    "my_focus": ["Personal Branding", "AI", "Business Digital."]
    
}
print("My name is", profil["my_name"])
print("I like", ", ".join(profil["like"]))
print("My dream is to become a ", profil["my_dream"])
print("I'm focused on", ", ".join(profil["my_focus"]))
print()

contact_message = "If, there anything you'd like to discuss with me." \
" Please contact me via email adnanslametwibowo@gmail.com"
print(f"{contact_message:^100}")