from yandex_cloud_ml_sdk import YCloudML

sdk = YCloudML(
    folder_id="b1g6f7feuufg79e0jh0f", auth="t1.9euelZqOjYqSmouYyJyWnpqaj5HGxu3rnpWazJGSjpKdnszKkpSWiY-UnZ3l8_dMP0g_-e8vL1hz_N3z9wxuRT_57y8vWHP8zef1656VmpnKyYuamc6ayMyKjZDOis-Z7_zF656VmpnKyYuamc6ayMyKjZDOis-Z._Njyn-9qZe388mFnIS_LF0b0gvpUfeI35ZBKP_F6XCY6Ze2wSSM2P45K9039xloVuUh1UM2SELw1KBHpLUNqDQ"
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