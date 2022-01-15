import requests, os, time
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://api.minecraftservices.com/minecraft/profile/skins"

bearer_token = input("Input your bearer token!")

file_names = os.listdir('./skins')

def change(file_name):
    skin = open(file_name, "rb")

    mp_encoder = MultipartEncoder(
        fields={
            "variant": "classic",
            "file": (file_name, skin, "image/png"),
        }
    )

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": mp_encoder.content_type
    }

    r = requests.post(url, headers=headers, data=mp_encoder)
    print(r.status_code)

try:

    for i in file_names:
        os.rename(f"./skins/{i}", f"./skins/{i[5:]}")

    for i in file_names:
        os.remove(f'./skins/{i}')

except FileExistsError:
    print("Skins already properly named!")

file_names = os.listdir('./skins')

ordered_names = [int(x[:len(x) - 4]) for x in file_names]
ordered_names.sort(key=int)

for i in ordered_names:
    file_name = f"./skins/" + str(i) + ".png"
    change(file_name)
    input("Press enter when the skin has been cached on NameMC.")