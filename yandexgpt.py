from yandex_cloud_ml_sdk import YCloudML

sdk = YCloudML(
    folder_id="b1g6f7feuufg79e0jh0f", auth="APi"
)

model = sdk.models.completions("yandexgpt-lite", model_version="rc")
model = model.configure(temperature=0.3)
result = model.run(
    [
        {"role": "system", "text": ""},
        {
            "role": "user",
            "text": "Напиши шаблон резюме",
        },
    ]
)

for alternative in result:
    print(alternative)